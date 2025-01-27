# Financial Disclosures Automation Tool

Ce projet est un outil automatisé conçu pour télécharger, extraire et analyser des fichiers de divulgation financière depuis une source publique, puis notifier les informations importantes via Telegram.

## Fonctionnalités

1. **Téléchargement Automatique :**  
   Télécharge un fichier ZIP contenant des divulgations financières depuis une URL prédéfinie.

2. **Extraction et Analyse :**  
   Décompresse le fichier ZIP, traite son contenu en analysant les fichiers XML, et associe les informations pertinentes à des membres.

3. **Notification via Telegram :**  
   Envoie un message Telegram pour notifier les mises à jour récentes, en évitant les doublons grâce à un fichier de suivi (`output.txt`).

4. **Nettoyage Automatique :**  
   Supprime les fichiers téléchargés et extraits après chaque cycle pour optimiser l'espace disque.

5. **Cycle Automatisé :**  
   Exécute le processus toutes les 10 secondes pour garantir que les données restent à jour.

---

## Prérequis

### 1. Python
Assurez-vous que Python 3.7+ est installé sur votre machine.

### 2. Bibliothèques Python nécessaires
Installez les dépendances avec la commande suivante :
```bash
pip install requests pyTelegramBotAPI schedule
```

---

## Structure du projet

```plaintext
.
├── data/
│   ├── output.txt           # Fichier pour suivre les notifications déjà envoyées
│   ├── 2024FD.xml           # Fichier XML extrait (temporaire, supprimé après exécution)
│   ├── 2024.zip             # Fichier ZIP téléchargé (temporaire, supprimé après exécution)
├── main.py                  # Fichier principal exécutant le cycle
├── Representative_Member.py # Gestion des membres et fichiers associés
├── read.py                  # Lecture du fichier xml 
├── telegram.py              # notification via l'application Telegram
├── README.md                # Documentation du projet
```

---
[Readme.md](Readme.md)
## Comment exécuter le projet ?

1. Clonez ce dépôt dans votre environnement de travail :
   ```bash
   git clone <lien_du_depot>
   cd <nom_du_projet>
   ```

2. Lancez le script principal :
   ```bash
   python main.py
   ```

Le script s'exécutera en boucle, téléchargeant, traitant et nettoyant les fichiers automatiquement.

---

## Points importants

- **Configuration Telegram** :  
  Dans le fichier `Representative_Member.py`, remplacez l'`API_TOKEN` et le `CHAT_ID` par vos informations Telegram. Assurez-vous que votre bot est configuré et a accès au chat spécifié.

- **Sécurité** :  
  N'incluez pas d'informations sensibles comme l'`API_TOKEN` directement dans le code. Utilisez des variables d'environnement pour les gérer.

- **Fichier `output.txt`** :  
  Ce fichier est utilisé pour suivre les numéros de fichiers déjà notifiés, afin d'éviter les doublons.

---

## Améliorations possibles

- Ajouter un fichier de configuration pour personnaliser l'URL, les intervalles de temps et d'autres paramètres.
- Gérer les erreurs réseau ou de téléchargement avec des mécanismes de reprise.
- Mettre en place une journalisation pour suivre les exécutions et les erreurs.

---

## Avertissement

Ce projet est un outil pédagogique ou professionnel. Assurez-vous d'avoir les autorisations nécessaires pour interagir avec les données téléchargées et envoyées via Telegram.
 