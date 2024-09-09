from datetime import datetime, timedelta


class File_transact:

    def __init__(self,
                 in_state_District,
                 in_year,
                 in_publication_Date,
                 in_Document_ID):
        self.state_District = in_state_District
        self.year = in_year
        self.publication_date = self.convert_to_datetime(in_publication_Date)
        self.Doc_ID = in_Document_ID

    def convert_to_datetime(self, date_str):
        # Liste des formats possibles
        formats = ["%m/%d/%Y"]
        for fmt in formats:
            try:
                # Essayer de convertir la date avec le format courant
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue

        # Si aucun des formats ne fonctionne, lever une exception ou gérer le cas
        raise ValueError(f"Date format for '{date_str}' does not match any expected format")

    def is_recent(self):
        # Calculer la date d'hier
        yesterday = datetime.now() - timedelta(days=2)
        # Comparer la date de publication avec la date d'hier
        return self.publication_date >= yesterday


class Membre:

    def __init__(self,
                 in_Prefix,
                 in_Last,
                 in_First,
                 in_Suffix,
                 ):
        self.prefix = in_Prefix
        self.last_Name = in_Last
        self.first_Name = in_First
        self.suffix = in_Suffix
        self.file = []

    def addFile(self, in_file):
        self.file.append(in_file)
        if (in_file.is_recent()):
            print("----------------")
            print(self)
            print("Publication Date:", in_file.state_District, in_file.publication_date)
            print("ID du document Rapport: ", in_file.Doc_ID)
            print("----------------")

    def __repr__(self):
        return f"Membre(last_Name='{self.last_Name}', first_Name={self.first_Name})\nnombre de fichier : {len(self.file)}"

    def __eq__(self, autre):
        return (self.last_Name == autre.last_Name) and (self.first_Name == autre.first_Name)

    def __hash__(self):
        return hash((self.last_Name, self.first_Name))