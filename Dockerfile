# базовый образ Python
FROM python:3.11

# создать и переключиться в рабочую директорию /app
WORKDIR /app

# скопировать файлы проекта в рабочую директорию
COPY . /app

RUN python -m pip install --upgrade pip
# установить зависимости
RUN pip install -r requirements.txt

# загрузить переменные окружения из файла .env
RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir 'python-dotenv'

# запустить Django-приложение
CMD ["python", "manage.py", "migrate"]
