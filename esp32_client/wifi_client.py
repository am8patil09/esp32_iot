import network
import time


#--- Wifi Configuration ---
SSID        = "XXXX"       #enter your ssid
PASSWORD    = "XXXX"       #enter wifi password
#--- Wifi Configuration ---


# --- Wifi Client to connect to WiFI ---
class WifiClient:
    def __init__(self, ssid, password):
        self.wlan = network.WLAN(network.STA_IF)
        self.ssid = ssid
        self.password = password

    def connect_wifi(self):
        #force restart connection to wifi
        #self.wlan.active(False)
        self.wlan.active(True)
        if not self.wlan.isconnected():
            print("Connecting to Wifi...")
            self.wlan.connect(self.ssid, self.password)
            while not self.wlan.isconnected():
                time.sleep(1)
                print("WiFi not connected yet ..")
        print ("Wifi connected. IP: " , self.wlan.ifconfig()[0])
