FROM python:3.8
EXPOSE 3000

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "predict.py"]
