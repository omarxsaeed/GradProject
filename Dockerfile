FROM ubuntu

ADD frame2.py .

RUN apt-get update -y

RUN apt-get install python3 -y

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "./frame2.py" ] 