FROM python:slim

WORKDIR /flask_app_Sascha
COPY . /flask_app_Sascha

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN  pip3 install mariadb==1.1.4

EXPOSE 5000
ENTRYPOINT python3 flask_app/__init__.py
