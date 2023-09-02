# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from tkinter.ttk import Progressbar
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(907, 599)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 490, 891, 101))
        font = QtGui.QFont()
        font.setFamily("VanBerger")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(650, 10, 241, 221))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(650, 270, 241, 221))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(130, 40, 181, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 66, 19))
        self.label_4.setObjectName("label_4")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(130, 80, 181, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 80, 66, 19))
        self.label_5.setObjectName("label_5")
        self.progressBar_3 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(130, 120, 181, 23))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 120, 66, 19))
        self.label_6.setObjectName("label_6")
        self.progressBar_4 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_4.setGeometry(QtCore.QRect(130, 160, 181, 23))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 160, 66, 19))
        self.label_7.setObjectName("label_7")
        self.progressBar_5 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_5.setGeometry(QtCore.QRect(130, 200, 181, 23))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 200, 66, 19))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(370, 10, 241, 221))
        self.label_9.setObjectName("label_9")
        self.progressBar_6 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_6.setGeometry(QtCore.QRect(130, 310, 181, 23))
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setObjectName("progressBar_6")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(40, 430, 66, 19))
        self.label_10.setObjectName("label_10")
        self.progressBar_7 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_7.setGeometry(QtCore.QRect(130, 390, 181, 23))
        self.progressBar_7.setProperty("value", 24)
        self.progressBar_7.setObjectName("progressBar_7")
        self.progressBar_8 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_8.setGeometry(QtCore.QRect(130, 350, 181, 23))
        self.progressBar_8.setProperty("value", 24)
        self.progressBar_8.setObjectName("progressBar_8")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 390, 66, 19))
        self.label_11.setObjectName("label_11")
        self.progressBar_9 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_9.setGeometry(QtCore.QRect(130, 270, 181, 23))
        self.progressBar_9.setProperty("value", 24)
        self.progressBar_9.setObjectName("progressBar_9")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(40, 350, 66, 19))
        self.label_12.setObjectName("label_12")
        self.progressBar_10 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_10.setGeometry(QtCore.QRect(130, 430, 181, 23))
        self.progressBar_10.setProperty("value", 24)
        self.progressBar_10.setObjectName("progressBar_10")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(40, 270, 66, 19))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(40, 310, 66, 19))
        self.label_14.setObjectName("label_14")
        self._update_timer = QtCore.QTimer()
        self._update_timer.start(5)
        self._update_timer.timeout.connect(self.get_data)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def get_data(self):
        # x_val = open("main_x.srpx","r").readlines()
        # y_val = open("main_y.srpx","r").readlines()
        hand=[0]*11
        handy=[0]*11
        for i in range(1,11):
            try:
                hand[i-1] = ((float(open("main_x.srpx","r").readlines()[i].split()[1]))*10)
            except:
                print("CrashSkip x")
            try:
                handy[i-1] = ((float(open("main_y.srpx","r").readlines()[i].split()[1]))*10)
            except:
                print("CrashSkip Y")
        #Somestuff are hardcoded and maybe inefficient for experimental perpouses...
        self.label_2.setText(str(open("main_x.srpx","r").read()))
        self.label_3.setText(str(open("main_y.srpx","r").read()))
        index_progress = int((((hand[1])-(hand[6]))/100)*(5)*500)
        middle_progress = int(((((hand[2])-(hand[6]))/100)*(5))*500)
        ring_progress = int(((((hand[3])-(hand[6]))/100)*(5))*500)
        pinky_progress = int(((((hand[4])-(hand[6]))/100)*(5))*500)
        thumb_progress = int(((((handy[5])-(handy[6]))/100)*(5))*1000)
        index_progress_y = int((((handy[1])-(hand[6]))/100)*(5)*500)
        middle_progress_y = int(((((handy[2])-(hand[6]))/100)*(5))*500)
        ring_progress_y = int(((((handy[3])-(hand[6]))/100)*(5))*500)
        pinky_progress_y = int(((((handy[4])-(hand[6]))/100)*(5))*500)
        #thumb_progress = int(((((handy[5])-(handy[6]))/100)*(5))*1000)
        switch_threshold = 20

        # if index_progress > switch_threshold:
        #     self.progressBar.setValue(index_progress)
        # else :
        #     self.progressBar.setValue(index_progress_y)
        # if middle_progress > switch_threshold:
        #     self.progressBar_2.setValue(middle_progress)
        # else :
        #     self.progressBar_2.setValue(middle_progress_y)
        # if ring_progress > switch_threshold:
        #     self.progressBar_3.setValue(ring_progress)
        # else :
        #     self.progressBar_3.setValue(ring_progress_y)
        # if pinky_progress > switch_threshold:
        #     self.progressBar_4.setValue(pinky_progress)
        # else:
        #     self.progressBar_4.setValue(pinky_progress_y)

        self.progressBar.setValue(index_progress)
        self.progressBar_2.setValue(middle_progress)
        self.progressBar_3.setValue(ring_progress)
        self.progressBar_4.setValue(pinky_progress)

        self.progressBar_5.setValue(thumb_progress)
        #print(setProgress)
        print(int((((hand[1])-(hand[6]))/100)*(5)))
        #os.system("cat main_x.srpx")
        #self.progressBar_2.setValue(((hand[1])/100)*(5))
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SERAPHIX SYSTEMS - GESTURESCAPE v0.1 [BETA]"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt;\">S E R A P H I X</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">HAND_CLOSED_STAT</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">HAND_DATA_DISP</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "INDEX"))
        self.label_5.setText(_translate("Dialog", "MIDDLE"))
        self.label_6.setText(_translate("Dialog", "RING"))
        self.label_7.setText(_translate("Dialog", "PINKY"))
        self.label_8.setText(_translate("Dialog", "THUMB"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">POSE_STAT</span></p><p><span style=\" font-size:14pt;\">UNDER_DEV</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "UNK"))
        self.label_11.setText(_translate("Dialog", "HANDS"))
        self.label_12.setText(_translate("Dialog", "LEGS"))
        self.label_13.setText(_translate("Dialog", "HEAD"))
        self.label_14.setText(_translate("Dialog", "TORSO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())