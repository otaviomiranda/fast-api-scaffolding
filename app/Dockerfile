FROM python:3.8.13-slim-buster

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat gcc build-essential

EXPOSE 8000

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "8000"]
