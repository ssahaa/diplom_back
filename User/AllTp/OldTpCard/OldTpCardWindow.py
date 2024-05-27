import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from WindowsPY.OldTpCard import Ui_MainWindow
from User.AllTp.TpCard.TpCardFunctions import getUserDataID
import requests
import os
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window

class OldTpCard(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None,data={}, dataMainTP= {}):
        super().__init__(parent)
        self.setupUi(self)
        self.data = data
        self.dataMainTp = dataMainTP
        self.initUI()
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)

        
    
    def initUI(self):
        self.pushButtonBack.clicked.connect(self.go_back)
        self.labelCreationDate.setText(self.data['creationDate'])
        self.labelCreationDate_2.setText('ТП есть' if self.data['dock'] else "ТП Нет")
        self.pushButtonDownload.clicked.connect(self.downloadNewTp)

    def downloadNewTp(self):
        url = self.data['dock']
        save_path = self.lineEditPath.text()
        if url is None:
            return
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(save_path, "Старый ТП" + " " + self.dataMainTp['TpName'] + " от "+ self.data['creationDate'] + ".docx")
            try:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    file.close()
            except:
                pass

    def go_back(self):
        self.close()
        self.parent().show()




# Отправляем GET-запрос для загрузки файла


# Проверяем, успешно ли загружен файл
