up:
	docker-compose up
stop:
	docker-compose stop
build:
	docker-compose build
migrations-test:
	docker-compose run --rm django ./manage.py makemigrations --settings=inventory.settings.test
migrate:
	docker-compose run --rm django ./manage.py makemigrations 
	docker-compose run --rm django ./manage.py migrate
requirements:
	docker-compose run --rm django pip install -r requirements.txt
get-requirements:
	docker-compose run --rm django pip freeze > requirements.txt
statics:
	docker-compose run --rm django ./manage.py collectstatic --no-input 
superuser:
	docker-compose run --rm django ./manage.py createsuperuser 
reset:
	docker-compose down -v
	rm -rf .pgdata/
startapp:
	docker-compose run --rm django ./manage.py startapp $(NAME)
	sudo chmod 777 -R ./$(NAME)
restart:
	docker-compose restart $(CONTAINER)
clean:
	rm -rf src/*/migrations/00**.py
	find . -name "*.pyc" -exec rm -- {} +
	rm -rf src/*/migrations/__pycache__/*
pylint:
	docker-compose run --rm django pylint $(APP)