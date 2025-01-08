CSV Upload and User Management API

This is a Django-based project that enables users to upload CSV files containing user information. The application validates the data and saves it to the database. Invalid rows are flagged with detailed errors, and duplicate email addresses are skipped gracefully.

Technologies Used

Frameworks: Django, Django REST Framework

Frontend: 

Database: PostgreSQL

File Handling: Python CSV module

Validation: Django REST Framework serializers

Install the required Python packages:

pip install django djangorestframework psycopg2
1. Configure the Database
2. 
Open the settings.py file located in the project/settings.py folder.

Update the database settings for PostgreSQL as shown below:


DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': 'your_database_name',
        
        'USER': 'your_database_user',
        
        'PASSWORD': 'your_database_password',
        
        'HOST': 'localhost',  # Or your database host
        
        'PORT': '5432',       # Default PostgreSQL port
        
    }
    
}


Save the file and ensure PostgreSQL is running.

2. Run Migrations
   
Generate and apply migrations to set up the database schema:

python manage.py makemigrations
python manage.py migrate

3. Start the Development Server

Run the server locally:


python manage.py runserver

4. Access the Application

Open your browser and navigate to:

http://127.0.0.1:8000/upload-csv/

