import cowsay
import pyttx3

engine = pyttx3.init()
this = input("what's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()