#instal one external modle and use it in your code

# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hey shruti you can doo this please dont give up")
engine.runAndWait()