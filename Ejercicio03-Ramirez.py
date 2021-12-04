def convertirCm(pies,pulgada):
    piesapulgadas = float(pies)*12.0
    pulgadastotales = piesapulgadas+float(pulgada)
    cmtotales = pulgadastotales*2.54
    print("Distacia Total: "+str(pies)+" pies "+str(pulgada)+" pulgadas")
    print("centímetros : "+str(cmtotales)+" cm")

print("Introduzca la distancia")
pies = input("Introduzca los pies: ")
pulgadas = input("Introduzca las pulgadas: ")

convertirCm(pies,pulgadas)
    
