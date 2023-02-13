FROM python:3.9

WORKDIR /app/

COPY ./app.py /app/
COPY ./utils/model.py /app/utils/
COPY ./utils/utils.py /app/utils/
COPY ./db/dummy.csv /app/db/
COPY ./requirements.txt /app/


RUN pip3 install -r requirements.txt

CMD uvicorn app:app --host=0.0.0.0 --reload