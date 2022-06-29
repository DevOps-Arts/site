FROM alpine:latest
RUN mkdir /site
WORKDIR /site
RUN apk update && apk add python3
COPY . /site
CMD python3 /site/run.py
EXPOSE 8005
