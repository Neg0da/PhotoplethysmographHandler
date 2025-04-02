# main.py

import Functions.device_manager
from Functions.simple_debug import debug
from Functions.print_scale import print_scale  # Importing the function to print the scale
import time
import config

arduino = Functions.device_manager.ArduinoConnection()

def main():
    print("TEST...")
    arduino.find_arduino_port()
    arduino.connect()
    
    data = arduino.read_data()
    print(f"Received data: {data}")

    arduino.disconnect()

if __name__ == "__main__":
    main()

