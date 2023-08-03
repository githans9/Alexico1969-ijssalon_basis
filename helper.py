

def decoreer ( tekst = ""):
    lengte = len ( tekst) + 4
    print ()
    print ( lengte * "*") 
    print (f"* { tekst} *")
    print ( lengte * "*")
    print ()

def fooi_pp (bedrag, personen):
    bedrag_pp = bedrag / personen
    return f"Het bedrag per persoon is { bedrag_pp} euro"

b = int (input ("welk berag zit er in de fooienpot ? "))
p  = int ( input ( "over hoeveel mensen moet de pot verdeeld worden ?"))

print ( fooi_pp ( b,p))

def onderstreep (tekst=""):
    uit = []
    uit .append ( tekst)
    uit . append ( len ( tekst) * "=")
    return uit


inkomsten =   { 
        " Aardbeien-ijs-totaal" : 1000 ,
        " Vanille-ijs-totaal" : 2000,
        " Chocolade-ijs-totaal" : 1500 ,
        " Waterijsjes-totaal" : 750 , }

values = inkomsten . values ()
keys = inkomsten . keys ()
#print ( values)
#print ( keys)


values = inkomsten . values ()
keys = inkomsten . keys ()
som = inkomsten
def som (som):
    global inkomsten
som = values
sum = sum ( values)
#print ( (sum))


    




