
- Python 3.12
- Docker  

### Local setup

After cloning the repo:

1. configure environment at .env:

   define SECRET_KEY,

   define WEB_PORT,

   define POSTGRES_PORT,

   define POSTGRES_DB, 

   define POSTGRES_USER

   define POSTGRES_PASSWORD

   define POSTGRES_HOST

   define EMAIL_HOST
   
   define EMAIL_PORT
   
   define EMAIL_HOST_USER

   defineEMAIL_HOST_PASSWORD

2. Build and run the docker container

```
docker-compose up -d --build    
```

3. Migrate database

```
docker-compose exec web python manage.py migrate --noinput
```

4. Check if the installation succeeds by opening the [http://localhost:<WEB_PORT>/]() 

5. Try it out:

   create events at '/events/'


