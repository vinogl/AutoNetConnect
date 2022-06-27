from message_window import Ui_MessageWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import os


class Message(QMainWindow, Ui_MessageWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.message_path = 'connect_message.txt'

        self.save_btn.clicked.connect(self.save_message)
        self.clear_btn.clicked.connect(self.clear_message)
        self.connect_btn.clicked.connect(self.connect)

        if os.path.exists(self.message_path):
            with open(self.message_path, 'r') as f_r:
                lines = f_r.readlines()
                self.user.setText(lines[0])
                self.password.setText(lines[1])

    def connect(self):
        from connect import connect
        user = self.user.text()
        password = self.password.text()
        connect(user=user, password=password)
        QMessageBox.about(self, '', '连接成功')

    def save_message(self):
        user = str(self.user.text())
        password = str(self.password.text())
        with open(self.message_path, 'w') as f_w:
            f_w.write(user + '\n' + password)

    def clear_message(self):
        if os.path.exists(self.message_path):
            os.remove(self.message_path)
        self.user.clear()
        self.password.clear()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Message()
    window.show()
    sys.exit(app.exec_())
