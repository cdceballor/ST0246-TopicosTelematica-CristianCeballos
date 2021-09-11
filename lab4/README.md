# Lab 4 (Práctica con RabbitMQ)

Creación de un projecto de gestión de tareas (productor(es) - consumidor(es)) utilizando python, Pika, docker, aws y rabbitMQ
## Esquema básico

![image](https://user-images.githubusercontent.com/35697740/132936289-b90d7a91-7ee5-4c8e-83fe-37fcd630a1f3.png)

## Construcción

Usaremos como base el siguiente repositorio: 
```
 https://github.com/st0263eafit/st026320212.git
```
y además, está el documento base aquí: https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos/blob/main/lab4/lab4-MOM-RabbitMQ.pdf

## Ejecución
Una vez se tenga el repositorio clonado:
```
git clone https://github.com/cdceballor/ST0246-TopicosTelematica-CristianCeballos
cd ST0246-TopicosTelematica-CristianCeballos/
cd Lab4/code/
```

ejecutaremos
```
python3 new_task.py
```
Para asignar la tarea, podemos agregar n tareas.
Luego para consumirlas:
```
python3 worker.py
```
Podemos generar todos los workers necesarios.

## Elaborado por
Cristian Darío Ceballos Rodríguez
cdceballor@eafit.edu.co
Tópicos especiales en telemática

## Fuente y referencia
https://programmerclick.com/article/837466359/
