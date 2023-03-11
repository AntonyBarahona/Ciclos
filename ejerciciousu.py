#se necesita un programa que permita almacenar el nombre de usuarios que utiliza un ordenador
usuarios=[]
x=True
numeros=0
while x==True:
    nombre=input("ingrese su nombre ")
    usuarios.append(nombre)
    pregunta=input("Desea agregar otro usuario s/n ")
    if pregunta=="s":
        pass
    else:
        x=False
for y in usuarios:
    numeros=numeros+1
    print(str(numeros)+" "+y)