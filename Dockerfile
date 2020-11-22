# Descarga la versión 3.8 de Python
FROM python:3.8-slim

#Crea el directorio /app/test
RUN mkdir -p app/test

#establecer el working directory 
WORKDIR /app/test

#copiar el fichero requirements.txt
COPY requirements.txt .

#installar los requisitos con pip
RUN pip install -r requirements.txt 

#ejecutar las pruebas
CMD ["invoke", "test"]
