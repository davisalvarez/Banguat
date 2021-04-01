from DataCollector import *

can = True
while(can):
    print("")
    print("Menú")
    print("Seleccione una opción:")
    print("")
    print("1. Buscar por un Día.")
    print("2. Buscar por Rango de Días.")
    print("3. Salir.")

    var = input("->")

    if(var=='1'):
        print("")
        print("1. Buscar por un Día.")
        print("")
        print("Ingrese la Fecha (DD-MM-AAAA):")
        year = input("->")
        print("Ingrese la Moneda (USD o EU):")
        moneda = input("->")
        print("")
        SearchByDay(year, moneda)
        #SearchByDay("20-11-2015", "USD")
    elif(var=='2'):
        print("")
        print("2. Buscar por Rango de Días.")
        print("")
        print("Ingrese la Fecha Inicial (DD-MM-AAAA):")
        year1 = input("->")
        print("Ingrese la Fecha Final (DD-MM-AAAA):")
        year2 = input("->")
        print("Ingrese la moneda (USD o EU):")
        moneda = input("->")
        print("")
        SearchByRange(year1, year2, moneda)
        #SearchByRange("15-07-2020", "19-08-2020", "USD")
    elif(var=='3'):
        can = False
        print("Hasta la próxima!")
    else:
        print("No es una opción valida!")

#print("Se ha identificado un problema con la Fecha. Debe estar entre el 2015 y hoy!")



