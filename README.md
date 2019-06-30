# Bcredi - Bank Statements Info Extraction

## How to Run Properly

This project is both an REST API and a matrix to image conversor.
The database is also hostded under the same docker-compose file

[Docker](https://www.docker.com/) is required for all environments.

### Setup instructions:

1. Clone this repository (you need [git](https://git-scm.com/) installed):
  
    `git clone git@github.com:bcredi/bcredi-img-rec.git`

### Running:

1. Run the bash script:
   
   *If running in local or staging:*
    
        docker-compose up
    
### Understand the application:

1. Flask handle the web part os the application, manananging routes and the io to bank
2. Celery is used to async heavy tasks when needed
3. You can find the Flask + Celery functions in the `server.py` file
4. You can better understand the code by reading the introduction of each tool
in its documentation of [Flask](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application) and [Celery](http://docs.celeryproject.org/en/latest/getting-started/introduction.html)

### REST endpoints:

**/create_user ['POST']**
this endpoint will check if any user with thar user name is already in the database,
if it`s not, a new user will be created.

expected input:
```
{   
	"username": "$nome_do_usuario",
    "email": "$email_do_usuario",
	"password": "$senha_do_usuario"
}
```

**/check_user ['POST']**
This endpoint will check if any user with that user name is already in the database,
if it is, the stored password will compared with the sent one, if they mach a sucess
message will be returned.

expected input:
```
{   
	"username": "$nome_do_usuario",
	"password": "$senha_do_usuario"
}
```

**/create_image ['POST']**
This endpoint will start a new async task and will return the new task id
expected input 
```
{   
    "user_id": "$id_do_ususario"
	"matrix": "8 9 9; 7 10 7; 10 2 10"
}
```

**/pull_state/<task_id> ['GET']**
This endpoint will expect a task id and will return the task status.


### REST return
If the seded request fails the return will be a json with an 'error' value
you may use the error value to provide some feedback to the user 
``` 
{
    "error": "username already in use"
}
```

If the request succeed the return wil be a 'sucess' value
```
{
    "sucess": "right password"
    "user_id": "$id_do_usuario"
}
```