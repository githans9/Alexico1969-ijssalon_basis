
prijzen = {
    " aardbei " : 3 ,
    " vanille" : 4 ,
    " chocolade" : 5, 
}

aanbieding = prijzen [" aardbei "] * 0.8   # maak gebruik van copy en paste ( aardbei) .

reclame_teks = f" Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts $ { aanbieding}"
# f = formatted string   // variabel = aanbieding {}
reclame_teks2 = reclame_teks [:63] # hierbij wordt de aanbieding ook rekenkundig 
reclame_teks3 = reclame_teks2.upper()
reclame_teks4 = reclame_teks3.split()
for el in reclame_teks4:    # el is devariable maar je kan ook bv er gebruiken.
    if len(el) > 4:          # len is de  teks
        print ( el.upper()) 
    else:
        print ( el.lower())














