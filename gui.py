# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import multiscale_modeling as mm
import numpy as np            
import random
from statistics import mode
from statistics import StatisticsError
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import multiscale_modeling as mm

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 389)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../2847_icy-tower-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lab1 = QtWidgets.QLabel(self.centralwidget)
        self.lab1.setGeometry(QtCore.QRect(0, 5, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab1.setFont(font)
        self.lab1.setObjectName("lab1")
        self.width = QtWidgets.QTextEdit(self.centralwidget)
        self.width.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.width.setObjectName("width")
        self.lab1_2 = QtWidgets.QLabel(self.centralwidget)
        self.lab1_2.setGeometry(QtCore.QRect(340, 0, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab1_2.setFont(font)
        self.lab1_2.setObjectName("lab1_2")
        self.lab1_3 = QtWidgets.QLabel(self.centralwidget)
        self.lab1_3.setGeometry(QtCore.QRect(470, 0, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab1_3.setFont(font)
        self.lab1_3.setObjectName("lab1_3")
        self.lab1_4 = QtWidgets.QLabel(self.centralwidget)
        self.lab1_4.setGeometry(QtCore.QRect(580, 0, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab1_4.setFont(font)
        self.lab1_4.setObjectName("lab1_4")
        self.lab1_5 = QtWidgets.QLabel(self.centralwidget)
        self.lab1_5.setGeometry(QtCore.QRect(670, 0, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab1_5.setFont(font)
        self.lab1_5.setObjectName("lab1_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName("label")
        self.height = QtWidgets.QTextEdit(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(10, 110, 71, 31))
        self.height.setObjectName("height")
        self.height_2 = QtWidgets.QLabel(self.centralwidget)
        self.height_2.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.height_2.setObjectName("height_2")
        self.number_of_grains = QtWidgets.QTextEdit(self.centralwidget)
        self.number_of_grains.setGeometry(QtCore.QRect(150, 50, 71, 31))
        self.number_of_grains.setObjectName("number_of_grains")
        self.height_4 = QtWidgets.QLabel(self.centralwidget)
        self.height_4.setGeometry(QtCore.QRect(140, 30, 121, 16))
        self.height_4.setObjectName("height_4")
        self.import_image = QtWidgets.QTextEdit(self.centralwidget)
        self.import_image.setGeometry(QtCore.QRect(30, 280, 71, 31))
        self.import_image.setObjectName("import_image")
        self.height_3 = QtWidgets.QLabel(self.centralwidget)
        self.height_3.setGeometry(QtCore.QRect(30, 260, 171, 16))
        self.height_3.setObjectName("height_3")
        self.import_image_push = QtWidgets.QPushButton(self.centralwidget)
        self.import_image_push.setGeometry(QtCore.QRect(129, 280, 71, 31))
        self.import_image_push.setObjectName("import_image_push")
        self.draw_push = QtWidgets.QPushButton(self.centralwidget)
        self.draw_push.setGeometry(QtCore.QRect(120, 150, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.draw_push.setFont(font)
        self.draw_push.setObjectName("draw_push")
        self.von_neumann_check = QtWidgets.QCheckBox(self.centralwidget)
        self.von_neumann_check.setGeometry(QtCore.QRect(120, 120, 91, 17))
        self.von_neumann_check.setObjectName("von_neumann_check")
        self.moore_check = QtWidgets.QCheckBox(self.centralwidget)
        self.moore_check.setGeometry(QtCore.QRect(210, 120, 70, 17))
        self.moore_check.setObjectName("moore_check")
        self.height_5 = QtWidgets.QLabel(self.centralwidget)
        self.height_5.setGeometry(QtCore.QRect(130, 100, 141, 16))
        self.height_5.setObjectName("height_5")
        self.number_of_inclusions = QtWidgets.QTextEdit(self.centralwidget)
        self.number_of_inclusions.setGeometry(QtCore.QRect(330, 50, 71, 31))
        self.number_of_inclusions.setObjectName("number_of_inclusions")
        self.size_of_inclusions = QtWidgets.QTextEdit(self.centralwidget)
        self.size_of_inclusions.setGeometry(QtCore.QRect(330, 110, 71, 31))
        self.size_of_inclusions.setObjectName("size_of_inclusions")
        self.height_6 = QtWidgets.QLabel(self.centralwidget)
        self.height_6.setGeometry(QtCore.QRect(320, 30, 121, 16))
        self.height_6.setObjectName("height_6")
        self.height_7 = QtWidgets.QLabel(self.centralwidget)
        self.height_7.setGeometry(QtCore.QRect(320, 90, 121, 16))
        self.height_7.setObjectName("height_7")
        self.shape_square_check = QtWidgets.QCheckBox(self.centralwidget)
        self.shape_square_check.setGeometry(QtCore.QRect(310, 170, 70, 17))
        self.shape_square_check.setObjectName("shape_square_check")
        self.shape_circular_check = QtWidgets.QCheckBox(self.centralwidget)
        self.shape_circular_check.setGeometry(QtCore.QRect(370, 170, 70, 17))
        self.shape_circular_check.setObjectName("shape_circular_check")
        self.height_8 = QtWidgets.QLabel(self.centralwidget)
        self.height_8.setGeometry(QtCore.QRect(320, 150, 121, 16))
        self.height_8.setObjectName("height_8")
        self.add_inculsions_push = QtWidgets.QPushButton(self.centralwidget)
        self.add_inculsions_push.setGeometry(QtCore.QRect(300, 200, 141, 41))
        self.add_inculsions_push.setObjectName("add_inculsions_push")
        self.dp_grain_ID = QtWidgets.QTextEdit(self.centralwidget)
        self.dp_grain_ID.setGeometry(QtCore.QRect(570, 50, 61, 31))
        self.dp_grain_ID.setObjectName("dp_grain_ID")
        self.dp_grain_number = QtWidgets.QTextEdit(self.centralwidget)
        self.dp_grain_number.setGeometry(QtCore.QRect(570, 100, 61, 31))
        self.dp_grain_number.setObjectName("number")
        self.height_9 = QtWidgets.QLabel(self.centralwidget)
        self.height_9.setGeometry(QtCore.QRect(530, 30, 121, 16))
        self.height_9.setObjectName("height_9")
        self.dp_clear_push = QtWidgets.QPushButton(self.centralwidget)
        self.dp_clear_push.setGeometry(QtCore.QRect(570, 150, 61, 41))
        self.dp_clear_push.setObjectName("dp_clear_push")
        # self.dp_redraw_push = QtWidgets.QPushButton(self.centralwidget)
        # self.dp_redraw_push.setGeometry(QtCore.QRect(570, 200, 61, 41))
        # self.dp_redraw_push.setObjectName("dp_redraw_push")
        self.height_10 = QtWidgets.QLabel(self.centralwidget)
        self.height_10.setGeometry(QtCore.QRect(660, 30, 121, 16))
        self.height_10.setObjectName("height_10")
        self.draw1 = QtWidgets.QPushButton(self.centralwidget)
        self.draw1.setGeometry(QtCore.QRect(660, 50, 61, 41))
        self.draw1.setObjectName("draw1")
        # self.draw2 = QtWidgets.QPushButton(self.centralwidget)
        # self.draw2.setGeometry(QtCore.QRect(660, 100, 61, 41))
        # self.draw2.setObjectName("draw1")
        # self.draw3 = QtWidgets.QPushButton(self.centralwidget)
        # self.draw3.setGeometry(QtCore.QRect(660, 150, 61, 41))
        # self.draw3.setObjectName("draw3")
        self.save_push = QtWidgets.QPushButton(self.centralwidget)
        self.save_push.setGeometry(QtCore.QRect(120, 220, 91, 41))
        self.save_push.setObjectName("save_push")
        self.import_image_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.import_image_2.setGeometry(QtCore.QRect(30, 226, 71, 31))
        self.import_image_2.setObjectName("import_image_2")
        self.height_11 = QtWidgets.QLabel(self.centralwidget)
        self.height_11.setGeometry(QtCore.QRect(40, 200, 171, 16))
        self.height_11.setObjectName("height_11")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(0, 770, 951, 16))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.validate_push = QtWidgets.QPushButton(self.centralwidget)
        self.validate_push.setGeometry(QtCore.QRect(10, 150, 71, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.validate_push.setFont(font)
        self.validate_push.setObjectName("validate_push")
        self.first_add_inclusions_push = QtWidgets.QPushButton(self.centralwidget)
        self.first_add_inclusions_push.setGeometry(QtCore.QRect(300, 250, 141, 41))
        self.first_add_inclusions_push.setObjectName("first_add_inclusions_push")
        self.chances_to_draw = QtWidgets.QTextEdit(self.centralwidget)
        self.chances_to_draw.setGeometry(QtCore.QRect(460, 50, 61, 31))
        self.chances_to_draw.setObjectName("chances_to_draw")
        self.chances_to_draw_push = QtWidgets.QPushButton(self.centralwidget)
        self.chances_to_draw_push.setGeometry(QtCore.QRect(460, 90, 61, 41))
        self.chances_to_draw_push.setObjectName("chances_to_draw_push")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#-------------------MAGIC STARTS----------------------------------------------------------------#

        #przypisanie buttonom funkcji
        self.draw_push.clicked.connect(self.draw)#draw
        self.validate_push.clicked.connect(self.lab_2_validate) #validate
        self.save_push.clicked.connect(self.save_image_push) #save
        self.import_image_push.clicked.connect(self.spit_values_import) #import

        self.add_inculsions_push.clicked.connect(self.validate_values)
        self.first_add_inclusions_push.clicked.connect(self.draw_inclusions_before)

        self.dp_clear_push.clicked.connect(self.lab3_draw1)
        # self.dp_redraw_push.clicked.connect(self.lab3_draw2)
        # self.first_add_inclusions_push.clicked.connect(self.lab_2)

        self.draw1.clicked.connect(self.lab5_draw1)
        # self.draw2.clicked.connect(self.lab5_draw2)
        # self.draw3.clicked.connect(self.lab5_draw3)

    def lab5_draw1(self):
        self.width_draw = int(self.width.toPlainText())
        self.height_draw = int(self.height.toPlainText())
        self.number_of_grains_draw = int(self.number_of_grains.toPlainText())

        if self.von_neumann_check.isChecked():
            self.von_neumann_check_draw = True
            self.moore_check_draw = False
        else:
            self.von_neumann_check_draw = False
            self.moore_check_draw = True

        try:
            grain_grow = mm.Grain_grow()
            grain_grow.lab5_1(self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)
        except:
            grain_grow = mm.Grain_grow()
            grain_grow.lab5_1(self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)

    def lab5_draw2(self):
        grain_grow = mm.Grain_grow()
        grain_grow.lab5_2_draw()
    
    def lab5_draw3(self):
        pass

    def lab3_draw1(self):
        self.draw1 = int(self.dp_grain_ID.toPlainText())
        self.draw2 = int(self.dp_grain_number.toPlainText())
        self.width_draw = int(self.width.toPlainText())
        self.height_draw = int(self.height.toPlainText())
        self.number_of_grains_draw = int(self.number_of_grains.toPlainText())
        if self.von_neumann_check.isChecked():
            self.von_neumann_check_draw = True
            self.moore_check_draw = False
        else:
            self.von_neumann_check_draw = False
            self.moore_check_draw = True

        grain_grow3 = mm.Grain_grow()
        grain_grow3.draw_1st_phase(self.draw1, self.draw2, self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)


    def lab3_draw2(self):
        pass

    def draw_background(self):
        self.number_of_inclusions_draw = int(self.number_of_inclusions.toPlainText())
        self.size_of_inclusions_draw = int(self.size_of_inclusions.toPlainText())
        self.width_draw = int(self.width.toPlainText())
        self.height_draw = int(self.height.toPlainText())
        self.number_of_grains_draw = int(self.number_of_grains.toPlainText())
        
        if self.shape_square_check.isChecked():
            self.shape_square_check_bool = True
            self.shape_circular_check_bool = False
        else:
            self.shape_square_check_bool = False
            self.shape_circular_check_bool = True

        if self.von_neumann_check.isChecked():
            self.von_neumann_check_draw = True
            self.moore_check_draw = False
        else:
            self.von_neumann_check_draw = False
            self.moore_check_draw = True

        grain_grow2 = mm.Grain_grow()
        grain_grow2.draw_after_before(self.number_of_inclusions_draw, self.size_of_inclusions_draw, self.shape_square_check_bool, self.shape_circular_check_bool, self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)

    def lab_2_whole(self):
        self.width_draw = int(self.width.toPlainText())
        self.height_draw = int(self.height.toPlainText())
        self.number_of_inclusions_draw = int(self.number_of_inclusions.toPlainText())
        self.size_of_inclusions_draw = int(self.size_of_inclusions.toPlainText())
        if self.shape_square_check.isChecked():
            self.shape_square_check_bool = True
            self.shape_circular_check_bool = False
        else:
            self.shape_square_check_bool = False
            self.shape_circular_check_bool = True

        self.error_label.setText("Correct data")
        return self.width_draw, self.height_draw, self.number_of_inclusions_draw, self.size_of_inclusions_draw, self.shape_square_check_bool, self.shape_circular_check_bool

    def lab_2_validate(self):
        self.width_draw, self.height_draw, self.number_of_inclusions_draw, self.size_of_inclusions_draw, self.shape_square_check_bool, self.shape_circular_check_bool = self.lab_2_whole()
        grain_grow = mm.Grain_grow()
        grain_grow.final_image_lab2(self.width_draw, self.height_draw, self.number_of_inclusions_draw, self.size_of_inclusions_draw, self.shape_square_check_bool, self.shape_circular_check_bool)

    def validate_values(self):

        self.number_of_inclusions_draw = int(self.number_of_inclusions.toPlainText())
        self.size_of_inclusions_draw = int(self.size_of_inclusions.toPlainText())
        self.width_draw = int(self.width.toPlainText())
        self.height_draw = int(self.height.toPlainText())
        self.number_of_grains_draw = int(self.number_of_grains.toPlainText())
        
        if self.shape_square_check.isChecked():
            self.shape_square_check_bool = True
            self.shape_circular_check_bool = False
        else:
            self.shape_square_check_bool = False
            self.shape_circular_check_bool = True

        if self.von_neumann_check.isChecked():
            self.von_neumann_check_draw = True
            self.moore_check_draw = False
        else:
            self.von_neumann_check_draw = False
            self.moore_check_draw = True

        grain_grow2 = mm.Grain_grow()
        grain_grow2.validate_vals(self.number_of_inclusions_draw, self.size_of_inclusions_draw, self.shape_square_check_bool, self.shape_circular_check_bool, self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)

        print('validated', self.number_of_inclusions_draw, self.size_of_inclusions_draw, self.shape_square_check_bool, self.shape_circular_check_bool, self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)

    def draw_inclusions_before(self):
        self.number_of_inclusions_draw = int(self.number_of_inclusions.toPlainText())
        self.size_of_inclusions_draw = int(self.size_of_inclusions.toPlainText())
        self.width_draw = int(self.width.toPlainText())
        self.height_draw = int(self.height.toPlainText())
        self.number_of_grains_draw = int(self.number_of_grains.toPlainText())
        
        if self.shape_square_check.isChecked():
            self.shape_square_check_bool = True
            self.shape_circular_check_bool = False
        else:
            self.shape_square_check_bool = False
            self.shape_circular_check_bool = True

        if self.von_neumann_check.isChecked():
            self.von_neumann_check_draw = True
            self.moore_check_draw = False
        else:
            self.von_neumann_check_draw = False
            self.moore_check_draw = True

        grain_grow2 = mm.Grain_grow()
        grain_grow2.draw_inc_before(self.number_of_inclusions_draw, self.size_of_inclusions_draw, self.shape_square_check_bool, self.shape_circular_check_bool, self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)
    
    def draw(self):

        self.width_draw = int(self.width.toPlainText())
        self.height_draw = int(self.height.toPlainText())
        self.number_of_grains_draw = int(self.number_of_grains.toPlainText())

        if self.von_neumann_check.isChecked():
            self.von_neumann_check_draw = True
            self.moore_check_draw = False
        else:
            self.von_neumann_check_draw = False
            self.moore_check_draw = True
        try:
            grain_grow = mm.Grain_grow()
            grain_grow.start(self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)
        except:
            grain_grow = mm.Grain_grow()
            grain_grow.start(self.width_draw, self.height_draw, self.number_of_grains_draw, self.von_neumann_check_draw, self.moore_check_draw)

    #save   
    def save_image_push(self):
            self._save_ = self.save_image.toPlainText()
            self.clear_padding_and_axis()
            plt.savefig('{}.png'.format(self._save_), bbox_inches = 'tight',
                        pad_inches = 0)
            
    #import
    def spit_values_import(self):
        try:
            self._import_image_ = str(self.import_image.toPlainText())
            img = mpimg.imread('{}.png'.format(self._import_image_))
            plt.matshow(img)
            plt.show()
            

        except:
            self.error_label.setText("Did not found such file... try again.")
            # self.spit_values_import()
            
    
#-------------------MAGIC ENDS----------------------------------------------------------------#

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multiscale Modeling"))
        self.lab1.setText(_translate("MainWindow", "Lab1"))
        self.lab1_2.setText(_translate("MainWindow", "Lab2"))
        self.lab1_3.setText(_translate("MainWindow", "Lab3"))
        self.lab1_4.setText(_translate("MainWindow", "Lab4"))
        self.lab1_5.setText(_translate("MainWindow", "Lab5"))
        self.label.setText(_translate("MainWindow", "Width"))
        self.height_2.setText(_translate("MainWindow", "Height"))
        self.height_4.setText(_translate("MainWindow", "Number of grains"))
        self.height_3.setText(_translate("MainWindow", "Insert name of an imageto import"))
        self.import_image_push.setText(_translate("MainWindow", "IMPORT"))
        self.draw_push.setText(_translate("MainWindow", "DRAW"))
        self.von_neumann_check.setText(_translate("MainWindow", "Von Neumann"))
        self.moore_check.setText(_translate("MainWindow", "Moore"))
        self.height_5.setText(_translate("MainWindow", "Select method of drawing"))
        self.height_6.setText(_translate("MainWindow", "Number of inclusions "))
        self.height_7.setText(_translate("MainWindow", "Size of inclusions"))
        self.shape_square_check.setText(_translate("MainWindow", "square"))
        self.shape_circular_check.setText(_translate("MainWindow", "circular"))
        self.height_8.setText(_translate("MainWindow", "Shape of inclusions"))
        self.add_inculsions_push.setText(_translate("MainWindow", "ADD INCLUSIONS AFTER"))
        self.height_9.setText(_translate("MainWindow", "Save grain ID/Grains"))
        self.dp_clear_push.setText(_translate("MainWindow", "DRAW"))
        # self.dp_redraw_push.setText(_translate("MainWindow", "DRAW 2"))
        self.height_10.setText(_translate("MainWindow", "Boundaries"))
        self.draw1.setText(_translate("MainWindow", "DRAW"))
        # self.draw2.setText(_translate("MainWindow", "DRAW 2"))
        # self.draw3.setText(_translate("MainWindow", "DRAW 3"))
        self.save_push.setText(_translate("MainWindow", "SAVE"))
        self.height_11.setText(_translate("MainWindow", "Insert name of an imageto save"))
        self.validate_push.setText(_translate("MainWindow", "VALIDATE"))
        self.first_add_inclusions_push.setText(_translate("MainWindow", "ADD INCLUSIONS BEFORE"))
        self.chances_to_draw_push.setText(_translate("MainWindow", "RE-DRAW"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionImport.setShortcut(_translate("MainWindow", "Ctrl+I"))

    def clear_padding_and_axis(self):
        plt.gca().set_axis_off()
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
                    hspace = 0, wspace = 0)
        plt.margins(0,0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
