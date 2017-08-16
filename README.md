# Redzza


## Api endpoints
| Endpoint | Parametros | Metodos | Retorno | Descripción |
| --- | --- | --- | --- | --- |
| / |  |  |  | Admin Django - WEB |
| /rest-auth/login/ | username, email, password | POST | token | Login api |
| /rest-auth/logout/ |  | POST | detail | Logout *Debe enviarse la cabecera Authorization con el token del usuario, para eliminar token* |
| /rest-auth/registration/ | username, password1, password2, email | POST | token | Registro api |
| /rest-auth/password/change/ | new_password1, new_password2, old_password | POST | detail | Cambio de contraseña |
| /rest-auth/password/reset/ | email | POST | detail | Olvide contraseña - *al correo llegara un link como el siguiente http://redzza.com/reset/MTg1/4on-ef2ef60380eb09fb2cb0/* /reset/uid/token/ |
| /rest-auth/password/reset/confirm/ | uid, token, new_password1, new_password2 | POST | detail | Olvide contraseña confirmacion - uid y token son enviados en el correo despues de usar /rest-auth/password/reset/ |
| /api/v1/ |  | GET | Lista de CRUDs | Modelos de la base de datos del negocio |
| /api/v1/apiServices/validateEmail/ | email | POST | exists, data | Verificacion de existencia de correo en modelo user |
| /api/v1/apiServices/createUser/ | email, first_name, last_name, password, place, i_search[] , i_have[] , suggesting | POST | token, success, msg, err, user | Creacion de un nuevo usuario |
| /api/v1/apiServices/loginUser/ | email o username, password | POST | token, success, msg, err, user, timetoken | Login de usuario al aplicativo mediante email o username y contraseña |
| /api/v1/apiServices/updateUser/ | username, first_name, last_name, email, avatar, icono, birth_date, gender, phone, biography, location, company, profession, address, avialability, i_search[] , i_have[] , tags[] | POST | success, msg, err | Edicion del perfil usuario *Un campo a la vez* |


## Paquetes pip

| Paquete       | Descripción   |
| ------------- | --------------|
| Django==1.11 | Django |
| pytz==2017.2 | Dependencia Django |
| psycopg2==2.7.3 | Paquete para gestion de base de datos PostgreSQL |
| Pillow==4.2.1 | Manejo de imagenes  |
| olefile==0.44 | Dependencia Pillow |
| gunicorn==19.7.1 | Ejecución en heroku |
| dj-database-url==0.4.2 | Ejecuión en heroku, base de datos |
| djangorestframework==3.4.6 | Django REST framework - Api |
| django-cors-headers==2.1.0 | Configuracion de CORS |
| django-rest-auth==0.9.1 | Autenticacion para Api |
| six==1.10.0 | Depencencia django-rest-auth |
| django-allauth==0.32.0 | Autenticacion para api |
| urllib3==1.22 | Dependencia django-allauth |
| requests-oauthlib==0.8.0 | Dependencia django-allauth |
| python3-openid==3.1.0 | Dependencia django-allauth |
| requests==2.18.3 | Dependencia django-allauth |
| defusedxml==0.5.0 | Dependencia django-allauth |
| oauthlib==2.0.2 | Dependencia django-allauth |
| chardet==3.0.4 | Dependencia django-allauth |
| certifi==2017.7.27.1 | Dependencia django-allauth |
| idna==2.5 | Dependencia django-allauth |
| djangorestframework-expiring-authtoken==0.1.4 | Token con expiracion de tiempo |



