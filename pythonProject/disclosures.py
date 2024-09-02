import requests

# URL du fichier PDF (remplacez cette URL par celle du document que vous souhaitez télécharger)
pdf_url = 'https://disclosures-clerk.house.gov/filing/2023-2024/Example_PDF.pdf'

# Effectuer la requête GET
response = requests.get(pdf_url)

# Vérifier si la requête a été effectuée avec succès
if response.status_code == 200:
    # Sauvegarder le fichier PDF localement
    with open('disclosure_document.pdf', 'wb') as file:
        file.write(response.content)

    print("Le document a été téléchargé et sauvegardé dans 'disclosure_document.pdf'.")
else:
    print(f"Erreur: {response.status_code}")
