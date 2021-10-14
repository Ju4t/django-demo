FROM python:alpine

LABEL maintainer="235620@qq.com"
LABEL org.opencontainers.image.title="django-test"
LABEL org.opencontainers.image.authors="235620@qq.com"

ENV PYTHONUNBUFFERED 1
ENV MIRRORS https://mirrors.aliyun.com

WORKDIR /app
COPY . /app

# Alpine Linux 源 指向最新的稳定版本
RUN echo $MIRRORS/alpine/latest-stable/main > /etc/apk/repositories; \
    echo $MIRRORS/alpine/latest-stable/community >> /etc/apk/repositories

# pip install
RUN apk update && \
apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl && \
# pillow -> jpeg-dev
apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && \

pip install --no-cache-dir -r requirements.txt -i $MIRRORS/pypi/simple

# run
#CMD python manage.py runserver 0.0.0.0:8000