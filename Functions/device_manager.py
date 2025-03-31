import serial.tools.list_ports
from Functions.debug import debug

def list_connected_devices():
    """Перевіряє всі підключені серійні пристрої."""
    ports = list(serial.tools.list_ports.comports())
    
    if not ports:
        debug("No devices connected.")
        return []

    # Створюємо список підключених пристроїв
    connected_devices = [port.device for port in ports]

    # Логуємо знайдені пристрої
    debug(f"Connected devices: {connected_devices}")
    for port in ports:
        debug(f"Device: {port.device}, Description: {port.description}")

    return connected_devices