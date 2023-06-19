
# Easybroker project

Utilizando el lenguaje de programación que prefieras crea una clase que consuma la API de EasyBroker para leer todas las propiedades de nuestra cuenta de staging e imprima sus títulos. Incluye al menos una prueba unitaria y envíanos tu código como un gist. La documentación y las credenciales de la cuenta de staging están disponibles en: https://dev.easybroker.com/docs.
## Installation


```bash
  git clone https://github.com/aaroncane/easybroker.git
  pip install -r requirements.txt
  set EASYBROKER_CLIENT_ID= *insert you client id*
  set URL=https://api.stagingeb.com/v1/
  cd src
```
    
## Run Locally

To run locally, run the following command

```bash
  py main.py
```
## Running Tests

To run tests, run the following command

```bash
  python -m unittest test.py
```

