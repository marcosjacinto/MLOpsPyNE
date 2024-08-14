# MLOps

Este projeto fornece uma configuração Docker Compose para executar Jupyter Lab e Mlflow, permitindo fluxos de trabalho eficientes de ciência de dados e aprendizado de máquina para o tutorial de MLOps apresentado na Python Nordeste 2024.

## Pré-requisitos

Antes de começar, certifique-se de que Docker e Docker Compose estão instalados em seu sistema.

### Instalar Docker

1. **Referência à Documentação Oficial:**
   - Siga as instruções de instalação do Docker na documentação oficial: [Documentação do Docker](https://docs.docker.com/get-docker/).

2. **Verificar Instalação do Docker:**
   Após a instalação, verifique se o Docker foi instalado corretamente executando:

   ```bash
   docker --version
   ```

## Rodando a aplicação

Uma vez que Docker e Docker Compose estejam instalados, você pode configurar e executar os serviços.

1. **Clone o Repositório**
Clone este repositório para sua máquina local:

```bash
git clone https://github.com/seu-repo/dockerized-jupyter-mlflow.git
cd dockerized-jupyter-mlflow
```

2. **Construa e Execute os Serviços**
Use Docker Compose para construir as imagens e iniciar os serviços:

```bash
docker compose up --build
```

Este comando irá:
Construir as imagens Docker para o Jupyter Lab e Mlflow.
Iniciar os serviços em segundo plano.

3. **Acesse os serviços**

No terminal localize a URL do jupyter lab que contém um token, exemplo:
```
http://127.0.0.1:8888/lab?token=5cb3f56ac2f1cc83735e31d0f94e2f3165bb7412815c58d6
```
Clique no link para abrir a interface do Jupyter Lab onde você executará os notebooks.

Execute os notebooks e para acompanhar os experimentos gerados no mlflow, abra http://localhost:8080

4. **Parando os serviços**

Utilize o comando abaixo para parar os containers:
```bash
docker compose down
```
