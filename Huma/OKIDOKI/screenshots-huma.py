from PIL import ImageGrab
import keyboard
import os

# Define the base folder where screenshots will be saved
save_folder = "Liesa"
os.makedirs(save_folder, exist_ok=True)  # Create the base folder if it doesn't exist

# Define the keys you're interested in for classification
keys_of_interest = ['q']

# Function to take a screenshot and save it in the corresponding folder
def take_screenshot(key):
    # Check if the key is one of the keys we want to classify
    if key not in keys_of_interest:
        return

    # Create a subfolder for the key press if it doesn't exist
    key_folder = os.path.join(save_folder, key)
    os.makedirs(key_folder, exist_ok=True)

    # Capture the screenshot (you can pass a specific region, e.g., left half of the screen)
    #screenshot = ImageGrab.grab()  # Capture the full screen by default
    screenshot = ImageGrab.grab(bbox=(0, 400, 1920, 655))

    # Get the screenshot count for this key
    screenshot_count = len(os.listdir(key_folder)) + 333

    # Save the screenshot in the corresponding subfolder with a numbered filename
    screenshot_filename = os.path.join(key_folder, f"{key}{screenshot_count}.png")
    screenshot.save(screenshot_filename)

    # Close the screenshot object
    screenshot.close()

    print(f"Screenshot saved as: {screenshot_filename} in folder: {key}")

# Function to handle key press events
def on_key_release(event):
    key = event.name  # Get the key that was released
    print(f"Key released: {key}")

    # Stop the program if the alt key is pressed
    if key == "alt":
        print("Alt key pressed. Exiting the program safely...")
        keyboard.unhook_all()  # Stop listening for key presses
    else:
        # Only take screenshots for 'z', 'q', or 'd'
        take_screenshot(key)

# Hook the keyboard to detect key releases
keyboard.on_release(on_key_release)

# The program runs indefinitely to listen for key releases
keyboard.wait()
