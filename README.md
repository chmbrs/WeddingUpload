# WeddingUploader App
# Heroku - Django - S3

A simple upload app for wedding photos.

## Features

- Upload photos directly to S3.
- Approve or not the photos uploaded by the guests.
- Like pictures and sort them.
- Latest Python 3.6 runtime environment and Django 2.

## How to Use

To run in your local machine, follow these steps:

1. Create your working environment. `(venv)$ `
2. Install the requirements. (`$ pip install -r requirements.txt`)
3. Set your environment variables (ex: `$ export AWS_ACCESS_KEY_ID:xxx`) for the S3 bucket or put them on:
   '../WeddingUpload/weddingupload/settings.py'

```
   AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
   AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
   AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME', '')
```
(replace with your credentials where the '' are)

*(for your safety, never, never commit your secret credential to any public repository)*

4. Run`(venv)$ python manage.py collectstatic` for sending the static files to S3.
5. Run`(venv)$ python manage.py migrate` and `(venv)$ python manage.py makemigrations` to create the models in the DB
6. Finally run`(venv)$ python manage.py runserver`
If everything went well you should see something like this:
```
Performing system checks...

System check identified no issues (0 silenced).
January 15, 2019 - 23:01:12
Django version 2.1.5, using settings 'weddingupload.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

  and follow similar steps

## License: MIT

Feedback and improvements to the project is extremely welcome. =)
