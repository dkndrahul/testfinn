Flight Project

Setup:

1.The first thing to do is to download the project which is based on python 3.5 version.

2.Create a virtual environment to install dependencies in and activate it:

  a - virtualenv testenv or environment_name
  
  b - source testenv/bin/activatefor linux and environment_name\Scripts\activate for windows
  
  Note: please check the python verion of your system is 3.5 or set the virtual environment version to 3.5

3. Then install the depedencies to your environment folder by running the following in terminal/ cmd 

   a- pip install -r requirements.txt

4. Once pip has finished downloading the dependencies, run the server and navigate to http://127.0.0.1:8000/

   a - python manage.py runserver


Project Steps:

1 - Created two models FlightsModel and PassengersModel in models.py file.

2 - Migrated the tables, using python manage.py makemigrations and python manage.py migrate commands

3 - Created serializers AllPassengerList, PassengerSerializer and FlightSerializer for converting python native types to json format.

4 - In views.py file, created PassengerViewset viewset class for returning the details of flights and passengers. 

5 - For the endpoint "get all passengers in flight", I overided "list" method of modelviewset. 

6 - For the endpoint "get passenger details", the default retrieve method from model viewset is used.

7 - At last, created urls.py to handle the controller views. This urls file is refered in the main project urls file(project/urls.py)
