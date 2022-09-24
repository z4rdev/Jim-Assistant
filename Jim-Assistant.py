print("Loading...")
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
import time

name = "Jim Assistant"
version = "Alpha 3.0"
listener = sr.Recognizer()
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
def en_language():
    engine.setProperty('voice', voices[1].id)
def es_language():
    engine.setProperty('voice', voices[0].id)
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="es-ES")
            command = command.lower()
            if 'jim' in command:
                command = command.replace('jim', '')
                print(command)
    except:
        pass
    return command


# IDEA: Hacer que se compruebe si las dependencias están instaladas, en el caso de que no lo estén preguntar si quieren descargarlas.

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep
        t -= 1
    talk("Fin del temporizador!")

# Funcion para que el bot hable el texto escrito, en vez de tener que poner print pongo talk y lee y escribe el texto en la consola
def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

# Idioma temporal hasta que se elija el deseado.

en_language()
talk("Succesfully loaded all settings.")
talk("Welcome to " + name)
talk("Version: " + version)

talk("What language do you want to use?")
es_language()
print("1) Español")
en_language()
print("2) English")

language = input()
if language == "1":
    es_language()
    talk("Idioma seleccionado: Español")
    language = 0
else:
    en_language()
    talk("Language selected: English")
    language = 1

talk("Initialization Completed.")
# Despues de crearlo al completo, hacer:
# def spanish: ...
# Y poner todo lo hecho en español dentro, y otro en ingles con lo mismo pero en otro idioma, y si selecciona español las ordenes sean en español
# Y si es en ingles que las preguntas y la voz sean en ingles.
# A partir de aqui ya se está ejecutando el asistente al completo, y se empiezan a cargar los comandos!
# Las funciones tienen que estar escritas debajo de esta linea
def en_commands():
    command = take_command()
    print(command)
    # TEMPORIZADOR
    if 'timer' in command:
        talk("Insert the time in minutes")
        t = input()
        countdown(int(t))
    # MUSICA
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing: ' + song)
        pywhatkit.playonyt(song)
    # HORA, DIA
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        date = datetime.date.today()
        talk("Today is: ")
        talk(date)
        talk("We are at: " + time)
    # WIKIPEDIA
    elif 'wikipedia' in command:
        wikipedia.set_lang('en')
        search = command.replace('wikipedia', '')
        talk("Searching...")
        info = wikipedia.summary(search, 3)
        talk(info) 
    # BUSCAR EN GOOGLE
    elif 'chrome' in command:
        search = command.replace('search in chrome', '')
        try:
            print("Searching...")
            talk(pywhatkit.search(search))
        except:
            print("An error ocurred!")
    # Buscar en google y que lo diga el asistente
    elif 'google' in command:
        search = command.replace('search in google', '')
        try:
            busqueda = pywhatkit.info(search, lines = 4)
            talk(search)
        except:
            print("An error ocurred!")
    # CHISTE
    elif 'joke' in command:
        talk(pyjokes.get_joke(language='en', category='all'))
    else:
        return

def es_commands():
    command = take_command()
    print(command)
    # TEMPORIZADOR
    if 'temporizador' in command:
        talk("Introduce el tiempo en segundos")
        t = input()
        countdown(int(t))
    # MUSICA
    if 'reproduce' in command:
        song = command.replace('reproduce', '')
        talk('Reproduciendo: ' + song)
        pywhatkit.playonyt(song)
    elif 'reproducir' in command:
        song = command.replace('reproducir', '')
        talk('Reproduciendo: ' + song)
        pywhatkit.playonyt(song)
    # HORA, DIA
    elif 'hora' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        date = datetime.date.today()
        talk("Hoy es:")
        talk(date)
        talk("Ahora son las " + time)
    # WIKIPEDIA
    elif 'wikipedia' in command:
        wikipedia.set_lang('es')
        search = command.replace('wikipedia', '')
        talk("Buscando...")
        info = wikipedia.summary(search, 3)
        talk(info) 
    # BUSCAR EN GOOGLE
    elif 'chrome' in command:
        search = command.replace('busca en chrome', '')
        try:
            print("Buscando...")
            talk(pywhatkit.search(search))
        except:
            print("Ha ocurrido un error!")
    # Buscar en google y que lo diga el asistente
    elif 'google' in command:
        search = command.replace('busca en google', '')
        try:
            busqueda = pywhatkit.info(search, lines = 4)
            talk(search)
        except:
            print("Ha ocurrido un error.")
    # CHISTE
    elif 'chiste' in command:
        talk(pyjokes.get_joke(language='es', category='all'))
    else:
        return
    
if language = 0:
    while True:
        es_commands()
        return
if language = 1:
    while True:
        en_commands()
        return
    
talk("Thanks for using me, more changes will be available in the future.")
talk("I am conscious that lot of things should be added to make this fully functional.\n Please be Patient")

# Si lees esto eres un friki jajajaja
# para q me voy a engañar yo tmb lo soy.
# Lo necesitaré cuando quiera cambiar el idioma.
"""
with sr.Microphone() as source:
    audio = listener.listen(source)
    try:
        print("You said: " + listener.recognize_google(audio) + "in french")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service")
        
        listener.recognize_google(audio, language="fr-FR")
"""
