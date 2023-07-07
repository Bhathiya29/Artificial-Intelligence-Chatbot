from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Adding the chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.geometry(10, 10, 480, 320)  # Coordinates of the area
        self.chat_area.setReadOnly(True)

        # Adding the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.geometry(10, 340, 480, 40)  # Coordinates of the area

        # Adding the button
        self.button = QPushButton('Send', self)
        self.button.geometry(500, 340, 100, 40)  # Coordinates of the button


        self.show()


class Chatbot:
    pass


app = QApplication()
main_window = ChatbotWindow()
sys.exit(app.exec())
