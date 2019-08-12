# whale-signup-test

This is a simple proof of concept using flask-login. If it seems like a good fit for whale-beta then I can integrate it into the existing app.

## Setup
Install dependencies with `pip3 install -r requirements.txt`

Open python3 in terminal and run:
* `from flaskLoginTest import db, create_app`
* Then create the db with `db.create_all(app=create_app())`

Exit python3 then set:
* `export FLASK_APP=flaskLoginTest`
* `export FLASK_DEBUG=1`
* Then execute `flask run`
