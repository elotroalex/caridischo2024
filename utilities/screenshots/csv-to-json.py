import csv
import json

# Step 2: Open the CSV file
with open('Directory of Caribbean Digital Scholarship - Data Sheet - 2024.csv', 'r') as csv_file:
    # Step 3: Convert CSV to dictionary
    csv_data = csv.DictReader(csv_file)

    # Step 4: Create an empty dictionary
    pid_link_dict = {}

    # Step 5: Iterate over CSV data
    for row in csv_data:
        pid_link_dict[row['pid']] = row['link']

# Step 6: Convert dictionary to JSON
json_data = json.dumps(pid_link_dict)

# Step 7: Write JSON to file
with open('pid_link.json', 'w') as json_file:
    json_file.write(json_data)