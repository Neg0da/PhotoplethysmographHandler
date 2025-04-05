# main.py

import time

simulated_arduino = True

def main():
    if simulated_arduino:
        from Functions.sine_simul import simulate_sine_wave
        sine_wave_generator = simulate_sine_wave(frequency_hz=1.0, step=0.05, do_print=False)
        try:
            while True:
                value = next(sine_wave_generator)
                print(f"Sine Wave Value: {value}")
                time.sleep(0.05)
        except KeyboardInterrupt:
            print("Simulation stopped by user.")
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
