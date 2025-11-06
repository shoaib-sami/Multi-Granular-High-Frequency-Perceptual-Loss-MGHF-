import os

# Define the directory containing the images
folder_path = 'path/to/your/folder'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file has the pattern '_1x.png'
    if '_1x.png' in filename:
        # Create the new filename by removing '_1x'
        new_filename = filename.replace('_1x.png', '.png')
        
        # Construct full file paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')
