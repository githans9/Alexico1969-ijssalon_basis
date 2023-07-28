
from algemene_functies import mijn_functie_2

# # FUNCTIEDEFINITIE
def aanbieding_1 ( smaak  , prijs   , korting  ):
    prijs_na_korting = prijs  - ( korting)
    uitvoer = f" Vandaag in de aanbieding: Emmertje ijs ( 1 liter ) in de smaak { smaak } , van { prijs} euro voor { prijs_na_korting} euro." 
    return uitvoer
## HOOFDPROGRAMMA
prijs_na_korting = aanbieding_1 ("aardbei", 4, 1 )
print (prijs_na_korting)

def inkomsten_totaal (inkomsten ):
    return  ( inkomsten )
lijst_1 = [ 220, 430,125, 160, 205, 90, 345]
sum = sum ( lijst_1) 
totaal = sum
bedrag_excl_btw = sum
btw = 0.09 * bedrag_excl_btw
bedrag_incl_btw = bedrag_excl_btw + btw 
print ( f" het totaal van alle inkomsten van deze week is {totaal} euro,waarover {btw} euro btw betaald dient te worden") 

def laag_en_hoog ( mijn_lijst):
    mijn_lijst = [ 220, 430,125, 160, 205, 90, 345]
    laagste = min ( mijn_lijst)
    hoogste = max ( mijn_lijst)
    mijn_lijst.append ( laagste)
    mijn_lijst.append (hoogste)
    return mijn_lijst
mijn_lijst = laag_en_hoog ( ())
print ( mijn_lijst)

def gemiddelde ( lijst_1 ):
     mijn_lijst = lijst_1
mijn_lijst_1 =  ( max  ( mijn_lijst))
mijn_lijst_2 =  ( min ( mijn_lijst))
mijn_lijst = mijn_lijst_1 + mijn_lijst_2 
bedrag = mijn_lijst /2
print (f"De gemiddelde inkomsten deze week zijn { bedrag}  euro ")

def meervoudig ( invoer_lijst):
    invoer_lijst = [ 10,5,3,2,1,2,9]
    tijdelijk = laag_en_hoog ( invoer_lijst)
    uitvoer = [ tijdelijk [0] , tijdelijk [1]]
    return uitvoer

def combinatie ( invoer_lijst_2):
    korte_lijst = laag_en_hoog ( invoer_lijst_2)
    uitvoer =  ( korte_lijst[0],korte_lijst[1])
    return uitvoer
