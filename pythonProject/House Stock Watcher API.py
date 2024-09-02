import requests
import json
# URL de l'API pour récupérer toutes les transactions des membres du Congrès
url = 'https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json'

# Effectuer la requête GET
response = requests.get(url)

# Vérifier si la requête a été effectuée avec succès
if response.status_code == 200:
    # Convertir la réponse en JSON
    data = response.json()

    # Sauvegarder les données dans un fichier JSON
    with open('congress_trading_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Les données ont été sauvegardées dans 'congress_trading_data.json'.")
else:
    print(f"Erreur: {response.status_code}")
