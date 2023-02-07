FROM python:3.9

WORKDIR /app/

COPY ./app.py /app/
COPY ./model.py /app/
COPY ./utils.py /app/
COPY ./dummy.csv /app/
COPY ./requirements.txt /app/

RUN pip3 install -r requirements.txt

CMD uvicorn app:app --host=0.0.0.0 --reload
