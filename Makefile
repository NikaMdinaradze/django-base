SETTINGS_DEV=core.settings.dev

makemigrations:
	@echo "Making Migration files"
	python manage.py makemigrations --settings=$(SETTINGS_DEV)

migrations:
	@echo "Running Migrations Docker"
	docker-compose run --rm api python src/manage.py migrate

build:
	@echo "building API test server docker"
	docker-compose build

run:
	@echo "starting API test server docker"
	docker-compose up

run_detached:
	@echo "starting API test server docker"
	docker-compose up -d

run_tests:
	@echo "running tests docker"
	docker-compose run --rm api python src/manage.py test

startapp:
	@echo "Creating app directory for $(app)"
	docker compose run --rm api sh -c "cd src/apps && python3 ../manage.py startapp $(app)"

createsuperuser:
	@echo "Creating super user"
	docker compose run --rm api python3 src/manage.py createsuperuser
