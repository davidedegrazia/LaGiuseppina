
import json
from datetime import datetime, timedelta

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Progetto.pianodilavoro.controller.ControllorePianoLavoro import ControllorePianoLavoro


class VistaPianoLavoro(object):
   def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 646)
        MainWindow.setMinimumSize(QtCore.QSize(0, 625))
        MainWindow.setMaximumSize(QtCore.QSize(692, 646))
        MainWindow.setStyleSheet("border: none;"
                                 "background-color: rgb(235,235,235); ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(692, 625))
        self.centralwidget.setMaximumSize(QtCore.QSize(692, 589))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_superiore = QtWidgets.QFrame(self.centralwidget)
        self.frame_superiore.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superiore.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superiore.setObjectName("frame_superiore")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superiore)
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_superiore)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 185))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color: rgb(255,255,255);"
                                      "color: rgb(0,0,0);")
        self.verticalLayout_10.addWidget(self.listWidget)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_att_compl = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_att_compl.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_att_compl.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";\n"
                                                "border-top-color: rgb(255, 0, 26);\n"
                                                "background-color: rgb(0, 160, 0);\n"
                                                "border-radius: 12px;\n"
                                                "color: rgb(255, 255, 255);")
        self.pushButton_att_compl.setObjectName("pushButton_att_compl")
        self.horizontalLayout_13.addWidget(self.pushButton_att_compl)
        self.pushButton_att_non_compl = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_att_non_compl.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_att_non_compl.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";\n"
                                                    "border-top-color: rgb(255, 0, 26);\n"
                                                    "background-color: rgb(209, 0, 0);\n"
                                                    "border-radius: 12px;\n"
                                                    "color: rgb(255, 255, 255);")
        self.pushButton_att_non_compl.setObjectName("pushButton_att_non_compl")
        self.horizontalLayout_13.addWidget(self.pushButton_att_non_compl)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_9.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";\n"
                                        "border-top-color: rgb(255, 0, 26);\n"
                                        "background-color: rgb(112, 112, 112);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 12px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_13.addWidget(self.pushButton_9)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.frame_superiore)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 72)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                      "border-top-color: rgb(255, 0, 26);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 12px;"
                                      "color: rgb(0,0,0);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_2.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                        "border-top-color: rgb(255, 0, 26);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 12px;"
                                        "color: rgb(0,0,0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_3.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                        "border-top-color: rgb(255, 0, 26);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 12px;"
                                        "color: rgb(0,0,0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(120, 42))
        self.pushButton_4.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                        "border-top-color: rgb(255, 0, 26);\n"
                                        "background-color: rgb(0, 122, 254);\n"
                                        "border-radius: 17px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_superiore)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_visualizza_task = QtWidgets.QWidget()
        self.page_visualizza_task.setObjectName("page_visualizza_task")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_visualizza_task)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_nome_titolo = QtWidgets.QLabel(self.page_visualizza_task)
        self.label_nome_titolo.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_nome_titolo.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                             "color: rgb(0,0,0);")
        self.label_nome_titolo.setObjectName("label_nome_titolo")
        self.verticalLayout_4.addWidget(self.label_nome_titolo)
        self.frame_bianco = QtWidgets.QFrame(self.page_visualizza_task)
        self.frame_bianco.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 16px;\n"
                                        "")
        self.frame_bianco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bianco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bianco.setObjectName("frame_bianco")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_bianco)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_nome_attivita = QtWidgets.QLabel(self.frame_bianco)
        self.label_nome_attivita.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                               "color: rgb(0,0,0);")
        self.label_nome_attivita.setObjectName("label_nome_attivita")
        self.verticalLayout_5.addWidget(self.label_nome_attivita)
        self.label_descrizione = QtWidgets.QLabel(self.frame_bianco)
        self.label_descrizione.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                             "color: rgb(0,0,0);")
        self.label_descrizione.setObjectName("label_descrizione")
        self.verticalLayout_5.addWidget(self.label_descrizione)
        self.label_assegnatari = QtWidgets.QLabel(self.frame_bianco)
        self.label_assegnatari.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                             "color: rgb(0,0,0);")
        self.label_assegnatari.setObjectName("label_assegnatari")
        self.verticalLayout_5.addWidget(self.label_assegnatari)
        self.label_giorniallascad = QtWidgets.QLabel(self.frame_bianco)
        self.label_giorniallascad.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                                "color: rgb(0,0,0);")
        self.label_giorniallascad.setObjectName("label_giorniallascad")
        self.verticalLayout_5.addWidget(self.label_giorniallascad)
        self.label_completata = QtWidgets.QLabel(self.frame_bianco)
        self.label_completata.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                            "color: rgb(0,0,0);")
        self.label_completata.setObjectName("label_completata")
        self.verticalLayout_5.addWidget(self.label_completata)
        self.verticalLayout_4.addWidget(self.frame_bianco)
        self.stackedWidget.addWidget(self.page_visualizza_task)
        self.page_crea_attivita = QtWidgets.QWidget()
        self.page_crea_attivita.setObjectName("page_crea_attivita")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_crea_attivita)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.page_crea_attivita)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_7.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                   "color: rgb(0,0,0);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.frame_biannco_2 = QtWidgets.QFrame(self.page_crea_attivita)
        self.frame_biannco_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-radius: 16px;\n"
                                           "")
        self.frame_biannco_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_biannco_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_biannco_2.setObjectName("frame_biannco_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_biannco_2)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(-1, 12, -1, 12)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                   "color: rgb(0,0,0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.lineEdit_nome_task = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_nome_task.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_nome_task.setStyleSheet("border-radius: 10px;\n"
                                              "background-color: rgb(235, 235, 235);"
                                              "color: rgb(0,0,0);")
        self.lineEdit_nome_task.setObjectName("lineEdit_nome_task")
        self.horizontalLayout_2.addWidget(self.lineEdit_nome_task)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                   "color: rgb(0,0,0);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_descrizione = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_descrizione.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_descrizione.setStyleSheet("border-radius: 10px;\n"
                                                "background-color: rgb(235, 235, 235);"
                                                "color: rgb(0,0,0);")
        self.lineEdit_descrizione.setObjectName("lineEdit_descrizione")
        self.horizontalLayout_3.addWidget(self.lineEdit_descrizione)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        self.label_10.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.lineEdit_assegnatari = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_assegnatari.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_assegnatari.setStyleSheet("border-radius: 10px;\n"
                                                "background-color: rgb(235, 235, 235);"
                                                "color: rgb(0,0,0);")
        self.lineEdit_assegnatari.setObjectName("lineEdit_assegnatari")
        self.horizontalLayout_4.addWidget(self.lineEdit_assegnatari)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.frame_7 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(12, -1, 355, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setMaximumSize(QtCore.QSize(120000, 16777215))
        self.label_11.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.dateEdit_new = QtWidgets.QDateEdit(self.frame_7)
        self.dateEdit_new.setMinimumSize(QtCore.QSize(0, 25))
        self.dateEdit_new.setMaximumSize(QtCore.QSize(120, 16777215))
        self.dateEdit_new.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: rgb(235, 235, 235);"
                                        "color: rgb(0,0,0);")
        self.dateEdit_new.setObjectName("dateEdit_new")

        tday = datetime.today().date()
        input_date = self.dateEdit_new.date().toPyDate()
        self.dateEdit_new.setDate(input_date)

        self.horizontalLayout_5.addWidget(self.dateEdit_new)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.frame_11 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setContentsMargins(400, 0, 110, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_salva_task = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_salva_task.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_salva_task.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                 "border-top-color: rgb(255, 0, 26);\n"
                                                 "background-color: rgb(0, 122, 254);\n"
                                                 "border-radius: 17px;\n"
                                                 "color: rgb(255, 255, 255);")
        self.pushButton_salva_task.setObjectName("pushButton_salva_task")
        self.horizontalLayout_6.addWidget(self.pushButton_salva_task)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.verticalLayout_6.addWidget(self.frame_biannco_2)
        self.stackedWidget.addWidget(self.page_crea_attivita)
        self.page_modifica_task = QtWidgets.QWidget()
        self.page_modifica_task.setObjectName("page_modifica_task")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_modifica_task)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_titolo_modifica = QtWidgets.QLabel(self.page_modifica_task)
        self.label_titolo_modifica.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                                 "color: rgb(0,0,0);")
        self.label_titolo_modifica.setObjectName("label_titolo_modifica")
        self.verticalLayout_9.addWidget(self.label_titolo_modifica)
        self.frame_bianco_3 = QtWidgets.QFrame(self.page_modifica_task)
        self.frame_bianco_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 16px;\n"
                                          "")
        self.frame_bianco_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bianco_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bianco_3.setObjectName("frame_bianco_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_bianco_3)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_12 = QtWidgets.QFrame(self.frame_bianco_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setContentsMargins(-1, 12, -1, 12)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.frame_12)
        self.label_12.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.lineEdit_modifica_nome = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_modifica_nome.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_modifica_nome.setStyleSheet("border-radius: 10px;\n"
                                                  "background-color: rgb(235, 235, 235);"
                                                  "color: rgb(0,0,0);")
        self.lineEdit_modifica_nome.setText("")
        self.lineEdit_modifica_nome.setObjectName("lineEdit_modifica_nome")
        self.horizontalLayout_7.addWidget(self.lineEdit_modifica_nome)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_bianco_3)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.frame_13)
        self.label_13.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.lineEdit_modifca_descrizione = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_modifca_descrizione.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_modifca_descrizione.setStyleSheet("border-radius: 10px;\n"
                                                        "background-color: rgb(235, 235, 235);"
                                                        "color: rgb(0,0,0);")
        self.lineEdit_modifca_descrizione.setObjectName("lineEdit_modifca_descrizione")
        self.horizontalLayout_8.addWidget(self.lineEdit_modifca_descrizione)
        self.verticalLayout_8.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_bianco_3)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.frame_14)
        self.label_14.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.lineEdit_modifica_assegnatari = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_modifica_assegnatari.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_modifica_assegnatari.setStyleSheet("border-radius: 10px;\n"
                                                         "background-color: rgb(235, 235, 235);"
                                                         "color: rgb(0,0,0);")
        self.lineEdit_modifica_assegnatari.setObjectName("lineEdit_modifica_assegnatari")
        self.horizontalLayout_9.addWidget(self.lineEdit_modifica_assegnatari)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_bianco_3)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setContentsMargins(12, -1, 355, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.frame_15)
        self.label_15.setMaximumSize(QtCore.QSize(120000, 16777215))
        self.label_15.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.dateEdit_mod = QtWidgets.QDateEdit(self.frame_15)
        self.dateEdit_mod.setMinimumSize(QtCore.QSize(0, 25))
        self.dateEdit_mod.setMaximumSize(QtCore.QSize(120, 16777215))
        self.dateEdit_mod.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: rgb(235, 235, 235);"
                                        "color: rgb(0,0,0);")
        self.dateEdit_mod.setObjectName("dateEdit_mod")
        self.dateEdit_mod.setDate(input_date)
        self.horizontalLayout_10.addWidget(self.dateEdit_mod)
        self.verticalLayout_8.addWidget(self.frame_15)
        self.frame_17 = QtWidgets.QFrame(self.frame_bianco_3)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_completata = QtWidgets.QCheckBox(self.frame_17)
        self.checkBox_completata.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                               "color: rgb(0,0,0);")
        self.checkBox_completata.setObjectName("checkBox_completata")
        self.horizontalLayout_12.addWidget(self.checkBox_completata)
        self.verticalLayout_8.addWidget(self.frame_17)
        self.frame_16 = QtWidgets.QFrame(self.frame_bianco_3)
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setContentsMargins(400, 0, 110, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_modifica_attivita = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_modifica_attivita.setMinimumSize(QtCore.QSize(130, 35))
        self.pushButton_modifica_attivita.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                        "border-top-color: rgb(255, 0, 26);\n"
                                                        "background-color: rgb(0, 122, 254);\n"
                                                        "border-radius: 17px;\n"
                                                        "color: rgb(255, 255, 255);")
        self.pushButton_modifica_attivita.setObjectName("pushButton_modifica_attivita")
        self.horizontalLayout_11.addWidget(self.pushButton_modifica_attivita)
        self.verticalLayout_8.addWidget(self.frame_16)
        self.verticalLayout_9.addWidget(self.frame_bianco_3)
        self.stackedWidget.addWidget(self.page_modifica_task)
        self.page_vuota = QtWidgets.QWidget()
        self.page_vuota.setObjectName("page_vuota")
        self.stackedWidget.addWidget(self.page_vuota)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # popolo la lista widget delle task
        self.controllore = ControllorePianoLavoro()
        for task in self.controllore.get_lista_task():
                self.listWidget.addItem(task.nome_task)

        # mette in lista solo le task completate
        def task_completate():
            self.listWidget.setStyleSheet("color: rgb(0, 160, 0);"
                                          "background-color: rgb(255,255,255);")
            self.listWidget.clear()
            with open('pianodilavoro/data/lista_task.json') as f:
                tasks = json.load(f)
            for task in tasks:
                if task['completata'] == "True":
                   self.listWidget.addItem(task['nome_task'])
        self.pushButton_att_compl.clicked.connect(lambda: task_completate())

        # mette in lista solo le task non completate
        def task_non_completate():
            self.listWidget.setStyleSheet("color: rgb(209, 0, 0);"
                                          "background-color: rgb(255,255,255);")
            self.listWidget.clear()
            with open('pianodilavoro/data/lista_task.json') as f:
                tasks = json.load(f)
            for task in tasks:
                if task['completata'] == "False":
                   self.listWidget.addItem(task['nome_task'])
        self.pushButton_att_non_compl.clicked.connect(lambda: task_non_completate())

        # mette in lista tutte le task
        def task_tutte():
            self.listWidget.setStyleSheet("color: rgb(0, 0, 0);"
                                              "background-color: rgb(255,255,255);")
            self.listWidget.clear()
            with open('pianodilavoro/data/lista_task.json') as f:
                tasks = json.load(f)
            for task in tasks:
                   self.listWidget.addItem(task['nome_task'])
        self.pushButton_9.clicked.connect(lambda: task_tutte())

        # visualizza le info di una task
        def visualizza_task():
            try:
                indice_di_controllo = self.listWidget.selectedIndexes()[0].row()
                self.stackedWidget.setCurrentWidget(self.page_visualizza_task)
                nomeselezionato = self.listWidget.currentItem().text()

                with open('pianodilavoro/data/lista_task.json') as f:
                        tasks = json.load(f)
                        selected = []
                        for task in tasks:
                            if task['nome_task'] == nomeselezionato:
                                task_richiesta = {
                                   "nome_task": task['nome_task'],
                                   "descrizione": task['descrizione'],
                                   "assegnatari": task['assegnatari'],
                                   "giorni_rimanenti_alla_scadenza": str(task['giorni_rimanenti_alla_scadenza']),
                                   "completata": str(task['completata'])
                                 }
                                selected.append(task_richiesta)

                self.label_nome_titolo.setText(selected[0]['nome_task'])
                self.label_nome_attivita.setText("Nome attività: " + str(selected[0]['nome_task']))
                self.label_descrizione.setText("Descrizione: " + str(selected[0]['descrizione']))
                self.label_assegnatari.setText("Assegnatari: " + str(selected[0]['assegnatari']))
                self.label_giorniallascad.setText("Data scadenza: " + str(selected[0]['giorni_rimanenti_alla_scadenza']))

                if selected[0]['completata'] == "False":
                        completata = "No"
                else:
                        completata = "Si"
                self.label_completata.setText("Completata: " + completata)
            except Exception:
                QMessageBox.setStyleSheet(MainWindow,"color: rgb(0, 0, 0); background-color: rgb(235, 235, 235); border:none;")
                QMessageBox.critical(MainWindow, 'ERRORE!', "Selezionare prima un'attività dalla lista!", QMessageBox.Ok, QMessageBox.Ok)

        self.pushButton.clicked.connect(lambda: visualizza_task())

        # aggiunge in lista e salva una nuova task
        def aggiungi_nuova_task():
                self.stackedWidget.setCurrentWidget(self.page_crea_attivita)
                self.dateEdit_new.setMinimumDate(QtCore.QDate(2022, datetime.today().date().day, datetime.today().date().month))
                tday = datetime.today().date()
                self.dateEdit_new.setDate(QtCore.QDate(2022, 11, 5))


                nometask = self.lineEdit_nome_task.text()
                descrizione = self.lineEdit_descrizione.text()
                assegnatari = self.lineEdit_assegnatari.text()

                input_date = self.dateEdit_new.date().toPyDate()
                days_to_expiry = input_date - tday
                completata = False

                if nometask == "" or descrizione == "" or assegnatari == "" or days_to_expiry.days == 0:
                        QMessageBox.setStyleSheet(MainWindow,
                                                  "color: rgb(0, 0, 0); background-color: rgb(235, 235, 235); border:none")
                        QMessageBox.critical(MainWindow, 'ERRORE!', 'Completa tutti i campi richiesti!', QMessageBox.Ok,
                                             QMessageBox.Ok)

                else:

                        task_creata = {
                                "nome_task": nometask,
                                "descrizione": descrizione,
                                "assegnatari": [assegnatari],
                                "giorni_rimanenti_alla_scadenza": days_to_expiry.days,
                                "completata": str(completata)
                        }

                        with open("pianodilavoro/data/lista_task.json", "r+") as file:
                                data = json.load(file)
                                data.append(task_creata)
                                file.seek(0)
                                json.dump(data, file)
                        self.listWidget.addItem(nometask)

                        self.lineEdit_nome_task.clear()
                        self.lineEdit_descrizione.clear()
                        self.lineEdit_assegnatari.clear()
                        self.dateEdit_new.setDate(tday)

                        QMessageBox.about(MainWindow, "", "La nuova attività è stata salvata con successo!")
                        QMessageBox.setStyleSheet(MainWindow, "color: rgb(0,0,0);"
                                                              "background-color: rgb(235, 235, 235);"
                                                              "border: none;")

        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_crea_attivita))
        def set_today_date():
            self.dateEdit_new.setDate(QtCore.QDate(2022, datetime.today().date().month, datetime.today().date().day))
        self.pushButton_4.clicked.connect(lambda: set_today_date())
        self.pushButton_salva_task.clicked.connect(lambda: aggiungi_nuova_task())

        # elimina una task selezionata dall'utente
        def elimina_task():
          try:
            indice_eccezioni = self.listWidget.selectedIndexes()[0].row()
            nomeselezionato = self.listWidget.currentItem().text()
            with open('pianodilavoro/data/lista_task.json') as f:
                tasks = json.load(f)
                i = 0
                for task in tasks:
                    if task['nome_task'] == nomeselezionato:
                       break
                    else: i = i+1
                QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0);"
                                                      "background-color: rgb(235, 235, 235);"
                                                      "border: none")
                q = QMessageBox.question(MainWindow, '', "Sei sicuro di voler eliminare " + "'"+ tasks[i]['nome_task'] + "'" + " dalla lista delle attività?", QMessageBox.Yes | QMessageBox.No)
                nome_da_eliminare = tasks[i]['nome_task']
                if q == QMessageBox.Yes:
                   del tasks[i]
                   with open("pianodilavoro/data/lista_task.json", 'w') as f:
                       json.dump(tasks, f)
                   with open('pianodilavoro/data/lista_task.json') as f:
                        lista_aggiornata = json.load(f)
                        self.listWidget.clear()
                        for task_aggiornata in lista_aggiornata:
                          self.listWidget.addItem(task_aggiornata['nome_task'])
                   self.stackedWidget.setCurrentWidget(self.page_vuota)
                   QMessageBox.about(MainWindow, "", "L'attività '" + nome_da_eliminare + "' è stata eliminata dalla lista!" )
                   QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0);"
                                                      "background-color: rgb(235, 235, 235);"
                                                      "border: none;")

                else: pass

          except Exception:
              QMessageBox.setStyleSheet(MainWindow,
                                        "color: rgb(0, 0, 0); background-color: rgb(235, 235, 235); border:none;")
              QMessageBox.critical(MainWindow, 'ERRORE!', "Selezionare prima un'attività dalla lista!", QMessageBox.Ok,QMessageBox.Ok)


        self.pushButton_3.clicked.connect(lambda: elimina_task())

        # modifica una task selezionata dall'utente
        def modifica_task():
            self.stackedWidget.setCurrentWidget(self.page_modifica_task)
            nomeselezionato = self.listWidget.currentItem().text()
            with open('pianodilavoro/data/lista_task.json') as f:
                tasks = json.load(f)
                i = 0
                for task in tasks:
                    if task['nome_task'] == nomeselezionato:
                        break
                    else:
                        i = i + 1
            self.lineEdit_modifica_nome.setText(tasks[i]['nome_task'])
            self.lineEdit_modifca_descrizione.setText(tasks[i]['descrizione'])
            self.lineEdit_modifica_assegnatari.setText(str(tasks[i]['assegnatari']))
            tday = datetime.today().date()
            difference_days = timedelta(days= tasks[i]['giorni_rimanenti_alla_scadenza'])
            day_expiry = tday + difference_days
            self.dateEdit_mod.setDate(QtCore.QDate(2022, day_expiry.month, day_expiry.day))
            """
            def update_task():

                tasks[i]['nome_task'] = self.lineEdit_modifica_nome.text()
                tasks[i]['descrizione'] = self.lineEdit_modifca_descrizione.text()
                tasks[i]['assegnatari'] = self.lineEdit_assegnatari.text

                tday = datetime.today().date()
                expiry_date = self.dateEdit_mod.date().toPyDate()
                days_to_expiry = expiry_date - tday
                tasks[i]['giorni_rimanenti_alla_scadenza'] = days_to_expiry.days

                if self.checkBox_completata.isChecked():
                   tasks[i]['completata'] = "True"
                else: tasks[i]['completata'] = "False"
                with open('pianodilavoro/data/lista_task.json', 'w') as f:
                    json.dump(tasks, f)

                print(tasks[i])
            self.pushButton_modifica_attivita.clicked.connect(lambda: update_task())
            """
        self.pushButton_2.clicked.connect(lambda: modifica_task())



   def retranslateUi(self, MainWindow):
     _translate = QtCore.QCoreApplication.translate
     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
     __sortingEnabled = self.listWidget.isSortingEnabled()
     self.listWidget.setSortingEnabled(False)

     self.listWidget.setSortingEnabled(__sortingEnabled)
     self.pushButton_att_compl.setText(_translate("MainWindow", "Mostra attività \n"
                                                                " completate"))
     self.pushButton_att_non_compl.setText(_translate("MainWindow", "Mostra attività \n"
                                                                    " non completate"))
     self.pushButton_9.setText(_translate("MainWindow", "Mostra tutte \n"
                                                        " le attività "))
     self.pushButton.setText(_translate("MainWindow", "Visualizza"))
     self.pushButton_2.setText(_translate("MainWindow", "Modifica"))
     self.pushButton_3.setText(_translate("MainWindow", "Elimina"))
     self.pushButton_4.setText(_translate("MainWindow", "Crea una \n"
                                                        " nuova attività"))
     self.label_nome_titolo.setText(_translate("MainWindow", "New Item 1"))
     self.label_nome_attivita.setText(_translate("MainWindow", "Nome attività: "))
     self.label_descrizione.setText(_translate("MainWindow", "Descrizione:"))
     self.label_assegnatari.setText(_translate("MainWindow", "Assegnatari:"))
     self.label_giorniallascad.setText(_translate("MainWindow", "Giorni rimanenti alla scadenza: "))
     self.label_completata.setText(_translate("MainWindow", "Completata: "))
     self.label_7.setText(_translate("MainWindow", "Crea una nuova attività!"))
     self.label_8.setText(_translate("MainWindow", "Nome attività: "))
     self.label_9.setText(_translate("MainWindow", "Descrizione:"))
     self.label_10.setText(_translate("MainWindow", "Assegnatari:"))
     self.label_11.setText(_translate("MainWindow", "Data scadenza:"))
     self.pushButton_salva_task.setText(_translate("MainWindow", "Salva attività"))
     self.label_titolo_modifica.setText(_translate("MainWindow", "New Item 1"))
     self.label_12.setText(_translate("MainWindow", "Nome attività: "))
     self.label_13.setText(_translate("MainWindow", "Descrizione:"))
     self.label_14.setText(_translate("MainWindow", "Assegnatari:"))
     self.label_15.setText(_translate("MainWindow", "Data scadenza:"))
     self.checkBox_completata.setText(_translate("MainWindow", "Completata"))
     self.pushButton_modifica_attivita.setText(_translate("MainWindow", "Modifica attività"))
