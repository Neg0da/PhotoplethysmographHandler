# main.py

from Functions.print_scale import print_scale
import time
import math

simulated_arduino = True

def simulate_sine_wave(frequency_hz=1.0):
    print("Simulation mode: Generating sine wave")
    t = 0.0
    step = 0.1
    while True:
        raw_value = math.sin(2 * math.pi * frequency_hz * t)
        shifted_value = (raw_value + 1) / 2
        print_scale(shifted_value, 20)
        time.sleep(step)
        t += step

def main():
    if simulated_arduino:
        simulate_sine_wave(frequency_hz=1.0)
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
