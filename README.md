# Blog Django

Ce projet est un blog simple construit avec Django. Il permet aux utilisateurs de gérer des articles de blog avec des fonctionnalités de création, lecture, mise à jour et suppression (CRUD).

## Fonctionnalités

- Affichage de la liste des articles
- Création d'articles par des utilisateurs authentifiés
- Édition et suppression d'articles
- Détails des articles avec affichage de l'auteur et de la date de création
- Authentification des utilisateurs

## Prérequis

- Python 3.x
- Django 3.x ou supérieur
- Une base de données (SQLite par défaut)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/blog-django.git
   cd blog-django
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows utilisez `env\Scripts\activate`
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```

5. Créez un superutilisateur pour accéder à l'interface d'administration :
   ```bash
   python manage.py createsuperuser
   ```

6. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

7. Accédez à l'application à l'adresse `http://127.0.0.1:8000/`.

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des problèmes ou des demandes de fonctionnalités.

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
