def piramide(): # 19 Isolda J
    print("Càlcul de l'àrea i del volum d'una piràmide ")
    abase = float(input("Longitud del centre de la base al centre del costat = "))
    acostat = float(input("Longitud del vèrtex al centre del costat = "))
    h = float(input("Alçada = "))
    area = (2*abase) * 4 * (abase + acostat)/2
    volum = pow((2 * abase),2) * h * (1/3)
    return area, volum

a,b = piramide()
print("L'area de la piràmide és: ",a," i el volum és: ",b)