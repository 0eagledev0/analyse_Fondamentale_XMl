import xml.etree.ElementTree as ET
from Representative_Member import *

def main():
    # Spécifie le chemin du fichier XML
    xml_file_path = 'data\\2024FD.xml'
    # Charger et parser le fichier XML
    tree = ET.parse(xml_file_path)
    # Obtenir la racine de l'arborescence XML
    root = tree.getroot()
    membres_liste = []
    # Parcourir les éléments dans le fichier XML
    for child in root:
        lastName =child[1].text
        firstName =child[2].text
        membres_liste.append(Membre(child[0].text,
                                    lastName,
                                    firstName,
                                    child[3].text))
    membres_liste = list(set(membres_liste))
    for child in root:
        lastName =child[1].text
        firstName =child[2].text
        if(child[4].text == "P"):
            file = File_transact(child[5].text,
                                child[6].text,
                                child[7].text,
                                child[8].text)
            for idx, membre in enumerate(membres_liste):
                if membre.last_Name == lastName and membre.first_Name == firstName:
                    membres_liste[idx].addFile(file)
                    break