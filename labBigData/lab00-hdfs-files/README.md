# Entrega Lab 00 - Big data (Manejo de archivos con clúster EMR aws)

En el siguiente laboratorio, pudimos implementar la creación de un clúster desde aws con el servicio de EMR que nos facilitaba la creación, conexión y manejo de las instancias de Ec2 y un bucket de S3.
## Creación

1. Procedemos a la creación desde aws - EMR en la barra de servicios y su debida configuración con sus servicios.

### paquetes a instalar.

```
versión del EMR 6.3.1
Hadoop 3.2.1
JupyterHub 1.2.0
Hive 3.1.2
Sqoop 1.4.7
Zeppelin 0.9.0
Tez 0.9.2
JupyterEnterpriseGateway 2.1.0
Hue 4.9.0
Spark 3.1.1
Livy 0.7.0
Hcatalog 3.1.2
```

Luego de esperar el tiempo estimado (entre 25 a 30 minutos) tendremos nuestro clúster.
![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab00-hdfs-files/WhatsApp%20Image%202021-11-12%20at%2017.39.57.jpeg)

Una vez con el clúster, debemos habilitar los puertos requeridos tales como el 22.

## Cómo trabajar
Debemos entrar a la instancia master y desde ahí poder ejecutar los comandos de hdfs dfs para proceder a copiar los archivos creando las carpetas requeridas para el proyecto.
Usaremos los datos dentro del dataset del siguiente github: https://github.com/st0263eafit/st0263_20212
dentro del github encontraremos un directorio con datasets, ahí será donde trabajaremos.

## Creado por
Cristian Darío Ceballos Rodríguez
cdceballor@eafit.edu.co

Tópicos especiales en telemática
