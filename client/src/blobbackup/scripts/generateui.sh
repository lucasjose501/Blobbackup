#!/bin/bash

pyuic6 src/blobbackup/ui/logindialog.ui -o src/blobbackup/ui/logindialog.py
pyuic6 src/blobbackup/ui/welcomedialog.ui -o src/blobbackup/ui/welcomedialog.py
pyuic6 src/blobbackup/ui/backupstarteddialog.ui -o src/blobbackup/ui/backupstarteddialog.py
pyuic6 src/blobbackup/ui/settingsdialog.ui -o src/blobbackup/ui/settingsdialog.py
pyuic6 src/blobbackup/ui/mainwindow.ui -o src/blobbackup/ui/mainwindow.py
pyuic6 src/blobbackup/ui/restoredialog.ui -o src/blobbackup/ui/restoredialog.py
pyuic6 src/blobbackup/ui/choosecomputerdialog.ui -o src/blobbackup/ui/choosecomputerdialog.py
pyuic6 src/blobbackup/ui/requestfulldiskdialog.ui -o src/blobbackup/ui/requestfulldiskdialog.py
pyuic6 src/blobbackup/ui/loadingdialog.ui -o src/blobbackup/ui/loadingdialog.py