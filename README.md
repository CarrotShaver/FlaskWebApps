# FlaskWebApps

### Install flask-wtf
- Any OS: `pip install flask-wtf`

### Start virtual environment
- Linux: `source env/bin/activate`
- Windows: `path\to\env\Scripts\activate`

### Create requirements.txt
- Note: Run everytime a new module is installed
- Any OS: `pip freeze > requirements.txt`

### Create flask run environment variable
- Linux: `export FLASK_APP=server.py`
- Windows: `set FLASK_APP=server.py`

### Turn on Flask Debugger
- Linux: `export FLASK_DEBUG=1`
- Windows: `set FLASK_DEBUG=1`

### Start Flask server
1. Bash: `source .env`
2. Any OS: `flask run`

### Initialize the manage.py
- Bash terminal: `python manage.py db init`

### Manage db, create new snapshot
- Bash terminal: 
    - `python manage.py db upgrade`
    - `python manage.py db migrate`
