FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/TaskManager

RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]