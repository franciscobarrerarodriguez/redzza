# Redzza  ![CircleCI](https://circleci.com/gh/larry852/redzza.svg?style=svg&circle-token=cd70aaea93f105fc9177883b44ce4eb1abd5f6be)

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
| /api/v1/apiServices/createUser/ | email, first_name, last_name, password, place | POST | token, success, msg, err, user | Creacion de un nuevo usuario - /verify-email/key/ |
| /api/v1/apiServices/loginUser/ | email o username, password | POST | token, success, msg, err, user, timetoken | Login aplicativo mediante email o username y contraseña |
| /api/v1/apiServices/updateUser/ | username, first_name, last_name, email, avatar, icono, birth_date, gender, phone, biography, location, company, profession, address, avialability, i_search[] , i_have[] , tags[] | PUT | success, msg, err | Edicion del perfil usuario *Un campo a la vez* |
| /api/v1/apiServices/newNotice/ | kind(1,2), thing(P,S), title, category, time, state, offer, place, colors, description, locations, urgency | POST | success, msg, err, notice | Nueva publicacion de servicio o producto |
| /api/v1/apiServices/updateNotice/ | notice, title, category, time, state, offer, place, colors, description, locations, urgency, visibility | PUT | success, msg, err | Edicion publicacion de servicio o producto *Un campo a la vez* |
| /api/v1/images/ | notice, image | POST | image | Imagen para notice |
| /api/v1/images/*ID*/ | | DELETE | success | Eliminacion de imagen por id de notice |
| /api/v1/videos/ | notice, video | POST | video | Video para notice |
| /api/v1/videos/*ID*/ | | DELETE | success | Eliminacion de video por id de notice |
| /api/v1/users/*ID*/getData/ |  | GET | success, data, err | Informacion de un usuario por su id |
| /api/v1/users/*ID*/getNotices/ |  | GET | success, data, err | Publicaciones de un usuario por su id |
| /api/v1/notices/*ID*/ |  | DELETE | success | Visibilidad a false de una notice por su id |
| /api/v1/notices/*ID*/getData/ |  | GET | notice | Obtencion de informacion de un notice por su id |
| /api/v1/apiServices/searchNotice/ | kind(1,2), title, categories, locations | POST | success, data, err | Busqueda, kind obligatorio |
| /api/v1/notices/*ID*/getComments/ |  | GET | success, data, err | Comentarios de una notice por su id |
| /api/v1/comments/ | notice, commentary | POST | comentary | Creacion de comentario para notice |
| /api/v1/comments/*ID*/ | notice, commentary | PUT | comentary | Edicion de un comentario para notice |
| /api/v1/comments/*ID*/ |  | DELETE | comentary | Eliminacion de un comentario para notice |
| /api/v1/apiServices/getHome/ |  | GET | success, data, next, err | Publicaciones del home de un usuario por su id, pagina 1 |
| /api/v1/apiServices/getHome?page=N |  | GET | success, data, next, err | Publicaciones del home de un usuario por su id, pagina N |
| /api/v1/apiServices/startConversation/ | text, image, user o notice | POST | success, msg, err | Iniciar una conversacion |
| /api/v1/apiServices/addMessage/ | conversation, text, image | POST | success, msg, err | Agregar mensaje a una conversacion existente |
| /api/v1/conversations/*ID*/ |  | GET | success | Recuperacion de una conversacion por su id |
| /api/v1/conversations/*ID*/ |  | DELETE | success | Eliminacion de una conversacion por su id |
| /api/v1/apiServices/getInbox/ |  | GET | success, data, err | Obtencion de mensajes de un usuario |
| /api/v1/apiServices/getCountNotifications/ |  | GET | success, count, err | Obtencion de numero de notificaciones |
| /api/v1/apiServices/reviewConversation/ | conversation | POST | success, msg, err | Lectura de una conversacion |
| /api/v1/places/ |  | GET | data, success | Obtencion de departamentos |
| /api/v1/places/*ID*/getCities/ |  | GET | data, success | Obtencion de ciudades de un departamento |
| /api/v1/categories/ |  | GET | data, success | Obtencion de macrocategorias |
| /api/v1/categories/*ID*/getSubCategories/ |  | GET | data, success | Obtencion de subcategorias de una macrocategoria |
| /api/v1/apiServices/checkToken/ | token | POST | detail: Invalid token, Token has expired, Token has valid, User inactive or deleted | Verificacion de estado de token |
| /api/v1/apiServices/checkFollowing/ | user | POST | success, following, err | Verificacion de seguimiento de perfil |


## Kind
- i_have(Ofrezco) --> 1 
- i_search(Busco) --> 2



