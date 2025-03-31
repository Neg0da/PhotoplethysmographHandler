# ./Functions/arduino_simulator.py

import math # This module is used for numerical operations
import time # This module is used for time-related functions
from Functions.debug import debug # Importing the debug module for logging

class ArduinoSimulator:
    def __init__(self, port, baudrate=9600):
        """Initialize the simulator with a port and baud rate"""
        self.port = port
        self.baudrate = baudrate
        self.connected = False
        self.start_time = time.time()  # Store the start time for sine wave simulation

    def connect(self):
        """Simulate connecting to the port"""
        if not self.connected:
            self.connected = True
            debug(f"Arduino connected to port {self.port} with baud rate {self.baudrate}.")
        else:
            debug("Arduino is already connected.")

    def retrieve_data(self):
        """Simulate sinus simulation and retrieving data from the Arduino"""
        if not self.connected:
            debug("Error: Cannot retrieve data. Arduino is not connected.")
        
        elapsed_time = time.time() - self.start_time  # Час роботи симулятора
        frequency = 1  # 1 Гц
        amplitude = 1  # Амплітуда 1
        sine_value = amplitude * math.sin(2 * math.pi * frequency * elapsed_time)

        return round(sine_value, 4)

    def close(self):
        """Simulate closing the connection"""
        if self.connected:
            self.connected = False
            debug(f"Connection to port {self.port} closed.")
        else:
            debug("Arduino is already disconnected.")
