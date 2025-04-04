#!/bin/sh

# echo "Waiting for postgres..."

# until pg_isready "${DATABASE_URL:-'postgis://localhost/galery'}"; do
#     echo "Awaiting Database container on  ${POSTGRES_HOST:-db}:${POSTGRES_PORT:-5432}"
#     sleep 1
# done

# echo "PostgreSQL started"

python manage.py migrate
# python manage.py loaddata ./commons/fixtures/*.xml
# python manage.py loaddata ./map_layers/fixtures/*.xml
# python manage.py loaddata ./species/fixtures/*.xml
# python manage.py loaddata ./geo_area/fixtures/*.xml.gz
echo "************** Create backend superuser ******************"

script="
from django.contrib.auth import get_user_model

username = '$SU_USERNAME';
password = '$SU_PWD';
email = '$SU_EMAIL';

User = get_user_model()

if User.objects.filter(is_superuser=True).count()==0:
    superuser=User.objects.create_user(username, email, password);
    superuser.is_superuser=True;
    superuser.is_staff=True;
    superuser.save();
    print('Superuser',username,'created.');
else:
    print('One or more Superuser already exists, creation skipped.')
"

printf "$script" | python manage.py shell

if [ "$DEBUG" = "True" ]; then
    python -m manage runserver 0.0.0.0:8000
else
    gunicorn -b 0.0.0.0:8000 config.wsgi --workers ${GUNICORN_WORKERS:-3}
fi
