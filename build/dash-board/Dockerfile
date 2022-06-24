FROM python:3.7

COPY ./code /usr/local/src/dash-board
WORKDIR /usr/local/src/dash-board

RUN pip install -r requirements.txt 

CMD ["gunicorn" , "--bind", "0.0.0.0:80", "--timeout", "180","DashBoard:server"]
