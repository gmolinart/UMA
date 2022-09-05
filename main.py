"""This is a core moduele for my qt app """


import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QTableWidget, QWidget


class StatusComboBox(QtWidgets.QComboBox):
    def __init__(self):
        super().__init__()
        self.items = ["done", "in progress", "waiting"]
        self.addItems(self.items)


class ProjectsComboBox(QtWidgets.QComboBox):
    def __init__(self):
        super().__init__()
        self.items = ["projectA", "projectB", "projectC"]
        self.addItems(self.items)


class VersionComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def __init__(self, version_list):
        super().__init__()
        self.items = version_list
        self.addItems(self.items)

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(VersionComboBox, self).showPopup()


class TaskTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(6)

        self.setHorizontalHeaderLabels(
            ["Task", "Version", "Status", "Bid\nDays", "Hours\nWorked", "Due\nDate "]
        )
        self.verticalHeader().hide()

        header = self.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def add_row(self):
        """adds row to current table """
        row_position = self.rowCount()
        return self.insertRow(row_position)

    def add_column(self):
        """Adds column to current table """
        column_position = self.columnCount()
        self.insertColumn(column_position)

    def add_row_from_list(self, items: list):
        column = 0
        row = self.rowCount() - 1
        self.add_row()
        for item in items:
            if item in StatusComboBox().items:
                status_combo = StatusComboBox()
                status_combo.setCurrentText(item)
                self.setCellWidget(row, column, status_combo)
            elif "." in item:
                version_combo = VersionComboBox([item])
                version_combo.setCurrentText(item)
                version_combo.popupAboutToBeShown.connect(
                    lambda: self.populate_version_combo(version_combo)
                )
                self.setCellWidget(row, column, version_combo)
            else:
                self.setItem(row, column, QtWidgets.QTableWidgetItem(item))
            column += 1
            self.update()

    def populate_version_combo(self, combo_box):
        all_items = [combo_box.itemText(i) for i in range(combo_box.count())]

        # fetch versions
        items = "001.000 001.001 001.002 ".split()

        for item in items:
            if item not in all_items:
                combo_box.addItem(item)


def load_style_sheet(style_file="stylesheet.css"):
    file_ = os.path.join(__file__.split("UMA")[0], "UMA", "resources", style_file)
    f = open(file_, "r")
    data = f.read()
    data.strip("\n")
    # path = APP_PATH.replace('\\', '/')
    # data = data.replace('<PATH>', path)
    return data



class Comments(QtWidgets.QWidget):
    """docstring for AnimatedWindow"""

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        self.pos_x = parent.frameGeometry().width() + 550
        self.pos_y = parent.frameGeometry().height()
        self.layout = QtWidgets.QVBoxLayout()
        self.messages_layout= QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        




        self.setStyleSheet("background-color:#313436;")

        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setStyleSheet("color:white;")
        self.send_message_btn = QtWidgets.QPushButton('send')

        self.layout.addLayout(self.messages_layout)
        self.layout.addSpacerItem(
            QtWidgets.QSpacerItem(
                300, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
            )
         )
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.send_message_btn)
        self.add_message('hello')
        self.add_message('hello')

        self.send_message_btn.clicked.connect(self.add_new_message)

    def add_new_message(self):
        self.add_message(self.text_edit.toPlainText())
        
    def add_message(self, message):

        self.message = QWidget()
        self.message.setStyleSheet("background-color:#3e454c;border-radius:15px;")
        self.message.resize(300, 100)
        self.message.setMinimumHeight(50)
        self.messages_layout.addWidget(self.message)
        self.text_layout = QtWidgets.QVBoxLayout(self.message)
        self.text = QtWidgets.QLabel(message)
        self.text_layout.addWidget(self.text)
        self.text.setWordWrap(True)
        self.text.setStyleSheet("color:white;padding:15px")  
        



    def open(self):
        self.anim = QtCore.QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(800)
        self.anim.setStartValue(QtCore.QRect(self.pos_x, self.pos_y, 0, 500))
        self.anim.setEndValue(QtCore.QRect(self.pos_x, self.pos_y, 500, 500))
        self.anim.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.anim.start()


class MyTasks(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.comments = None
        self.main_window = QtWidgets.QWidget()
        self.layout_item = QtWidgets.QVBoxLayout()
        self.header = QtWidgets.QHBoxLayout()
        self.table = TaskTable()
        self.populate_table()
        self.setCentralWidget(self.main_window)
        self.main_window.setLayout(self.layout_item)

        self.show_comments_btn = QtWidgets.QPushButton("Show\nComments")
        # :::::::::::::::HEADER:::::::::::::::::::
        self.header.addWidget(QtWidgets.QLabel("My Tasks"))
        self.header.addSpacerItem(
            QtWidgets.QSpacerItem(
                300, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
            )
        )
        self.header.addWidget(ProjectsComboBox())
        self.header.addWidget(self.show_comments_btn)
        self.show_comments_btn.clicked.connect(self.show_comments_window)

        self.layout_item.addLayout(self.header)
        self.layout_item.addWidget(self.table)

    def show_comments_window(self, checked):
        if not self.comments:
            self.comments = Comments(self.main_window)
            self.comments.setStyleSheet(load_style_sheet())
            self.comments.show()
            self.comments.open()

    def populate_table(self):
        self.table.add_row_from_list(
            ["0010_0020_lighting", "001.012", "in progress", "3", "1", "9/13"]
        )
        self.table.add_row_from_list(
            ["0010_0020_lighting", "001.012", "in progress", "3", "1", "9/13"]
        )
        self.table.add_row_from_list(
            ["0010_0020_lighting", "001.012", "in progress", "3", "1", "9/13"]
        )
        self.table.add_row_from_list(
            ["0010_0020_lighting", "001.012", "in progress", "3", "1", "9/13"]
        )
        self.table.add_row_from_list(
            ["0010_0020_lighting", "001.012", "in progress", "3", "1", "9/13"]
        )
        self.table.add_row_from_list(
            ["0010_0020_lighting", "001.012", "in progress", "3", "1", "9/13"]
        )


app = QApplication(sys.argv)
tasks = MyTasks()
tasks.show()


app.setStyleSheet(load_style_sheet())
# Start the event loop.
app.exec()
