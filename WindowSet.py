import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
screen_size = screen.size()
screen_width = screen_size.width()
screen_height = screen_size.height()

WINDOW_WIDTH = int(screen_width * 0.9)
WINDOW_HEIGHT = int(screen_height * 0.9)

CENTER_X = int(screen_width - WINDOW_WIDTH)
CENTER_Y = int(screen_width - WINDOW_HEIGHT) 



def center_window(window):
    screen = QApplication.primaryScreen()
    window.setGeometry(
        int(screen.size().width() / 2 - window.frameSize().width() / 2),
        int(screen.size().height() / 2 - window.frameSize().height() / 2),
        window.frameSize().width(),
        window.frameSize().height()
    )