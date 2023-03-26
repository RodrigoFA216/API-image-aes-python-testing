# API documentation
- Dependencies:
    - anyio
    - click
    - colorama
    - fastapi
    - h11
    - idna
    - numpy
    - opencv-python
    - pycodestyle
    - pydantic
    - sniffio
    - starlette
    - typing_extensions
    - uvicorn
- Dev Dependencies:
    - autopep8

# Miscelaneus

Los tres niveles del modelo de madurez de Richardson para API REST son los siguientes:

1. Nivel 0 - POX (Plain Old XML): 

- Este nivel es el más básico y no cumple con ninguna de las restricciones de Fielding. Las aplicaciones en este nivel utilizan HTTP como un simple canal de transporte para enviar y recibir mensajes XML.

2. Nivel 1 - RESTful Resources: 

- Este nivel introduce el concepto de recursos y la identificación de recursos a través de URIs. Las aplicaciones en este nivel utilizan HTTP para acceder a los recursos y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en ellos.

3. Nivel 2 - HTTP Verbs: 

- Este nivel introduce el uso correcto de los verbos HTTP para realizar operaciones CRUD en los recursos identificados por URIs. Las aplicaciones en este nivel utilizan los verbos HTTP GET, POST, PUT y DELETE para realizar operaciones CRUD en los recursos.

4. Nivel 3 - HATEOAS (Hypermedia as the Engine of Application State): 

- Este nivel introduce la idea de que los recursos deben contener enlaces a otros recursos relacionados. Las aplicaciones en este nivel utilizan los enlaces para navegar por la aplicación y realizar operaciones CRUD en los recursos.