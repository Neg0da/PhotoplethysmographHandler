import config

debug_mode = config.DEBUG_MODE

def debug(message: str):
    """
    Ця функція виводить повідомлення для налагодження
    Args:
        message (str): Повідомлення буде надруковано.
    """
    if debug_mode == "OFF":
        return
    elif debug_mode == "ON":
        print(f"DEBUG: {message}")
        input("Press Enter to next step...")
    elif debug_mode == "ALL":
        print(f"DEBUG: {message}")