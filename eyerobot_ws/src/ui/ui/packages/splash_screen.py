import os
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen
import sys
sys.append(1, '..')
from .configs.

class SplashScreen:
    def __init__(self):
        self.splash = QSplashScreen()
        self.splash.setPixmap(QPixmap("../icons/logo_black.jpg"))
        self.splash.showMessage("<h1 style='color:white;'>Medical Autonomy and Precision Surgery Laboratory</h1>",
                                alignment=Qt.AlignBottom | Qt.AlignHCenter)

    def show(self):
        self.splash.show()

    def finish(self, replacing_ui: PyQt5.QtWidgets.QWidget):
        self.splash.finish(replacing_ui)
