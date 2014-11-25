
#!/usr/bin/env python

import sys
import DB_manager as db
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Dialog.ui'
#
# Created: Mon Nov 24 22:47:39 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.dbu = db.DatabaseUtility('UsernamePassword_DB', 'masterTable')
        self.setupUi(self)
        self.confirm = None
        
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName(_fromUtf8("Login_Dialog"))
        Login_Dialog.resize(285, 134)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Login_Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Login_Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.user_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.user_lineEdit.setObjectName(_fromUtf8("user_lineEdit"))
        self.horizontalLayout.addWidget(self.user_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.password_lineEdit.setInputMask(_fromUtf8(""))
        self.password_lineEdit.setText(_fromUtf8(""))
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.newUser_btn = QtGui.QPushButton(self.groupBox)
        self.newUser_btn.setObjectName(_fromUtf8("newUser_btn"))
        self.horizontalLayout_4.addWidget(self.newUser_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.login_btn = QtGui.QPushButton(self.groupBox)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.horizontalLayout_4.addWidget(self.login_btn)
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "TPayne\'s User Login", None))
        self.groupBox.setTitle(_translate("Login_Dialog", "Super Ham!", None))
        self.label.setText(_translate("Login_Dialog", "Username", None))
        self.label_2.setText(_translate("Login_Dialog", "Password", None))
        self.newUser_btn.setText(_translate("Login_Dialog", "New User", None))
        self.login_btn.setText(_translate("Login_Dialog", "Login", None))
        self.cancel_btn.setText(_translate("Login_Dialog", "Cancel", None))


    @QtCore.pyqtSignature("on_cancel_btn_clicked()")
    def Cancel_btn(self):
        self.close()

    @QtCore.pyqtSignature("on_login_btn_clicked()")
    def Login_btn(self):
        username = self.user_lineEdit.text()
        password = self.password_lineEdit.text()
        if not username:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Username Missing!')
        elif not password:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Password Missing!')
        else:
            self.AttemptLogin(username, password)

    def AttemptLogin(self, username, password):
        t = self.dbu.GetTable()
        print (t)
        for col in t:
            if username == col[1]:
                if password == col[2]:
                    QtGui.QMessageBox.information(self, 'BOOYA!', 'Success!!')
                    self.close()
                else:
                    QtGui.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
                    return

    @QtCore.pyqtSignature("on_newUser_btn_clicked()")
    def NewUser_btn(self):
        self.newUser = Ui_Register(self.dbu)
        self.newUser.show()

class Ui_Register(QtGui.QDialog):
    def __init__(self, dbu):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.dbu = dbu

    def setupUi(self, Register_Dialog):
        Register_Dialog.setObjectName(_fromUtf8("Register_Dialog"))
        Register_Dialog.resize(372, 187)
        Register_Dialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Register_Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Register_Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.username_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.username_lineEdit.setObjectName(_fromUtf8("username_lineEdit"))
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.password_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.confirmPassword_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.confirmPassword_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.confirmPassword_lineEdit.setObjectName(_fromUtf8("confirmPassword_lineEdit"))
        self.horizontalLayout_4.addWidget(self.confirmPassword_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_btn = QtGui.QPushButton(self.groupBox)
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.horizontalLayout_3.addWidget(self.add_btn)
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Register_Dialog)

    def retranslateUi(self, Register_Dialog):
        Register_Dialog.setWindowTitle(_translate("Register_Dialog", "Register New User", None))
        self.groupBox.setTitle(_translate("Register_Dialog", "I Love Ham!", None))
        self.label_2.setText(_translate("Register_Dialog", "Username", None))
        self.label.setText(_translate("Register_Dialog", "Password", None))
        self.label_3.setText(_translate("Register_Dialog", "Confirm Password", None))
        self.label_4.setText(_translate("Register_Dialog", "Not Included: Phone, Address, Social Security Number, Credit Card...", None))
        self.add_btn.setText(_translate("Register_Dialog", "Add", None))
        self.cancel_btn.setText(_translate("Register_Dialog", "Cancel", None))


    @QtCore.pyqtSignature("on_cancel_btn_clicked()")
    def Cancel_btn(self):
        self.close()

    @QtCore.pyqtSignature("on_add_btn_clicked()")
    def Add_btn(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        cpassword = self.confirmPassword_lineEdit.text()
        if not username:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'Username Missing')
        elif password != cpassword:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'Passwords Do Not Match')
        else:
            t = self.dbu.GetTable()
            print (t)
            for col in t:
                if username == col[1]:
                    QtGui.QMessageBox.warning(self, 'Dang it!', 'Username Taken. :(')
            else:
                self.dbu.AddEntryToTable (username, password)
                QtGui.QMessageBox.information(self, 'Awesome!!', 'User Added SUCCESSFULLY!')
                self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Login()
    ex.show()
    sys.exit(app.exec_())
