FROM python:3.9

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python mydjangoproject/manage.py migrate && \
    python mydjangoproject/manage.py runserver 0.0.0.0:8000
