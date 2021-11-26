# Lab 03.2 - Uso de Pyspark

En el siguiente laboratorio, usaremos un dataset de casos de covid e implementaremos operaciones de agrupación y conteo para dar respuesta a unas preguntas de negocio que buscan saber desde los municipios con más casos de covid registrados hasta el total de casos registrados por sexo.

## Cómo trabajaremos
Desde nuestra instancia master en el EMR, nos conectaremos a Jupyter Notebook y crearemos un nuevo archivo, donde ejecutaremos el código que se encuentra en el repositorio y el cual nos dará el siguiente resultado leyendo el dataset que se encuentra en el bucket de S3.

Mostrar:

```
Las 10 ciudades con más contagiados
```
![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0032-covid/cities.jpg)

```
Los 10 departamentos con más contagiados
```
![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0032-covid/dep2.jpg)

```
casos de covid por edad
```
![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0032-covid/edad.jpg)

```
Las 10 fechas registradas con más contagiados
```
![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0032-covid/fecha.jpg)

```
El total de contagiados con base al sexo de las personas
```
![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0032-covid/sexo.jpg)

Adicional a esto, se mostrará que las variables por paquetes quedaron almacenados en S3:

![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0032-covid/variables.jpg)

Y la manera de guardarlas:

![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0032-covid/variableJupyter.jpg)

Adjuntamos el repositorio guía para solucionar este laboratorio: https://github.com/st0263eafit/st0263_20212/blob/main/bigdata/lab3-2-pyspark.txt

## Creado por
Cristian Darío Ceballos Rodríguez
cdceballor@eafit.edu.co

Tópicos especiales en telemática
