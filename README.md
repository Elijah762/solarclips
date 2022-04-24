# SOLARECLIPSE
Authors: Adittya Das, Elijah Moya, Izzy Montemayor, Mei Sullum
Website: www.solarclips.tech

WE ARE SOLARECLIPS
------------------
SOLARECLIPS combines social media and movie ticketing into a single application. Our app allows movie enthusiasts to friend others, create reviews, buy movie tickets, receive movie and concession discounts, and have an overall pleasant experience within our site. Not only can our users create their own reviews, but they can explore other reviews and use our app to message others, which is easily accessible!
- allows you to see friends’ reviews
- gives user pleasant site experience
- incentives for buying concessions in advance
    - reusable cups and popcorn buckets - sustainability
- social movie application

------------------
HOW TO RUN
------------------
Before running the server you must...
python -m pip install --user virtualenv 

[In the second solarclips folder]
Windows > .venv\Scripts\Activate.ps1 
macOS > source .venv/bin/activate

[cd .. out of folder and]
Download dependeinces by running this in root:
pip install -r requirements.txt

[Create super user to gain admin access]
> python manage.py createsuperuser

Navigate to 127.0.0.1:8000/admin/ for admin login
Navigate to 127.0.0.1:8000 for shopper view

[cd into second solarclips and run]
Once all dependecies are downloaded run > python manage.py runserver

REQUIREMENTS
------------
Python 3.8 or above
