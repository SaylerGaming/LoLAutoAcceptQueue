import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from design import Ui_MainWindow
from PySide6.QtGui import QFontDatabase
import webbrowser
from threading import Thread

from mainWithClasses import main as QueueLogic
from config import Config
from bot import main as telegramBot
from createImages import create, doesImagesExists

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.config = Config()

        if self.config.isFirstLaunch:
            create('./src/acceptQueueExample.png', 'https://i.ibb.co.com/vZYKXcx/acceptQueue.png')
            create('./src/inQueueExample.png', 'https://i.ibb.co.com/hfq4r1Q/inQueue.png')
            self.config.isFirstLaunch = False

        self.ui.le_chat_id.setText(self.config.chatId)
        self.ui.le_in_queue_sensitivity.setText(f'{self.config.inQueueSensitivity}')
        self.ui.le_accept_queue_sensitivity.setText(f'{self.config.queueSencitivity}')

        QFontDatabase.addApplicationFont('fonts/Rubik-Regular.ttf')
        if self.config.writableToChat:
            self.ui.checkBox.click()
        self.ui.btn_find_game.clicked.connect(lambda: self.findQueue())
        self.ui.btn_write_bot.clicked.connect(lambda: self.writeToBot())
        self.ui.btn_set_id.clicked.connect(lambda: self.setData(self.ui.le_chat_id.text(), self.ui.le_accept_queue_sensitivity.text(), self.ui.le_in_queue_sensitivity.text(), self.ui.checkBox.isChecked()))
        
    def findQueue(self):
        if doesImagesExists():
            Thread(target=lambda: QueueLogic(self), daemon=True).start()
            
        else:
            self.openDialogWindow('Ошибка', 'Изображения не были созданы!')
    def writeToBot(self):
        webbrowser.open('https://t.me/LeagueNotifierBot')
        telegramBot()
    def setData(self, chatId, queueSencitivity, inQueueSensitivity, writableToChat):
        self.config.setData(chatId, queueSencitivity, inQueueSensitivity, writableToChat)
    def setWritableToChat(self, value):
        self.config.setWritableToChat(value)
    def setStatusQueue(self, value):
        self.ui.lbl_status.setText(value)
    def openDialogWindow(self, title, text):
        dialog = QMessageBox()
        dialog.setText(text)
        dialog.setWindowTitle(title)
        dialog.setIcon(QMessageBox.Icon.Critical)
        dialog.exec()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()