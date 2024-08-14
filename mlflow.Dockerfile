FROM python:3.10.14-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# cmd is mlflow server --host 127.0.0.1 --port 8080 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ../mlruns    
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "8080", "--backend-store-uri", "sqlite:///mlflow.db", "--default-artifact-root", "../mlruns"]