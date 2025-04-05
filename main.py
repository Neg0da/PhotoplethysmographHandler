# main.py

import Functions.sine_simul as sine_simul
import time
import math

simulated_arduino = True

def main():
    if simulated_arduino:
        sine_simul.simulate_sine_wave(frequency_hz=1.0)
    else:
        import Functions.device_manager
        arduino = Functions.device_manager.ArduinoConnection()
        try:
            arduino.connect()
            data = arduino.read_data()
            print(f"Received data: {data}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            arduino.disconnect()

if __name__ == "__main__":
    main()
