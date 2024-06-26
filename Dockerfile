FROM python:3.12

WORKDIR /app

COPY utils.txt .
RUN pip install --no-cache-dir -r utils.txt

COPY . .

CMD ["python", "./main.py"]
