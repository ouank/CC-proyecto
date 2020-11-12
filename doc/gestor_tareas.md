# Configuración correcta del gestor de tareas y justificación de la misma

El gestor de tareas elegido es [invoke](http://www.pyinvoke.org/).

Hay muchas opciones posibles para un gestor de tareas. Mi elección final fue **invoke** porque sigue la sintaxis común de Python y por lo tanto está más sencillo escribir y debug para mí, ya que todo este proyecto también está escrito en Python y el use de comandos desde la línea de órdenes. Además, es fácil de instalar y comenzar:\
	<code>$pip install invoke<code>

Investigué algunas otras gestores de tareas, tres de las cuales eran [Makefile](https://en.wikipedia.org/wiki/Makefile), [pybuilder](https://pybuilder.io/) y [SCons](https://scons.org/). 
Todas esas cuatro son capaces de hacer la automatización de tareas que necesito para mi proyecto. Personalmente encuentro la sintaxis del Makefile un poco complicada, especialmente para la tarea en cuestión. Preferí **invoke** sobre los otros dos en particular por su sintaxis intuitiva lo que lleva a las razones mencionadas anteriormente.

## Task Automation

Invoke proporciona una API limpia y de alto nivel para ejecutar comandos desde línea de órdenes y definir/organizar la función de la tarea desde un simple fichero *tasks.py*:
En este fichero sólo necesitamos importar el módulo de task de invoke\
	<code>$from invoke import task<code>

y entonces se puede empezar a definir nuestras tareas que necesitan ser automatizadas.
Cada tarea necesita tener el decorador *@task*. 
En este paso del proyecto definimos las siguientes tareas.\
install: installar los dependencias del proyecto\
clean: Limpieza de los \__pycache__\
test: ejecutar de las pruebas \
![Fichero Tasks.py](imgs/fichero_tareaspy.png)\
Para ejecutar uno de los tareas sólo se necesita ejecutar:\
	<code>$invoke \<tarea> 

El fichero tasks.py se encuentre [aquí](../tasks.py)

