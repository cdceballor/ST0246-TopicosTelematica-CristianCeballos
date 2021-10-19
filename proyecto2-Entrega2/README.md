# Entrega 2 - Producto 2 (Mejora en temas de escalabilidad, rendimiento y seguridad a la página wordpress)

En el siguiente proyecto, se crea una página con fuente de Wordpress y se despliega con Docker en una máquina virtual de google cloud platform, siguiente, procederemos a separar las capas en: una de aplicación, una de server y una de base de datos con unas características específicas que se ven reflejadas en la siguiente arquitectura.


![Alt text](D:/Semestre 9/TopicosTelematica/arquitect.png "Optional Title")
## Uso

Usaremos: 
Comandos de docker
En la vm usaremos Ubuntu 16.04
Usaremos certificado ssl letsencrypt con certbot
Instancia de Wordpress
Balanceador de carga provieniente del CDN
Patrón Master Slave para las bases de datos con MySql
Conceptos de seguridad previamente implementados por parte de GCP
 
## Conceptos dentro de la aplicación

- Escalabilidad: Se implementó un patrón de master slave que busca tener 2 bases de datos (Cada una en instancias diferentes) conectadas entre sí para poder tener una alta tolerancia a fallos, de esta forma, en caso de que una base de datos falle, la otra esté pendiente para pasar a ser a quien se le escriban los datos; Este patrón lo implementamos con MySql.

- Rendimiento: Se implementó según las características de la arquitectura un intermediario (CDN) que estará entre el browser y el balanceador de cargar (lb) cuya función es almacenar en caché los datos estáticos solicitados por el cliente, de tal forma que en las siguientes peticiones que haga el cliente para dichos archivos estáticos ya estén almacenados en caché y el CDN pueda retornarlos sin necesidad de hacer la petición hasta la capa de aplicación incrementando así el rendimiento de los tiempos de respuesta de la aplicación.

- Seguridad: Se utilizó los servicios de Google Cloud Platform ya que estos nos garantizaba más seguridad en nuestro aplicativo, teniendo en cuenta: Los posibles ataques, caídas del sistema, extracción de información por parte de terceros, y demás métodos que alteraran ya fuesen el funcionamiento de la aplicación o los datos de los usuarios que la visitaban.

Es importante recalcar que estos dos últimos conceptos (Rendimiento y seguridad) fueron implementados con los servicos de GCP ya que nos garantizaban funcionamiento y estabilidad.

## Creado por
Sebastian Loaiza Correa
sloaizac@eafit.edu.co
Kevin Gutierrez Gomez
kgutierreg@eafit.edu.co
Cristian Darío Ceballos Rodríguez
cdceballor@eafit.edu.co

Tópicos especiales en telemática
