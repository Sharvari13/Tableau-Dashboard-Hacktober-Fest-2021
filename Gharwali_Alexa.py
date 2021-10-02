import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
engine. setProperty("rate", 178)
engine.say('I am your Alexa!')
engine.say('What can I do for you today ?')
engine.runAndWait()
print(sr.Microphone.list_microphone_names())
try:
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=1)

        print('I am listening...')
        voice = listener.listen(source)
        print('Finished listening!')
        try:
            command = listener.recognize_google(voice)
            print('Finished Googling!')

            engine.say(command)
            engine.runAndWait()
            print(command)
            command = command.lower()
            if 'alexa' in command:
                print('Alexa: '+command)
            else:
                print('I\'m not Alexa '+command)
        except:
            print("Sorry, could not recognise")
except:
    print('yha aya')
    pass
