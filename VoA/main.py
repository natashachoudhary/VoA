
import mapUttPrompt as func
import recognizer as recog

#import gen_SDC as gen_SDC


re = recog.recognizer()
#create object of recognizer class

re.eInit()
for i in range(0,3):
    audio = re.eListening()
    utterance,result = re.eProcessing()
    if result!=0:
        print "processing your input"
        #utterance = 
        prompt = re.processUtterance(utterance)
        re.ePrompting(prompt)
        break


