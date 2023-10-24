FROM python:3.10
EXPOSE 80

# manual installation
RUN pip install fastapi uvicorn

WORKDIR    /opt/oracle
RUN        apt-get update && apt-get install -y libaio1 wget unzip

# copy whole installation (minus dockerignore)
COPY . /app

# install additional dependencies (might have duplicates?)
# (was pipenv previously but had problems with alpine)
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# set workdir to have subscripts in scope
WORKDIR /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]