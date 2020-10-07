# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lista.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ListWindow(object):
    def setupUi(self, ListWindow):
        if not ListWindow.objectName():
            ListWindow.setObjectName(u"ListWindow")
        ListWindow.resize(484, 338)
        self.centralwidget = QWidget(ListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tb_covid = QTableWidget(self.centralwidget)
        if (self.tb_covid.columnCount() < 4):
            self.tb_covid.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_covid.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_covid.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_covid.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_covid.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_covid.setObjectName(u"tb_covid")
        self.tb_covid.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.tb_covid)

        ListWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ListWindow)
        self.statusbar.setObjectName(u"statusbar")
        ListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListWindow)

        QMetaObject.connectSlotsByName(ListWindow)
    # setupUi

    def retranslateUi(self, ListWindow):
        ListWindow.setWindowTitle(QCoreApplication.translate("ListWindow", u"Lista de Casos de COVID 19", None))
        ___qtablewidgetitem = self.tb_covid.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListWindow", u"DNI", None));
        ___qtablewidgetitem1 = self.tb_covid.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ListWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tb_covid.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListWindow", u"Apellido", None));
        ___qtablewidgetitem3 = self.tb_covid.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ListWindow", u"Fecha", None));
    # retranslateUi

