
import socket
import time 
from PyQt5.QtWidgets import *
import os
import cv2
# Constants
PORT = 8080
IMAGE_PRERFIX = "scene"
IMAGE_STARTING_NUMBER = "04051"
IMAGE_ENDING_NUMBER = ""
NUMBER_JUMP = 50
CHUNK_SIZE = 4096
EOF_IMAGE = b'\n\n'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create server AF_INET = IP, INET stands for interbet
client.connect(('localhost', PORT))
# file = open("imageData\cees.jpg", 'rb')
# image = cv2.imread("imageData\scene04051.png")
# cv2.imshow('image', image)
image_folder = 'imageData/'
file_list = os.listdir(image_folder)
starting_time = time.perf_counter()
while True:
    for filename in file_list:
        
        file = open(os.path.join(image_folder+filename), 'rb')
        image_data = file.read(CHUNK_SIZE)
        while image_data:
            client.send(image_data)
            image_data = file.read(CHUNK_SIZE)
        client.send(EOF_IMAGE)
        send_time = time.perf_counter()- starting_time
        print("sent " + filename + " at time ", send_time)
        time.sleep(1/45)
        
file.close()
client.close()
# # def main():
# #     app = QApplication([])
# #     window = QWidget()
# #     window.show()
# #     app.exec_()

# # if __name__=='__main__':
# #     main()
