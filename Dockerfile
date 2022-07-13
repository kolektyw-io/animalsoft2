FROM python:3.9
COPY src /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD gunicorn -b :8000 animalsoft.wsgi