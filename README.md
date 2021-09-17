# Inventory 
It's a project for small and medium-sized companies that need to keep track of all their products    
    
## Initial setup    
 You must create a file in the root of the project with the name .env with the following data:    
    
    #Django
    DEBUG=False      
    SECRET_KEY=g-d^%97w4jgu_+2fzo&io3^tqq71315vv8kv80%%_xm#aqx38g      
    TZ=America/Bogota      
    DJANGO_SETTINGS_MODULE=inventory.settings.local      
          
    #Postgres      
    POSTGRES_DB=inventory_db      
    POSTGRES_USER=inventory_user      
    POSTGRES_PASSWORD=inventory2021**.      
    POSTGRES_HOST=postgres      
    POSTGRES_PORT=5432      
          
    #Redis      
    REDIS_URL=redis://redis:6379/0    
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
  
## Test Environment  
  
In the following url you will be able to carry out tests in a secure environment, with the following superuser:  
[Inventory - Test Environment URL](https://inventory-enodev.herokuapp.com/)  
  
 - **User:** root  
 - **Password:** 3n0cd3v

## Sort packages in the requirements.txt file

First you need to add the package to the requirements.txt file, then you run the **make build** command.
Finally, so that the packages are ordered and with their version established in the requirements.txt file, you must execute the following command.

    $ make get-requirements
