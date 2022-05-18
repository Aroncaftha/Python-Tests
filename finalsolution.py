import json
with open('Paquetes.json', 'r')as file:
    arch = file.read()

packs = json.loads(arch)
listaPaquetes = packs["PAQUETES"]

def calcularCosto(alto, ancho, profundo):
    volumen  = alto*ancho*profundo
    costo =  volumen*5
    if alto > 30:
        costo +=2000
    if costo > 10000: 
        costo += (costo*0.19)
    return costo
    
def costoTotal(listaPaquetes, descuento):
    costo, cont, indexsel = 0, 0, 0 
    for n in (listaPaquetes):
        cont += 1
        alto, ancho, profundo = listaPaquetes[indexsel]['ALTO'], listaPaquetes[indexsel]['ANCHO'], listaPaquetes[indexsel]['PROFUNDO']
        costo += calcularCosto(alto, ancho, profundo)
        if cont == len(listaPaquetes):
            costo -= (descuento*costo/100)
        indexsel+=1
    return(costo) 

print(costoTotal(listaPaquetes, 10))