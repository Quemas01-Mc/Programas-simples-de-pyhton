import os
import random
numeros="1234567890"
caracteres=".,-/()¨ç´{}¿?*+!#@$%&Ç"
letras="qwertyuiopasdfghjklñzxcvbnm"
NombreVal = False
while not NombreVal:
    os.system("cls")
    print('=======================================')
    print('| -------- CASINO LA RATA  -----------|') 
    print('=======================================') 
    print('-----------  Bienvenido  --------------')
    print('-------- Solo mayores de edad ---------')
    print('=======================================')
    print('-Donde vendemos mejor que otros lugares')
    print('=======================================')
    print('¿Cual es tu nombre?')
    print('---------------------------------------') 
    Nombre = str(input())
    Hay_numeros =  False
    Hay_caracteres = False
    for error in  Nombre :
        for Num in numeros:
            if error == Num:
                Hay_numeros = True
        for  Carac in caracteres:
            if error == Carac:
                Hay_caracteres = True
            
    if Hay_numeros == True or Nombre == " ":
        print('==================================')
        print('Ingresaste un numeros solo letras')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        os.system("cls")
        continue
    elif Hay_caracteres == True:
        print('==================================')
        print('Ingresaste un caracteres solo letras')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        os.system("cls")
        continue
    else:
        break
    
EdadV = False
Edad0 = 0 
while True:
    os.system("cls")
    print('=======================================')
    print(f'Hola {Nombre} ¿Qué edad tienes?') 
    print('---------------------------------------') 
    Edad=input("Ingrese su edad :  ")
    Hay_letras =  False
    Hay_caracteres = False
    for error in  Edad :
        for Let in letras:
            if error == Let:
                Hay_letras = True
        for  Carac in caracteres:
            if error == Carac:
                Hay_caracteres = True
            
    if Hay_letras == True or Edad == " ":
        print('==================================')
        print('Ingresaste letras solo numeros')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        os.system("cls")
        continue
    elif Hay_caracteres == True:
        print('==================================')
        print('Ingresaste un caracteres solo numeros')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        os.system("cls")
        continue
    else:
        Edad0 = int(Edad)
        os.system("cls")
        break

