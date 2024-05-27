import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from Auth.authClass import AuthWindow
from docx import Document
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH

def center_window(window):
    screen = QApplication.primaryScreen()
    window.setGeometry(
        int(screen.size().width() / 2 - window.frameSize().width() / 2),
        int(screen.size().height() / 2 - window.frameSize().height() / 2),
        window.frameSize().width(),
        window.frameSize().height()
    )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        * {
            background: rgb(243, 255, 234);
            font-size: 14pt;
        }
    """)
    
    auth_window = AuthWindow()
    auth_window.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    center_window(auth_window)
    #auth_window.setGeometry(0 ,0 , WINDOW_WIDTH, WINDOW_HEIGHT)
    
    auth_window.show()
    sys.exit(app.exec_())