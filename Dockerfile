FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE ${PORT}
#EXPOSE 5000

# running tests
RUN pytest

#ENTRYPOINT ["quart",  "run",  "--host=0.0.0.0",  "--port=5000"]
RUN chmod +x prod.sh
ENTRYPOINT ["./prod.sh"]
