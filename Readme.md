# Urban Routes - Automatización de pruebas de la aplicación Web

## Descripción del proyecto

En el presente proyecto se realizara la automatización para pedir un taxi teniendo en cuenta los requisitos de la aplicación web para realizar un pedido con éxito.

## Tecnologías y técnicas utilizadas

- Selenium WebDriver : Permite reproducir los pasos para concluir una solicitud dentro de la aplicación donde se realizan las pruebas a través de scripts por lo cual es una herramienta para la automatización de testing web que soporta diversos navegadores.
- Python : Lenguaje de programación mayormente utilizado en las aplicaciones web, el cual permite realizar pruebas automatizadas claras y comprensibles.
- Pycharm: IDE que esta enfocado en Python.
- Localizadores: Se requiere el uso de lozacalizadores como ID - CLASS_NAME - XPATH - CSS_SELECTOR para reconocer y ubicar en la aplicación web mediante el uso de inspección de HTML

Antes de realizar las pruebas se debe:

- Instalar Pytest y Selenium, utiliza los comandos
```sh
pip install pytest
```
```sh
pip install selenium
```

- Verificar que se tiene instalado ChromeDriver y que el PATH ha sido actualizado

- Actualizar la URL en el file `data.py`
- Declarar los localizadores segun las pruebas que se requiera en `UrbanRoutesPage.py`
- Declarar en `main.py` los scripts para las pruebas
- En el file `helpers.py`contiene funciones complementarias que son  utilizadas en las pruebas automatizadas de la aplicación web a través de métodos.  

Durante las prueba

- Tener en cuenta que para correr las pruebas debes utilizar :
```sh
pytest main.py
```

## Pruebas en la apliciación web

1. Configurar la dirección
2. Seleccionar la tarifa Comfort
3. Agregar un número de teléfono
4. Agregar una tarjeta de crédito
5. Escribir un mensaje para el controlador
6. Pedir una manta y pañuelos
7. Pedir dos helados
8. Validar que parece el modal para buscar un taxi
9. Esperar a que aparezca la información del conductor en el modal


---
Ruth Ordoñez - Sprint 8


