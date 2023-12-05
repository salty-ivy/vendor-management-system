runserver:
	python3 vendor_management_system/manage.py runserver


db:
	python3 vendor_management_system/manage.py makemigrations
	python3 vendor_management_system/manage.py migrate