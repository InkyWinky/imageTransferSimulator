import socket
import cv2
import numpy as np

def receive_images_from_server(server_ip, server_port):
    CHUNK_SIZE = 4096
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    EOF_IMAGE = b'\n\n'
    print("Waiting for connection...")
    client_socket, address = server_socket.accept()
    print("Connected to:", address)
    image_data = b''


    while True:
        try:
            # Receive image data from the client
            image_data = b''
            while True:
                chunk = client_socket.recv(CHUNK_SIZE)
                if chunk.endswith(EOF_IMAGE):
                    break
                image_data += chunk

            # Convert image data to OpenCV format
            nparr = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Display the received image
            cv2.imshow('Received Image', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop if 'q' is pressed
                break
        except Exception as e:
            print("Error receiving image:", e)
            break

    client_socket.close()
    server_socket.close()

# Usage
if __name__ == "__main__":
    server_ip = 'localhost'  # Listen on all available network interfaces
    server_port = 8080

    receive_images_from_server(server_ip, server_port)