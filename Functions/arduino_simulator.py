# ./Functions/arduino_simulator.py

class ArduinoSimulator:
    def __init__(self, port, baudrate=9600):
        # Initialize the simulator with a port and baud rate
        self.port = port
        self.baudrate = baudrate

    def connect(self):
        """Simulate connecting to the port"""
        print(f"Arduino connected to port {self.port} with baud rate {self.baudrate}.")

    def read_data(self):
        """Simulate receiving data"""
        # Assume Arduino always responds with this string
        return "Received: Hello, Arduino!"

    def send_data(self, data):
        """Simulate sending data"""
        print(f"Data sent: {data}")

    def close(self):
        """Simulate closing the port"""
        print(f"Connection to port {self.port} closed.")
