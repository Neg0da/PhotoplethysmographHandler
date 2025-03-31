# ./Functions/simple_debug.py
# This module provides a simple debugging utility that logs messages based on the debug mode set in the configuration.
# It allows for different levels of debugging output, including pausing execution for user input.

import config
import logging

# Retrieve the debug mode from the configuration
debug_mode = config.DEBUG_MODE

# Logging configuration
# Set up logging with DEBUG level and a specific format for log messages
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def debug(message: str) -> None:
    """
    This function is used for debugging purposes.
    It logs debug messages and optionally pauses execution based on the debug mode.
    
    Args:
        message (str): The message to be printed for debugging.
    
    Returns:
        None
    """
    # Match the current debug mode and execute the corresponding behavior
    match debug_mode:
        case "OFF":
            # If the debug mode is OFF, do nothing
            pass
        case "ON":
            # If the debug mode is ON, log the debug message
            logger.debug(f": {message}")
            # Pause execution and wait for the user to press Enter
            input("Press Enter to proceed to the next step...")
        case "ALL":
            # If the debug mode is ALL, log the debug message without pausing
            logger.debug(f": {message}")
        case _: 
            # If the debug mode is unknown, log a warning message
            logger.warning(f"Unknown debug mode: {debug_mode}")
