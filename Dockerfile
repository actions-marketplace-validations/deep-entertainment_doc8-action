FROM python:3

COPY entrypoint.py /entrypoint.py

RUN pip3 -qqq install doc8

ENTRYPOINT ["python", "/entrypoint.py"]
