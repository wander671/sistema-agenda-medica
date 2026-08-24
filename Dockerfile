# Imagem base do Python
FROM python:3.14-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o requirements.txt
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto para dentro do container
COPY . .

# Expõe a porta da aplicação Flask
EXPOSE 5000

# Inicia a aplicação
CMD ["python", "app.py"]