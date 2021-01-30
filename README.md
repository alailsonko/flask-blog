## Flask Blog

### Documentation

### Commands

*** To rebuild the image
```shell
./manage.py compose build web
```

*** To spin up the containers
```shell
./manage.py compose up -d
```

*** To connect to the Postgres DB
```shell
./manage.py compose exec db psql -U postgres
```

*** To run DB initialization
```shell
./manage.py flask db init
```

*** To migrate
```shell
./manage.py flask db migrate
```

*** To upgrade
```shell
./manage.py flask db update
```

*** To run tests
```shell
./manage.py test
```

*** if first time running run
```shell
./manage.py create-initial-db
```

*** To create migrations
```shell
./manage.py flask db migrate -m "Initial user model"
```
