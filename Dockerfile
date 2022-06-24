FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip3 install flask

ADD . /app
WORKDIR /app

EXPOSE 5000

CMD ["python3", "main.py"]