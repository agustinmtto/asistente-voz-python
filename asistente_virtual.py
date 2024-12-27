import pyjokes
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import webbrowser
import wikipedia
import datetime


# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 1

        # informar que comenzo la grabacion
        print("Ya puedes comenzar a hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido.lower()

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("ups, no entendi")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"


# Funcion para que el asistente escuche
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el dia de la semana
def pedir_dia():

    #Crear variable con datos de hoy
    dia = datetime.date.today()

    # Crear variable con el dia de la semana
    dia_semana = dia.weekday()

    # Diccionario con nombres de los días
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}

    # Decir el dia y la fecha
    hablar(f"Claro, hoy es un muy buen {calendario[dia_semana]}")

# Informar la hora
def pedir_hora():
    # Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos"

    # Decir la hora
    hablar(hora)

# Funcion saludar
def saludo_inicial():

    # Crear variable con datos e hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif hora.hour >= 6 and hora.hour < 13:
        momento = "Buenos Dias"
    else:
        momento = "Buenas tardes"

    # Decir saludo
    hablar(f"Hola {momento}, soy Siri, tu asistente personal. En que puedo ayudarte hoy?")

def principal():
    # Saludar
    saludo_inicial()

    comenzar = True
    while comenzar:

        # Activar el micro y guardar pedido en string

        pedido = transformar_audio_en_texto().lower()

        if "abrir youtube" in pedido:
            hablar("Con gusto, estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "abrir navegador" in pedido:
            hablar("Claro, estoy en eso...")
            webbrowser.open("https://www.google.com")
            continue

        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue

        elif "qué hora es" in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)

        elif "busca en internet" in pedido:
            hablar("Buscando información en internet")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue

        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue

        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue

        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple" : "APPL",
                       "amazon" : "AMZN",
                       "google" : "GOOGL"}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontre, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Lo siento, no he podido encontrar la acción...")

        elif "adiós" in pedido:
            hablar("Perfecto, estaré aquí para cualquier consulta que tengas...")
            break
principal()