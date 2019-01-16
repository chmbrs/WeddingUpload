# WeddingUploader App
# Heroku - Django - S3

A simple upload app for wedding photos.

## Features

- Preview and upload photos directly to S3.
- Approve or not the photos uploaded by the guests.
- Like pictures and sort them.
- Latest Python 3.6 runtime environment and Django 2.

## How to Use

To run in your local machine, follow these steps:

1. Create your working environment. `$ python3 -m venv /path/to/venv`
2. Install the requirements. (`(venv)$ pip install -r requirements.txt`)
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
7. Create a superuser and enter the Django admin to approve and publish the uploaded photos.

## Screenshots

![Screenshot1](/static/images/screen1.png?raw=true "Screenshot1")
![Screenshot2](/static/images/screen2.png?raw=true "Screenshot2")
![Screenshot3](/static/images/screen3.png?raw=true "Screenshot3")
![Screenshot4](/static/images/screen4.png?raw=true "Screenshot4")
![Screenshot5](/static/images/screen5.png?raw=true "Screenshot5")

## Deployment to Heroku
This project is ready to run in Heroku.

Export the S3 credentials to Heroku variables with the CLI or the web platform.
Ex:
`$ heroku config:set GITHUB_USERNAME=joesmith`


    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

  and follow similar steps as above from step 4 but in Heroku's server. (requirements are installed with pipfile.lock automatically when you push)
  Ex:
  `$ heroku run python manage.py migrate`


## License: MIT

Feedback and improvements to the project is extremely welcome. =)

(All the images used are labeled for reuse with modification)
