<<<<<<< HEAD
FROM python:3.8-slim-buster
WORKDIR /service
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3","app.py" ]
=======

>>>>>>> 8067418791aed780497459414c2046bad2ce7a23
