print("----------------")
print("---Bienvenido---")
print("----------------")
print("Procesos automatizados")
print("----------------")
print("1.temperatura")
print("2.Valor de sueldos")
print("3.Calculo de areas")
print("________________")
Op=int(input())
if Op==1:
    print("Verificando la temperatura")
    import random
    Temperatura= random.randint(1, 50)
    print(Temperatura)
    if Temperatura<=27 and Temperatura>=17 :
       print("Muy bien supiendo a :",Temperatura)
    else:
       print("No es posible ")
       if Temperatura >= 27:
           print("La temperatura es my alta se bajara a : 27 ")
       if Temperatura <= 17:
           print("La temperatu es muy baja se subira a : 17 ")
else:
   print("")
if Op==2:
    print("Bienvenido a valor de los sueldos")
    print("Cuanto ganas al mes :")
    id=int(input())
    print("Tu sueldo  es de :",id)
    Diario=id/30
    print("Tu ganas por diario",Diario)
    print("Por mensual",id)
    Anual=id*12
    print("Por Anual",Anual)
if Op == 3 :
 print ("Bienvenido al calculo de áreas ")
 print ("----------------------------")
 print ("Qué deseas hacer ")
 print ("1.Calculo de cuadrado")
 print ("2.Calculo de triangulo")
 print ("3.Calculo de circulo")
 print ("4.Calculo de rectangulo")
 print ("----------------------------")
Op2=int(input())
if Op2==1:
    print("dame el largo de tu cuadro")
    largo=int(input())
    total=largo**2
if Op2==2:
    print()

    total=0.5*base*altura
if Op2==3:
    print()
    total=π(radio**2)
if Op2==4:
    print()
    total=largo*ancho