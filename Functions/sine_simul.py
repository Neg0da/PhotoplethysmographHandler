# ../Functions/sine_simul.py
# Status: Complete
# This code simulates a sine wave and prints it to the console in a scaled format.

import time
import math

def print_scale(sine_value, scale_length=10):
    """
    Function to display the sine wave value as a scaled bar on the console.
    
    Parameters:
    sine_value (float): The value of the sine wave to display (in the range from -1 to 1).
    scale_length (int): The length of the scale to be displayed (default is 10 units).
    """
    scaled_value = int(sine_value * scale_length)
    scale = '▀' * scaled_value + ' ' * (scale_length - scaled_value)
    print(f"Value: {sine_value:+.5f} | {scale}")

def simulate_sine_wave(frequency_hz=1.0, step=0.05, do_print=True):
    """
    Function to simulate a sine wave and display it in real time.
    
    Parameters:
    frequency_hz (float): The frequency of the sine wave (in Hz).
    step (float): The time step between calculations (in seconds).
    do_print (bool): If True, print the sine wave to the console.

    Outputs:
    shifted_value (float): The shifted value of the sine wave.
    """
    print("Simulation mode: Generating sine wave")
    t = 0.0
    while True:
        raw_value = math.sin(2 * math.pi * frequency_hz * t)
        shifted_value = (raw_value + 1) / 2
        if do_print:
            print_scale(shifted_value, 20)
        yield shifted_value
        time.sleep(step)
        t += step

def main():
    frequency = float(input("Enter the frequency of the sine wave (Hz): "))
    simulate_sine_wave(frequency)

if __name__ == "__main__":
    main()
