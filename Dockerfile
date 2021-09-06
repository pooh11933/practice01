FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/pooh11933/practice01.git

WORKDIR /home/practice01/

RUN echo "SECRET_KEY=django-insecure-7zu&oubtvc%9s9gzr!!&(n4%w$+jf4@2dqx2iwp85d-ob*i=n#" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]