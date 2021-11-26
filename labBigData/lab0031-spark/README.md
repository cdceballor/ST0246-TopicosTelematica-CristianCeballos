# Lab 03.1 - pyspark y primeros pasos con wordcount.txt

En el siguiente laboratorio, trabajaremos con Spark para contar el total de palabras que se encuentran en un archivo .txt ejecutando el código desde HDFS, S3 y Jupyter, y luego, almacenar esos resultados en paquetes.

## Cómo trabajaremos
Primero que nada, entraremos a nuestro EMR y a nuestra instancia master, donde podremos ejecutar el código para contar las palabras y luego almacenarlo tanto en HDFS y S3, el código lo podemos encontrar en: https://github.com/st0263eafit/st0263_20212/tree/main/bigdata/03-spark 

## Pasar datos del repositorio a hadoop
clonaremos dentro de la instancia el repositorio: https://github.com/st0263eafit/st0263_20212.git   y entraremos hasta la carpeta de datasets.
Procederemos, desde nuestra instancia, a escribir el comando 

Ejecutaremos la primera instrucción:
```
$ pyspark
>>> files_rdd = sc.textFile("hdfs:///datasets/gutenberg-small/*.txt")
>>> files_rdd = sc.textFile("s3://st0263datasets/gutenberg-small/*.txt")
>>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
>>> wc = wc_unsort.sortBy(lambda a: -a[1])
>>> for tupla in wc.take(10):
>>>     print(tupla)
>>> wc.saveAsTextFile("hdfs:///tmp/wcout1")

* asi salva wc un archivo por rdd.
* si quiere que se consolide en un solo archivo de salida:

$ pyspark
>>> ...
>>> ...
>>> wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout2")
```
La salida será:

![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0031-spark/save.jpg)

O desde la terminal:

![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0031-spark/terminal1.jpg)

Luego para confirmar existencia de los archivos:

![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0031-spark/save1.jpg)

Al usar el mismo código pero en un archivo de Jupyter tendremos:

![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0031-spark/save2.jpg)


Y luego, revisaremos la existencia de nuevo con:

![arquitect](https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/labBigData/lab0031-spark/terminal2.jpg)
## Creado por
Cristian Darío Ceballos Rodríguez
cdceballor@eafit.edu.co

Tópicos especiales en telemática
