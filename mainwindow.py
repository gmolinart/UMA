# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModelRenamer(object):
    def setupUi(self, ModelRenamer):
        ModelRenamer.setObjectName("ModelRenamer")
        ModelRenamer.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ModelRenamer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.treeView = QtWidgets.QTreeView(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setObjectName("treeView")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.treeView)
        self.horizontalLayout.addWidget(self.frame_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 39, 361, 461))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.resolution_lb = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.resolution_lb.setObjectName("resolution_lb")
        self.gridLayout_3.addWidget(self.resolution_lb, 0, 0, 1, 1)
        self.group_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.group_le.setObjectName("group_le")
        self.gridLayout_3.addWidget(self.group_le, 6, 1, 1, 1)
        self.index_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.index_le.setObjectName("index_le")
        self.gridLayout_3.addWidget(self.index_le, 3, 1, 1, 1)
        self.name_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.name_le.setObjectName("name_le")
        self.gridLayout_3.addWidget(self.name_le, 2, 1, 1, 1)
        self.name_lb = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout_3.addWidget(self.name_lb, 2, 0, 1, 1)
        self.index_lb = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.index_lb.setObjectName("index_lb")
        self.gridLayout_3.addWidget(self.index_lb, 3, 0, 1, 1)
        self.resolution_cb = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.resolution_cb.setObjectName("resolution_cb")
        self.gridLayout_3.addWidget(self.resolution_cb, 0, 1, 1, 1)
        self.mtl_cb = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.mtl_cb.setObjectName("mtl_cb")
        self.gridLayout_3.addWidget(self.mtl_cb, 1, 1, 1, 1)
        self.group_lb = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.group_lb.setObjectName("group_lb")
        self.gridLayout_3.addWidget(self.group_lb, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 8, 1, 1, 1)
        self.mtl_lb = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.mtl_lb.setObjectName("mtl_lb")
        self.gridLayout_3.addWidget(self.mtl_lb, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)
        self.position_lb = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.position_lb.setObjectName("position_lb")
        self.gridLayout_3.addWidget(self.position_lb, 4, 0, 1, 1)
        self.position_cb_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.position_cb_2.setObjectName("position_cb_2")
        self.gridLayout_3.addWidget(self.position_cb_2, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 7, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        ModelRenamer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModelRenamer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        ModelRenamer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModelRenamer)
        self.statusbar.setObjectName("statusbar")
        ModelRenamer.setStatusBar(self.statusbar)

        self.retranslateUi(ModelRenamer)
        QtCore.QMetaObject.connectSlotsByName(ModelRenamer)

    def retranslateUi(self, ModelRenamer):
        _translate = QtCore.QCoreApplication.translate
        ModelRenamer.setWindowTitle(_translate("ModelRenamer", "Model "))
        self.groupBox.setTitle(_translate("ModelRenamer", "GroupBox"))
        self.resolution_lb.setText(_translate("ModelRenamer", "Resolution"))
        self.name_lb.setText(_translate("ModelRenamer", "Name"))
        self.index_lb.setText(_translate("ModelRenamer", "Index"))
        self.group_lb.setText(_translate("ModelRenamer", "Group Name"))
        self.mtl_lb.setText(_translate("ModelRenamer", "Mtl Group"))
        self.label_6.setText(_translate("ModelRenamer", "Additional Attrs:"))
        self.position_lb.setText(_translate("ModelRenamer", "position"))
        self.pushButton.setText(_translate("ModelRenamer", "Refactor"))
