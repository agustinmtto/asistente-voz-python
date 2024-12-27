# Asistente Virtual Personal en Python

Este es un asistente virtual personal simple desarrollado en Python. Utiliza reconocimiento de voz, síntesis de voz y varias bibliotecas para realizar tareas básicas a través de comandos de voz.

## Descripción

El asistente puede realizar las siguientes funciones:

*   **Escuchar y reconocer comandos de voz:** Utiliza `speech_recognition` para capturar y transcribir el audio del micrófono a texto.
*   **Responder con voz:** Utiliza `pyttsx3` para sintetizar texto en voz y dar respuestas al usuario.
*   **Informar la fecha y hora actual:** Informa el día de la semana y la hora actual.
*   **Abrir sitios web:** Abre YouTube y Google en el navegador web predeterminado.
*   **Buscar información en Wikipedia:** Busca y resume información en Wikipedia.
*   **Buscar en internet:** Realiza búsquedas en internet a través de `pywhatkit`.
*   **Reproducir videos de YouTube:** Reproduce videos directamente desde YouTube a través de `pywhatkit`.
*   **Contar chistes:** Genera chistes aleatorios utilizando la biblioteca `pyjokes`.
*   **Consultar precios de acciones:** Busca y da el precio actual de acciones de empresas como Apple, Amazon y Google, utilizando `yfinance`.
*   **Saludar y despedirse:** Saluda al usuario al iniciar y se despide al finalizar la interacción.

## Requisitos

*   Python 3.6 o superior.
*   Las siguientes bibliotecas de Python:
    *   `pyjokes`
    *   `pyttsx3`
    *   `speech_recognition`
    *   `pywhatkit`
    *   `yfinance`
    *   `webbrowser`
    *   `wikipedia`
    *   `datetime`
    *   Puedes instalarlas usando pip:
        ```bash
        pip install pyjokes pyttsx3 SpeechRecognition pywhatkit yfinance wikipedia
        ```

## Instalación y Configuración

1.  Asegúrate de tener Python instalado.
2.  Clona o descarga este repositorio.
3.  Instala las dependencias listadas en "Requisitos".
4.  Asegúrate de tener un micrófono configurado y funcionando.

## Uso

1.  Ejecuta el script principal, `main.py` (o como hayas nombrado tu archivo):
    ```bash
    python main.py
    ```
2.  El asistente te saludará.
3.  Comienza a dar comandos por voz.
4.  El asistente responderá según el comando detectado.
5.  Para finalizar la interacción, di "adiós".

## Comandos de Voz Reconocidos

El asistente reconoce los siguientes comandos (entre otros, puede interpretar algunos similares):

*   "abrir youtube"
*   "abrir navegador"
*   "qué día es hoy"
*   "qué hora es"
*   "busca en wikipedia [tema]"
*   "busca en internet [tema]"
*   "reproducir [canción/video]"
*   "broma"
*   "precio de las acciones de [nombre de la acción]"
    (Soporta *apple, amazon, google*)
*   "adiós"

## Consideraciones

*   **Idioma:** El script está configurado para español argentino (`es-ar`).
*   **Reconocimiento de voz:** La precisión del reconocimiento de voz puede variar según el ruido ambiente y la calidad del micrófono.
*   **Conexión a internet:** El asistente requiere conexión a internet para buscar información, ejecutar búsquedas y reproducir videos.
*   **Uso de API de terceros:** Ten en cuenta los límites de uso de las APIs de los sitios y servicios utilizados por el asistente.

## Limitaciones

*   El asistente tiene un repertorio limitado de comandos.
*   Puede tener dificultades para comprender dialectos o acentos diferentes.
*   La respuesta del asistente a acciones como "buscar en internet" o "reproducir" puede variar dependiendo del resultado de las APIs.

## Futuras Mejoras

*   Ampliar el repertorio de comandos y tareas.
*   Mejorar la capacidad de comprensión y procesamiento del lenguaje natural.
*   Integrar más servicios y APIs.
*   Añadir soporte para más idiomas.
