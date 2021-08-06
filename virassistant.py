from re import sub
import speech_recognition as sr
import yagmail


#create a recognizer..
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("clear background noise..")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("waiting for your message..")
    recordedaudio = recognizer.listen(source)
    print("Done recording..")
#Printing message..
    try:
        print('Printing message..')
        text=recognizer.recognize_google(recordedaudio, language='en-US')

        print('Your message {}'.format(text))

    except Exception as ex:
        print(ex)

#Sending the email..
reciever='melhaouiasmaa.1@gmail.com'
message=text
sender=yagmail.SMTP('melhaouiasmaa@gmail.com')
sender.send(to=reciever, subject='You did iiiit !',contents=message)