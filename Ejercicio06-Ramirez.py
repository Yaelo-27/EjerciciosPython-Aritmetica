import math
def hora(segundos):
    minutos = float(segundos)/60
    horas = minutos/60
    horas_decimal,horas_entera = math.modf(horas)
    minutos_decimal,minutos_entera = math.modf(minutos)

    minutos_total = horas_decimal*60
    segundos_total  = minutos_decimal*60

    
    print("Segundos introducidos :"+segundos)
    print("Horas : "+str(int(horas_entera))+" minutos: "+str(int(minutos_total))+" segundos: "+str(int(segundos_total)))
    
    
    

segundos = input('Introduzca los segundos: ')

hora(segundos)
        
    

    
    
