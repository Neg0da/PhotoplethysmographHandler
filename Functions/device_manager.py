import serial
import time

def find_arduino():
    """Знаходить підключений Arduino за VID/PID або описом."""
    print("Searching for connected devices...")
    ports = list(serial.tools.list_ports.comports())

    if not ports:
        print("No devices connected.")
        return None

    for port in ports:
        print(f"Found port: {port.device}, Description: {port.description}, VID: {port.vid}")
        if "Arduino" in port.description or port.vid == 0x2341:  # 0x2341 - VID для більшості Arduino
            print(f"Arduino found: {port.device}")
            return port.device

    print("No Arduino found.")
    return None

def connect_to_arduino():
    """Шукає Arduino і підключається до нього."""
    print("Attempting to connect to Arduino...")
    arduino_port = find_arduino()
    if not arduino_port:
        print("Arduino is not connected.")
        return None

    try:
        print(f"Opening serial connection to {arduino_port}...")
        ser = serial.Serial(arduino_port, baudrate=9600, timeout=2)  # timeout збільшено для тесту
        print(f"Connected to Arduino on {arduino_port}")
        return ser
    except serial.SerialException as e:
        print(f"Failed to connect to Arduino: {e}")
        return None

if __name__ == "__main__":
    # Тестування функцій
    ser = connect_to_arduino()
    if ser:
        print("Connection successful!")
        time.sleep(2)  # Затримка для тестування
        ser.close()
        print("Connection closed.")
    else:
        print("Connection failed.")
