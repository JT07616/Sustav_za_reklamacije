FROM python:3.9
WORKDIR app/
COPY requirements.txt req.txt
RUN apt-get update && apt-get install -y \
    ca-certificates \
    openssl \
    sqlite3 \
    tzdata \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip3 install -r req.txt
COPY . .
EXPOSE 8080
CMD ["python3", "app.py"]