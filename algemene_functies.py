def mijn_functie_1 ( x):
    return   x
  
print (mijn_functie_1 (2*2))
print (mijn_functie_1 (4*4))
print (mijn_functie_1 (10*10))
print (mijn_functie_1 (12*12))

def mijn_functie_2 (a=12.3, b=10.5):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)    
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst
print ( mijn_functie_2 ())


