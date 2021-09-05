#  ---- Create virtual env ------#
python3 -m venv env

# ----- activate virtual env and go inside virtual env -----#
source env/bin/activate

# ----- Install Django -----#
pip install django


# ---- django create Project ------#

django-admin startproject mainProject

    -- it will create a project called "mainProject"
    -- and an app called "mainProject"

#----------- run server -------------#
python manage.py runserver

#------------ reload project with models ----------#
    add all the app name in seetings.py
    python manage.py makemigrations && python manage.py migrate


#------------ create new app --------#
    cd mainProject
    python manage.py startapp app1

add app name in seetings.py :
    INSTALLED_APPS :[
        'app1',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]


#---- seeting for template folder and static folder -----#

    1. in mainProject folder : go to seetings.py
    2. TEMPLATES -> DIRS -> os.path.join(BASE_DIR, "frontend/templates"), 
    3. for static folder add the below lined in the seeting.py file:
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "frontend/static"),
        ]
    4. add /static/file name , example:
        /satic/main.css
        /static/style.css
        /static/myscript.js


#--------  install mysql connector ----------#
pip install mysql-connector-python

on ubuntu , sometime mysql connector instalation creates issue . then install this package:
    sudo apt-get install python3-dev libmysqlclient-dev


#---------- creating admin ----------#
python manage.py  createsuperuser


# --------- to edit any model from admin panel -----------#
-- go to admin.py in the perticular app
-- add the model 
        import Model
        admin.site.register(ModelName)


#--------- adding media folder and url (for images , docs ,etc ) --------#
in seetings.py : add these lines
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

in urls.py of main project app: add theses after "urlpatterns" array
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

to use any media use: http://website/media/.....






#----------- delete an app from django project ----------#

1. remove all db : python manage.py migrate <app_name>> zero
2. from seetings.py -> from INSTALLED_APPS array -> remove <app_name>
3. reove the app from url.py 
4. delete the folder