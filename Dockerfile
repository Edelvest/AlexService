FROM python:3.8.3-alpine3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/
RUN set -ex \
&& apk add --no-cache -t build-deps \
alpine-sdk \
linux-headers \
jpeg-dev \
postgresql-dev
RUN pip install -r requirements.txt
COPY . /app/
COPY docker-entrypoint.sh /app/
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]




