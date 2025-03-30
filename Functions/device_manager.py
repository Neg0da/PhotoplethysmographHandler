# device_manager.py

import serial.tools.list_ports

def list_connected_devices():
    """Перевіряє всі підключені серійні пристрої."""
    ports = list(serial.tools.list_ports.comports())
    connected_devices = []
    for port in ports:
        connected_devices.append(port.device)
    return connected_devices
