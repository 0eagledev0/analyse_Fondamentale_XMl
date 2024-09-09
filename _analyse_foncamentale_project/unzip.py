import zipfile
import os
import requests
import glob
import read as Run
# Path to the zip file
zip_url = 'https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2024FD.zip'
zip_file_path = 'data\\2024.zip'

# Destination folder to extract files
extract_folder = 'data\\extract'

# Download the zip file
response = requests.get(zip_url)
with open(zip_file_path, 'wb') as file:
    file.write(response.content)

print("File downloaded successfully!")

# Create the folder if it doesn't exist
os.makedirs(extract_folder, exist_ok=True)

# Unzipping the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print("File unzipped successfully!")

import time
print("annalyse...")
time.sleep(5)
Run.main()

#-------------------------------------------------------------------------------------------------
# SUPRIMER LES FICHIERS
# Specify the directory
#
# os.remove("data\\extract\\2024FD.txt")
# os.remove("data\\2024.zip")
# os.remove("data\\extract\\2024FD.xml")
# print("All files deleted successfully!")
