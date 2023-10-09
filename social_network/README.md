This is a sanitized version of the makers seed_project [https://github.com/makersacademy/databases-in-python-project-starter]. It includes the seeds but not the music classes or unnecessary tests. 

# Fork to your account on github then clone to your local directory

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Create the database
; createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME

# Run the tests
; pytest

# Run the app
; python app.py

