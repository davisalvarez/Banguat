import datetime
from CollectorBot import *

def SearchByDay(fecha, moneda):

    try:
        fechaI = datetime.datetime.strptime(fecha, "%d-%m-%Y")
    except ValueError:
        print("Fecha en formato incorrecto, debería ser: DD-MM-AAAA")
        return 0
    limite = datetime.datetime(2014, 12, 31)

    if (fechaI > limite and fechaI < datetime.datetime.now()) :

        fecha = fecha.split("-")
        if(moneda=='EU'):
            currency = 18
        else:
            currency = 2

        year = int(fecha[2])
        year = year - 2015 + 18
        fecha[2] = str(year)

        rate = starBot(fechaI=fecha,fechaF=fecha, moneda=currency,dias=3)

        if(len(rate)>0):
            print("Date: "+str(fechaI))
            print("Currency: "+moneda)
            print("Rate: "+str(rate[0]))
            return 1
        else:
            return 0
    return 0

def SearchByRange(fechaI, fechaF, moneda):

    try:
        fechaI2 = datetime.datetime.strptime(fechaI, "%d-%m-%Y")
        fechaF2 = datetime.datetime.strptime(fechaF, "%d-%m-%Y")
        if(fechaF2 < fechaI2):
            print("Fecha Inicial es después  de la Fecha Final.")
            return 0
    except ValueError:
        print("Fecha en formato incorrecto, debería ser: DD-MM-AAAA")
        return 0
    limite = datetime.datetime(2014, 12, 31)

    if (fechaI2 > limite and fechaI2 < datetime.datetime.now()) :
        if (fechaF2 > limite and fechaF2 < datetime.datetime.now()):

            fechaI = fechaI.split("-")
            fechaF = fechaF.split("-")
            if(moneda=='EU'):
                currency = 18
            else:
                currency = 2

            year = int(fechaI[2])
            year = year - 2015 + 18
            fechaI[2] = str(year)

            year = int(fechaF[2])
            year = year - 2015 + 18
            fechaF[2] = str(year)

            delta = fechaF2 - fechaI2


            rate = starBot(fechaI=fechaI,fechaF=fechaF, moneda=currency,dias=delta.days+3)


            if (len(rate) > 0):
                mean = sum(rate) / len(rate)

                print("Start date: " + str(fechaI2))
                print("End  date : " + str(fechaF2))
                print("Currency: " + moneda)
                print("Rate: " + str(rate[0]))
                print("Mean: " + str(mean))
                print("Max: " + str(max(rate)))
                print("Min: " + str(min(rate)))
                return 1
            else:
                return 0
        return 0