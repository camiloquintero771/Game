# PICAS Y FIJAS
Este es un proyecto para el desarrollo del juego PICAS y FIJAS
    
## Initial setup    
 You must create a file in the root of the project with the name .env with the following data:    
    
    #Django
    DEBUG=True
    SECRET_KEY=a2yvfghss3w(3tm)$3p_(*r1k$0u@hpp^^w8@9%1x(&e=_mu==
    TZ=America/Bogota    
    DJANGO_SETTINGS_MODULE=Game.settings
        
    #Postgres    
    POSTGRES_DB=Game_db
    POSTGRES_USER=Game_user
    POSTGRES_PASSWORD=Game2021**.
    POSTGRES_HOST=postgres    
    POSTGRES_PORT=5432

 Then you must run the following command to build all the project containers:    
    
 $ make build    
Finally you should generate the initial Django migrations, for them execute the following command    
    
 $ make migrate    
## Run project    
 To run the project you must execute the following command    
    
 $ make up    
> If you have problems connecting Django with Postgres, you should run the command: make restart CONTAINER=django    
 ## Other commands    
    
 1. **Create a new app:** make startapp NAME=example    
 2. **Generate migrations:** make migrate    
 3. **Create a superuser:** make superuser  
  
## Instrucciones de uso

para ingresar los datos correctamente el url debe quedar de la siguiten forma:

http://0.0.0.0:8000/juego/numero

donde número es el número que usted, desea ingresar


## Sort packages in the requirements.txt file

First you need to add the package to the requirements.txt file, then you run the **make build** command.
Finally, so that the packages are ordered and with their version established in the requirements.txt file, you must execute the following command.

    $ make get-requirements
