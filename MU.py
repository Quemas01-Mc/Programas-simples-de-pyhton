import os
import random

numeros = "1234567890"
caracteres = ".,-/()¨ç´{}¿?*+!#@$%&Ç"
letras = "qwertyuiopasdfghjklñzxcvbnm"

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

    Hay_numeros = False
    Hay_caracteres = False
    Hay_letras_invalidas = False
    
    if Nombre == "":
        pass 
    else:
        for char in Nombre:
            for num in numeros:
                if char == num:
                    Hay_numeros = True
            for carac in caracteres:
                if char == carac:
                    Hay_caracteres = True
            

    if Nombre == "":
        print('==================================')
        print('El nombre no puede estar vacio.')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        continue
    elif Hay_numeros == True:
        print('==================================')
        print('Ingresaste numeros, solo se permiten letras y espacios')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        continue
    elif Hay_caracteres == True:
        print('==================================')
        print('Ingresaste caracteres especiales, solo se permiten letras y espacios')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        continue
    else:
        NombreVal = True
        break
    
Edad0 = 0 
while True:
    os.system("cls")
    print('=======================================')
    print(f'Hola {Nombre} ¿Qué edad tienes?') 
    print('---------------------------------------') 
    Edad = input("Ingrese su edad :  ")

    Hay_letras = False
    Hay_caracteres = False
    Es_valido = True

    if Edad == "":
        Es_valido = False
    else:
        for char in Edad:
            for let in letras:
                if char == let:
                    Hay_letras = True
            for carac in caracteres:
                if char == carac:
                    Hay_caracteres = True
            
    if Edad == "":
        print('==================================')
        print('La edad no puede estar vacia.')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        continue
    elif Hay_letras == True:
        print('==================================')
        print('Ingresaste letras, solo se permiten numeros')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
        continue
    elif Hay_caracteres == True:
        print('==================================')
        print('Ingresaste un caracteres, solo se permiten numeros')
        print(':(')
        print('Intentalo de nuevo')
        print('===================================')
        print('-----Enter para continuar----')
        print('==================================')
        input() 
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
        
        OpcionValida = False
        Opcion = ""
        while not OpcionValida:
            os.system("cls")
            print('=========== Menu ============') 
            print('1.Bar------------------------')
            print('2.Juegos---------------------')
            print('3.Salir----------------------')
            print('_____________________________')
            Opcion = input("Ingrese un numero 1,2 o 3 : ")
            os.system("cls")
            
            Hay_letras = False
            Hay_caracteres = False
            
            if Opcion == "":
                Hay_caracteres = True 
            else:
                for char in Opcion :
                    for let in letras:
                        if char == let:
                            Hay_letras = True
                    for carac in caracteres:
                        if char == carac:
                            Hay_caracteres = True
            
            if Hay_letras == True or Opcion == "":
                print('==================================')
                print('Ingresaste letras o esta vacio, solo se permiten numeros 1, 2 o 3')
                print(':(')
                print('Intentalo de nuevo')
                print('===================================')
                print('-----Enter para continuar----')
                print('==================================')
                input() 
                continue
            elif Hay_caracteres == True:
                print('==================================')
                print('Ingresaste caracteres especiales, solo se permiten numeros 1, 2 o 3')
                print(':(')
                print('Intentalo de nuevo')
                print('===================================')
                print('-----Enter para continuar----')
                print('==================================')
                input() 
                continue
            else:
                
                Opcion_int = int(Opcion)
                if Opcion_int == 1 or Opcion_int == 2 or Opcion_int == 3:
                    Opcion = Opcion_int
                    OpcionValida = True
                    break
                else:
                    print('==================================')
                    print('Ingresaste un numero invalido. Debe ser 1, 2 o 3.')
                    print(':(')
                    print('Intentalo de nuevo')
                    print('===================================')
                    print('-----Enter para continuar----')
                    print('==================================')
                    input() 
                    continue

        if Opcion == 1:      
            I = True 
            while I == True:
                os.system("cls")
                print('========= Menú de Licores =========')
                print('1. Martini .............. $ 2.10') 
                print('2. Negroni .............. $ 4.00') 
                print('3. Jugo de mora ......... $ 2.50') 
                print('===================================')
                print('¿Qué deseas comprar? (Ingresa 1, 2 o 3)')
                print('-----------------------------------') 
                print('Puedes ganar un descuento si superas una compra de mas de 3 bebidas')
                print('___________________________________________________________________')
                
                Comprar_str = input()
                
                
                Hay_letras_compra = False
                Hay_caracteres_compra = False
                
                if Comprar_str == "":
                    Hay_caracteres_compra = True 
                else:
                    for char in Comprar_str:
                        for let in letras:
                            if char == let:
                                Hay_letras_compra = True
                        for carac in caracteres:
                            if char == carac:
                                Hay_caracteres_compra = True
                
                if Comprar_str == "" or Hay_letras_compra or Hay_caracteres_compra:
                    print('==================================')
                    print('Ingresaste un valor invalido . Solo 1, 2 o 3.')
                    print(':(')
                    print('Intentalo de nuevo')
                    print('===================================')
                    print('-----Enter para continuar----')
                    print('==================================')
                    input() 
                    os.system("cls")
                    continue
                
                Comprar = int(Comprar_str)
                
                
                Costo = 0.0
                if Comprar == 1:
                    Costo = 2.10
                elif Comprar == 2:
                    Costo = 4.00
                elif Comprar == 3: 
                    Costo = 2.50
                else:
                    print('==================================')
                    print('Ingresaste un numero invalido. Debe ser 1, 2 o 3.')
                    print(':(')
                    print('Intentalo de nuevo')
                    print('===================================')
                    print('-----Enter para continuar----')
                    print('==================================')
                    input() 
                    os.system("cls")
                    continue

                
                os.system("cls")
                print(f'Qué buena elección {Nombre} ¿Cuánto deseas llevar?')
                print('--------------------------------------------------------') 
                
                
                Chi_str = input(": ")
                Hay_letras_cant = False
                Hay_caracteres_cant = False
                
                if Chi_str == "":
                    Hay_caracteres_cant = True 
                else:
                    for char in Chi_str:
                        for let in letras:
                            if char == let:
                                Hay_letras_cant = True
                        for carac in caracteres:
                            if char == carac:
                                Hay_caracteres_cant = True
                
                if Chi_str == "" or Hay_letras_cant or Hay_caracteres_cant:
                    print('==================================')
                    print('Ingresaste una cantidad invalida '
                          '. Solo números enteros.')
                    print(':(')
                    print('Intentalo de nuevo')
                    print('===================================')
                    print('-----Enter para continuar----')
                    print('==================================')
                    input() 
                    os.system("cls")
                    continue
                
                Chi = int(Chi_str)

                if Chi <= 0:
                    print('==================================')
                    print('La cantidad debe ser mayor a 0.')
                    print(':(')
                    print('Intentalo de nuevo')
                    print('===================================')
                    print('-----Enter para continuar----')
                    print('==================================')
                    input() 
                    os.system("cls")
                    continue
                
                
                Unidades = Chi 
                TotalUni = TotalUni + Unidades
                Total = Chi * Costo
                TotalCO = TotalCO + Total
                
                os.system("cls")
                print(f"Has añadido {Chi} unidades. Total acumulado en bar: ${TotalCO:.2f}")
                print('===================================================================')
                
                
                while True:
                    print('Quieres hacer algo mas antes de irte s/n')
                    print('------------------------------------------------------------')
                    print('s: Volver al menú de licores del Bar')
                    print('n: Ir al menú principal')
                    print('------------------------------------------------------------')
                    barOp = input("Escriba s/n : ")
                    
                    if barOp == "s":
                        I = True 
                        Bucle = True 
                        break
                    elif barOp == "n":
                        I = False 
                        break 
                    else:
                        print('==================================')
                        print('Ingresaste una opcion invalida. Solo "s" o "n".')
                        print(':(')
                        print('Intentalo de nuevo')
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        os.system("cls")
                        continue
            

        elif Opcion == 2:
            
            if DineroPa == 0:
                while True:
                    os.system("cls")
                    print(f'¿Cuánta plata quieres poner para apostar? {Nombre} (Solo números)')
                    print('---------------------------------------------------')
                    dinero_str = input()
                    
                    
                    Hay_letras_dinero = False
                    Hay_caracteres_dinero = False
                    
                    if dinero_str == "":
                        Hay_caracteres_dinero = True
                    else:
                        try:
                            dinero_val = float(dinero_str)
                            for char in dinero_str:
                                if char in letras:
                                    Hay_letras_dinero = True
                                if char in caracteres and char != '.':
                                    Hay_caracteres_dinero = True
                        except ValueError:
                            Hay_letras_dinero = True 
                            
                    
                    if dinero_str == "" or Hay_letras_dinero or Hay_caracteres_dinero:
                        print('==================================')
                        print('Ingresaste un valor invalido. Solo números.')
                        print(':(')
                        print('Intentalo de nuevo')
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        continue
                    
                    dinero = float(dinero_str)
                    if dinero <= 0:
                        print('==================================')
                        print('El dinero a apostar debe ser mayor a 0.')
                        print(':(')
                        print('Intentalo de nuevo')
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        continue
                    
                    DineroPa = dinero 
                    break

            Juefo = 's' 
            while Juefo == 's':
                os.system("cls")
                print('==========================')
                print(f'Tu saldo actual es de: ${dinero:.2f}')
                print('¿Qué quieres jugar?')
                print('======== Menú  ===========')
                print('1.Es par o impar----------')
                print('2.Piedra,Papel o Tijera---')
                print('3.Carrera de caballos-----')
                print('4.Volver al Menú Principal')
                print('__________________________')
                
                Juego_str = input("Elija 1, 2, 3 o 4: ")
                
                
                Hay_letras_juego = False
                Hay_caracteres_juego = False
                
                if Juego_str == "":
                    Hay_caracteres_juego = True
                else:
                    for char in Juego_str:
                        if char in letras:
                            Hay_letras_juego = True
                        if char in caracteres:
                            Hay_caracteres_juego = True
                
                if Juego_str == "" or Hay_letras_juego or Hay_caracteres_juego:
                    print('==================================')
                    print('Ingresaste un valor invalido. Solo números 1, 2, 3 o 4.')
                    print(':(')
                    print('Intentalo de nuevo')
                    print('===================================')
                    print('-----Enter para continuar----')
                    print('==================================')
                    input() 
                    continue
                
                Juego = int(Juego_str)

                
                if Juego == 4:
                    Juefo = 'n' 
                    Bucle = True 
                    continue

                
                if Juego in [1, 2, 3]:
                    
                    
                    LOP = "s"
                    Apuesta = 0.0
                    while LOP == "s":
                        os.system("cls")
                        print(f'Tu saldo es de: ${dinero:.2f}')
                        print('==========================')
                        print(f'Ingresa el monto a apostar: mínimo $1, máximo ${dinero:.2f}') 
                        print('=======================================================')
                        Apuesta_str = input()
                        
                        
                        Hay_letras_apuesta = False
                        Hay_caracteres_apuesta = False
                        
                        if Apuesta_str == "":
                            Hay_caracteres_apuesta = True
                        else:
                            try: 
                                Apuesta_val = float(Apuesta_str)
                                for char in Apuesta_str:
                                    if char in letras:
                                        Hay_letras_apuesta = True
                                    
                                    if char in caracteres and char != '.':
                                        Hay_caracteres_apuesta = True
                            except ValueError:
                                Hay_letras_apuesta = True 
                                
                        if Hay_letras_apuesta or Hay_caracteres_apuesta:
                            print('==================================')
                            print('Ingresaste un valor invalido. Solo números.')
                            print(':(')
                            print('Intentalo de nuevo')
                            print('===================================')
                            print('-----Enter para continuar----')
                            print('==================================')
                            input() 
                            continue
                        
                        Apuesta = float(Apuesta_str)
                        
                        if Apuesta <= dinero and Apuesta >= 1:
                            LOP = "n"
                        else:
                            print('==================================')
                            print('El monto de la apuesta es invalido. Debe ser mínimo $1 y no superar tu saldo.')
                            print(':(')
                            print('Intentalo de nuevo')
                            print('===================================')
                            print('-----Enter para continuar----')
                            print('==================================')
                            input() 
                            os.system("cls")
                            continue
                            
                    
                    if Juego == 1:
                        Buc = 's'
                        while Buc == 's':
                            os.system("cls")
                            print("===========================")
                            print('Bienvenido a es par o impar')
                            print('===========================')
                            print(f'Apostaste: ${Apuesta:.2f}')
                            print('Dime, ¿es par o impar?')
                            print('===========================')
                            print('1.Par')
                            print('2.Impar')
                            print('___________________________')
                            
                            PoI = input()
                            
                            
                            if PoI not in ['1', '2']:
                                print('==================================')
                                print('Ingresaste una opcion invalida. Solo 1 o 2.')
                                print(':(')
                                print('Intentalo de nuevo')
                                print('===================================')
                                print('-----Enter para continuar----')
                                print('==================================')
                                input() 
                                continue
                            
                            Elnumero = random.randint(1, 50)
                            es_par = Elnumero % 2 == 0
                            
                            os.system("cls")
                            
                            if PoI == '1': 
                                print('Escogiste par')
                                print('==============')
                                if es_par:
                                    print(f'El número fue par: {Elnumero}')
                                    print('Ganaste')
                                    dinero += Apuesta
                                    TotalGa += Apuesta 
                                else:
                                    print(f'El número fue impar: {Elnumero}')
                                    print('Perdiste')
                                    dinero -= Apuesta
                                    
                            elif PoI == '2': 
                                print('Escogiste impar')
                                print('===============')
                                if not es_par:
                                    print(f'El número fue impar: {Elnumero}')
                                    print('Ganaste')
                                    dinero += Apuesta
                                    TotalGa += Apuesta 
                                else:
                                    print(f'El número fue par: {Elnumero}')
                                    print('Perdiste')
                                    dinero -= Apuesta
                            
                            print('============================')
                            print(f'Tu saldo actual es: ${dinero:.2f}')
                            print('============================')
                            
                            if dinero <= 0:
                                print('Te quedaste sin dinero. Fin del juego.')
                                Buc = 'n'
                                Bucle = False
                                Juefo = 'n'
                            else:
                                print('¿Quieres seguir jugando Par o Impar? s/n') 
                                print('----------------------------')
                                Ele = input()
                                if Ele == 's':
                                    Buc = 's'
                                    if Apuesta > dinero:
                                        LOP = "s" 
                                        Buc = 'n' 
                                        Juefo = 's' 
                                    else:
                                        os.system("cls")
                                        pass
                                else:
                                    Buc = 'n'
                                    Juefo = 's' 
                                    os.system("cls")
                                    
                    
                    elif Juego == 2:
                        Buc = 's'
                        while Buc == 's':
                            os.system("cls")
                            print(f'Tu saldo es de: ${dinero:.2f}')
                            print('=========================')
                            print(f'Apostaste: ${Apuesta:.2f}')
                            print('===============')
                            print('Elije entre :')
                            print('===============')
                            print('1.Piedra------|')
                            print('2.Tijera------|') 
                            print('3.Papel-------|')
                            print('---------------')
                            
                            Op = input()
                            os.system("cls")
                            
                            
                            if Op not in ['1', '2', '3']:
                                print('==================================')
                                print('Ingresaste un numero invalido. Solo 1, 2 o 3.')
                                print(':(')
                                print('Intentalo de nuevo')
                                print('===================================')
                                print('-----Enter para continuar----')
                                print('==================================')
                                input() 
                                continue 
                                
                            Ga = random.randint(1, 3) 
                            
                            resultado = ""
                            
                            
                            if Op == '1': 
                                print('Elegiste piedra')
                                if Ga == 1: 
                                    resultado = "empate"
                                    print('Yo elegi piedra')
                                elif Ga == 2: 
                                    resultado = "gana"
                                    print('Yo elegi tijera')
                                else: 
                                    resultado = "pierde"
                                    print('Yo elegi papel')
                            
                            elif Op == '2': 
                                print('Elegiste tijeras')
                                if Ga == 1: 
                                    resultado = "pierde"
                                    print('Yo elegi piedra')
                                elif Ga == 2: 
                                    resultado = "empate"
                                    print('Yo elegi tijera')
                                else: 
                                    resultado = "gana"
                                    print('Yo elegi papel')
                                    
                            elif Op == '3': 
                                print('Elegiste papel')
                                if Ga == 1: 
                                    resultado = "gana"
                                    print('Yo elegi piedra')
                                elif Ga == 2: 
                                    resultado = "pierde"
                                    print('Yo elegi tijera')
                                else: 
                                    resultado = "empate"
                                    print('Yo elegi papel')
                            
                            
                            print('============================')
                            
                            
                            if resultado == "gana":
                                print('Tu ganaste')
                                dinero += Apuesta
                                TotalGa += Apuesta
                            elif resultado == "pierde":
                                print('Yo gane (La casa gana)')
                                dinero -= Apuesta
                            elif resultado == "empate":
                                print('Empate')
                                print('Nadie gana')
                                
                            print('============================')
                            print(f'Tu saldo actual es: ${dinero:.2f}')
                            print('============================')
                            
                            if dinero <= 0:
                                print('Te quedaste sin dinero. Fin del juego.')
                                Buc = 'n'
                                Bucle = False
                                Juefo = 'n'
                            else:
                                print('Quieres seguir jugando Piedra, Papel o Tijera? s/n')
                                print('----------------------------')
                                Ele = input()
                                
                                if Ele == 's':
                                    Buc = 's'
                                    if Apuesta > dinero:
                                        LOP = "s" 
                                        Buc = 'n' 
                                        Juefo = 's' 
                                else:
                                    Buc = 'n'
                                    Juefo = 's' 
                                    os.system("cls")
                                    
                    
                    elif Juego == 3:
                        
                        buc3 = "s"
                        
                        while buc3 == "s":
                            os.system("cls")
                            print("=============================")
                            print('A que caballo quieres apostar (1, 2, 3)')
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
                                print('Ingresaste un numero invalido. Solo 1, 2 o 3.')
                                print(':(')
                                print('Intentalo de nuevo')
                                print('===================================')
                                print('-----Enter para continuar----')
                                print('==================================')
                                input() 
                                buc3 = "s"
                                
                        
                        
                        os.system("cls")
                        print(f'Apostaste ${Apuesta:.2f} al caballo {NombreCA}')
                        print('Inicia la carrera...')
                        print('-----------------------------------')
                        
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
                        print('-----Enter para ver el avance 1----')
                        print('==================================')
                        input() 
                        
                        
                        NUm_final = random.randint(1, 3) 
                        Ganador_ID = NUm_final
                        
                        if Ganador_ID == 1:
                            Ganador_Nombre = "Secretariat"
                        elif Ganador_ID == 2:
                            Ganador_Nombre = "Justify"
                        else:
                            Ganador_Nombre = "Cigar"
                            
                        
                        os.system("cls")
                        print('--- Resultado Final ---')
                        
                        
                        print("========================")
                        print(f"El ganador fue {Ganador_Nombre}")
                        print("========================")
                        print(f"Tu escojiste a {NombreCA}")
                        print("========================")
                        
                        if ID == Ganador_ID:
                            print("Ganaste, felicidades")
                            dinero += Apuesta
                            TotalGa += Apuesta
                        else:
                            print(f'Perdiste ${Apuesta:.2f}')
                            dinero -= Apuesta
                            print('La casa gana')
                            
                        print('============================')
                        print(f'Tu saldo actual es: ${dinero:.2f}')
                        print('============================')

                        
                        if dinero <= 0:
                            print('Te quedaste sin dinero. Fin del juego.')
                            buc3 = "n"
                            Bucle = False
                            Juefo = 'n'
                        else:
                            print('Quieres seguir jugando Carreras? s/n') 
                            print('----------------------------')
                            Ele = input()
                            
                            if Ele == 's':
                                Juefo = "s" 
                                
                                if Apuesta > dinero:
                                        LOP = "s" 
                                        buc3 = 'n' 
                                        Juefo = 's' 
                                else:
                                    buc3 = "s" 
                                os.system("cls")
                            else:
                                buc3 = "n"
                                Juefo = 's' 
                                os.system("cls")
                                
                   
                    else: 
                        print('==================================')
                        print('Ingresaste un numero invalido. Debe ser 1, 2, 3 o 4.')
                        print(':(')
                        print('Intentalo de nuevo')
                        print('===================================')
                        print('-----Enter para continuar----')
                        print('==================================')
                        input() 
                        Juefo = 's' 
                
                else: 
                    print('==================================')
                    print('Ingresaste un numero invalido. Debe ser 1, 2, 3 o 4.')
                    print(':(')
                    print('Intentalo de nuevo')
                    print('===================================')
                    print('-----Enter para continuar----')
                    print('==================================')
                    input() 
                    Juefo = 's' 
        
        elif Opcion == 3:
            Bucle = False


    os.system("cls")
    Descuento = 0.0
    TotalAPagar = TotalCO
    
    
    if TotalUni >= 3:
        Descuento = TotalCO * 0.1
        TotalAPagar = TotalCO - Descuento 
        
    
    
    PagOP = "s"
    PagoET = ''
    while PagOP == "s":
        print(f'El total a pagar del bar es: ${TotalAPagar:.2f} (ya incluye descuento)')
        print('========================================')
        if DineroPa > 0:
            print(f'Tu saldo final de apuestas es ${dinero:.2f}')
            print(f'Total de dinero ganado : ${TotalGa:.2f}')
        print('=======================================')
        print('Como quieres pagar tu consumo del bar:')
        print('================================')
        print('1.Efectivo')
        print('2.Tarjeta')
        print('-------------------------------')
        Pago_str = input("Elija un numero de 1/2 : ")
        
        
        if Pago_str == '1':
            PagoET = 'Efectivo'
            PagOP = "n"
        elif Pago_str == '2':
            PagoET = 'Tarjeta'
            PagOP = "n"
        else:
            print('==================================')
            print('Ingresaste un numero invalido. Solo 1 o 2.')
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
    if TotalUni > 0:
        print(f'Productos: {TotalUni:.0f} bebidas ')
        print(f'Subtotal (Bebidas sin desc.): ${TotalCO:.2f}')
        if TotalUni >= 3:
            print(f'Descuento (10% por 3+ bebidas): ${Descuento:.2f}')
        print('------------------------------------')
        print(f'TOTAL A PAGAR (Bebidas): ${TotalAPagar:.2f}') 
        print(f'Método de Pago: {PagoET}')
    else:
        print('No se realizaron compras de bebidas.')
        
    print('=======================================')
    print('--------- Apuestas echas --------------')
    print(f"Dinero inicial para apostar : ${DineroPa:.2f}")
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