import pyautogui
import keyboard
import os
from datetime import datetime
import time

# Define base directory for screenshots
base_dir = os.path.abspath("screenshots")
print(f"Base directory for screenshots: {base_dir}")

# Define the directories where screenshots will be saved
folders = {
    "haut": os.path.join(base_dir, "up"),
    "gauche": os.path.join(base_dir, "left"),
    "droite": os.path.join(base_dir, "right"),
    "bas": os.path.join(base_dir, "down")
}

# Create the folders if they do not exist
for folder in folders.values():
    os.makedirs(folder, exist_ok=True)

def save_screenshot(direction):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot = pyautogui.screenshot()
    filepath = os.path.join(folders[direction], f"screenshot_{timestamp}.png")
    
    print(f"Saving screenshot to: {filepath}")  # Debugging line
    
    try:
        screenshot.save(filepath)
        print(f"Screenshot saved to {filepath}")
    except Exception as e:
        print(f"Error saving screenshot: {e}")

# Main loop: Listen for key presses and take screenshots
try:
    print("Press the arrow keys to take a screenshot. Press 'q' to quit.")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f"Key pressed: {event.name}")  # Debugging line
            
            if event.name in folders:
                save_screenshot(event.name)
            elif event.name == 'q':
                print("Closing the program...")
                break
except KeyboardInterrupt:
    print("Program interrupted. Exiting.")
except Exception as e:
    print(f"An error occurred: {e}")
