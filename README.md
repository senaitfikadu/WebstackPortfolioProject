# Instraction to run the app
    - Create Virtual environment. 
        python -m venv venv

    - Activate the Virtual environment.
        source venv/bin/activate
    - Install required packages
        pip install -r requirements.txt

    - Create migration.
        python manage.py makemigration

    - Apply the change to database
        python manage.py migrate

    - To run the app
        python manage.py runserver

    - To create the admin user
       python manage.py createsuperuser

    - To create the django app
       python manage.py startapp portfolio# WebstackPortfolioProject
