FROM python:3.7-alpine
MAINTAINER Sergio B SDBWebApps

ENV PYTHONUNBUFFERED 1

# store dependencies
COPY ./requirements.txt /requirements.txt
# RUN apk add --update --no-cache postgresql-client jpeg-dev
# RUN apk add --update --no-cache --virtual .tmp-build-deps \
    #   gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
# RUN apk del .tmp-build-deps

# directory to store app code - also to share with other containers, i.e nginx or a webserver that needed to serve these media files
RUN mkdir /app
WORKDIR /app
COPY ./app /app
# create directory to save media
# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static
# create user that's run app - avoid root acct.
RUN adduser -D user
# change owner
# RUN chown -R user:user /vol/
# RUN chmod -R 755 /vol/web
USER user