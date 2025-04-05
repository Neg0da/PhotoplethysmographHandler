# ./Functions/print_scale.py
# Status: Complete
# Description: This script contains a function to print a scaled representation of a sine wave value.

SCALE_LENGTH = 10

def print_scale(sine_value, scale_length=SCALE_LENGTH):

    scale_length = SCALE_LENGTH
    scaled_value = int(sine_value * scale_length)

    scale = '▀' * scaled_value + ' ' * (scale_length - scaled_value)

    print(f"Value: {sine_value:+.5f} | {scale}")

if __name__ == "__main__":
    print("Demonstrating print_scale with test values:")

    for i in range(15):
        value = i / 10
        print_scale(value)
