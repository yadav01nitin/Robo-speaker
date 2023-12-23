#import os
#if __name__ == '__main__':
#       print("Welcome to RoboSpeaker 1.1. Created by Nitin")
#      while True:
#         x=input("Enter what do you want me to speak: ")
#        if x=="q":
#           os.system("say 'bye bye bye' ")
#          break
#     command=f"say {x}"
#    os.system(command)

# this is robo speaker for mac operating thats it.


# This is for windows.

import pyttsx3
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Nitin")
    engine = pyttsx3.init()
    while True:
        x=input("Enter what do you want me to speak: ")
        engine.setProperty('rate', 100)
        if x=="q":
            engine.say("bye bye bye")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()


