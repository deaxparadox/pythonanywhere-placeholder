FROM python:3.11-bullseye

# RUN apt update 
# RUN apt install useradd

RUN useradd -m -s /bin/bash normal

USER normal

WORKDIR /home/normal/django-app

COPY --chown=normal:normal . .

RUN export PATH="$PATH:/home/normal/.local/bin"
RUN export PRODUCTION=1

RUN pip install --upgrade pip && pip install -r requirements_django.txt

EXPOSE 8000

ENTRYPOINT [ "bash", "entrypoint.sh" ]