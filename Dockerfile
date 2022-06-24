FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3-pip unzip xvfb libxi6 libgconf-2-4 wget
RUN apt-get -y install libnss3
RUN apt-get -y install libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev
RUN pip3 install flask
RUN pip3 install splinter

RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver ./bin

ADD . /app
WORKDIR /app

EXPOSE 5000

CMD ["python3", "main.py"]
