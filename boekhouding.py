

from presentatie import presenteer
from helper  import som

def inkomsten ():
    inkomsten = { 
        " Aardbeien-ijs-totaal" : 1000 ,
        " Vanille-ijs-totaal" : 2000,
        " Chocolade-ijs-totaal" : 1500 ,
        " Waterijsjes-totaal" : 750 ,
    }

totaal_inkomsten = som

presenteer = inkomsten/ totaal_inkomsten

print 

with open ( ' boekhuoding . csv', 'w' , newline= '' ) as csvfile :
    for key , value in inkomsten . items () :
        writer = csv . writer ( csvfile , delimiter= ';' )
        writer . writerow ( [ key , key ] )