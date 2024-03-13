FROM python:3.10.13-alpine3.18

RUN mkdir -p /app 
#/usr/src/app defaults

WORKDIR /app

COPY app.py ./
# . . =all files in the same Floder put in workdirไฟล์ทั้งหมดในโฟลเดอร์นี้เอาไปลงในเวิ้คได

RUN pip install FLASK

RUN pip install requests

CMD python app.py