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





