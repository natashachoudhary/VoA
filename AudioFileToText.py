import speech_recognition as sr 
import os
#AUDIO_FILE = (r"C:\Personal\LnT\Speech\CoC\Backup\Backup\Sound recordings Max 13-08-2019\COMMAND_MyV_AcousticalSpeedWarning.wav")

path = r"C:\Personal\LnT\Speech\CoC\Backup\Backup\Sound recordings Max 13-08-2019"

# use the audio file as the audio source 
list = []  
r = sr.Recognizer() 
for root, d, f in os.walk(path):
    for files in f:
        if files.endswith('.wav'):
            #print files
            list.append(os.path.join(root,files))
#print list

for i in range(0,len(list)):
    with sr.AudioFile(list[i]) as source:
        
        audio = r.record(source)   
      
    try:
        text =  r.recognize_google(audio,language = 'de-DE') #use show_all = True to see other values; returns a dict
        print(text.encode('utf-8')) 
      
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

