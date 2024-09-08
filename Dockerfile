FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

# Running the Django app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "DjangoWeatherReminder.wsgi:application"]