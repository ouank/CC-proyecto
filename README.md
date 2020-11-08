# La Selva Urbana
En este repositorio se va a desarrollar un proyecto para la asignatura de Cloud Computing del Máster de Ingeniería Informática de la Universidad de Granada durante el curso 2020/21.

La configuración de git y Github se encuentra [aquí](setup_documentation/prep_repo.md)

## Descripción del problema
En este momento, el 55% de la población mundial vive en un área urbana. Se estima que este número aumentará al 68% para [2050](https://www.un.org/development/desa/en/news/population/2018-revision-of-world-urbanization-prospects.html). En Europa y América del Norte ya hay un 74% y un 82% de la población que vive en áreas urbanas, respectivamente.
Pero hay mucha gente que anhela la naturaleza y además, el nivel de estrés aumenta debido a la [urbanización](https://www.researchgate.net/publication/299078166_Impacts_of_urbanization_process_on_mental_health), entre otras razones. Se demuestra que tener plantas en su área de vivienda o trabajo puede [reducir el estrés](https://psychcentral.com/news/2020/01/06/plants-shown-to-reduce-stress-at-work/153075.html).
Pero no es fácil elegir la planta de interior adecuada que sobreviva a las condiciones que puedan darse en  cualquier espacio determinado. Si el ambiente es demasiado oscuro o brillante, cálido o frío, húmedo o seco, o simplemente muy ventoso, su planta moriría aunque la riegue y fertilice lo suficiente.

## Descripción del proyecto
Por esta razón, el objetivo de este proyecto es crear un sistema que le ayude a encontrar las plantas adecuadas para las condiciones pertinentes. El sistema le ofrecerá una selección de plantas de interior que se adapten en base a su ubicación, la dirección de su ventana, la frecuencia con la que desea cuidar sus plantas, entre otros criterios


## Arquitectura
Este Proyecto hará uso de la arquitectura basada en microservicios. Ésta se ajusta adecuadamente al proyecto, ya que éste tendrá que dividirse en diferentes servicios independientes que tendrán que trabajar juntos para dar al cliente el mejor resultado. 
Como primer borrador, algunos de estos microservicios serán: un [API](https://ip-api.com/) para obtener la ubicación del cliente, el frontend, la base de datos para seleccionar las plantas, un API para redirigir al cliente a páginas con más información según las plantas determinadas, un [API](https://pypi.org/project/Wikipedia-API/) para mostrar información básica de la planta. 

## Roles
Tan pronto como este proyecto se termine, habrá principalmente dos grupos de personas que podrán beneficiarse de ello. 
1. Como usario de ese aplicación podrá encontrar plantas nuevas y adecuadas y/o las condiciones que las necesitan.
2. Como Vendedor de plantas puede actualizar su lista de productos (dependiendo de la mayoría de las solicitudes de búsqueda), puede ver en qué región hay muchas solicitudes (para la expansión de negocio) y/o anunciar


## Hoja de ruta (Roadmap)

### Desarollo
En la primera fase del desarrollo creo la sistema funcional más simple posible. Esta sistema consiste en tres partes diferentes:
- [Crear la interfaz de usuario más simple](https://github.com/ouank/selva_urbana/issues/18)
- [Crear el sistema más simple de middle tier information brokering system](https://github.com/ouank/selva_urbana/issues/19)
- [Crear una base de datos simple con pocos ejemplos](https://github.com/ouank/selva_urbana/issues/20)

En la segunda fase, se añaden a la aplicación funciones adicionales que satisfacen las necesidades de ciertos roles. Esas funciones son, por ejemplo: 
- [Implementar el Algoritmo de Búsqueda para navegar por el Banco de Datos por criterios](https://github.com/ouank/selva_urbana/issues/14)
- [Añadir la fórmula de solicitud](https://github.com/ouank/selva_urbana/issues/15)

Simultáneamente, las tres partes básicas también se refinan a un estándar MVP.
- [Refinar la base de datos a una solución MVP](https://github.com/ouank/selva_urbana/issues/21)
- [Refinar el sistema de middle tier information brokering system a la solución MVP](https://github.com/ouank/selva_urbana/issues/22)
- [Refinar el frontend a la solución MVP](https://github.com/ouank/selva_urbana/issues/23)

En la fase final del desarrollo, se crea una tubería de análisis de datos. La tubería debe cubrir al menos las siguientes funciones:
- [Registrar el tráfico en la aplicación](https://github.com/ouank/selva_urbana/issues/16)
- [Analizar las solicitudes y el tráfico de datos](https://github.com/ouank/selva_urbana/issues/17)

### Pruebas 
Esta es la fase de pruebas. Hay que crear pruebas (ya empiezan a crear pruebas durante la fase de desarrollo) y ejecutar todas las pruebas para comprobar si todo está bien.
### Primer despliegue de la aplicación en una plataforma de la nube
En esta fase la aplicación se pone en línea para una fase de prueba. 
### Arreglar el código
### Despliegue final

## Miscelánea
###User Stories
[Los historis de usarios estan decribido aquí](project_information/user_stories.md)

### Primer borrador de unas clases (corresponden a unas historias de usarios)
[Aquí](src/utils/) hay el primer borrador de unas clases.

## Milestones y issues
[un esbozo del proyecto en hitos se puede encontrar aquí](project_information/milestones.md)

