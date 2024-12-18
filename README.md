# Entrega3

Para esta entrega se continua con la idea de crear algo que sea útil para manejar la informacion de alumnos de un estudio de pilates. 
El estudio se llama COOLates, y esta es su pagina de presentacion, con una seccion especial para crear y buscar alumnos

La rama principal se llama 'pilates', mientras que las app creadas se llaman
- app_alumnos: maneja la DB de alumnos del estudio
- app_profes: maneja la DB de profesores
    Esta app se enfoca en clases basadas en vistas
- app_acceso: maneja los accesos y perfiles de usuarios (dueños o gerentes del estudio)

Se prueba la parte de admin y permisos con lo siguiente: 

## SUPERUSER
username = admin
email = admin@admin.com
password = admin

## User
username = juanita
password = 2347cool
staff status = staff
permisos = Staff   - Grupo de permisos creados para el staff del estudio

## User
username = higuclap
password = chispita47

username = gremlina
password = pollito1

username = clarita
password = clar2323

username = fbodan
email = fbodan@hotmail.com
clave = fabi2323
repetir = fabi2323
nombre = fabiola
apellido = bodan

Algunos usuarios tienen su propio avatar, al igual que algunos profesores
La pagina se encuentra organizada de tal forma que sólo los usuarios logueados puedan crear/modificar/eliminar profesores o alumnos
Los usuarios pueden pos sí sólos cambiar su clave
Se utilizaron imagenes libres o propias para el proyecto, y se utilizó el bootstrap: 
        https://startbootstrap.com/theme/one-page-wonder