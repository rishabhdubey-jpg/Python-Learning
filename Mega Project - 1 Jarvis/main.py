import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests 



recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')
newsapi = "c53cf63b6c51403db28c6c33ed815fec"

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 170)
# engine.setProperty('volume', 1.0)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open snapchat" in c:
        speak("Opening Snapchat")
        webbrowser.open("https://www.snapchat.com/web/")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country-in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                 speak(article['title'])
        
    else:
        # Let openAI handle the request
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.WaitTimeoutError:
            print("Listening timeout")
        except Exception as e:
            print("Error:", e)

