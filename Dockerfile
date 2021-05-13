From python:3.8

WORKDIR /code

COPY requirements.txt

RUN pip install -r requirements.txt

COPY src/

ENTRYPOINT ["python3"]
CMD ["app.py"]
