# Hero
FastAPI is a popular package nowadays, and I have decided to share my setup for an async web-server using this
framework. The Hero app repository is an example of ultimate setup for async web-service.

## Dependencies
Here is a short description of python packages used in the article (just to make a whole picture to save your time):

1. [Poetry](https://python-poetry.org) - is a tool for dependency management and packaging in Python. It allows you to
   declare the libraries your project depends on and it will manage (install/update) them for you;
2. [FastAPI](https://fastapi.tiangolo.com) - is a modern, fast (high-performance), web framework for building APIs with
   Python 3.6+ based on standard Python type hints;
3. [Pydantic](https://pydantic-docs.helpmanual.io) - Data validation and settings management using Python type hinting;
4. [SQLAlchemy](https://www.sqlalchemy.org) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that
   gives application developers the full power and flexibility of SQL;
5. [SQLModel](https://sqlmodel.tiangolo.com) - SQLModel is a library for interacting with SQL databases from Python
   code, with Python objects;
6. [Alembic](https://alembic.sqlalchemy.org/en/latest/) - Alembic is a lightweight database migration tool for usage
   with the SQLAlchemy Database Toolkit for Python.

## mysql 
`docker run --name=mysql1 -p 3307:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql/mysql-server:8.0`<br/>
then enter into the container `docker exec -it [container-id] bash`<br/>
then log into mysql `mysql -u root -p`<br/>
create DB<br/>
create user `CREATE USER 'heroes_my'@'%' IDENTIFIED BY 'heroes_my';`<br/>
and then grant privileges <br/>
`GRANT ALL ON *.* TO 'heroes_my'@'%';` <br/>
`FLUSH PRIVILEGES;` <br/>

## env file
update environment variables. for example mysql url will be like `mysql+asyncmy://heroes_my:heroes_my@0.0.0.0:3307/heroes_db`

## Alembic Migration and commands
Alembic Initilization `alembic init -t async migrations`<br/>
Alembic migration file generation `alembic revision --autogenerate -m "heroes"`<br/>
Alembic run migration `alembic upgrade head`

## Deployment
Use this command to build Docker container: `docker build --build-arg ENV_FILE=".env" -t hero-app -f Dockerfile .`<br/>
And this command to start container: `docker run --network [common_services_common] -d -p "8080:80" --name hero-app hero-app`<br/>

Use this command to build Docker container for Worker: `docker build --build-arg ENV_FILE=".env" -t hero-app2 -f DockerfileCelery .`<br/>
And this command to start container: `docker run --network [common_services_common] -d --name hero-app2 hero-app2`<br/>

if we dont need to attach container to any existing network then `--network [common_services_common]` this have to be removed from the `docker run` command.<br/>
if redis or mysql is running from different network then we add this `--network [common_services_common]` in the `docker run` command and in connection url we put service name as hostname and the port of that container.<br/>

example:<br/>
```DB_ASYNC_CONNECTION_STR="mysql+asyncmy://root:root@mysql-5:3306/bl_cms"```<br/>
```CELERY_BROKER_URL="redis://redis:6379"```


## poetry related commands
add plugin: `poetry add [plugin-name]`<br/>
add plugin under specific group: `poetry add [plugin-name] --group [group name]`<br/>
install plugins from pyproject file: `poetry install`<br/>
remove plugin: `poetry remove [plugin-name]`

## Instructions to add new api endpoint
1. first create a new folder under `app`<br/>
2. always remember to add __init__.py file to any new folder created<br/>
3. then create 4 files under this newly created folder<br/>
   a. `api.py` - we'll add our endpoints here<br/>
   b. `models.py` - DB models will be there id needed<br/>
   c. `dependencies.py` - we'll add our DB connections related stuff here<br/>
   d. `crud.py` - this file will have the DB functions<br/>
   other than those files we can create service files to have the business logic<br/>
4. then in `endpoints.py` under `router` -> `api_v*` we should our endpoints created in the previous step

## Celery worker run
`celery -A app.core.celery_conf worker --loglevel=INFO`<br/>
for local --loglevel can be `DEBUG`


Source: https://medium.com/@estretyakov/the-ultimate-async-setup-fastapi-sqlmodel-alembic-pytest-ae5cdcfed3d4
