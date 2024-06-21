import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import os
from PIL import Image
from selenium.common.exceptions import TimeoutException
import csv

## config

# initializing venv
# python3 -m venv venv
# source venv/bin/activate

output_folder_png = 'screenshots/png'
output_folder_jpg = 'screenshots/jpg'

# Create directories
os.makedirs(output_folder_png, exist_ok=True)
os.makedirs(output_folder_jpg, exist_ok=True)

with open('pid_link.json', 'r') as json_file:
    urls = json.load(json_file)

#For Firefox driver
firefox_service = FirefoxService(executable_path="/Users/renekooiker/Desktop/www/caridischo-screenshots/geckodriver")
firefox_options = FirefoxOptions()
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

# Iterate and take screenshots
start_pid = 'cds10'
start = False

# Set a page load timeout for the driver
driver.set_page_load_timeout(30)  # set a 30-second timeout

# Initialize an empty list to store error messages
errors = []

for pid, url in urls.items():
    try:
        # Check if the PNG and JPG files already exist
        png_path = os.path.join(output_folder_png, f"{pid}.png")
        jpg_path = os.path.join(output_folder_jpg, f"{pid}.jpg")
        if os.path.exists(png_path) and os.path.exists(jpg_path):
            print(f"Files {png_path} and {jpg_path} already exist. Skipping...")
            continue
        driver.get(url)
        time.sleep(5)  # wait for the page to load

        driver.save_screenshot(png_path)
        # Convert PNG to JPG
        with Image.open(png_path) as img:
            rgb_im = img.convert('RGB')
            rgb_im.save(jpg_path)
        print(f"PNG screenshot saved to {png_path}")
        print(f"JPG screenshot saved to {jpg_path}")
    except Exception as e:
        # Store the error message and continue with the next iteration
        errors.append(f"Error for {pid}: {str(e)}")
        continue

# Quit the WebDriver
driver.quit()

# Print all error messages at the end
if errors:
    print("\nErrors occurred during execution:")
    for error in errors:
        print(error)
else:
    print("No errors occurred during execution.")

# After the script runs, check whether files exist for each pid
# Check if any files are missing for each pid
missing_files = []
for pid, url in urls.items():
    png_path = os.path.join(output_folder_png, f"{pid}.png")
    jpg_path = os.path.join(output_folder_jpg, f"{pid}.jpg")
    if not os.path.exists(png_path) or not os.path.exists(jpg_path):
        missing_files.append(pid)

# Print the list of pids with missing files
# Create a dictionary to store the links and labels
pid_links_labels = {}

# Read the CSV file and populate the dictionary
with open('Directory of Caribbean Digital Scholarship - Data Sheet - 2024.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        pid = row[0]
        label = row[1]
        link = row[5]
        pid_links_labels[pid] = (label, link)

# Print the links and labels for missing files
if missing_files:
    print("Missing files for the following pids:")
    for pid in missing_files:
        link, label = pid_links_labels.get(pid, ("", ""))
        print(f"PID: {pid}, Link: {link}, Label: {label}")
else:
    print("All files exist for all pids.")

