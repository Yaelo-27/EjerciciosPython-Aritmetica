def convertirF(celsius):
    calculo = float(celsius)*1.8
    fahrenheit = calculo + 32
    print("Grados en celsius: "+celsius)
    print("Grados en fahrenheit: "+str(fahrenheit))

celsius = input('Introduzca los grados en Cº')

convertirF(celsius)
        
