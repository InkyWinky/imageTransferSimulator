
import socket
import time 
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QApplication, QStatusBar
from PyQt5.QtCore import Qt
import sys
import os
import cv2
import math
# Constants
def start_client(PORT):
    #This function connects the client to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create server AF_INET = IP, INET stands for interbet
    client.connect(('localhost', PORT))
    return client

def start_sending_images(client, fps, chunk_size=4096):
    #This function sends images at a specified fps
    #Default chunksize is 4096 bytes for each image chunk

    EOF_IMAGE = b'\n\n' #Identifies when an image ends in socket stream
    starting_time = time.perf_counter() #start timing immediately after connection
    IMAGE_FOLDER = 'imageData/'
    file_list = os.listdir(IMAGE_FOLDER) #Get a list of all the file names in the image folder


    for filename in file_list:
        
        file = open(os.path.join(IMAGE_FOLDER+filename), 'rb') #read file
        image_data = file.read(chunk_size)
        while image_data: #while still reading the image send chunks of it over
            client.send(image_data)
            image_data = file.read(chunk_size)
        client.send(EOF_IMAGE)
        send_time = time.perf_counter()- starting_time
        file.close()
        print("sent " + filename + " at time ", send_time)
        time.sleep(1/fps)

def close_client(client):
    #This function closes the client
    client.close()

        

class MainWindow(QMainWindow):
    def __init__(self,client):
        super().__init__()
        self.pixel_height = 7.04
        self.focal_length = 5
        self.working_dist = 1100
        self.train_speed = 130
        self.image_height = 512
        self.client = client

        self.setGeometry(0, 0, 500, 463)
        self.setWindowTitle("Client Camera Configuration Settings")

        centralwidget = QWidget(self)
        self.setCentralWidget(centralwidget)

        self.SendImagesButton = QPushButton(centralwidget)
        self.SendImagesButton.setGeometry(190, 340, 121, 31)
        self.SendImagesButton.setText("Send Images")
        self.SendImagesButton.clicked.connect(self.update_settings)

        self.headingLabel = QLabel(centralwidget)
        self.headingLabel.setGeometry(140, 0, 211, 41)
        font = self.headingLabel.font()
        font.setPointSize(14)
        font.setBold(True)
        self.headingLabel.setFont(font)
        self.headingLabel.setText("Configuration Settings")

        #Heading
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
        self.image_height_label = QLabel()
        self.image_height_label.setText("Image Height ")
        self.verticalLayout_3.addWidget(self.image_height_label)

        verticalLayoutWidget_2 = QWidget(centralwidget)
        verticalLayoutWidget_2.setGeometry(270, 80, 71, 121)
        self.verticalLayout_4 = QVBoxLayout(verticalLayoutWidget_2)
        self.lineEdit = QLineEdit() #pixel height in micro metres
        self.lineEdit.setText(str(self.pixel_height))
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setText(str(self.focal_length))#focal length in mm
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QLineEdit()
        self.lineEdit_3.setText(str(self.working_dist)) #working distance in mm
        self.verticalLayout_4.addWidget(self.lineEdit_3)

        self.lineEdit_img_height = QLineEdit()
        self.lineEdit_img_height.setText(str(self.image_height)) #working distance in mm
        self.verticalLayout_4.addWidget(self.lineEdit_img_height)

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
        self.lineEdit_4.setText(str(self.train_speed))#train speed in km/hr
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
        self.label_pixels = QLabel()
        self.label_pixels.setText("pixels")
        self.verticalLayout_8.addWidget(self.label_pixels)

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


    def update_settings(self):
        new_pixel_height = self.lineEdit.text()
        new_focal_length = self.lineEdit_2.text()
        new_working_dist = self.lineEdit_3.text()
        new_train_speed = self.lineEdit_4.text()
        new_image_height = self.lineEdit_img_height.text()

        try:
            self.pixel_height = float(new_pixel_height)
            self.focal_length = float(new_focal_length)
            self.working_dist = float(new_working_dist)
            self.train_speed = float(new_train_speed)
            self.image_height=float(new_image_height)
        except ValueError:
            print("Invalid values.")
        fps = calculate_fps(self.pixel_height, self.focal_length,self.working_dist, self.train_speed, self.image_height)
        self.label_13.setText(str(fps))
        time.sleep(1)
        start_sending_images(self.client, fps)
def calculate_fps(ph, fl, wd, spd, ih):
    vert_fov_deg = 2*math.atan(ph*(10**-3)/(2*fl))
    vert_fov_mm = 2*(math.tan(vert_fov_deg/2)*wd)
    mmps = spd*((1000*100*10)/(60*60))
    acq =mmps/vert_fov_mm
    fps = acq/ih
    return fps



def open_gui(client):
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow(client)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    PORT = 8080
    client = start_client(PORT)
    open_gui(client)
