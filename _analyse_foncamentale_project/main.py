import zipfile
import os
import requests
import read as run_reader
import schedule
import time

def run():
    zip_url = 'https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2024FD.zip'
    zip_file_path = 'data\\2024.zip'
    extract_folder = 'data\\'
    response = requests.get(zip_url)
    with open(zip_file_path, 'wb') as file:
        file.write(response.content)
    os.makedirs(extract_folder, exist_ok=True)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print("annalyse...")
    time.sleep(5)
    run_reader.main()
    #-------------------------------------------------------------------------------------------------
    # SUPRIMER LES FICHIERS
    os.remove("data\\2024FD.txt")
    os.remove("data\\2024.zip")
    os.remove("data\\2024FD.xml")



while True:
    run()
    time.sleep(10)