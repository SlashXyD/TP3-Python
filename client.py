
import requests
from PyQt5.QtWidgets import QMessageBox
class Main():
    def query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":

    main = Main()
    hostname = "127.0.0.1:8000"
    res = main.query(hostname)
    if res:
        print(res)

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your IP:", self)
        self.label1.move(10, 1)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 30)

        self.label5 = QLabel("Enter your API Key:", self)
        self.label5.move(10, 70)
        self.text5 = QLineEdit(self)
        self.text5.move(10, 100)

        self.label6 = QLabel("Enter the Hostname:", self)
        self.label6.move(10, 140)
        self.text6 = QLineEdit(self)
        self.text6.move(10, 170)


        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 210)
        self.button = QPushButton("Send", self)
        self.button.move(10, 240)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text6.text()
#        ip = self.text1.text()
#        api_key = self.text5.text()

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname)
            if res:
                self.label2.setText("Answer%s" % (res["Hello"]))
                self.label2.adjustSize()
                self.show()

    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()

    #Run the app
    app.exec_()