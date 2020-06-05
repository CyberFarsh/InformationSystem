FROM python:3.8

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

EXPOSE 80

RUN pip install --upgrade pip

ARG APP_DIR
WORKDIR $APP_DIR
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
# workers = 2*CPU + 1; timeout default = 30
CMD gunicorn InformationSystem.wsgi:application --timeout 300 --workers 3 --bind 0.0.0.0:80