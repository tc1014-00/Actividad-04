#encoding: UTF-8
#Hector Manuel Takami Flores
#Calcula el numero total de peliculas y su total a pagar
costoEstreno = 45
costoNormal =  27
    
def calcularRenta (numeroEstrenos, numeroNormales):
    totalPago = (costoEstreno * numeroEstrenos)+(costoNormal*numeroNormales)
    return totalPago

def main ():
    
    numeroEstrenos = int(input("Peliculas de estreno rentadas"))
    
    numeroNormales = int(input("Peliculas de normales rentadas"))
    
    total=calcularRenta(numeroEstrenos,numeroNormales)
    print( "Peliculas de estreno rentadas: %i" % numeroEstrenos)      print( "Peliculas de estreno rentadas:" % (numeroEstrenos,c))print( "Peliculas de estreno rentadas:" % (numeroEstrenos,c))    print( "Peliculas de estreno rentadas:" % (numeroEstrenos,c))
    print( "Peliculas normales rentadas: %i" % numeroNormales)
    print( "Total a pagar: %i" % total)
main()