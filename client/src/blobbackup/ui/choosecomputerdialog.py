# Form implementation generated from reading ui file 'src/blobbackup/ui/choosecomputerdialog.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChooseComputerDialog(object):
    def setupUi(self, ChooseComputerDialog):
        ChooseComputerDialog.setObjectName("ChooseComputerDialog")
        ChooseComputerDialog.resize(400, 150)
        ChooseComputerDialog.setMinimumSize(QtCore.QSize(400, 150))
        self.verticalLayout = QtWidgets.QVBoxLayout(ChooseComputerDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(ChooseComputerDialog)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.computers_combo_box = QtWidgets.QComboBox(ChooseComputerDialog)
        self.computers_combo_box.setObjectName("computers_combo_box")
        self.verticalLayout.addWidget(self.computers_combo_box)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.continue_button = QtWidgets.QPushButton(ChooseComputerDialog)
        self.continue_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.continue_button.setObjectName("continue_button")
        self.horizontalLayout_2.addWidget(self.continue_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ChooseComputerDialog)
        QtCore.QMetaObject.connectSlotsByName(ChooseComputerDialog)

    def retranslateUi(self, ChooseComputerDialog):
        _translate = QtCore.QCoreApplication.translate
        ChooseComputerDialog.setWindowTitle(_translate("ChooseComputerDialog", "Choose Computer - Blobbackup"))
        self.label_4.setText(_translate("ChooseComputerDialog", "Choose the computer you want to restore from."))
        self.continue_button.setText(_translate("ChooseComputerDialog", "Continue"))
