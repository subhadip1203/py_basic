## Developments
Setup Virtual Environment in the project directory :
  1. Create Virtual environment : `python3 -m venv env`
  2. starting Virtual environment : `source env/bin/activate`
  3. stopping Virtual environment : `deactivate`

2. Setup and install Django dependencies
  - for new project install django python-dotenv gunicorn etc 
  `pip install django gunicorn  python-dotenv`

  - to save installed packages :
  `pip freeze > requirements. txt`

  - to install packages from requirements. txt file :
  `pip install -r requirements.txt `


3. Environment Variables: make a file `.env`.

4. Local API Server uses a self signed certificate

  - create a folder with name cert:  `mkdir cert`
  - go inside the folder : `cd cert`
  - as django & gunicorn user 127.0.0.1 as host , create a host in the name of 127.0.0.1  `mkcert -cert-file cert.pem -key-file key.pem  127.0.0.1`
  - install the cert in the laptop or system `mkcert -install`


5. Run the server by gunicorn 

  - without ssl certificates : `gunicorn project_setup.wsgi:application --bind 0.0.0.0:8000`
  - with ssl certificates : `gunicorn project_setup.wsgi:application --keyfile=./cert/key.pem --certfile=./cert/cert.pem`
  - with certificate and hot reload : `gunicorn project_setup.wsgi:application --reload --keyfile=./cert/key.pem --certfile=./cert/cert.pem`