if Edad0 >= 18:
        Bucle = True
        TotalUni = 0 
        TotalCO = 0  
        TotalGa = 0  
        DineroPa = 0 
        dinero = 0
        while Bucle == True:
            os.system("cls")
            print('=========== Menu ============') 
            print('1.Bar------------------------')
            print('2.Juegos---------------------')
            print('_____________________________')
            Opcion = input("Ingrese un numero 1,2 : ")
            os.system("cls")
            Hay_letras =  False
            Hay_caracteres = False
            for error in  Opcion :
                for Let in letras:
                    if error == Let:
                        Hay_letras = True
            for  Carac in caracteres:
                    if error == Carac:
                        Hay_caracteres = True
                        
                    
            if Hay_letras == True or Nombre == " ":
                print('==================================')
                print('Ingresaste letras solo numeros')
                print(':(')
                print('Intentalo de nuevo')
                print('===================================')
                print('-----Enter para continuar----')
                print('==================================')
                input() 
                os.system("cls")
                continue
            elif Hay_caracteres == True:
                print('==================================')
                print('Ingresaste un caracteres solo numeros')
                print(':(')
                print('Intentalo de nuevo')
                print('===================================')
                print('-----Enter para continuar----')
                print('==================================')
                input() 
                os.system("cls")
                continue
            else:
                Opcion = int(Opcion)
                os.system("cls")
                break
                            
        I = True 
        if Opcion == 1:      
                while I == True:
                    os.system("cls")
                    print('========= Menú de Licores =========')
                    print('1. Martini .............. $ 2.10') 
                    print('2. Negroni .............. $ 4.00') 
                    print('3. Jugo de mora ......... $ 2.50') 
                    print('===================================')
                    print('¿Qué deseas comprar?')
                    print('-----------------------------------') 
                    print('Puedes ganar un descuento si superas una compra de mas de 3 vevidas')
                    print('___________________________________________________________________')
                    Comprar=int(input())
                    os.system("cls")
                    if Comprar == 1:
                        print(f'Qué buena elección {Nombre} ¿Cuánto deseas llevar?')
                        print('--------------------------------------------------------') 
                        Chi = int(input(": "))
                        Costo = 2.10
                        Unidades = Chi 
                        TotalUni = TotalUni+Unidades
                        Total = Chi * Costo
                        TotalCO = TotalCO+Total
                        I = False
                        Bucle= False
                    elif Comprar == 2:
                      print(f'Qué buena elección {Nombre} ¿Cuánto deseas llevar?')
                      print('--------------------------------------------------------') 
                      Chi = int(input(": "))
                      Costo = 4.00
                      Unidades = Chi 
                      TotalUni = TotalUni+Unidades
                      Total = Chi * Costo
                      TotalCO = TotalCO+Total
                      I = False
                      Bucle=False
                    elif Comprar == 3 : 
                        print(f'Qué buena elección {Nombre} ¿Cuánto deseas llevar?')
                        print('--------------------------------------------------------')
                        Chi = int(input(": "))
                        Costo = 2.50
                        Unidades = Chi 
                        TotalUni = TotalUni+Unidades
                        Total = Chi * Costo
                        TotalCO = TotalCO+Total
                        I = False
                        Bucle = False
                    else:
                        print('==================================')
                        print('Ingresaste un numero invalido')
                        print(':(')
                        print('Intentalo de nuevo')
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        Bucle = 'n'
                        continue
                        os.system("cls")
                        
                        
                    print('Quieres hacer algo mas antes de irte s/n')
                    print('----------------------------------------') 
                    barOp=input("Escriba s/n : ")
                    if barOp == "s":
                        I = False
                        Bucle = True
                    elif barOp == "n" :
                        I = False
                        Bucle = False 
        elif Opcion == 2:        
                print(f'¿Cuánta plata quieres poner para apostar? {Nombre}')
                print('---------------------------------------------------')
                dinero = float(input())   
                DineroPa = dinero
                Juefo = 's'
               
                while Juefo == 's':
                    print('==========================')
                    print('¿Qué quieres jugar?')
                    print('======== Menú  ===========')
                    print('1.Es par o impar----------')
                    print('2.Piedra,Papel o Tijera---')
                    print('3.Carrera de caballos-----')
                    print('__________________________')
                    Juego = input()
                    os.system("cls")
                    LOP = "s"
                    while LOP == "s":
                     print(f'Tu saldo es de: ${dinero:.2f}')
                     print('==========================')
                     print(f'Ingresa el monto a apostar: mínimo $1, máximo ${dinero:.2f}') 
                     print('=======================================================')
                     Apuesta = float(input())
                     if Apuesta <= dinero and Apuesta >= 1:
                      LOP = "n"
                     else:
                        print('==================================')
                        print('Ingresaste un numero invalido')
                        print(':(')
                        print('Intentalo de nuevo')
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        LOP = "s" 
                        os.system("cls")
                    if Juego == '1':
                        Buc = 's'
                        
                        while Buc == 's':
                            os.system("cls")
                            print("===========================")
                            print('Bienvenido a es par o impar')
                            print('===========================')
                            print('Ya tengo el número pensado')
                            print('===========================')
                            print('Dime, ¿es par o impar?')
                            print('===========================')
                            print('1.Par')
                            print('2.Impar')
                            print('___________________________')
                            PoI = input()
                            
                            Elnumero = random.randint(1, 50)
                            es_par = Elnumero % 2 == 0
                            
                           
                            if PoI == '1':
                                print('Escogiste par')
                                print('==============')
                                if es_par:
                                    print(f'El número fue par: {Elnumero}')
                                    print('Ganaste')
                                    dinero += Apuesta
                                    TotalGa += Apuesta 
                                    print(f'Ganaste en total: ${dinero:.2f}')
                                    print('============================')
                                else:
                                    print(f'El número fue impar: {Elnumero}')
                                    print('===============================')
                                    print(f'Perdiste ${Apuesta:.2f}')
                                    print('=============================')
                                    dinero -= Apuesta
                                    print(f'Te quedas con ${dinero:.2f}')
                                    print('==============================')
                                    print('La casa gana')
                                    print('==============================')
                                    
                            
                            elif PoI == '2':
                                print('Escogiste impar')
                                print('===============')
                                if not es_par:
                                    print(f'El número fue impar: {Elnumero}')
                                    print('Ganaste')
                                    dinero += Apuesta
                                    TotalGa += Apuesta 
                                    print(f'Ganaste en total: ${dinero:.2f}')
                                    print('============================')
                                else:
                                    print(f'El número fue par: {Elnumero}')
                                    print('===============================')
                                    print(f'Perdiste ${Apuesta:.2f}')
                                    print('===============================')
                                    dinero -= Apuesta
                                    print(f'Te quedas con ${dinero:.2f}')
                                    print('===============================')
                                    print('La casa gana')
                                    print('===============================')
                                    
                            
                            if dinero <= 0:
                                print('Te quedaste sin dinero. Fin del juego.')
                                Buc = 'n'
                                Bucle = 'n'
                                Juefo = 'n'
                            else:
                                print('¿Quieres seguir jugando? s/n') 
                                print('----------------------------')
                                Ele = input()
                                if Ele == 's':
                                    Buc = 's'
                                    os.system("cls")
                                else:
                                    print('======================================')
                                    print(f'Te retiras con el total de ${dinero:.2f}')
                                    print('======================================')
                                    Buc = 'n'
                                    Bucle = 'n'
                                    Juefo = 'n'
                            
                    elif Juego == '2':
                        Buc = 's'
                        
                        while Buc == 's':
                            print(f'Tu saldo es de: ${dinero:.2f}')
                            print('=========================')
                            print(f'Ingresa el monto a apostar mínimo $1, máximo ${dinero:.2f}')
                            print('-------------------------------------------------------')
                            Apuesta = float(input())    
                            print('===============')
                            print('Elije entre :')
                            print('===============')
                            print('1.Piedra------|')
                            print('2.Tijera------|') 
                            print('3.Papel-------|')
                            print('---------------')
                            
                            Op = input()
                            os.system("cls")
                            
                            print('==============')
                            Ga = random.randint(1, 3) 
                            
                           
                            resultado = ""
                            
                            
                            if Op == '1':
                                print('Elejiste piedra')
                                print('===============')
                                if Ga == 1:
                                    resultado = "pierde"
                                    print('Yo elegi papel')
                                elif Ga == 2: 
                                    resultado = "gana"
                                    print('Yo elegi tijera')
                                else: 
                                    resultado = "empate"
                                    print('Yo elegi piedra')
                            
                          
                            elif Op == '2':
                                print('Elejiste tijeras')
                                if Ga == 1: 
                                    resultado = "pierde"
                                    print('Yo elegi piedra')
                                elif Ga == 2: 
                                    resultado = "gana"
                                    print('Yo elegi papel')
                                else:
                                    resultado = "empate"
                                    print('Yo elegi tijera')
                                    
                           
                            elif Op == '3':
                                print('Elejiste papel')
                                if Ga == 1:
                                    resultado = "pierde"
                                    print('Yo elegi tijera')
                                elif Ga == 2: 
                                    resultado = "gana"
                                    print('Yo elegi piedra')
                                else:
                                    resultado = "empate"
                                    print('Yo elegi papel')
                            
                           
                            else:
                                print('==================================')
                                print('Ingresaste un numero invalido')
                                print(':(')
                                print('Intentalo de nuevo')
                                print('===================================')
                                print('-----Enter para continuar----')
                                print('==================================')
                                input() 
                                continue 
                                
                            print('============================')
                            
                           
                            if resultado == "gana":
                                print('Tu ganaste')
                                dinero += Apuesta
                                TotalGa += Apuesta
                                print('============================')
                                print(f'Ganaste en total : ${dinero:.2f}')
                                print('============================')
                            elif resultado == "pierde":
                                print('Yo gane')
                                print('============================')
                                print(f'Perdiste ${Apuesta:.2f}')
                                print('============================')
                                dinero -= Apuesta
                                print(f'Te quedas con ${dinero:.2f}')
                                print('============================')
                                print('La casa gana')
                                print('============================')
                            elif resultado == "empate":
                                print('Empate')
                                print('============================')
                                print('Nadie gana')
                                print('============================')
                                print(f'Dinero apostado $ {Apuesta:.2f}')

                            
                            if dinero <= 0:
                                print('Te quedaste sin dinero. Fin del juego.')
                                Buc = 'n'
                                Bucle = 'n'
                                Juefo = 'n'
                            else:
                                print('Quieres seguir juegando? s/n')
                                print('----------------------------')
                                Ele = input()
                                
                                if Ele == 's':
                                    Buc = 's'
                                else:
                                    Buc = 'n'
                                    Bucle = 'n'
                                    Juefo = 'n'
                                    
                    elif Juego == '3':
                        
                        buc3 = "s"
                        
                        while buc3 == "s":
                            print("=============================")
                            print('A que caballo quieres apostar')
                            print("=============================")
                            print('1.Secretariat')
                            print('2.Justify')
                            print('3.Cigar')
                            print("-----------------------------")
                            Caballo = input()
                            
                            NombreCA = ''
                            ID = 0
                            
                            if Caballo == '1':
                                NombreCA = 'Secretariat'
                                ID = 1
                                buc3 = "n"
                            elif Caballo == '2':
                                NombreCA = 'Justify'
                                ID = 2
                                buc3 = "n"
                            elif Caballo == '3':
                                NombreCA = 'Cigar'
                                ID = 3
                                buc3 = "n"
                            else:
                                print('==================================')
                                print('Ingresaste un numero invalido')
                                print(':(')
                                print('Intentalo de nuevo')
                                print('===================================')
                                print('-----Enter para continuar----')
                                print('==================================')
                                input() 
                                os.system("cls")
                                buc3 = "s"
                                
                        
                        
                                print(f'Ingresa el monto a apostar: mínimo $1, máximo ${dinero:.2f}') # [cite: 80]
                                print('--------------------------------------------------------')
                                Apuesta = float(input())
                        
                        
                        
                        
                        
                        os.system("cls")
                        print('-------|\__-------------------------------------------------------')
                        print(' ______|´ |)-----------------------------------------------------')
                        print('/  |1| /-------------------------------------------------------') 
                        print(' ----- |\__------------------------------------------------------')
                        print(' ______|´ |)-----------------------------------------------------')
                        print('/  |2|   /-------------------------------------------------------')
                        print(' ------|\__------------------------------------------------------')
                        print(' ______|´ |)-----------------------------------------------------')
                        print('/  |3| /-------------------------------------------------------') 
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        
                        NUm = random.randint(1, 3)
                        os.system("cls")
                        
                        
                        if NUm == 1:
                            
                            print('------------------------|\__-------------------------------------')
                            print('----------------- ______|´ |)------------------------------------')
                            print('-----------------/  |2| /--------------------------------------') 
                            print(' --------------- |\__--------------------------------------------')
                            print('---------- ______|´ |)-------------------------------------------')
                            print('----------/  |1|   /----------------------------------------------')
                            print(' ------|\__------------------------------------------------------')
                            print(' ______|´ |)-----------------------------------------------------')
                            print('/  |3| /-------------------------------------------------------') 
                        elif NUm == 2:
                             
                            print('------------------------|\__-------------------------------------')
                            print('----------------- ______|´ |)------------------------------------')
                            print('-----------------/  |3| /--------------------------------------') 
                            print(' --------------- |\__--------------------------------------------')
                            print('---------- ______|´ |)-------------------------------------------')
                            print('----------/  |2|   /----------------------------------------------')
                            print(' ------|\__------------------------------------------------------')
                            print(' ______|´ |)-----------------------------------------------------')
                            print('/  |1| /-------------------------------------------------------') 
                        else: 
                            print('------------------------|\__-------------------------------------')
                            print('----------------- ______|´ |)------------------------------------')
                            print('-----------------/  |2| /--------------------------------------') 
                            print(' --------------- |\__--------------------------------------------')
                            print('---------- ______|´ |)-------------------------------------------')
                            print('----------/  |3|   /----------------------------------------------')
                            print(' ------|\__------------------------------------------------------')
                            print(' ______|´ |)-----------------------------------------------------')
                            print('/  |1| /-------------------------------------------------------') 
                            
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        NUm = random.randint(1, 3)
                        os.system("cls")
                        
                        
                        if NUm == 1:
                            
                            print('------------------------------------|\__--------------------------')
                            print('----------------------------- ______|´ |)------------------------')
                            print('-----------------------------/  |3| /--------------------------') 
                            print(' ----------------------------------------------------|\__--------')
                            print('-----------------------------------------------______|´ |)-------')
                            print('----------------------------------------------/  |1|   /---------')
                            print('------------------------|\__-------------------------------------')
                            print('----------------- ______|´ |)------------------------------------')
                            print('-----------------/  |2| /--------------------------------------') 
                        elif NUm == 2:
                        
                            print('------------------------------------|\__--------------------------')
                            print('----------------------------- ______|´ |)------------------------')
                            print('-----------------------------/  |1| /--------------------------') 
                            print(' ----------------------------------------------------|\__--------')
                            print('-----------------------------------------------______|´ |)-------')
                            print('----------------------------------------------/  |3|   /---------')
                            print('------------------------|\__-------------------------------------')
                            print('----------------- ______|´ |)------------------------------------')
                            print('-----------------/  |2| /--------------------------------------') 
                        else: 
                            
                            print('------------------------------------|\__--------------------------')
                            print('----------------------------- ______|´ |)------------------------')
                            print('-----------------------------/  |1| /--------------------------') 
                            print(' ----------------------------------------------------|\__--------')
                            print('-----------------------------------------------______|´ |)-------')
                            print('----------------------------------------------/  |3|   /---------')
                            print('------------------------|\__-------------------------------------')
                            print('----------------- ______|´ |)------------------------------------')
                            print('-----------------/  |2| /--------------------------------------')
                            
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input()
                        NUm = random.randint(1, 3)
                        os.system("cls")
                        
                        
                        Ganador_ID = 0
                        
                        if NUm == 1:
                            
                            print('------------------------------------|\__--------------------------')
                            print('----------------------------- ______|´ |)------------------------')
                            print('-----------------------------/  |3| /--------------------------') 
                            print(' ----------------------------------------------------|\__--------')
                            print('-----------------------------------------------______|´ |)-------')
                            print('----------------------------------------------/  |2|   /---------')
                            print('-------------------------------------------------------------|\__')
                            print('-------------------------------------------------------______|´ |)')
                            print('------------------------------------------------------/  |1| /') 
                        elif NUm == 2:
                            
                            print('------------------------------------|\__--------------------------')
                            print('----------------------------- ______|´ |)------------------------')
                            print('-----------------------------/  |2| /--------------------------') 
                            print(' ----------------------------------------------------|\__--------')
                            print('-----------------------------------------------______|´ |)-------')
                            print('----------------------------------------------/  |1|   /---------')
                            print('-------------------------------------------------------------|\__')
                            print('-------------------------------------------------------______|´ |)')
                            print('------------------------------------------------------/  |3| /') 
                            Ganador_ID = 3
                        else: 
                            
                            print('------------------------------------|\__--------------------------')
                            print('----------------------------- ______|´ |)------------------------')
                            print('-----------------------------/  |1| /--------------------------') 
                            print(' ----------------------------------------------------|\__--------')
                            print('-----------------------------------------------______|´ |)-------')
                            print('----------------------------------------------/  |3|   /---------')
                            print('-------------------------------------------------------------|\__')
                            print('-------------------------------------------------------______|´ |)')
                            print('------------------------------------------------------/  |2| /') 
                            Ganador_ID = 2

                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        os.system("cls")
                        
                        
                        if Ganador_ID == 1:
                            Ganador_Nombre = "Secretariat"
                        elif Ganador_ID == 2:
                            Ganador_Nombre = "Justify"
                        else:
                            Ganador_Nombre = "Cigar"
                            
                        print("========================")
                        print(f"El ganador fue {Ganador_Nombre}")
                        print("========================")
                        print(f"Tu escojiste a {NombreCA}")
                        print("========================")
                        
                        if ID == Ganador_ID:
                            print("Ganaste felizidades")
                            print("===================")
                            dinero += Apuesta
                            TotalGa += Apuesta
                            print(f'Ganaste en total : ${dinero:.2f}')
                            print('============================')
                        else:
                            print(f'Perdiste ${Apuesta:.2f}')
                            print('==============================')
                            dinero -= Apuesta
                            print(f'Te quedas con ${dinero:.2f}')
                            print('==============================')
                            print('La casa gana')
                            print('==============================')

                        
                        if dinero <= 0:
                            print('Te quedaste sin dinero. Fin del juego.')
                            buc3 = "n"
                            Buc = 'n'
                            Bucle = 'n'
                            Juefo = 'n'
                        else:
                            print('Quieres seguir juegando? s/n') 
                            print('----------------------------')
                            Ele = input().lower()
                            
                            if Ele == 's':
                                Juefo = "s"
                                os.system("cls")
                            else:
                                buc3 = "n"
                                Buc = 'n'
                                Bucle = 'n'
                                Juefo = 'n'
                                
                   
                    else:
                        print('==================================')
                        print('Ingresaste un numero invalido')
                        print(':(')
                        print('Intentalo de nuevo')
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        Juefo = 's'
                        
           
        elif Bucle == "s":
            print('==================================')
            print('Ingresaste un numero invalido')
            print(':(')
            print('Intentalo de nuevo')
            print('===================================')
            print('-----Enter para continuar----')
            print('==================================')
            input() 
            Bucle = True
                
        
        os.system("cls")
        Descuento = 0.0
        TotalAPagar = TotalCO
        
        
        if TotalUni >= 3:
            Descuento = TotalCO * 0.1
            TotalAPagar = TotalCO - Descuento
            
        
        print(f'El total a pagar del bar es: ${TotalCO:.2f}')
        print('========================================')
        print(f'El total a pagar del casino es ${DineroPa:.2f}')
        PagOP="s"
        while PagOP == "s":
         print('=======================================')
         print('Como quieres pagar tu consumo :')
         print('================================')
         print('1.Efectivo')
         print('2.Tarjeta')
         print('-------------------------------')
         Pago = int(input("Elija un numero de 1/2 : "))
        
         PagoET = ''
         if Pago == 1:
            PagoET = 'Efectivo'
            PagOP = "n"
         elif Pago == 2:
            PagoET = 'Tarjeta'
            PagOP = "n"
         else:
            print('==================================')
            print('Ingresaste un numero invalido')
            print(':(')
            print('Intentalo de nuevo')
            print('===================================')
            print('-----Enter para continuar----')
            print('==================================')
            input()
            os.system("cls")
            PagOP = "s"
        os.system("cls")
        print('====================================')
        print('------- FACTURA DE COMPRA ----------') 
        print('====================================')
        print(f'Cliente: {Nombre}')
        print('------------------------------------')
        print(f'Productos: {TotalUni:.0f} bebidas ')
        print(f'Subtotal: ${TotalCO:.2f}')
        if TotalUni >= 3:
          print(f'Descuento (10% por 3+ bebidas): ${Descuento:.2f}')
        print('------------------------------------')
        print(f'TOTAL A PAGAR: ${TotalCO:.2f}') 
        print(f'Método de Pago: {PagoET}')
        print('=======================================')
        print('--------- Apuestas echas --------------')
        print(f"Dinero apostado : ${DineroPa:.2f}")
        print(f'Total de dinero ganado : ${TotalGa:.2f}')
        print(f'Te retiras con el total de ${dinero:.2f}')
        print('====================================')
        print('      ¡Gracias por visitarnos!')
        print('====================================')
else:
        print('--------------------------------------------------------------------')
        print(f'Lo siento, {Nombre}, pero no tienes la edad necesaria para ingresar')
        print(':(')
        print('--------------------------------------------------------------------')
        print(f'Esperamos su regreso {Nombre}')
        print('================================')
