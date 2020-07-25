echo"##### Se Esta Instalando Postgres #####"
sudo apt update
sudo apt install postgresql postgresql-contrib

echo"##### Creando Usuario en Postgres #####"
sudo -u postgres crateuser paola
sudo -u postgres psql -c "ALTER USER paola WITH PASSWORD 'test1234';"

echo "##### Creando Base de Datos #####"
sudo -u postgres createdb app_products
sudo -u postgres psql -c "grant all privileges on database app_products to paola;"
