def convertirC(fahrenheit):
    calculo = float(fahrenheit)-32
    calculo_2= calculo*5
    celsius = calculo_2/9
    print("Grados en fahrenheit: "+fahrenheit+" Fº")
    print("Grados en celsius: "+str(celsius)+" Cº")

fahrenheit = input('Introduzca los grados en Fº')

convertirC(fahrenheit)
