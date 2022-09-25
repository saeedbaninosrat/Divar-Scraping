FROM python:3.10

WORKDIR /usr/src/app

COPY diva .

RUN ls -l

RUN pip install scrapy

WORKDIR /usr/src/app/divar/spiders

# RUN scrapy crawl divar -o 19sep.csv -t csv

CMD ["scrapy", "crawl", "divar","-o", "19sep.csv", "-t", "csv"]

