python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
export PATH="$PATH:/home/normal/.local/bin"
export PRODUCTION=1
# which django-admin
# echo "$PATH"
python manage.py placeholder --populate --row 100
echo
python manage.py runserver 0.0.0.0:8000