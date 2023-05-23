FROM python:3.9

WORKDIR /fire_detect

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt update

RUN apt install python3-opencv -y

COPY . .

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
