# La Selva Urbana
En este repositorio se va a desarrollar un proyecto para la asignatura de Cloud Computing del Máster de Ingeniería Informática de la Universidad de Granada durante el curso 2020/21.

## Descripción del problema
En este momento, el 55% de la población mundial vive en un área urbana. Se estima que este número aumentará al 68% para [2050](https://www.un.org/development/desa/en/news/population/2018-revision-of-world-urbanization-prospects.html). En Europa y América del Norte ya hay un 74% y un 82% de la población que vive en áreas urbanas, respectivamente.
Pero hay mucha gente que anhela la naturaleza y además, el nivel de estrés aumenta debido a la [urbanización](https://www.researchgate.net/publication/299078166_Impacts_of_urbanization_process_on_mental_health), entre otras razones. Se demuestra que tener plantas en su área de vivienda o trabajo puede [reducir el estrés](https://psychcentral.com/news/2020/01/06/plants-shown-to-reduce-stress-at-work/153075.html).
Pero no es fácil elegir la planta de interior adecuada que sobreviva a las condiciones que puedan darse en  cualquier espacio determinado. Si el ambiente es demasiado oscuro o brillante, cálido o frío, húmedo o seco, o simplemente muy ventoso, su planta moriría aunque la riegue y fertilice lo suficiente.

## Descripción del proyecto
Por esta razón, el objetivo de este proyecto es crear un sistema que le ayude a encontrar las plantas adecuadas para las condiciones pertinentes. El sistema le ofrecerá una selección de plantas de interior que se adapten en base a su ubicación, la dirección de su ventana, la frecuencia con la que desea cuidar sus plantas, entre otros criterios


## Información del proyecto
Los siguientes enlaces le llevarán a una descripción más detallada del proyecto.

La [descripción de la arquitectura](doc/arquitectura.md) en la que se basará este proyecto.

La descripción de [los historias de usarios](doc/user_stories.md)

[Un esbozo del proyecto en milestones](doc/milestones.md)

Una descripción de [los roles](doc/roles.md) en este proyecto.

[La planificación del proyecto y la hoja de ruta](doc/roadmap.md)

## Docker
Elección y justificación del [contenedor base](doc/docker.md)\
[Dockerfile](Dockerfile) y la [prueba](doc/imgs/docker_passed_tests.png) que funciona\
[Contenedor subido a Docker Hub y configuración de la actualización automática.](doc/docker_hub_config.md)\
[Github Container Registry](doc/ghcr_setup.md)\
Avance del proyecto:\
	- Añadió dos HUs nuevos: [HU5](https://github.com/ouank/selva_urbana/issues/29) y [HU6](https://github.com/ouank/selva_urbana/issues/21)\
	- [Avance de código](src/db/plantdb.py)\
	- He terminado un [HU](https://github.com/ouank/selva_urbana/issues/14)

## Gestor de tareas, pruebas y avance del proyecto

Configuración correcta del [gestor de tareas](doc/gestor_tareas.md) y justificación de la misma.\
Elección y justificación de la [biblioteca de aserciones](doc/bib_aserciones.md) usada.\
Elección y justificación del [marco de pruebas](doc/marco_pruebas.md) usado.\
Correcta relación entre avance de código (incluyendo los tests) y HUs.\
	- 1. [código](src/db/plantdb.py), [tests](src/tests/test_plantdb.py), [HU](https://github.com/ouank/selva_urbana/issues/14)\
	- 2. [código](src/user/user.py), [tests](src/tests/test_user.py), [HU](https://github.com/ouank/selva_urbana/issues/15)\
Tests significativos: tests unitarios del [usario](src/tests/test_user.py) y de la [base de datos](src/tests/test_plantdb.py).\
Avance de codigo: - changed from sqlite3 to sqlalchemy for [object relational mapping](src/db/plantdb.py)


