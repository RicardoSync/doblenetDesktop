# doblenetDesktop
# NOTA!
Es necesario tener un servidor directo al microtik para guardad la base de datos MySQL
ademas de ejecutar el script de cortes automaticos

# Requisitos
pip install -r requirements.txt


# Obtener requisitos
pip freeze > requirements.txt

# Importar base de datos al servidor
mysql -h 122.122.126.99 -u dni -p alpha < alpha.sql

# Para hacerlo funcionar en servidor
1.- Debe de ser un pc con linux de preferencia elementaryos
2.- Instalar mysql con sudo apt install mysql-server

Despues entrar a mysql como root usando el comando

sudo -i

Despues escribir el comando 
mysql -u root -p
Ingresar la password de usuario.

# Cpnfigurar MYSQL
una vez en mysql ingresar los comandos:

CREATE USER 'dni'@'%' IDENTIFIED BY 'MinuzaFea265/';

Despues
GRANT ALL PRIVILEGES ON . TO 'dni'@'%' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON . TO 'dni'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
CREATE DATABASE alpha;

# Finalizacion
Escribir el comando exit;
Despues exit para salir de root.

# Configuracion de permisos

Ahora para acceder a mysql del servidor desde la pc remota damos los permisos modificando
sudo nano /etc/mysql/my.cnf

Y buscamos la linea "bind-address = 127.0.0.1"
y le agregamos al inicio un "#" para comentar

Con cntl + o guardamos  y ctrl + x salimos

Ahora reiniciar
sudo systemctl restart mysql


sudo ufw allow 3306/tcp



# Base dedatos
Para que el sistema funcione de manera correcta, importa la base de datos que esta en BD a la base de datos alpha de mysql
con el comando:
mysql -u dni -p alpha < alpha.sql
