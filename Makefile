docker-compose:
	docker-compose up --build

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate
