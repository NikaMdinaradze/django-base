# Django Base Project

## Project requirements

* docker >= 20.10.0
```docker --version```
* docker-compose >= 1.29.0
```docker-compose --version```
* python >= 3.10


# Development Environment Set Up

## Start project local
### Clone Project to your local environment
```bash
  git clone git@github.com:NikaMdinaradze/django-base.git
```

## Run project using docker-compose
#### Build and start containers
Build images and start containers. Migration command will be run during startup.
```bash
  make build
  make run
```

#### Working with running container
* When container is running
```bash
  docker-compose exec api <your_command>
```
* Without running container
```bash
  docker-compose run --rm api <your_command>
```

### Installation pre-commit

```bash
  make install_pre_commit
```

### Unit tests
Run tests
```bash
  make run_tests
```

### Startapp
Create Django application
```bash
  make startapp app=your_app_name
```

## Project Structure

```bash
src/
    apps/
         app_name/
              models/
              serializers/
              views/
              urls/
              ... # other app modules
         ...      # all other apps will be placed here
    core/
         settings/
    utils/
          ...

docker-compose.yml
dockerfiles/
    Dockerfile
    ...
requirements.txt
```
