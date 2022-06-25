FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3-pip unzip xvfb libxi6 libgconf-2-4 wget firefox

RUN python3 -m pip install --upgrade pip
RUN pip3 install flask selenium requests

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
RUN tar -xvzf geckodriver*
RUN mv geckodriver* ./bin

ADD . /app
WORKDIR /app

EXPOSE 8080

CMD ["python3", "main.py"]
