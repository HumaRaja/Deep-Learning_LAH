from PIL import ImageGrab
import keyboard
import time
import os

# Define the base folder where screenshots will be saved
save_folder = "Liesa"
os.makedirs(save_folder, exist_ok=True)  # Create the base folder if it doesn't exist

# Define the keys you're interested in for classification
keys_of_interest = ['d', 's']

# Function to take a screenshot and save it in the corresponding folder
def take_screenshot(key):
    # Check if the key is one of the keys we want to classify
    if key not in keys_of_interest:
        return
    
    # Create a subfolder for the key press if it doesn't exist
    key_folder = os.path.join(save_folder, key) 
    os.makedirs(key_folder, exist_ok=True)
    
    # Capture the screenshot
    screenshot = ImageGrab.grab()
    
    # Create a timestamp to make the filename unique
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    # Save the screenshot in the corresponding subfolder
    screenshot_filename = os.path.join(key_folder, f"screenshot_{timestamp}.png")
    screenshot.save(screenshot_filename)
    
    # Close the screenshot object
    screenshot.close()

    print(f"Screenshot saved as: {screenshot_filename} in folder: {key}")

# Function to handle key press events
def on_key_press(event):
    key = event.name  # Get the key that was pressed
    print(f"Key pressed: {key}")
    
    # Stop the program if the tab key is pressed
    if key == "alt":
        print("Alt key pressed. Exiting the program safely...")
        keyboard.unhook_all()  # Stop listening for key presses
    else:
        # Only take screenshots for 'z', 'q', 'd', or 's'
        take_screenshot(key)

# Hook the keyboard to detect key presses
keyboard.on_press(on_key_press)

# Keep the program running to listen for key presses
keyboard.wait()  # This will keep the script running until manually stopped


