from json import tool
import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("my main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("./icons/monkey.png"), "your button", self)
        button_action.setStatusTip("this is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("./icons/block.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        toolbar.addSeparator()
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addSeparator()
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("Click", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()