FROM python:3.10

WORKDIR /usr/src/app

COPY diva .

RUN ls -l

RUN pip install requests

WORKDIR /usr/src/app

CMD ["python", "token-finder.py"]