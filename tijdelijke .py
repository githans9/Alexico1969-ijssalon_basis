from helper import decoreer

def print_aanbieding ():
    prijzen = {
        " aardbei " : 3 ,
        " vanille" : 4 ,
        " chocolade" : 5, 
    }

    aanbieding = prijzen [" aardbei "] * 0.8   

    reclame_teks = f" Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts $ { aanbieding}"
    
    reclame_teks2 = reclame_teks [:63]  
    reclame_teks3 = reclame_teks2.upper()
    reclame_teks4 = reclame_teks3.split()
    
    for el in reclame_teks4:    
        if len(el) > 4:          
            print ( el.upper()) 
        else:
            print ( el.lower())
decoreer ( "aanbiedingen")

print_aanbieding () 














