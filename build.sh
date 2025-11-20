#!/bin/bash

# Colectar archivos estáticos
python manage.py collectstatic --no-input

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario si no existe (opcional)
# python manage.py shell << END
# from django.contrib.auth.models import User
# if not User.objects.filter(username='admin').exists():
#     User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
# END
