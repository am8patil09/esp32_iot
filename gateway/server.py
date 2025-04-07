import socket


SERVER_IP   = "0.0.0.0" #enter your server ip where you want to send data
SERVER_PORT = 8989 #enter your server port where you want to send data

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

print("Listening for connection...")
while True:
    try:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Client disconnected")
                break
            print("Recieved data: ", data.decode().strip())
    except Exception as e:
        print("Exception: ", e)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break
