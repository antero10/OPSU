#Code Book

#Spanish
---
##Intro

Para inicializar el proyecto se debe inicializar los spiders de scrapy usando `scrapy crawl oportunitiesBook`, esto hara 3 pasos principales:

* Paso Uno : Encontrara 585 posibles universidades, variable guardada en el settings.py como `MAX_URL`
* Paso Dos: Extraera del HTML, toda la informacion necesaria como: nombre, direccion, estado y carreras 
* Paso Tres: Lo guardara en Mongo en la Base de datos `OpsuProject` y en la colección `data`. Estan en el settings.py para su configuracion

## Variables

* `name` Nombre de la universidad
* `courses` Arreglo de cursos de la universidad
* `category` Categoria de la univrsidad Boolean 1 si es privada y 0 si es publica
* `direction` Direccion de la universidad, esta variable luego se conviere en estado y contacto
* `contact` Contacto de la universidad
* `state` Estado de la universidad

# English
---
## Intro

To initialize the project must be initialized using scrapy spiders crawl scrapy `oportunitiesBook`, this will make three main steps:

* Step One: You will find 585 prospective colleges variable stored in the settings.py as `MAX_URL`
* Step Two: HTML extract all necessary information such as: name, address, state and careers
* Step Three: I keep in Mongo Database OpsuProject` `and the` data` collection. Are in the settings.py for configuration

## Variables

* `Name` University name
* `Courses` Agreement college courses
* `Category` the Boolean Category 1 if it is private univrsidad and 0 if it is published
* `Direction` Address of the university, this variable then conviere state and contact
* `Contact` Contact College
* `State` State University