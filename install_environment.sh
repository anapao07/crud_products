echo "##### Actualizando el Sistema Operativo #####"
sudo apt update

echo "##### Instalando Python3.8 #####"
sudo apt install python3.8 python3-dev libpq-dev python3-distutils python3-venv

echo "##### Instalando pip3 #####"
sudo apt install python3-pip

echo "###### Instalando Virtualenv #####"
sudo pip3 install virtualenv

echo "##### Creando Entorno Virtual #####"
virtualenv -p python3.8 crudenv

echo "##### Instalando Requerimientos Necesarios de  Pthon #####"
bash -c "source crudenv/bin/activate && pip install -r requirements.txt"

