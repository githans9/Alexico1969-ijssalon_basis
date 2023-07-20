
aardbei = 4/1
def aanbeiding_1 (korting, prijs , smaak):
    global aardbei
    aardbei = 4/1
    return aardbei
liter = aardbei 
korting = 0.1
prijs = korting *36
#print ( f" liter prijs" , liter, " korting " , korting , " korting prijs " , prijs)    
print ( f" vandaag in de aanbeiding : emmertje ijs ( 1 liter) in de smaak aardbei , van" , liter," euro voor ", prijs,"euro")

def inkomsten_totaal (inkomsten ):
    return  ( inkomsten )

lijst_1 = [ 220, 430,125, 160, 205, 90, 345]

sum = sum ( lijst_1) # sum is een functie die de lijst optelt
#print (sum)
totaal = sum
bedrag_excl_btw = sum
#print( "bedrag (exclusief btw): " + str(bedrag_excl_btw) + "0")
btw = 0.09 * bedrag_excl_btw
#print( "btw (9%): " +  str(btw) + "0")
bedrag_incl_btw = bedrag_excl_btw + btw 
#print( "bedrag (inclusief btw): " + str(bedrag_incl_btw) + "0")
print ( f" het totaal van alle inkomsten van deze week is {totaal} euro,waarover {btw} euro btw betaald dient te worden") 

def laag_en_hoog ():
    mijn_lijst = lijst_1
#print ( max  ( lijst_1))
#print ( min  ( lijst_1))

def gemiddelde ():
     mijn_lijst = lijst_1
mijn_lijst_1 =  ( max  ( lijst_1))
mijn_lijst_2 =  ( min ( lijst_1))
mijn_lijst = mijn_lijst_1 + mijn_lijst_2 
#print (" totaal" ,mijn_lijst )
bedrag = mijn_lijst /2

print (f"De gemiddelde inkomsten deze week zijn { bedrag}  euro ")
'''
dataset = [ 90,345 ]
lengte = len ( dataset)

som = sum ( dataset)         deze functie kon ik niet gebruiken sum error
gemiddelde = som / lengte

print ( " het gemiddelde is " + str ( gemiddelde))
'''
def meervoudig (invoer_lijst):
    return ( invoer_lijst)

invoer_lijst = [ 10, 5 , 3, 2, 1, 2, 9]
         
print ( max ( invoer_lijst))
print ( min ( invoer_lijst))