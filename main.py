import sys
import threading
from time import sleep
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")

class Backend(QObject):
    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(str, arguments=['updater'])
    def updater(self, dt_string):
        self.updated.emit(dt_string)

    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()
    def _bootUp(self):
        while True:
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            self.updater(dt_string)
            sleep(0.1)


QQuickWindow.setSceneGraphBackend('software')
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')
back_end = Backend()
engine.rootObjects()[0].setProperty('backend', back_end)
engine.rootObjects()[0].setProperty('currTime', dt_string)

back_end.bootUp()

sys.exit(app.exec())