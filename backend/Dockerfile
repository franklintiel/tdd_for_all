FROM python:3.6.3-alpine
RUN mkdir /usr/src/app && mkdir /usr/src/app/backend && mkdir /usr/src/app/files && mkdir /usr/src/app/files/logs && mkdir /usr/src/app/files/media
WORKDIR /usr/src/app/backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . .
RUN pip install --upgrade pip
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev libjpeg
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN chmod +x entrypoint.sh
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/America/Bogota /etc/localtime
ENTRYPOINT [ "./entrypoint.sh" ]

