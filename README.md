# Parcial01_JuanManuelZpata


## Respuesta a:
Luego, explique cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa.

##

Mantendríamos este microservicio únicamente encargado de los cálculos (factorial, par/impar).
Crearíamos otro microservicio llamado servicio_historial, que se encargaría de guardar los resultados en una base de datos.

##

Comunicación entre servicios:

Desde nuestro microservicio de cálculo, enviaríamos una solicitud HTTP (POST) al otro servicio usando la librería requests para registrar el resultado.

Por ejemplo:

import requests

data = {
    "numero": numero,
    "factorial": fact,
    "etiqueta": etiqueta
}

requests.post("http://localhost:5001/guardar", json=data)


**Ventajas de este diseño:**

1. Permite escalar cada servicio por separado.
2. Si el servicio de historial falla, el cálculo sigue funcionando.
3. Facilita el mantenimiento y la evolución de cada componente.
