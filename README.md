# Bienvendos al repositorio oficial de AlgoriSoft

Este proyecto inicio desde el año 2019 para los siguientes cursos de mi canal de [Youtube](https://www.youtube.com/c/AlgoriSoft "Youtube"):

- [Curso de Python con Django de 0 a Máster | Español](https://youtube.com/playlist?list=PLxm9hnvxnn-j5ZDOgQS63UIBxQytPdCG7 "Curso de Python con Django de 0 a Máster | Español")
- [Curso de Deploy de un Proyecto Django en un VPS Ubuntu | Español](https://youtube.com/playlist?list=PLxm9hnvxnn-hFNSoNrWM0LalFnSv5oMas "Curso de Deploy de un Proyecto Django en un VPS Ubuntu | Español")

# Instalación

##### 1) Clonar o descargar el proyecto del repositorio

`git clone https://gitlab.com/tutorship/apolo.git`

##### 2) Crear un entorno virtual para posteriormente instalar las librerias del proyecto

- `python3 -m venv venv` (Windows)
-  `virtualenv venv -ppython3` (Linux)

##### 3) Instalar el complemento de [weasyprint](https://weasyprint.org/ "weasyprint")

- Si estas usando Windows debe descargar el complemento de [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases "GTK3 installer"). En algunas ocaciones se debe colocar en las variables de entorno como primera para que funcione y se debe reiniciar el computador.
- Si estas usando Linux debes instalar las [librerias](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#linux "librerias") correspondientes a la distribución que tenga instalado en su computador.

##### 4) Activar el entorno virtual de nuestro proyecto

- `cd venv\Scripts\activate.bat` (Windows)
- `source venv/bin/active` (Linux)

##### 5) Instalar todas las librerias del proyecto que se encuentran en la carpeta deploy

- `pip install -r deploy/requirements.txt`

##### 6) Crear la base de datos con las migraciones y el superuser para iniciar sesión.

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`



------------

#  Si te gusta y te sirve mi contenido ✅🙏
### ¡Apóyame! para seguir haciéndolo siempre 😊👏
Paso la mayor parte de mi tiempo creando contenido y ayudando a futuros programadores sobre el desarrollo web con tecnología open source.

🤗💪¡Muchas Gracias!💪🤗

**Puedes apoyarme de la siguiente manera.**

**Suscribiéndote**
https://www.youtube.com/c/AlgoriSoft?sub_confirmation=1

**Siguiendo**
https://www.facebook.com/algorisoft

**Donando por PayPal**
williamjair94@hotmail.com

***AlgoriSoft te desea lo mejor en tu aprendizaje y crecimiento profesional como programador 🤓.***


