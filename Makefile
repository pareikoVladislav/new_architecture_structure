run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

createadmin:
	python manage.py createsuperuser
