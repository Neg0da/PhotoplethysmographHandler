# main.py

# Importing the ArduinoSimulator class and the function to list connected devices
from Functions.arduino_simulator import ArduinoSimulator
from Functions.device_manager import list_connected_devices

def main():
    # Check if there are any connected devices
    devices = list_connected_devices()
    if devices:
        print("Connected devices:")
        for device in devices:
            print(device)
        
        # Create an object to simulate Arduino
        arduino = ArduinoSimulator(port=devices[0])  # Connect to the first device in the list
        arduino.connect()

        # Send data to Arduino
        arduino.send_data("Hello, Arduino!")
        
        # Read response from Arduino (simulation)
        data = arduino.read_data()
        if data:
            print(f"Received from Arduino: {data}")
        
        # Close the connection
        arduino.close()
    else:
        print("No connected serial devices.")

if __name__ == "__main__":
    main()
