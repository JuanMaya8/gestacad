📘 Sistema Académico – README

Bienvenido al Sistema Académico, una plataforma desarrollada en Django para gestionar usuarios, estudiantes, cursos, calificaciones y asistencias.

Este archivo explica:

✅ Cómo instalar el proyecto
✅ Cómo configurar la base de datos
✅ Cómo ejecutar el servidor
✅ Cómo crear usuarios y roles
✅ Cómo funciona la asignación automática del rol estudiante
✅ Dependencias requeridas
✅ Estructura del proyecto

📦 1. Requisitos

Antes de comenzar, instala:

Python 3.10+

pip

virtualenv (opcional pero recomendado)

Git

SQLite (ya viene incluido con Python)

⚙️ 2. Instalación del Proyecto

Clona el repositorio:

git clone https://github.com/tuproject/sistema-academico.git
cd sistema-academico

Crea un entorno virtual:
python -m venv venv

Activa el entorno virtual:

En Windows:
venv\Scripts\activate

En Linux/Mac:
source venv/bin/activate

Instala las dependencias:
pip install django pillow

📂 3. Dependencias

Tu requirements.txt debería incluir:
Django==4.2
pillow

Si usas crispy-forms o bootstrap, añade también:
django-crispy-forms
crispy-bootstrap5

🛠️ 4. Migraciones y Base de Datos
python manage.py makemigrations
python manage.py migrate

🔑 5. Crear Superusuario
python manage.py createsuperuser

Este usuario será admin y podrá:

Registrar usuarios

Activarlos y desactivarlos

Crear cursos

Ver asistencias y calificaciones

🚀 6. Ejecutar el Servidor
python manage.py runserver

Visita:

👉 http://127.0.0.1:8000/

👤 7. Roles en el Sistema

El modelo Usuario tiene un campo rol, que puede ser:

admin

docente

estudiante

✔ Asignación automática de Estudiante

Si un usuario tiene rol estudiante, se crea automáticamente:

Su objeto Estudiante

Su perfil de matrícula

Esto ocurre en:

usuarios/signals.py

📘 8. Endpoints Principales

| URL                            | Descripción          |
| ------------------------------ | -------------------- |
| `/usuarios/login/`             | Login                |
| `/usuarios/registro/`          | Registrar usuario    |
| `/dashboard/`                  | Dashboard según rol  |
| `/cursos/`                     | Lista de cursos      |
| `/estudiantes/inscribir/<id>/` | Inscribir a un curso |


🔐 9. Control de Roles

Accesos protegidos con:

@rol_requerido(['admin'])
@rol_requerido(['docente'])
@rol_requerido(['estudiante'])

Archivo:

usuarios/decorators.py

📁 10. Estructura del Proyecto

sistema_academico/
│
├── usuarios/
│   ├── models.py
│   ├── views.py
│   ├── signals.py
│   ├── decorators.py
│
├── estudiantes/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── cursos/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── evaluaciones/
│   ├── models.py
│   ├── views.py
│
├── dashboard/
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── navbar.html
│
├── manage.py
└── README.md

🧪 11. Tests (Opcional)
Ejemplo:
python manage.py test

🎯 12. Contribuciones

¡Pull requests y mejoras son bienvenidas!

🧑‍💻 13. Autor

Juan David Maya Benavides
Estudiante de Ingeniería de Software
Universidad Cooperativa de Colombia

