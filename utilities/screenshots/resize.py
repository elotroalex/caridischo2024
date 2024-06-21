from PIL import Image
import os
import time

# Set the directory containing the images
directory = '/Users/renekooiker/Desktop/www/caridischo-screenshots/screenshots/to-add'

# Set the desired size
desired_size = (1366, 683)
desired_quality = 95

# Get list of all files in directory sorted by creation date
files = sorted(os.listdir(directory), key=lambda x: os.path.getctime(os.path.join(directory, x)))

# Rename all files in order of creation date
for i, filename in enumerate(files):
    extension = os.path.splitext(filename)[1]
    os.rename(os.path.join(directory, filename), os.path.join(directory, f'cds{i+1}{extension}'))

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # Open the image file
        img = Image.open(os.path.join(directory, filename))
        # Resize the image while maintaining aspect ratio
        img.thumbnail(desired_size)
        # Convert the image to RGB if it's RGBA
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # Save the resized image back to the file
        img.save(os.path.join(directory, filename))
        # Convert PNG to JPG and vice versa
        if filename.endswith(".png"):
            img.save(os.path.join(directory, filename.rsplit('.', 1)[0] + '.jpg'), 'JPEG')
        elif filename.endswith(".jpg"):
            img.save(os.path.join(directory, filename.rsplit('.', 1)[0] + '.png'), 'PNG')

print("All images have been renamed, resized and converted.")