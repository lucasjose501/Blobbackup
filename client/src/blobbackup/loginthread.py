import os
import json
import subprocess
import tempfile

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.api import login, get_computer
from blobbackup.config import config, save_config
from blobbackup.util import (
    CREATE_NO_WINDOW,
    is_windows,
    get_password_from_keyring,
    get_restic_add_password_command,
    get_restic_list_passwords_command,
    get_restic_delete_password_command,
    get_restic_unlock_command,
    save_password_in_keyring,
    get_restic_env,
)


class LoginThread(QThread):
    finished = pyqtSignal(bool)
    trial_over = pyqtSignal()

    def __init__(self, email, password, reauth):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.reauth = reauth

    def run(self):
        user = login(self.email, self.password)
        if not user:
            self.finished.emit(False)
            return
        allowed_to_backup = user["subscribed"] or user["on_trial"]
        if not allowed_to_backup:
            self.trial_over.emit()
            return
        if self.reauth:
            update_email_and_password(self.email, self.password)
        self.finished.emit(True)


def update_email_and_password(email, password):
    old_password = get_password_from_keyring()
    computer = get_computer(email, password, config["meta"]["computer_id"])

    config["meta"]["email"] = email
    save_config()

    if old_password != password:
        add_new_password_to_repo(computer, old_password, password)
        unlock_repo(computer, password)
        remove_all_but_new_password_from_repo(computer, password)
        save_password_in_keyring(password)


def add_new_password_to_repo(computer, old_password, password):
    with tempfile.TemporaryDirectory() as root:
        password_file = os.path.join(root, "password.txt")
        with open(password_file, "w") as f:
            f.write(password)
        if is_windows():
            subprocess.run(
                get_restic_add_password_command(password_file),
                env=get_restic_env(computer, old_password),
                creationflags=CREATE_NO_WINDOW,
            )
        else:
            subprocess.run(
                get_restic_add_password_command(password_file),
                env=get_restic_env(computer, old_password),
            )


def unlock_repo(computer, password):
    if is_windows():
        subprocess.run(
            get_restic_unlock_command(),
            env=get_restic_env(computer, password),
            creationflags=CREATE_NO_WINDOW,
        )
    else:
        subprocess.run(
            get_restic_unlock_command(),
            env=get_restic_env(computer, password),
        )


def remove_all_but_new_password_from_repo(computer, password):
    if is_windows():
        ret = subprocess.run(
            get_restic_list_passwords_command(),
            env=get_restic_env(computer, password),
            stdout=subprocess.PIPE,
            creationflags=CREATE_NO_WINDOW,
        ).stdout
    else:
        ret = subprocess.run(
            get_restic_list_passwords_command(),
            env=get_restic_env(computer, password),
            stdout=subprocess.PIPE,
        ).stdout
    keys = json.loads(ret)
    for key in sorted(keys, key=lambda k: k["created"])[:-1]:
        if is_windows():
            subprocess.run(
                get_restic_delete_password_command(key["id"]),
                env=get_restic_env(computer, password),
                creationflags=CREATE_NO_WINDOW,
            )
        else:
            subprocess.run(
                get_restic_delete_password_command(key["id"]),
                env=get_restic_env(computer, password),
            )
