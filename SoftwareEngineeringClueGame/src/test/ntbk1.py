from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Notebook(object):
    
    def setupUi(self, Notebook):
        Notebook.setObjectName("Notebook")
        Notebook.resize(1253, 712)
        self.Ntbk_Title = QtWidgets.QLabel(Notebook)
        self.Ntbk_Title.setGeometry(QtCore.QRect(470, 0, 191, 61))
        self.Ntbk_Title.setScaledContents(True)
        self.Ntbk_Title.setObjectName("Ntbk_Title")
        
        # Accusation checkboxes
        self.acc_Scarlett = QtWidgets.QCheckBox(Notebook)
        self.acc_Scarlett.setGeometry(QtCore.QRect(210, 160, 21, 41))
        self.acc_Scarlett.setText("")
        self.acc_Scarlett.setIconSize(QtCore.QSize(40, 40))
        self.acc_Scarlett.setObjectName("acc_Scarlett")
        
        self.acc_Mustard = QtWidgets.QCheckBox(Notebook)
        self.acc_Mustard.setGeometry(QtCore.QRect(210, 220, 21, 41))
        self.acc_Mustard.setText("")
        self.acc_Mustard.setIconSize(QtCore.QSize(40, 40))
        self.acc_Mustard.setObjectName("acc_Mustard")
        
        self.acc_Orchid = QtWidgets.QCheckBox(Notebook)
        self.acc_Orchid.setGeometry(QtCore.QRect(210, 280, 21, 41))
        self.acc_Orchid.setText("")
        self.acc_Orchid.setIconSize(QtCore.QSize(40, 40))
        self.acc_Orchid.setObjectName("acc_Orchid")
        
        self.acc_Green = QtWidgets.QCheckBox(Notebook)
        self.acc_Green.setGeometry(QtCore.QRect(210, 340, 21, 41))
        self.acc_Green.setText("")
        self.acc_Green.setIconSize(QtCore.QSize(40, 40))
        self.acc_Green.setObjectName("acc_Green")
        
        self.acc_Plum = QtWidgets.QCheckBox(Notebook)
        self.acc_Plum.setGeometry(QtCore.QRect(210, 460, 21, 41))
        self.acc_Plum.setText("")
        self.acc_Plum.setIconSize(QtCore.QSize(40, 40))
        self.acc_Plum.setObjectName("acc_Plum")
        
        self.acc_Peacoke = QtWidgets.QCheckBox(Notebook)
        self.acc_Peacoke.setGeometry(QtCore.QRect(210, 400, 21, 41))
        self.acc_Peacoke.setText("")
        self.acc_Peacoke.setIconSize(QtCore.QSize(40, 40))
        self.acc_Peacoke.setObjectName("acc_Peacoke")
        
        self.acc_Hall = QtWidgets.QCheckBox(Notebook)
        self.acc_Hall.setGeometry(QtCore.QRect(1130, 350, 21, 41))
        self.acc_Hall.setText("")
        self.acc_Hall.setIconSize(QtCore.QSize(40, 40))
        self.acc_Hall.setObjectName("acc_Hall")
        
        self.acc_Ballroom = QtWidgets.QCheckBox(Notebook)
        self.acc_Ballroom.setGeometry(QtCore.QRect(1130, 470, 21, 41))
        self.acc_Ballroom.setText("")
        self.acc_Ballroom.setIconSize(QtCore.QSize(40, 40))
        self.acc_Ballroom.setObjectName("acc_Ballroom")
        
        self.acc_BilliaryRoom = QtWidgets.QCheckBox(Notebook)
        self.acc_BilliaryRoom.setGeometry(QtCore.QRect(1130, 410, 21, 41))
        self.acc_BilliaryRoom.setText("")
        self.acc_BilliaryRoom.setIconSize(QtCore.QSize(40, 40))
        self.acc_BilliaryRoom.setObjectName("acc_BilliaryRoom")
        
        self.acc_Study = QtWidgets.QCheckBox(Notebook)
        self.acc_Study.setGeometry(QtCore.QRect(1130, 170, 21, 41))
        self.acc_Study.setText("")
        self.acc_Study.setIconSize(QtCore.QSize(40, 40))
        self.acc_Study.setObjectName("acc_Study")
        
        self.acc_Library = QtWidgets.QCheckBox(Notebook)
        self.acc_Library.setGeometry(QtCore.QRect(1130, 230, 21, 41))
        self.acc_Library.setText("")
        self.acc_Library.setIconSize(QtCore.QSize(40, 40))
        self.acc_Library.setObjectName("acc_Library")
        
        self.acc_Conversary = QtWidgets.QCheckBox(Notebook)
        self.acc_Conversary.setGeometry(QtCore.QRect(1130, 290, 21, 41))
        self.acc_Conversary.setText("")
        self.acc_Conversary.setIconSize(QtCore.QSize(40, 40))
        self.acc_Conversary.setObjectName("acc_Conversary")
        
        self.acc_DiningRoom = QtWidgets.QCheckBox(Notebook)
        self.acc_DiningRoom.setGeometry(QtCore.QRect(1130, 590, 21, 41))
        self.acc_DiningRoom.setText("")
        self.acc_DiningRoom.setIconSize(QtCore.QSize(40, 40))
        self.acc_DiningRoom.setObjectName("acc_DiningRoom")
        
        self.acc_Kitchen = QtWidgets.QCheckBox(Notebook)
        self.acc_Kitchen.setGeometry(QtCore.QRect(1130, 650, 21, 41))
        self.acc_Kitchen.setText("")
        self.acc_Kitchen.setIconSize(QtCore.QSize(40, 40))
        self.acc_Kitchen.setObjectName("acc_Kitchen")
        
        self.acc_Lounge = QtWidgets.QCheckBox(Notebook)
        self.acc_Lounge.setGeometry(QtCore.QRect(1130, 530, 21, 41))
        self.acc_Lounge.setText("")
        self.acc_Lounge.setIconSize(QtCore.QSize(40, 40))
        self.acc_Lounge.setObjectName("acc_Lounge")
        
        self.acc_Rope = QtWidgets.QCheckBox(Notebook)
        self.acc_Rope.setGeometry(QtCore.QRect(650, 350, 21, 41))
        self.acc_Rope.setText("")
        self.acc_Rope.setIconSize(QtCore.QSize(40, 40))
        self.acc_Rope.setObjectName("acc_Rope")
        
        self.acc_Wrench = QtWidgets.QCheckBox(Notebook)
        self.acc_Wrench.setGeometry(QtCore.QRect(650, 470, 21, 41))
        self.acc_Wrench.setText("")
        self.acc_Wrench.setIconSize(QtCore.QSize(40, 40))
        self.acc_Wrench.setObjectName("acc_Wrench")
        
        self.acc_Candlestick = QtWidgets.QCheckBox(Notebook)
        self.acc_Candlestick.setGeometry(QtCore.QRect(650, 410, 21, 41))
        self.acc_Candlestick.setText("")
        self.acc_Candlestick.setIconSize(QtCore.QSize(40, 40))
        self.acc_Candlestick.setObjectName("acc_Candlestick")
        
        self.acc_Revolver = QtWidgets.QCheckBox(Notebook)
        self.acc_Revolver.setGeometry(QtCore.QRect(650, 170, 21, 41))
        self.acc_Revolver.setText("")
        self.acc_Revolver.setIconSize(QtCore.QSize(40, 40))
        self.acc_Revolver.setObjectName("acc_Revolver")
        
        self.acc_Dagger = QtWidgets.QCheckBox(Notebook)
        self.acc_Dagger.setGeometry(QtCore.QRect(650, 230, 21, 41))
        self.acc_Dagger.setText("")
        self.acc_Dagger.setIconSize(QtCore.QSize(40, 40))
        self.acc_Dagger.setObjectName("acc_Dagger")
        
        self.acc_LeadPipe = QtWidgets.QCheckBox(Notebook)
        self.acc_LeadPipe.setGeometry(QtCore.QRect(650, 290, 21, 41))
        self.acc_LeadPipe.setText("")
        self.acc_LeadPipe.setIconSize(QtCore.QSize(40, 40))
        self.acc_LeadPipe.setObjectName("acc_LeadPipe")
        
        
        ###################### Lines and Labels #######################
        
        self.label_2 = QtWidgets.QLabel(Notebook)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 251, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Notebook)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 131, 51))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Notebook)
        self.line.setGeometry(QtCore.QRect(160, 160, 16, 351))
        self.line.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Notebook)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 131, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Notebook)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 131, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Notebook)
        self.label_6.setGeometry(QtCore.QRect(20, 330, 131, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Notebook)
        self.label_7.setGeometry(QtCore.QRect(20, 390, 131, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Notebook)
        self.label_8.setGeometry(QtCore.QRect(20, 450, 131, 51))
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(Notebook)
        self.line_2.setGeometry(QtCore.QRect(10, 200, 311, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Notebook)
        self.line_3.setGeometry(QtCore.QRect(10, 260, 311, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Notebook)
        self.line_4.setGeometry(QtCore.QRect(10, 320, 311, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Notebook)
        self.line_5.setGeometry(QtCore.QRect(10, 380, 311, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Notebook)
        self.line_6.setGeometry(QtCore.QRect(10, 500, 311, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Notebook)
        self.line_7.setGeometry(QtCore.QRect(10, 440, 311, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Notebook)
        self.line_8.setGeometry(QtCore.QRect(870, 270, 311, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_9 = QtWidgets.QLabel(Notebook)
        self.label_9.setGeometry(QtCore.QRect(880, 100, 251, 51))
        self.label_9.setObjectName("label_9")
        self.library_lab = QtWidgets.QLabel(Notebook)
        self.library_lab.setGeometry(QtCore.QRect(880, 220, 131, 51))
        self.library_lab.setObjectName("library_lab")
        self.billiary_label = QtWidgets.QLabel(Notebook)
        self.billiary_label.setGeometry(QtCore.QRect(880, 400, 201, 51))
        self.billiary_label.setObjectName("billiary_label")
        self.label_12 = QtWidgets.QLabel(Notebook)
        self.label_12.setGeometry(QtCore.QRect(880, 340, 131, 51))
        self.label_12.setObjectName("label_12")
        self.line_9 = QtWidgets.QFrame(Notebook)
        self.line_9.setGeometry(QtCore.QRect(870, 510, 311, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_13 = QtWidgets.QLabel(Notebook)
        self.label_13.setGeometry(QtCore.QRect(880, 280, 201, 51))
        self.label_13.setObjectName("label_13")
        self.line_10 = QtWidgets.QFrame(Notebook)
        self.line_10.setGeometry(QtCore.QRect(870, 450, 311, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Notebook)
        self.line_11.setGeometry(QtCore.QRect(870, 210, 311, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_14 = QtWidgets.QLabel(Notebook)
        self.label_14.setGeometry(QtCore.QRect(880, 460, 131, 51))
        self.label_14.setObjectName("label_14")
        self.line_12 = QtWidgets.QFrame(Notebook)
        self.line_12.setGeometry(QtCore.QRect(1080, 170, 16, 531))
        self.line_12.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_15 = QtWidgets.QLabel(Notebook)
        self.label_15.setGeometry(QtCore.QRect(880, 160, 131, 51))
        self.label_15.setObjectName("label_15")
        self.line_13 = QtWidgets.QFrame(Notebook)
        self.line_13.setGeometry(QtCore.QRect(870, 330, 311, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(Notebook)
        self.line_14.setGeometry(QtCore.QRect(870, 390, 311, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(Notebook)
        self.line_15.setGeometry(QtCore.QRect(870, 690, 311, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.label_16 = QtWidgets.QLabel(Notebook)
        self.label_16.setGeometry(QtCore.QRect(880, 520, 131, 51))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Notebook)
        self.label_17.setGeometry(QtCore.QRect(880, 640, 131, 51))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Notebook)
        self.label_18.setGeometry(QtCore.QRect(880, 580, 201, 51))
        self.label_18.setObjectName("label_18")
        self.line_16 = QtWidgets.QFrame(Notebook)
        self.line_16.setGeometry(QtCore.QRect(870, 630, 311, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_18 = QtWidgets.QFrame(Notebook)
        self.line_18.setGeometry(QtCore.QRect(870, 570, 311, 16))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_17 = QtWidgets.QFrame(Notebook)
        self.line_17.setGeometry(QtCore.QRect(440, 270, 311, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.label_19 = QtWidgets.QLabel(Notebook)
        self.label_19.setGeometry(QtCore.QRect(450, 100, 251, 51))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Notebook)
        self.label_20.setGeometry(QtCore.QRect(450, 220, 131, 51))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Notebook)
        self.label_21.setGeometry(QtCore.QRect(450, 400, 131, 51))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Notebook)
        self.label_22.setGeometry(QtCore.QRect(450, 340, 131, 51))
        self.label_22.setObjectName("label_22")
        self.line_19 = QtWidgets.QFrame(Notebook)
        self.line_19.setGeometry(QtCore.QRect(440, 510, 311, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.label_23 = QtWidgets.QLabel(Notebook)
        self.label_23.setGeometry(QtCore.QRect(450, 280, 151, 51))
        self.label_23.setObjectName("label_23")
        self.line_20 = QtWidgets.QFrame(Notebook)
        self.line_20.setGeometry(QtCore.QRect(440, 450, 311, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(Notebook)
        self.line_21.setGeometry(QtCore.QRect(440, 210, 311, 16))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.label_24 = QtWidgets.QLabel(Notebook)
        self.label_24.setGeometry(QtCore.QRect(450, 460, 131, 51))
        self.label_24.setObjectName("label_24")
        self.line_22 = QtWidgets.QFrame(Notebook)
        self.line_22.setGeometry(QtCore.QRect(600, 170, 16, 351))
        self.line_22.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.label_25 = QtWidgets.QLabel(Notebook)
        self.label_25.setGeometry(QtCore.QRect(450, 160, 131, 51))
        self.label_25.setObjectName("label_25")
        self.line_23 = QtWidgets.QFrame(Notebook)
        self.line_23.setGeometry(QtCore.QRect(440, 330, 311, 16))
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(Notebook)
        self.line_24.setGeometry(QtCore.QRect(440, 390, 311, 16))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        
       
        

        self.retranslateUi(Notebook)
        QtCore.QMetaObject.connectSlotsByName(Notebook)

    def retranslateUi(self, Notebook):
        _translate = QtCore.QCoreApplication.translate
        Notebook.setWindowTitle(_translate("Notebook", "Dialog"))
        self.Ntbk_Title.setText(_translate("Notebook", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">NoteBook</span></p></body></html>"))
        self.label_2.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Suspects</span></p></body></html>"))
        self.label_3.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Scarlett</span></p></body></html>"))
        self.label_4.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Mustard</span></p></body></html>"))
        self.label_5.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Orchid</span></p></body></html>"))
        self.label_6.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Green</span></p></body></html>"))
        self.label_7.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Peacoke</span></p></body></html>"))
        self.label_8.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Plum</span></p></body></html>"))
        self.label_9.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Rooms</span></p></body></html>"))
        self.library_lab.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Library</span></p></body></html>"))
        self.billiary_label.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Billiard Room</span></p></body></html>"))
        self.label_12.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hall</span></p></body></html>"))
        self.label_13.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Conversary</span></p></body></html>"))
        self.label_14.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Ball Room</span></p></body></html>"))
        self.label_15.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Study</span></p></body></html>"))
        self.label_16.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Lounge</span></p></body></html>"))
        self.label_17.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Kitchen</span></p></body></html>"))
        self.label_18.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dining Room</span></p></body></html>"))
        self.label_19.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Weapons</span></p></body></html>"))
        self.label_20.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dagger</span></p></body></html>"))
        self.label_21.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Candlestick</span></p></body></html>"))
        self.label_22.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Rope</span></p></body></html>"))
        self.label_23.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Lead Pipe</span></p></body></html>"))
        self.label_24.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Wrench</span></p></body></html>"))
        self.label_25.setText(_translate("Notebook", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Revolver</span></p></body></html>"))


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Notebook = QtWidgets.QDialog()
    ui = Ui_Notebook()
    ui.setupUi(Notebook)
    Notebook.show()
    sys.exit(app.exec_())
'''