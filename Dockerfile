FROM python:alpine
WORKDIR /app


RUN pipenv install  

COPY . /app
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]