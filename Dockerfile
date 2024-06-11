FROM python:3
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get -update && apt-get install -y python3 python3-pip && pip3 install -r requirements.txt
COPY . /app
CMD ["python", "run.py"]
EXPOSE 5001