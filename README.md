# Proyecto imageproject - prueba técnica imágenes en formato A4
Aplicativo encargado de recibir imágenes en formato JPG de cualquier dimensión (Ancho x alto) para ajustarlas a una hoja de hoja tamaño A4 (796 x 1123 pixeles) sin márgenes. Se cumple con las siguientes reglas:
* La orientación de la página es definida a partir de la orientación de la imagen (Horizontal/Vertical).
* La imagen no pierde perder su ratio (Relación de aspecto ancho por alto).
* Ninguna imagen es agrandada en el proceso, solo encogida cuando corresponda.
* Se aprovecha el máximo de la hoja A4.

## Aspectos funcionales

### Rendimiento y optimización de recursos

### Seguridad

### Cobertura de pruebas unitarias

### Índice de deuda técnica

### Código limpio + clean architecture

### Stack usado

* [PostgreSQL](https://www.python.org/) - Es un gestor de base de datos de código libre con gran escalabilidad y robusto, tiene la capacidad de establecer un entorno de alta disponibilidad ya que permite que los clientes hagan consultas de solo lectura mientras el servidor esta en modo de recuperación. Tiene una gran cantidad de extensiones disponibles y se integra con múltiples lenguajes de programación.

* [Python](https://www.python.org/) - Está desarrollado bajo una licencia de código abierto. Es uno de los lenguajes de programación más versátiles que existen, puede ser usado en muchos campos diferentes. Cuenta con una amplia comunidad. Su característica multiplataforma permite que este pueda ser usado en diferentes sistemas operativos.

* [Pip](https://pypi.org/project/pip/) - Es un gestor de paquetes de python, una de sus principales ventajas es el número de librerías disponibles, la facilidad de instalación y la documentación. Permite gestionar listas de paquetes y sus números de versión correspondientes a través de un archivo de requisitos. 

* [Django](https://www.djangoproject.com/) - Es un framework web de alto nivel que permite el desarrollo rápido de sitios web seguros y mantenibles. Es gratuito y de código abierto, tiene una comunidad amplia y activa. Es modular lo que facilita la escalabilidad. Permite usar todos los paquetes disponibles de python.

* [Boostrap](https://getbootstrap.com/) - Uno de los frameworks más populares a nivel de front end. Permite crear interfaces web con CSS y Javascript que se adaptan en función del tamaño de la pantalla. Facilita plantillas, fuentes, botones y elementos de navegación.

* [Pillow](https://pillow.readthedocs.io/en/stable/) - Es una biblioteca gratuita de Python que agrega soporte para abrir, manipular y guardar muchos formatos de archivos de imágenes diferentes. Esta posee el método thumbnail() que permite redimensionar una imagen sin perder su relación de aspecto.

### Estrategia de despliegue

### Responsive
## Aspectos no funcionales 
