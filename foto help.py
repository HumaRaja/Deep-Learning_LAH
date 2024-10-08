import os
import re
 
def rename_images(directory):
    # Regular expression to match filenames like screenshot_YYYYMMDD_HHMMSS
    pattern = re.compile(r'screenshot_(\d{8})_(\d{6})')
 
    # Get a list of files in the directory
    files = os.listdir(directory)
 
    # Initialize counter for 'd{n}' filenames
    count = 1
 
    for file_name in sorted(files):
        # Check if the file matches the pattern
        match = pattern.match(file_name)
        if match:
            # Extract date and time parts from the filename
            date_part = match.group(1)
            time_part = match.group(2)
 
            # Create the new filename
            new_file_name = f"d{count}_{date_part}_{time_part}.png"
 
            # Get full paths for renaming
            old_file_path = os.path.join(directory, file_name)
            new_file_path = os.path.join(directory, new_file_name)
 
            # Rename the file
            os.rename(old_file_path, new_file_path)
 
            print(f"Renamed: {file_name} -> {new_file_name}")
 
            # Increment the counter
            count += 1
 
# Example usage
directory = '/path/to/your/images'
rename_images(directory)