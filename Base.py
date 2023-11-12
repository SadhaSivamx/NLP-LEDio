import joblib,nltk
import pickle
import serial
# Replace 'COMX' with the actual COM port of your Arduino
ser = serial.Serial('COM8', 9600, timeout=1)
off=[" turning off the LED now.","The LED has been switched off.","LED deactivated."]
on=["turning on the LED now","Alexa is activating the LED.","LED activated."]
# Load the model from the file
import tensorflow as tf
# Specify the path where you saved the model
saved_model_path = 'Modelio/Modelio'
loaded_model = tf.keras.models.load_model(saved_model_path)
# Now, 'loaded_model' contains your previously saved model

Words=["'m", 'a', 'ability', 'able', 'action', 'activate', 'active', 'appreciate', 'appreciated', 'asking',
'at', 'be', 'being', 'can', 'capability', 'carry', 'chance', 'command', 'comply', 'could', 'deactivate',
'disable', 'do', 'down', 'enable', 'enabling', 'execute', 'feasible', 'for', 'great', 'have', 'i', 'if', 'in', 'is',
'it', 'kindly', 'led', 'light', 'make', 'me', 'might', 'mind', 'moment', 'much', "n't", 'need', 'not', 'now',
'of', 'off', 'on', 'out', 'perform', 'please', 'possible', 'power', 'request', 'requesting', 'right', 'sure', 'switch',
'switching', 'task', 'that', 'the', 'there', 'this', 'to', 'too', 'trouble', 'turn', 'turned', 'turning', 'up', 'within', 'wondering',
'would', 'you', 'your']
def MakePredictions(sent):
    Tempo=[]
    temp=nltk.word_tokenize(sent)
    for __ in Words:
        if __ in temp:
            Tempo.append(1)
        else:
            Tempo.append(0)
    c=list(loaded_model.predict([Tempo]))
    import random
    print(c[0][0])
    if float(c[0][0])<=0.5:
        command = '0'
        ser.write(command.encode('utf-8'))
        ans=random.choice(off)
        print(ans)
        return ans
    elif float(c[0][0])>=0.5:
        command = '1'
        ser.write(command.encode('utf-8'))
        ans=random.choice(on)
        print(ans)
        return ans
