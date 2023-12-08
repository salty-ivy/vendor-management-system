runserver:
	python3 src/manage.py runserver


db:
	python3 src/manage.py makemigrations
	python3 src/manage.py migrate

app:
	python3 src/manage.py startapp $(NAME)
	mv $(NAME) src

superuser:
	python3 src/manage.py createsuperuser

urls:
	python3 src/manage.py show_urls
