# Lab 01 - Manejo de archivos con hdfs y hadoop

En el siguiente laboratorio, copiaremos los archivos que dejamos iniciados en el anterior laboratorio (lab00), lo que haremos será copiar los archivos de un github a hadoop y luego a un bucket de S3.

## Cómo trabajaremos
Primero que nada, debemos ingresar a nuestro master conectado a la instancia de Ec2, de esta forma, nos permitirá trabajar con todos los comandos necesarios para lograr el objetivo.

## Pasar datos del repositorio a hadoop
clonaremos dentro de la instancia el repositorio: https://github.com/st0263eafit/st0263_20212.git   y entraremos hasta la carpeta de datasets.
Procederemos, desde nuestra instancia, a escribir el comando 

```
user@master$ hdfs dfs -mkdir /user/<username>/datasets
```

para poder crear una carpeta, ojo, cambiar el username por el nombre de usuario de tu preferencia.

Una vez creada la carpeta, usaremos el comando
user@master$ hdfs dfs -copyFromLocal /datasets/* /user//datasets/

para copiar los datos desde la carpeta datasets del repositorio clonado, hasta nuestra cuenta en hadoop previamente creada.

Al final, podremos ya tener los datos dentro de Hadoop.
Hadoop
![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab01-s3-files/WhatsApp%20Image%202021-11-12%20at%2017.41.03.jpeg)

En el proceso de S3, funciona idénticamente igual, lo único que cambia es que ahora no será el comando con hdfs dfs -copyFromLocal sino que cambiará por hadoop distcp ya que copiaremos de hadoop hacia S3.

```
user@master$ hadoop distcp s3://(bucketName)/datasets/*
```

Y así tendremos resultado de los datos dentro de S3.

S3
![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab01-s3-files/WhatsApp%20Image%202021-11-12%20at%2017.40.44.jpeg)

Para más detalles, consultar: https://github.com/st0263eafit/st0263_20212/tree/main/bigdata/01-hdfs
## Creado por
Cristian Darío Ceballos Rodríguez
cdceballor@eafit.edu.co

Tópicos especiales en telemática
