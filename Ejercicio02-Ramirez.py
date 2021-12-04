def calcularImc(peso,altura):
    alturatotal = pow(float(altura),2)
    imc = float(peso)/alturatotal
    salida = str("{:,.1f}".format(imc))
    if imc > 25.0:
        print("IMC: "+salida)
        print("Su indice de imc está elevado")
        print("Recuerde: esos límites dependen de la edad, del sexo,etc...")
    elif imc <= 25.0 or imc>=20.0:
        print("IMC: "+salida)
        print("Su indice de imc está normal")
        print("Recuerde: esos límites dependen de la edad, del sexo,etc...")


peso = input("Introduzca su peso ")
altura = input("Introduzca su altura ")

calcularImc(peso,altura)
    
    
    
    
