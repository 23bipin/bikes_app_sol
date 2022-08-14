
This app 


STEPS TO BUILD THE APP:

Download/clone the repository
Install django, pandas (check requirements.txt)

Run,
$ python manage.py makemigrations helsinki_bikes
$ python manage.py migrate 

$ python manage.py data_setup
$ python manage.py station_details

$ python manage.py runserver [7000]

Create a folder for project.

Install virtual environment [optional]
$ python -m venv .venv_name
$ source .venv_name/bin/activate

Install Django [django 4.0 recommened]
$ python -m pip install django

Create project
$ django-admin startproject bikes .

Create App
$ python manage.py startapp bikes_helsinki

Add App in bikes/settings.py [commented "#bips"]

Create urls.py inside the app (bikes_helsinki). Link the urls.py inside "bikes" with the one inside the app. Check urls.py inside bikes/urls.py, commented "#bips"

Create "templates" folder

Create inside templates folder,
base.html,  #base html code file
home.html,  #index page
datatable.html, #main filter page
search.html #individual station details page

Update bikes_helsinki/urls.py

Create "static" folder
Inside "static" folder create "css", "data" and "images" folder. 
In settings.py add the "static" folder location. (commented #bips)

Create database in the models.py file inside bikes_helsinki folder.
Migrate the database mode;
$ python manage.py makemigrations helsinki_bikes
$ python manage.py migrate 

Install Pandas(for data processing)
$ pip install pandas

Create files for custom filters:
Create management/custom folder in the root folder.
data_setup.py is created for data filteration
Run, 
$ python manage.py data_setup

station_details.py is created similarly for individual station filteration.
Run,
$ python manage.py station_details

Follow codes inside datatable.html for filtering.
Follow codes inside search.html for individual station filtering.

Modify .views.py accordingly.

Folder "static" contains custom css file, images and databases.

-Folium (for maps)
[maps work under progress]




