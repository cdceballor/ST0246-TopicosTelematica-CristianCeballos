# Lab 02 - Ejercicio con mapreduce 

En el siguiente laboratorio, trabajaremos con mapreduce para poder solucionar un ejercicio de calcular algunos valores teniendo en cuenta la llave (key) y el valor (value) con operaciones tales como map (agrupar) y reduce (filtrar y operar).

## Lo que necesitamos

Instalaremos la librería de MRJob

```
pip install mrjob
```

usaremos el concepto de MapReducer que se encuentra en el siguiente video:
https://www.youtube.com/watch?v=PAAwR4eRuBY&list=PLMF23FOyQZQswzIJFLmqTGF5iyIfknYlz&index=8

una vez comprendido cómo funciona, ejecutaremos el código con los siguientes comandos para encontrar:

El salario promedio por Sector Económico (SE)

```
py .\File.py .\dataempleados.csv 
```

El salario promedio por Empleado

```
py .\salPromEmpleado.py .\dataempleados.csv
```

Número de SE por Empleado que ha tenido a lo largo de la estadística
```
py .\numSE.py .\dataempleados.csv
```
## Creado por
Cristian Darío Ceballos Rodríguez
cdceballor@eafit.edu.co

Tópicos especiales en telemática
