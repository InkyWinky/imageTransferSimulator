from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QApplication, QStatusBar
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 500, 463)
        self.setWindowTitle("MainWindow")

        centralwidget = QWidget(self)
        self.setCentralWidget(centralwidget)

        self.SendImagesButton = QPushButton(centralwidget)
        self.SendImagesButton.setGeometry(190, 340, 121, 31)
        self.SendImagesButton.setText("Send Images")

        self.headingLabel = QLabel(centralwidget)
        self.headingLabel.setGeometry(140, 0, 211, 41)
        font = self.headingLabel.font()
        font.setPointSize(14)
        font.setBold(True)
        self.headingLabel.setFont(font)
        self.headingLabel.setText("Configuration Settings")

        self.label_3 = QLabel(centralwidget)
        self.label_3.setGeometry(40, 40, 56, 19)
        font = self.label_3.font()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("Camera")

        verticalLayoutWidget = QWidget(centralwidget)
        verticalLayoutWidget.setGeometry(80, 80, 161, 121)
        self.verticalLayout_3 = QVBoxLayout(verticalLayoutWidget)
        self.label = QLabel()
        self.label.setText("Pixel Height ")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QLabel()
        self.label_2.setText("Focal Length ")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QLabel()
        self.label_4.setText("Working Distance ")
        self.verticalLayout_3.addWidget(self.label_4)

        verticalLayoutWidget_2 = QWidget(centralwidget)
        verticalLayoutWidget_2.setGeometry(270, 80, 71, 121)
        self.verticalLayout_4 = QVBoxLayout(verticalLayoutWidget_2)
        self.lineEdit = QLineEdit()
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.lineEdit_2 = QLineEdit()
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QLineEdit()
        self.verticalLayout_4.addWidget(self.lineEdit_3)

        self.line = QLabel(centralwidget)
        self.line.setGeometry(40, 60, 421, 16)
        self.line.setFrameShape(QLabel.HLine)
        self.line.setFrameShadow(QLabel.Sunken)

        self.label_5 = QLabel(centralwidget)
        self.label_5.setGeometry(40, 250, 56, 19)
        font = self.label_5.font()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setText("Train")

        self.line_2 = QLabel(centralwidget)
        self.line_2.setGeometry(40, 270, 421, 16)
        self.line_2.setFrameShape(QLabel.HLine)
        self.line_2.setFrameShadow(QLabel.Sunken)

        verticalLayoutWidget_3 = QWidget(centralwidget)
        verticalLayoutWidget_3.setGeometry(80, 280, 161, 41)
        self.verticalLayout_5 = QVBoxLayout(verticalLayoutWidget_3)
        self.label_6 = QLabel()
        self.label_6.setText("Speed")
        self.verticalLayout_5.addWidget(self.label_6)

        verticalLayoutWidget_4 = QWidget(centralwidget)
        verticalLayoutWidget_4.setGeometry(270, 280, 71, 41)
        self.verticalLayout_6 = QVBoxLayout(verticalLayoutWidget_4)
        self.lineEdit_4 = QLineEdit()
        self.verticalLayout_6.addWidget(self.lineEdit_4)

        verticalLayoutWidget_5 = QWidget(centralwidget)
        verticalLayoutWidget_5.setGeometry(350, 280, 117, 41)
        self.verticalLayout_7 = QVBoxLayout(verticalLayoutWidget_5)
        self.label_9 = QLabel()
        self.label_9.setText("km/hr")
        self.verticalLayout_7.addWidget(self.label_9)

        verticalLayoutWidget_6 = QWidget(centralwidget)
        verticalLayoutWidget_6.setGeometry(350, 80, 61, 121)
        self.verticalLayout_8 = QVBoxLayout(verticalLayoutWidget_6)
        self.label_10 = QLabel()
        self.label_10.setText("um")
        self.verticalLayout_8.addWidget(self.label_10)
        self.label_11 = QLabel()
        self.label_11.setText("mm")
        self.verticalLayout_8.addWidget(self.label_11)
        self.label_12 = QLabel()
        self.label_12.setText("mm")
        self.verticalLayout_8.addWidget(self.label_12)

        self.label_7 = QLabel(centralwidget)
        self.label_7.setGeometry(80, 390, 159, 31)
        self.label_7.setText("Image Transfer Rate:")

        self.label_8 = QLabel(centralwidget)
        self.label_8.setGeometry(270, 390, 115, 31)
        self.label_8.setText("Images per second")

        self.label_13 = QLabel(centralwidget)
        self.label_13.setGeometry(220, 390, 41, 31)
        self.label_13.setText("0")

        self.menubar = self.menuBar()
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
