#./Functions/print_scale.py

import config

def print_scale(sine_value):
    """Function to display a scale for sinusoidal values"""

    scale_length = config.SCALE_LENGTH  # Length of the scale (can be increased)
    scaled_value = int((sine_value + 2) * (scale_length // 2))  # Scaling

    # Create the scale with padding
    scale = '▀' * scaled_value + ' ' * (scale_length - scaled_value)

    # Format the output with alignment
    print(f"Value: {sine_value:+.5f} | {scale.center(scale_length)}")
