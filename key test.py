from PIL import ImageGrab
import keyboard
import time
import os
import sys  # Import sys to exit the programgrafm
# Function to take a screenshot and save it
# Define the folder where screenshots will be saved
save_folder = "Liesa"
os.makedirs(save_folder, exist_ok=True)  # Create the folder if it doesn't exist


def take_screenshot(key):
    # Capture the entire screen
    screenshot = ImageGrab.grab(bbox=(2, 1, 960, 1025))
    
    # Create a timestamp to make the filename unique
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    # Save the screenshot with the pressed key as the filename
    screenshot_filename = os.path.join(save_folder, f"screenshot_{key}_{timestamp}.png")
    screenshot.save(screenshot_filename)
    
    # Close the screenshot image object
    screenshot.close()

    print(f"Screenshot saved as: {screenshot_filename}")

# Function that will be called when a key is pressed
def on_key_press(event):
    key = event.name  # Get the name of the key
    print(f"Key pressed: {key}")

    # Stop the program if the delete key is pressed
    if key == "m":
        print("Delete key pressed. Exiting the program safely...")
        exit()  # Safely exit the program
    
    # Take a screenshot when any key is pressed
    else:
        take_screenshot(key)

# Hook the keyboard to detect key presses
keyboard.on_press(on_key_press)

# Keep the program running to listen for key presses
keyboard.wait()  # This will keep the script running until manually stopped