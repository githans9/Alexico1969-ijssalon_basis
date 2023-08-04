from flask import Flask
app = Flask (__name__)

from helper import  onderstreep

uitvoer = onderstreep ( "AANBIEDING")
uitvoer . append ( "Aardbeinijs, emmertje van 5 liter : 5 euro")
uitvoer . append ( " Aardbeienijs, emmertje van 5 liter : 2 euro")

print ()
for el in uitvoer :

 print (el)

@app.route ('/prijzen')
def recepten ():
    return " Binnenkort verschijnen hier enkele recepten "