FROM python:2.7
LABEL maintainer="Prashanth P"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
#ENTRYPOINT [ "python" ]
CMD [ "python", "app.py" ]