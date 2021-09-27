FROM python:3.9.0

WORKDIR /home/

RUN echo "v4"

RUN git clone https://github.com/ojh789ojh/study_ai_django2.git

WORKDIR /home/study_ai_django2/

RUN echo "SECRET_KEY=django-insecure-h-xxkou3vqca!(5@tqp=se&mdabot+2!6yjr-794jpmfk#$if%" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --settings=gis_1.settings.deploy --noinput && python manage.py migrate --settings=gis_1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_1.settings.deploy gis_1.wsgi --bind 0.0.0.0:8000"]
