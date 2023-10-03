docker-compose:
	docker-compose -f ./docker/docker-compose.yaml --env-file .env up --build

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate