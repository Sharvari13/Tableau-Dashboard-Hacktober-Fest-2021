#Author at your final display size
#By default, Tableau dashboards are set to use a fixed size and if you keep this setting, be sure to construct your visualization at the size it will be viewed at. You can also set Size to Automatic, which makes Tableau automatically adapt the overall dimensions of a visualization based on screen size. This means that if you design a dashboard at 1300 x 700 pixels, Tableau will resize it for smaller displays—and sometimes this results in scrunched views or scrollbars. The Range sizing feature is helpful for avoiding this.
# 001 - Adithya -
# This dashboard is used to show various patient's information of the Hospital.
# Link - https://public.tableau.com/app/profile/harish.s.n/viz/PatientLOSTableauDashboard/PatientLOSDashboard?publish=yes

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



