# Entrega 1 - Producto 2 (Creación y despliegue de una página monolítica con Wordpress)

En el siguiente proyecto, se crea una página con fuente de Wordpress y se despliega con Docker en una máquina virtual de google cloud platform.

## Uso

Usarempos 
Comandos de docker
En la vm usaremos Ubuntu 16.04
Usaremos certificado ssl letsencrypt con certbot
Instancia de Wordpress
 
## Ejecución
Crear la instancia de GCP y colocaremos 
```
Seguir los siguientes [pasos](https://dev.to/gelopfalcon/crear-un-vm-linux-en-gcp-2e0d#:~:text=Crea%20una%20instancia%20de%20m%C3%A1quina%20virtual%201-%20En,el%20nombre%20que%20quieres%20que%20tu%20instancia%20tenga.)
```

Una vez conectados con ssh desde la instancia de GCP, procederemos a instalar todo lo necesario para trabajar

Desde el dominio del root (sudo -i)
```
    1  add-apt-repository ppa:certbot/certbot
    2  apt-get update
    3  apt-get install python-certbot-nginx
    4  certbot --nginx -d sudomain.com -d www.sudomain.com
    5  cp /etc/letsencrypt/live/www.susudominio.com/* /home/suusuariodevm/wordpress/ssl/
    6  cp /etc/letsencrypt/live/sudominio.com/* /home/suusuariodevm/wordpress/ssl/
    7  cp /etc/letsencrypt/options-ssl-nginx.conf /home/suusuariodevm/wordpress/ssl/
    8  cp /etc/letsencrypt/ssl-dhparams.pem /home/suusuariodevm/wordpress/ssl/
    9  sudo chmod +x /usr/local/bin/docker-compose
   10  clear
   11  exit
```

Desde el usuario de vm
```
    1  sudominio.com suipestatica
    2  www.sudominio.com suipestatica
    8  sudo apt-get update -y
    9  sudo apt-get upgrade -y && sudo shutdown -r now
   11  sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.sudominio.com --manual --preferred-challenges dns-01 certonly
   20  mkdir wordpress ssl
   25  cd wordpress/
   26  mkdir ssl
   27  sudo su
   29  sudo apt-get install docker -y
   36  sudo apt-get remove apache2
   37  sudo service nginx restart
   38  sudo apt-get install docker
   39  sudo apt update
   41  sudo apt-get upgrade
   45  sudo apt-get install git -y
   50  sudo systemctl enable docker
   53  sudo apt-get install docker -y
   54  sudo apt-get update
   62  sudo apt-get install docker.io
   64  sudo systemctl enable docker
   65  sudo systemctl start docker
   66  sudo usermod -a -G docker suusuariodevm
   67  sudo curl -L https://github.com/docker/compose/releases/download/1.27.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
   68  sudo chmod +x /usr/local/bin/docker-compose
```
Ya tendremos la aplicación ejecutada y corriendo en docker

## Creado por
Cristian Darío Ceballos Rodríguez
cdceballor@eafit.edu.co
Tópicos especiales en telemática

Fuente: https://github.com/st0263eafit/st026320212/tree/main/docker-nginx-wordpress-ssl-letsencrypt