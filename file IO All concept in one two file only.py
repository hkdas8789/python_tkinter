"""
see video no : -  26
see video no : -  27
see video no : -  29
see video no : -  31
see video no : -  32

"""

def speak(voice,string):
    import pyttsx3
    en=pyttsx3.init()
    vo=en.getProperty('voices')
    en.setProperty('voice',vo[voice].id)
    en.say(string)
    en.runAndWait()
a=0
while True:
    a+=1
    speak(0,"The German pliticians ,who signed, the Treaty ,of Versailles ,in November, month of 1918.")
    if a==5:
        break
