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
Como primer borrador, algunos de estos microservicios serán: un [API](https://ip-api.com/) para obtener la ubicación del cliente, el frontend, la base de datos para seleccionar las plantas, un API para redirigir al cliente a páginas con más información según las plantas determinadas.


