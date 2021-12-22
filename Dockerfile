FROM ubuntu

ADD Frame.py .

RUN apt-get update -y

RUN apt-get install python3 -y

ENTRYPOINT [ "python3" ]

CMD [ "./Frame.py" ] 