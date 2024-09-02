import requests
import json

# URL de l'API pour récupérer les transactions des membres du Sénat pour 2023
url = 'https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/2023/transactions.json'

# Effectuer la requête GET
response = requests.get(url)

# Vérifier si la requête a été effectuée avec succès
if response.status_code == 200:
    # Convertir la réponse en JSON
    data = response.json()

    # Sauvegarder les données dans un fichier JSON
    with open('senate_trading_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Les données ont été sauvegardées dans 'senate_trading_data.json'.")
else:
    print(f"Erreur: {response.status_code}")
