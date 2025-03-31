# ./Functions/device_manager.py

import serial
import serial.tools.list_ports
import time

class ArduinoConnection:
    def __init__(self, baudrate=9600, timeout=1):
        """
        Initializes the ArduinoConnection class with default baudrate and timeout.
        """
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def find_arduino_port(self):
        """
        Searches for an Arduino device among available COM ports.
        Returns the port name if found, otherwise returns None.
        """
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(f"Found port: {port.device}, VID: {port.vid}, PID: {port.pid}, Description: {port.description}")
            # Check for official Arduino VID (0x2341) or common clone VID (0x1A86)
            if port.vid in [0x2341, 0x1A86]:
                return port.device
        return None

    def connect(self):
        """
        Connects to the detected Arduino device.
        If no Arduino is found, prints an error message.
        """
        port = self.find_arduino_port()
        if port:
            try:
                # Establish a serial connection with the detected port
                self.serial_conn = serial.Serial(port, self.baudrate, timeout=self.timeout)
                time.sleep(2)  # Wait for Arduino initialization
                print(f"Connected to {port}")
            except serial.SerialException as e:
                print(f"Connection error: {e}")
                self.serial_conn = None
        else:
            print("Arduino not found")

    def send_data(self, data):
        """
        Sends data to the connected Arduino.
        If no connection exists, prints an error message.
        """
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.write(f"{data}\n".encode())
        else:
            print("Error: No connection to Arduino")

    def read_data(self):
        """
        Reads data from the connected Arduino.
        Returns the received data as a string, or None if no connection exists.
        """
        if self.serial_conn and self.serial_conn.is_open:
            return self.serial_conn.readline().decode().strip()
        return None

    def disconnect(self):
        """
        Closes the serial connection to the Arduino.
        """
        if self.serial_conn:
            self.serial_conn.close()
            print("Connection closed")

# Example usage
if __name__ == "__main__":
    arduino = ArduinoConnection()
    print("Checking available COM ports:")
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"{port.device}: {port.description} (VID: {port.vid}, PID: {port.pid})")
    
    # Attempt to connect to Arduino
    arduino.connect()
    
    if arduino.serial_conn:
        # Send data to Arduino
        arduino.send_data("Hello Arduino")
        # Read response from Arduino
        response = arduino.read_data()
        if response:
            print("Received:", response)
        # Disconnect from Arduino
        arduino.disconnect()