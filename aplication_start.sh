echo "Iniciar Aplicacion"
bash -c source "crudenv/bin/activate && python manage.py makemigrations && pythobn manage.py migrate && python manage.py runserver"