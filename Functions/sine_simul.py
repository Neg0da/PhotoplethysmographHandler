import time
import math

def print_scale(sine_value, scale_length=10):
    scaled_value = int(sine_value * scale_length)
    scale = '▀' * scaled_value + ' ' * (scale_length - scaled_value)
    print(f"Value: {sine_value:+.5f} | {scale}")

def simulate_sine_wave(frequency_hz=1.0, step=0.05):
    print("Simulation mode: Generating sine wave")
    t = 0.0
    while True:
        raw_value = math.sin(2 * math.pi * frequency_hz * t)
        shifted_value = (raw_value + 1) / 2  
        print_scale(shifted_value, 20)
        time.sleep(step)
        t += step

def main():
    frequency = float(input("Enter the frequency of the sine wave (Hz): "))
    simulate_sine_wave(frequency)

if __name__ == "__main__":
    main()
