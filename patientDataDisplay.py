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


""" The code classes the classes of flowers based on their 
    sepal-length, sepal-width,	petal-length and	petal-width.
    (Using the KNN classification technique)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv(url, names=names)
print(dataset.shape)

dataset.head()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=5, p=2, metric='euclidean')
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
