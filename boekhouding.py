
import csv
from presentatie import presenteer
from helper  import sum


inkomsten =   { 
        " Aardbeien-ijs-totaal" : 1000 ,
        " Vanille-ijs-totaal" : 2000,
        " Chocolade-ijs-totaal" : 1500 ,
        " Waterijsjes-totaal" : 750 , }

for k, v in inkomsten . items ():
 print (k, v)
totaal_inkomsten = sum
sum = totaal_inkomsten

print ( "-------------")
print ( f" totaal : ", totaal_inkomsten)

with open ( ' boekhuoding . csv', 'w' , newline= '' ) as csvfile :
    for key , value in inkomsten . items () :
        writer = csv . writer ( csvfile , delimiter= ';' )
        writer . writerow ( [ key , key ] )
