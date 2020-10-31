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

## User Stories
Desde los roles (+yo como el administrador) podemos inferir historias de usarios:
- [Como buscador de plantas, quiero buscar plantas con mis propios criterios](https://github.com/ouank/selva_urbana/issues/14)
- [Como buscador de plantas, quiero hacer sugerencias de nuevas plantas para añadir a las base de datos](https://github.com/ouank/selva_urbana/issues/15)
- [Como buscador de plantas, quiero buscar por plantas concretas para ver cual condicciónes necesitan](https://github.com/ouank/selva_urbana/issues/14)
- [Como Administrador de la aplicación, quiero analisar los actividades de los usarios para desarrollar más la aplicación](https://github.com/ouank/selva_urbana/issues/16)
- [Como Administrador de la aplicación, quiero analizar cuánto tráfico habrá en mi aplicación](https://github.com/ouank/selva_urbana/issues/16)
- [Como empresa quiero ver qué tipo de plantas son las más buscadas (para poder proporcionarlas)](https://github.com/ouank/selva_urbana/issues/17)	
- [Como negocio quiero ver de qué región provienen la mayoría de las solicitudes de los usuarios (para expandir el negocio)](https://github.com/ouank/selva_urbana/issues/17)
- [Como anunciante quiero hacer publicidad dirigida](https://github.com/ouank/selva_urbana/issues/17)

## Primer borrador de unas clases (corresponden a unas historias de usarios)
[Aquí](src/utils/) hay el primer borrador por unas clases.

## Milestones y issues
- [Especificar el proyecto](https://github.com/ouank/selva_urbana/milestone/2)
	- [8 Issues para especificat el proyecto](https://github.com/ouank/selva_urbana/milestone/2?closed=1)
- [Crear la funcionalidad básica más simple](https://github.com/ouank/selva_urbana/milestone/3)
	- [Crear la interfaz de usuario más simple](https://github.com/ouank/selva_urbana/issues/18)
	- [Crear el sistema más simple de middle tier information brokering system](https://github.com/ouank/selva_urbana/issues/19)
	- [Crear una base de datos simple con pocos ejemplos](https://github.com/ouank/selva_urbana/issues/20)
- [Refinar las funcionalidades del sistema a un estándar MVP](https://github.com/ouank/selva_urbana/milestone/4)
	- [Implementar el Algoritmo de Búsqueda para navegar por el Banco de Datos por criterios](https://github.com/ouank/selva_urbana/issues/14)
	- [Añadir la fórmula de solicitud](https://github.com/ouank/selva_urbana/issues/15)
	- [Refinar la base de datos a una solución MVP](https://github.com/ouank/selva_urbana/issues/21)
	- [Refinar el sistema de middle tier information brokering system a la solución MVP](https://github.com/ouank/selva_urbana/issues/22)
	- [Refinar el frontend a la solución MVP](https://github.com/ouank/selva_urbana/issues/23)
- [Crear una tubería de análisis de datos](https://github.com/ouank/selva_urbana/milestone/5)
	- [Registrar el tráfico en la aplicación](https://github.com/ouank/selva_urbana/issues/16)
	- [Analizar las solicitudes y el tráfico de datos](https://github.com/ouank/selva_urbana/issues/17)
- [Crear y ejecutar con éxito todas las pruebas](https://github.com/ouank/selva_urbana/milestone/6)
- [Despliegue final de la aplicación en la plataforma de la nube](https://github.com/ouank/selva_urbana/milestone/7)

## Hoja de ruta
### Especifique el proyecto
En primer lugar, es necesario especificar el proyecto:\
¿Quién se beneficiará de este proyecto? ¿Quiénes serán los usuarios? \
--> Definir los roles del proyecto\
Elija un patrón de arquitectura que el proyecto seguirá.\
Crear la hoja de ruta del proyecto.

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
