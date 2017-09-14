# Redzza

## Modelo E-R
![MER](modeloE-R.png?raw=true "Modelo E-R")

## Api endpoints
| Endpoint | Parametros | Metodos | Retorno | Descripción |
| --- | --- | --- | --- | --- |
| / |  |  |  | Admin Django - WEB |
| /rest-auth/login/ | username, email, password | POST | token | Login api |
| /rest-auth/registration/verify-email/ | key | POST | detail | Verificacion de correo |
| /rest-auth/logout/ |  | POST | detail | Logout *Identificacion de user mediante token* |
| /rest-auth/password/change/ | new_password1, new_password2, old_password | POST | detail | Cambio de contraseña |
| /rest-auth/password/reset/ | email | POST | detail | Olvide contraseña - /reset/uid/token/ |
| /rest-auth/password/reset/confirm/ | uid, token, new_password1, new_password2 | POST | detail | Olvide contraseña confirmacion - uid y token son enviados en el correo despues de usar /rest-auth/password/reset/ |
| /api/v1/ |  | GET | Lista de CRUDs | Modelos de la base de datos del negocio |
| /api/v1/apiServices/validateEmail/ | email | POST | exists, data | Verificacion de existencia de correo |
| /api/v1/apiServices/createUser/ | email, first_name, last_name, password, place, i_search[] , i_have[] , suggesting | POST | token, success, msg, err, user | Creacion de un nuevo usuario - /verify-email/key/ |
| /api/v1/apiServices/loginUser/ | email o username, password | POST | token, success, msg, err, user, timetoken | Login aplicativo mediante email o username y contraseña |
| /api/v1/apiServices/updateUser/ | username, first_name, last_name, email, avatar, icono, birth_date, gender, phone, biography, location, company, profession, address, avialability, i_search[] , i_have[] , tags[] | PUT | success, msg, err | Edicion del perfil usuario *Un campo a la vez* |
| /api/v1/apiServices/newNotice/ | kind(1,2), thing(P,S), title, category, time, state, offer, place, colors, description, locations, urgency | POST | success, msg, err, notice | Nueva publicacion de servicio o producto |
| /api/v1/apiServices/updateNotice/ | notice, title, category, time, state, offer, place, colors, description, locations, urgency, visibility | PUT | success, msg, err | Edicion publicacion de servicio o producto *Un campo a la vez* |
| /api/v1/images/ | notice, image | POST | image | Imagen para notice |
| /api/v1/images/*ID*/ | | DELETE | success | Eliminacion de imagen por id de notice |
| /api/v1/videos/ | notice, video | POST, DELETE | video | Video para notice |
| /api/v1/videos/*ID*/ | | DELETE | success | Eliminacion de video por id de notice |
| /api/v1/users/*ID*/getData/ |  | GET | success, data, err | Informacion de un usuario por su id |
| /api/v1/users/*ID*/getNotices/ |  | GET | success, data, err | Publicaciones de un usuario por su id |
| /api/v1/notices/*ID*/ |  | DELETE | success | Visibilidad a false de una notice por su id |
| /api/v1/notices/*ID*/getData/ |  | GET | notice | Obtencion de informacion de un notice por su id |
| /api/v1/apiServices/searchNotice/ | kind(1,2), title, categories, locations | POST | success, data, err | Busqueda, kind obligatorio |
| /api/v1/notices/*ID*/getComments/ |  | GET | success, data, err | Comentarios de una notice por su id |
| /api/v1/comments/ | notice, profile, commentary | POST | comentary | Creacion de comentario para notice |
| /api/v1/comments/*ID*/ | notice, profile, commentary | PUT | comentary | Edicion de un comentario para notice |
| /api/v1/comments/*ID*/ |  | DELETE | comentary | Eliminacion de un comentario para notice |
| /api/v1/apiServices/getHome/ |  | GET | success, data, err | Publicaciones del home de un usuario por su id |
| /api/v1/apiServices/startConversation/ | notice, text, image | POST | success, msg, err | Iniciar una conversacion |
| /api/v1/apiServices/addMessage/ | conversation, text, image | POST | success, msg, err | Agregar mensaje a una conversacion existente |
| /api/v1/conversations/*ID*/ |  | DELETE | success | Eliminacion de una conversacion por su id |
| /api/v1/apiServices/getInbox/ |  | GET | success, data, err | Obtencion de mensajes de un usuario |
| /api/v1/apiServices/getCountNotifications/ |  | GET | success, count, err | Obtencion de numero de notificaciones |
| /api/v1/apiServices/reviewConversation/ | conversation | POST | success, msg, err | Lectura de una conversacion |
| /api/v1/places/ |  | GET | data, success | Obtencion de departamentos |
| /api/v1/places/*ID*/getCities/ |  | GET | data, success | Obtencion de ciudades de un departamento |
| /api/v1/categories/ |  | GET | data, success | Obtencion de macrocategorias |
| /api/v1/categories/*ID*/getSubCategories/ |  | GET | data, success | Obtencion de subcategorias de una macrocategoria |
| /api/v1/apiServices/checkToken/ |  | GET | detail: Invalid token, Token has expired, Token has valid | Verificacion de estado de token |


## Kind
- i_have(Ofrezco) --> 1 
- i_search(Busco) --> 2

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



