import os
import random
Carga = "#"
for Carga in range(20):
    print("",Carga)
    
    input()
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
Nombre = input()
os.system("cls")
print('=======================================')
print(f'Hola {Nombre} ¿Qué edad tienes?') 
print('---------------------------------------') 
Edad=int(input("Ingrese su edad :  "))
if Edad >= 18:
        Bucle = 's'
        TotalUni = 0 # Total de unidades (bebidas)
        TotalCO = 0  # Total del consumo (bar)
        TotalGa = 0  # Total ganado en juegos
        DineroPa = 0 # Dinero puesto para apostar (inicial)
        dinero = 0
        
        # Mientras Bucle='s' Hacer
        while Bucle == 's':
            print('¿Qué activida deseas hacer?')
            print('=========== Menu ============') 
            print('1.Bar')
            print('2.Juegos')
            print('-----------------------------')
            Opcion = int(input("Ingrese un numero 1,2 : "))
            os.system("cls")
            if Opcion == 1:
                I = 's'
                # Mientras I='s' Hacer
                while I == 's':
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
                        I = "n"
                        Bucle="n"
                    elif Comprar == 2:
                      print(f'Qué buena elección {Nombre} ¿Cuánto deseas llevar?')
                      print('--------------------------------------------------------') 
                      Chi = int(input(": "))
                      Costo = 4.00
                      Unidades = Chi 
                      TotalUni = TotalUni+Unidades
                      Total = Chi * Costo
                      TotalCO = TotalCO+Total
                      I = "n"
                      Bucle="n"
                    elif Comprar == 3 : 
                        print(f'Qué buena elección {Nombre} ¿Cuánto deseas llevar?')
                        print('--------------------------------------------------------')
                        Chi = int(input(": "))
                        Costo = 2.50
                        Unidades = Chi 
                        TotalUni = TotalUni+Unidades
                        Total = Chi * Costo
                        TotalCO = TotalCO+Total
                        I = "n"
                        Bucle ="n"
                    elif I == "s" :
                        print('==================================')
                        print('Ingresaste un numero invalido')
                        print(':(')
                        print('Intentalo de nuevo')
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        Bucle = 'n'
                        I="s"
                        os.system("cls")
                    else:
                      print('Quieres hacer algo mas antes de irte s/n')
                      print('----------------------------------------') 
                      barOp=input("Escriba s/n : ")
                      if barOp == "s":
                        I = "s"
                        Bucle = "s"
                      elif barOp == "n" :
                        I = "n"
                        Bucle ="n" 
            elif Opcion == 2:        
                print(f'¿Cuánta plata quieres poner para apostar? {Nombre}')
                print('---------------------------------------------------')
                dinero = float(input())   
                DineroPa = dinero
                Juefo = 's'
                # Mientras Juefo='s' Hacer
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
                        # Mientras Buc='s' Hacer
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
                            
                            Elnumero = random.randint(1, 50) # Simula Aleatorio(1,50)
                            es_par = Elnumero % 2 == 0
                            
                            # Opción 1: Escogió Par
                            if PoI == '1':
                                print('Escogiste par')
                                print('==============')
                                if es_par:
                                    print(f'El número fue par: {Elnumero}')
                                    print('Ganaste')
                                    dinero += Apuesta
                                    TotalGa += Apuesta # Se suma solo la ganancia
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
                                    
                            # Opción 2: Escogió Impar
                            elif PoI == '2':
                                print('Escogiste impar')
                                print('===============')
                                if not es_par:
                                    print(f'El número fue impar: {Elnumero}')
                                    print('Ganaste')
                                    dinero += Apuesta
                                    TotalGa += Apuesta # Se suma solo la ganancia
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
                                    
                            # Si pierde o se queda sin dinero
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
                        # Mientras Buc='s' Hacer
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
                            Ga = random.randint(1, 3) # Simula Aleatorio(1,3) para la casa
                            
                            # Opciones de juego (Piedra, Papel, Tijera)
                            resultado = ""
                            
                            # Opción 1: Jugador Piedra
                            if Op == '1':
                                print('Elejiste piedra')
                                print('===============')
                                if Ga == 1: # Casa: Papel
                                    resultado = "pierde"
                                    print('Yo elegi papel')
                                elif Ga == 2: # Casa: Tijera
                                    resultado = "gana"
                                    print('Yo elegi tijera')
                                else: # Ga == 3, Casa: Piedra
                                    resultado = "empate"
                                    print('Yo elegi piedra')
                            
                            # Opción 2: Jugador Tijera
                            elif Op == '2':
                                print('Elejiste tijeras')
                                if Ga == 1: # Casa: Piedra
                                    resultado = "pierde"
                                    print('Yo elegi piedra')
                                elif Ga == 2: # Casa: Papel
                                    resultado = "gana"
                                    print('Yo elegi papel')
                                else: # Ga == 3, Casa: Tijera
                                    resultado = "empate"
                                    print('Yo elegi tijera')
                                    
                            # Opción 3: Jugador Papel
                            elif Op == '3':
                                print('Elejiste papel')
                                if Ga == 1: # Casa: Tijera
                                    resultado = "pierde"
                                    print('Yo elegi tijera')
                                elif Ga == 2: # Casa: Piedra
                                    resultado = "gana"
                                    print('Yo elegi piedra')
                                else: # Ga == 3, Casa: Papel
                                    resultado = "empate"
                                    print('Yo elegi papel')
                            
                            # De Otro Modo: (Opción inválida)
                            else:
                                print('==================================')
                                print('Ingresaste un numero invalido')
                                print(':(')
                                print('Intentalo de nuevo')
                                print('===================================')
                                print('-----Enter para continuar----')
                                print('==================================')
                                input() # Simula Leer ok
                                continue # Volver al inicio del ciclo Buc
                                
                            print('============================')
                            
                            # Mostrar resultados y actualizar dinero
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

                            # Si pierde o se queda sin dinero
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
                        # Carrera de caballos
                        buc3 = "s"
                        # Selección de caballo
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
                                input() # Simula Leer ok
                                os.system("cls")
                                buc3 = "s"
                                
                        # Monto a apostar
                        
                                print(f'Ingresa el monto a apostar: mínimo $1, máximo ${dinero:.2f}') # [cite: 80]
                                print('--------------------------------------------------------')
                                Apuesta = float(input())
                        
                        
                        # Simulación de la carrera (se reproduce la lógica de impresión del original)
                        
                        # --- Etapa 1
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
                        
                        # --- Etapa 2 (Los prints simulan el avance de los caballos)
                        if NUm == 1:
                            # Posición: 2, 1, 3
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
                             # Posición: 3, 2, 1
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
                        input() # Simula Leer KI
                        NUm = random.randint(1, 3)
                        os.system("cls")
                        
                        # --- Etapa 3
                        if NUm == 1:
                            # Posición: 3, 1, 2
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
                            # Posición: 1, 3, 2
                            print('------------------------------------|\__--------------------------')
                            print('----------------------------- ______|´ |)------------------------')
                            print('-----------------------------/  |1| /--------------------------') 
                            print(' ----------------------------------------------------|\__--------')
                            print('-----------------------------------------------______|´ |)-------')
                            print('----------------------------------------------/  |3|   /---------')
                            print('------------------------|\__-------------------------------------')
                            print('----------------- ______|´ |)------------------------------------')
                            print('-----------------/  |2| /--------------------------------------') 
                        else: # NUm == 3
                            # Posición: 1, 3, 2 (repetido en el original)
                            print('------------------------------------|\__--------------------------')
                            print('----------------------------- ______|´ |)------------------------')
                            print('-----------------------------/  |1| /--------------------------') # [cite: 93]
                            print(' ----------------------------------------------------|\__--------')
                            print('-----------------------------------------------______|´ |)-------')
                            print('----------------------------------------------/  |3|   /---------')
                            print('------------------------|\__-------------------------------------')
                            print('----------------- ______|´ |)------------------------------------')
                            print('-----------------/  |2| /--------------------------------------') # [cite: 94]
                            
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() # Simula Leer KI
                        NUm = random.randint(1, 3)
                        os.system("cls")
                        
                        # --- Etapa Final (Meta)
                        Ganador_ID = 0
                        
                        if NUm == 1:
                            # Posición: 3, 2, 1 -> Ganador: 1 (Secretariat)
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
                            # Posición: 2, 1, 3 -> Ganador: 3 (Cigar)
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
                        else: # NUm == 3
                            # Posición: 1, 3, 2 -> Ganador: 2 (Justify)
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
                        input() # Simula Leer KI
                        os.system("cls")
                        
                        # --- Resultado de la carrera
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

                        # Si pierde o se queda sin dinero
                        if dinero <= 0:
                            print('Te quedaste sin dinero. Fin del juego.')
                            buc3 = "n"
                            Buc = 'n'
                            Bucle = 'n'
                            Juefo = 'n'
                        else:
                            print('Quieres seguir juegando? s/n') # [cite: 101, 102, 103, 104, 105, 106]
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
                                
                    # De Otro Modo: (Juego inválido)
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
                        
            # De Otro Modo: (Opción de actividad inválida)
            elif Bucle == "s":
                 print('==================================')
                 print('Ingresaste un numero invalido')
                 print(':(')
                 print('Intentalo de nuevo')
                 print('===================================')
                 print('-----Enter para continuar----')
                 print('==================================')
                 input() # Simula Leer ok
                 Bucle = 's'
                
        # Bloque de pago y factura
        os.system("cls")
        Descuento = 0.0
        TotalAPagar = TotalCO
        
        # Si TotalUni>=3 Entonces
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
