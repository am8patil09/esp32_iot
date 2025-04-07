import time
import socket
import sys

SERVER_IP   = "xx:xx:xx:xx" #enter your server ip where you want to send data
SERVER_PORT = 8989 #enter your server port where you want to send data

# --- Data publisher to send data to server ---
class DataPublisherSocket:
    def __init__(self, connect_retry = 5):
        self.connect_retry = connect_retry
        self.sock = self.socket_init()

    def socket_init(self):
        sock = None
        for i in range(self.connect_retry):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((SERVER_IP, SERVER_PORT))
                print("Connected to server")
                return sock
            except Exception as e:
                print("Socket couldnt connect to server Error: %s. Ensure server is running on Server IP: %s and Server Port: %s" %(e, SERVER_IP, str(SERVER_PORT)))
                print("Retry attempts left %d" %(self.connect_retry - i - 1))
                time.sleep(2)
        print("Maximum Socket Connect Attempts reached. Exiting...")
        sys.exit(1) #Exit after max retries

    def send_data(self, data):
        try:
            self.sock.send(data.encode())
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            sys.exit(1)
        except OSError:
            self.sock = self.socket_init()
            print("Error Sending message over socket. Reconnecting...")
        except Exception as e:
            print(e)
            sys.exit(1)


#--- Sensor Data queue ---
class PublisherQueue:
    def __init__(self, lock):
        self.queue = []
        self.lock = lock

    def get_q_data(self):
        if len(self.queue) > 0:
            data = self.queue.pop(0)
            return data
        else:
            return None

    def add_q_data(self, data):
        self.queue.append(data)
