# ./main.py

import Functions.debug as debug   # Імпортуємо функцію 

def main():
    # Викликаємо функцію debug, передаючи повідомлення для налагодження
    debug("This is a debug message to check the debug mode.")
    
    # Інші частини вашої програми
    print("Main program is running.")

if __name__ == "__main__":
    main()