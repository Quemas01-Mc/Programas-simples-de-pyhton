from ast import For
import os
import random
os.system("cls")
print( '=======================================')
print( '| -------- CASINO LA RATA  -----------|')
print( '=======================================')
print( '-----------  Bienvenido  --------------')
print( '-------- Solo mayores de edad ---------')
print( '=======================================')
print( '-Donde vendemos mejor que otros lugares')
print( '=======================================')
print(  "¿Cual es tu nombre?")
print( "---------------------------------------")
Nombre=input("Ingrese su nombre :  ")
os.system("cls")
print( '=======================================')
print("Hola",Nombre,"Que edad tienes ?")
print( "---------------------------------------")
Edad=int(input("Ingrese su edad :  "))
if Edad >= 18:
    Bucle = "s"
    TotalUni = 0
    TotalCO = 0
    TotalGa = 0
    DineroPa = 0
    while Bucle == "s":
        print("Que actividad deseas hacer ?")
        print('=========== Menu ============')
        print('1.Bar')
        print('2.Juegos')
        print('-----------------------------')
        OpcionAc=int(input("Elija una opcion de 1/2 : "))
        if OpcionAc == 1 :
           os.system("cls")
           print("========= Menu de Licores =========")
           print('1. Martini .............. $ 2.10')
           print('2. Negroni .............. $ 4.00')
           print('3. Jugo de mora ......... $ 2.50')
           print('===================================')
           print('Puedes ganar un descuento si superas una compra de mas de 3 vevidas')
           print('-------------------------------------------------------------------')
           print("Que deseas comprar ?")
           print( '___________________')
           
        elif OpcionAc == 2 :
            Bucle = "n"
        else :
         print('==================================')
         print('Ingresaste un numero invalido')
         print(':(')
         print('Intentalo de nuevo')
         print('===================================')
         print('-----Enter para continuar----')
         print('==================================')
         input()
         Bucle="s"
else :
    print('--------------------------------------------------------------------')
    print( 'Lo siento ,',Nombre ,' pero no tienes la edad necesaria para ingresar')
    print(':(')
    print('--------------------------------------------------------------------')
    exit()


if OpcionAc == 2:
    os.system("cls")
    print("Cuanta plata quieres apostar  ?",Nombre)
    print('---------------------------------------------------')
    Dinero=int(input("Ingresa el monto para apostar : "))
    DineroPa = Dinero
    os.system("cls")
    juego = "s"
    while juego == "s":
        print("==========================")
        print("Que quieres juegar ?")
        print('======== Menu  ===========')
        print('1.Es par o impar----------')
        print('2.Piedra,Papel o Tijera---')
        print('3.Carrera de caballos-----')
        print('__________________________')
        OpcionJu=int(input("Ingresa un numero del 1,2 o 3 : "))
        os.system("cls")
        if OpcionJu== 1:
            print('Tu saldo es de: $',Dinero)
            print('==========================')
            BucleAp = "s"
            while BucleAp == "s":
             print("Ingresa el monto a apostar: minimo $1, maximo $",Dinero)
             Apuesta=int(input("Ingresa del monto : "))
             if Apuesta >= 1 and Apuesta <= Dinero:
                 print('Bienvenido a es par o impar')
                 print('===========================')
                 print('Ya tengo el numero pensado')
                 print('Dime, es par o impar?')
                 print('===========================')
                 print('1.Par')
                 print('2.Impar')
                 print('___________________________')
                 OpcionPa=int(input("Ingrese el numero 1/2 : "))
                 if OpcionPa == 1 :
                     print('Escogiste par')
                     print('==============')
                     NumeroRand=random.randint(1,100)
                     if NumeroRand % 2 == 0 :
                        print('El numero fue par: ',NumeroRand)
                     else :
                         print()
                 BucleAp="n"
                 juego="n"
             else:
                 print("Invalido ingrese de nuevo")
                 BucleAp="s"
        elif OpcionJu == 2 :
            print("Juego en mantenimiento vuelva mas despues")
        elif OpcionJu == 3 :
            print("Juego en mantenimiento vuelva mas despues")
        else:
         print('==================================')
         print('Ingresaste un numero invalido')
         print(':(')
         print('Intentalo de nuevo')
         print('===================================')
         print('-----Enter para continuar----')
         print('==================================')
         input()
         juego="s"
            
        