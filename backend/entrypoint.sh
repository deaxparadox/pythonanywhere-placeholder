python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py placeholder --populate --row 10
echo
python manage.py runserver 0.0.0.0:8000