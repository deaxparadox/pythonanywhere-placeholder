FROM python:3.11.1-alpine

# RUN apt update 
# RUN apt install useradd
# RUN apk update
# RUN apk add -y useradd

# RUN useradd -m -s /bin/bash normal

ARG user=normal

RUN adduser --disabled-password ${user} 
USER ${user}

WORKDIR /home/normal/django-app

COPY --chown=normal:normal . .

ENV PATH="$PATH:/home/${user}/.local/bin"
ENV PRODUCTION=1

RUN pip install --upgrade pip && pip install -r requirements_django.txt

EXPOSE 8000

ENTRYPOINT [ "sh", "entrypoint.sh" ]