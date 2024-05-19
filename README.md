# taller06
## Taller realizado por:
    * Camilo López y Jorge Armijos

### Problemática

* Crear un proceso de importación de datos. Desde la siguiente dirección web a una base de datos local. Usar sqlite como gestor de base de datos y además usar la librería SqlAlchemy para la creación de la entidad, guardar registros y consulta de información.

Considerandos:
* Analizar lo que se realiza en la carpeta ejmplo01
* Trabajar en la carpeta ejercicio-02
* La data está en la siguiente dirección: https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json

* Crear una entidad con los siguientes atributos:
	* Nombre de pais
	* Capital
	* Continente
	* Dial
	* Geoname ID
	* ITU
	* Lenguajes
	* Si es independiente

* Leer los datos en su entorno local
	* Usar la libreria requests: import requests; primero instalar la librería: pip install requests
	* Usar el método get: requests.get(dirección del archivo json en str)
	* Obtener los datos en json a través de .json():  

* Guardar los registros en la base de datos local.
* Realizar la siguientes consultas, usar archivos separados para cada consulta.:
	* Presentar todos los países del continente americano
	* Presentar los países de Asía, ordenados por el atributo Dial.
	* Presentar los lenguajes de cada país.
	* Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
	* Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".

* Presentar capturas de pantalla de la base de datos en sqlite
 ## Taller realizado por
 
  * Camilo López y Jorge Armijos
   
# Se creo e inserto en la base de datos
*![Cree e inserte en la base](https://raw.githubusercontent.com/PlataformasWeb-P-AA2024/taller06-Jcod7/main/img/cree%20e%20inserte%20en%20la%20base.png)
# Tabla paises creada en el SQLite
*![Cree tabla paises](https://raw.githubusercontent.com/PlataformasWeb-P-AA2024/taller06-Jcod7/main/img/cree%20tabla%20paises.png)
# Datos insertados en SQLite
*![Datos insertados en SQLite](https://raw.githubusercontent.com/PlataformasWeb-P-AA2024/taller06-Jcod7/main/img/datos%20insertados%20en%20sqlite.png)
# Consulta 1: Todos los países del continente americano
*![Países continente americano](https://raw.githubusercontent.com/PlataformasWeb-P-AA2024/taller06-Jcod7/main/img/paises%20continente%20americano.png)
# Consulta 2: Países de Asia, ordenados por el atributo Dial
*![Por atributo dial](https://raw.githubusercontent.com/PlataformasWeb-P-AA2024/taller06-Jcod7/main/img/por%20atributo%20dial.png)
# Consulta 3: Lenguajes de cada país
*![Lenguaje por cada país](https://raw.githubusercontent.com/PlataformasWeb-P-AA2024/taller06-Jcod7/main/img/lenguaje%20por%20cada%20pa%C3%ADs.png)
# Consulta 4: Los países ordenados por la capital, siempre que el país pertenezca a Europa
*![Países capital de Europa](https://raw.githubusercontent.com/PlataformasWeb-P-AA2024/taller06-Jcod7/main/img/paises%20capital%20de%20europa.png)
# Consulta 5: Todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito"
*![Países con cadena 'uador'](https://raw.githubusercontent.com/PlataformasWeb-P-AA2024/taller06-Jcod7/main/img/paises%20con%20cadena%20uador.png)

### Importante
* Se sugiere realizar un script por cada tarea: crear entidad; guardar información y consultar información

