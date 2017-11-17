# m7011e17-semi-anonymous-questions

## Description
m7011e17-semi-anonymous-questions created by GitHub Classroom

Our project aspire to follow the proposed idea of semi-anonymous questions.

In order to alleviate uncertainty from lectures students will be free to ask anonymous questions. In terms, these questions will populate a board where they can be voted upon to emphasis importance, and students can anonymously answer questions to help their peers. The teacher can also use this platform to decide upon questions to answer in following lectures.

If students abuse the webpage then designated teacher users can decide to either warn or directly block the anonymous account. The teacher create the accounts for the student-circle, so students who are locked out can't re-enter the circle without teacher authentication.

## Back-End
Framework: Django, https://www.djangoproject.com/
Database: SQL Light

## Front-End
TBT

## Deployment
1. Make an account on https://www.pythonanywhere.com
2. Fork the repository
3. Follow these steps : https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/ using the fork as repo

## Live Webpage
The live webpage focus on setting up and testing right now and doesn't have any real content. 

* http://floood.pythonanywhere.com/
* http://floood.pythonanywhere.com/music
* http://floood.pythonanywhere.com/admin

## Run Locally (WINDOWS)
Follow these steps to run the server locally
1. Download the Repo
2. Install Python 3.6.3 (and make sure environment paths are set up for python and easy_install)
3. Install Django 1.11.7
4. In power shell navigate to the downloaded repo
5. execute 'python manage.py runserver'

If nothing went wrong the webpage should now be accessible on localhost:8000

Obs: This set up does not utilize a virtual environment, so make sure you run the correct python and django versions
