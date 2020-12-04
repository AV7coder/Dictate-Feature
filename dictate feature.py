from os import name

import speech_recognition as sr
r = sr.Recognizer() # making a object named r which is the recognizer

#print(sr.Microphone)

if __name__ == "__main__":

    
    #It takes microphone input from the user and returns string output
    def app():
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.
        except Exception as w:
            print(w)
        
    app()