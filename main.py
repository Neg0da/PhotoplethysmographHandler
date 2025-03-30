# main.py

# Importing the ArduinoSimulator class and the function to list connected devices
from Functions.arduino_simulator import ArduinoSimulator
from Functions.device_manager import list_connected_devices
from Functions.debug import debug
from Functions.print_scale import print_scale  # Importing the function to print the scale
import time
import config

def main():
    devices = list_connected_devices()  # List all connected devices
    if not devices:
        debug("No devices connected.")
        return
    
    arduino = ArduinoSimulator(devices[0])  # Create an instance of ArduinoSimulator with the first connected device
    arduino.connect()  # Simulate the connection

    debug("Starting Arduino simulator...")

    # Infinite loop to simulate retrieving and printing sine wave values
    try:
        while True:
            sine_value = arduino.retrieve_data()  # Get the sine wave data
            print_scale(sine_value)
            time.sleep(config.SLEEP_TIME)  # Wait for n second before getting the next value


    except KeyboardInterrupt:
        # Gracefully handle program exit when the user presses Ctrl+C
        debug("Simulation stopped by user.")
        arduino.close()  # Close the Arduino simulator connection
    

if __name__ == "__main__":
    main()

