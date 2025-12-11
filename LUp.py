import os
import datetime
import random

# Lista principal que almacenará TODOS los diccionarios de cita
citas_agendadas_lista = []
citas_agendadas = 0 
citalis = "PENDIENTE"
Hoy = datetime.datetime.now()

# Definiciones de caracteres para validación 
LETRAS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMEROS = '0123456789'
CARACTERES_DECIMALES = ".,!#$%&'()*+,-./:;<=>?@[\]^_`{|}"

# Variables globales para el historial clínico/reportes
todosloshistoriales = ""
pacientes = []

print("___________")
print("---------- BIENVENIDO -----------")
print("---------------------------------")
print("- A la Agendación de Citas Médicas -")
print("---------------------------------")
print("¿A qué nombre se realizará la cita médica?")
Nombre_del_paciente=input("Ingrese el nombre: ")
os.system("cls")
Bucle_menu="s"
while Bucle_menu == "s":
    print(f"Hola {Nombre_del_paciente}, ¿qué opción deseas?")
    print("----------- MENÚ -------------")
    print("1. Reservar cita")
    print("2. Ver cita")
    print("3. Control de cita")
    print("4. Historial clínico")
    print("5. Reportes")
    print("___________")
    Opciones_menu=int(input("Escribe un número: "))
    os.system("cls")
    if Opciones_menu == 1:
        # =======================================================
        # SOLICITUD DE NOMBRES
        # =======================================================
        Validacion = False
        while not Validacion:
            os.system("cls")
            print("RESERVACIÓN DE CITAS") 
            print("---------------------------------")
            print("¿Cuáles son tus dos nombres?") 
            print("Ejemplo : Juan José")
            print("_________________________________")
            Nombres_del_paciente = input("Nombres: ")
            
            Hay_errores = False
            Hay_Caracteres = False
            for Error in Nombres_del_paciente:
                if Error in NUMEROS:
                    Hay_errores = True
                    break
                elif Error in CARACTERES_DECIMALES:
                    Hay_Caracteres = True
                    break

            if Hay_errores == True or Nombres_del_paciente == "" :
                os.system("cls")
                print('======================================================')
                print('Ingresaste números o el campo está vacío. Solo letras.') 
                print('======================================================')
                input('---------- Presiona ENTER para continuar -------------')
                continue
            elif Hay_Caracteres == True:
                os.system("cls")
                print('==================================')
                print('Ingresaste decimales, solo letras.') 
                print('====================================')
                input('-- Presiona ENTER para continuar --')
                continue
            else:
                Validacion = True
        
        # =======================================================
        # SOLICITUD DE APELLIDOS
        # =======================================================
        Validacion = False
        while not Validacion:
            os.system("cls")
            print("---------------------------------")
            print("¿Cuáles son sus apellidos?")
            print("Ejemplo : García López")
            print("_________________________________")
            Apellidos_del_paciente = input("Apellidos: ")
            Hay_Caracteres = False
            Hay_errores = False
            for Error in Apellidos_del_paciente:
                if Error in NUMEROS:
                    Hay_errores = True
                    break
                elif Error in CARACTERES_DECIMALES:
                    Hay_Caracteres = True
                    break
            if Hay_errores == True or Apellidos_del_paciente == "":
                os.system("cls")
                print('======================================================')
                print('Ingresaste números o el campo está vacío. Solo letras.') 
                print('======================================================')
                input('----------- Presiona ENTER para continuar ------------')
                continue
            elif Hay_Caracteres == True:
                os.system("cls")
                print('==================================')
                print('Ingresaste decimales, solo letras.') 
                print('====================================')
                input('-- Presiona ENTER para continuar --')
                continue
            else:
                Validacion = True

        # =======================================================
        # SOLICITUD DE EDAD
        # =======================================================
        Edad_valida = False
        edad = 0
        while not Edad_valida:
            os.system("cls")
            print("---------------------------------")
            print("¿Cuántos años tienes?")
            print("Ejemplo : 18")
            print("_________________________________")
            Edad = input("Edad: ")
            
            Hay_Caracteres = False
            Hay_Letras = False
            
            for Error in Edad:
                if Error in CARACTERES_DECIMALES:
                    Hay_Caracteres = True
                    break
                elif Error in LETRAS:
                    Hay_Letras = True
                    break
            
            if Hay_Caracteres == True:
                os.system("cls")
                print('==================================')
                print('Ingresaste decimales, solo enteros.') 
                print('====================================')
                input('-- Presiona ENTER para continuar --')
                continue
            elif Hay_Letras == True:
                os.system("cls")
                print('==================================')
                print('Ingresaste letras, solo números.') 
                print('====================================')
                input('-- Presiona ENTER para continuar --')
                continue
            elif Edad == "":
                os.system("cls")
                print('==================================')
                print('El campo de edad no puede estar vacío.') 
                print('====================================')
                input('-- Presiona ENTER para continuar --')
                continue
            else:
                edad = int(Edad)
                if edad > 0 and edad < 120: 
                    Edad_valida = True
                else:
                    os.system("cls")
                    print('==================================')
                    print('Ingresaste una edad inválida (debe ser positiva y real).') 
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue
            
        # =======================================================
        # SOLICITUD DE ESPECIALIDAD DE CITA
        # =======================================================
        while True:
            os.system("cls")
            print("---------------------------------")
            print("Elija el tipo de cita")
            print("1. Medicina general")
            print("2. Control medico")
            print("3. Revision de medicamentos")
            print("__________________________________")
            Especialidad = input("Opción: ")
            
            Hay_Caracteres = False
            Hay_Letras = False
            
            for Error in Especialidad:
                if Error in CARACTERES_DECIMALES:
                    Hay_Caracteres = True
                    break
                elif Error in LETRAS:
                    Hay_Letras = True
                    break

            if Hay_Caracteres == True:
                os.system("cls")
                print('==================================')
                print('Ingresaste decimales, solo enteros.') 
                print('====================================')
                input('-- Presiona ENTER para continuar --')
                continue
            elif Hay_Letras == True:
                os.system("cls")
                print('==================================')
                print('Ingresaste letras, solo números.') 
                print('====================================')
                input('-- Presiona ENTER para continuar --')
                continue
            elif Especialidad == "":
                os.system("cls")
                print('==================================')
                print('El campo de edad no puede estar vacío.') 
                print('====================================')
                input('-- Presiona ENTER para continuar --')
                continue
            else:
                Opcion_de_Especialida = int(Especialidad)
                if Opcion_de_Especialida == 1:
                    Cita_de_paciente = "Medicina general"
                    break
                elif Opcion_de_Especialida == 2:
                    Cita_de_paciente = "Control medico"
                    break
                elif Opcion_de_Especialida == 3:
                    Cita_de_paciente = "Revision de medicamentos"
                    break
                else:
                    os.system("cls")
                    print('==================================')
                    print('Ingresaste un dato inválido. Elige 1, 2 o 3.') 
                    print('====================================')
                    input('-- Presiona ENTER para continuar --')
                    continue 

        # =======================================================
        # SOLICITUD DE MOTIVO
        # =======================================================
        os.system("cls")
        print("------------------------------------------")
        print("¿Cuál es su motivo para agendar esta cita?")
        print("__________________________________________") 
        Motivo = input("Motivo: ")

        # =======================================================
        # SOLICITUD DE CÉDULA (CON VALIDACIÓN DE LONGITUD DE 10)
        # =======================================================
        ci = False
        while not ci:
            os.system("cls") 
            print("------------------------------------------")
            print("Ingrese su cédula (debe tener 10 dígitos y solo números):") 
            print("__________________________________________")
            Cedula = input("Cédula: ")
            
            Hay_Caracteres = False
            Hay_Letras = False
            
            # Validación de formato (solo números)
            for Error in Cedula:
                if Error in CARACTERES_DECIMALES:
                    Hay_Caracteres = True
                    break
                elif Error in LETRAS:
                    Hay_Letras = True
                    break 
                    
            if Hay_Caracteres or Hay_Letras:
                os.system("cls")
                print('======================================================================')
                print('La cédula solo debe contener números enteros, sin letras ni símbolos.') 
                print('======================================================================')
                input('-------------- Presiona ENTER para continuar -------------------------')
                continue
            
            # Validación de longitud (exactamente 10)
            else:
                longitud = 0
                for Contador in Cedula:
                    longitud+=1
                
                if longitud == 10:
                    ci = True
                elif longitud < 10:
                    os.system("cls")
                    print('==================================')
                    print(" Ingresaste menos de diez números.")
                    print(f"Faltan {10 - longitud} números.")
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue
                else: # longitud > 10
                    os.system("cls")
                    print('==================================')
                    print("¡Error! Ingresaste más de diez números.")
                    print(f"Sobran {longitud - 10} números.")
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue
         #========================================================
        # SOLICITUD DE AÑO
        #========================================================
        Año_ct = False
        Año = 0
        while not Año_ct:
            os.system("cls")
            print("--- AGENDAMIENTO DE FECHA ---")
            print("--- Agendamiento de año  ---")
            print(f"Dime que año quieres tu cita (desde : {Hoy.year}) :") 
            Año_de_cita = input("Año : ")

            Hay_Carcteres = False
            Hay_Letras = False
            for Error in Año_de_cita:
                if Error in CARACTERES_DECIMALES or Error in LETRAS:
                    Hay_Carcteres = True
                    break
                    
            if Hay_Carcteres or Año_de_cita == "":
                os.system("cls")
                print('==================================')
                print('Ingrese solo números enteros para el año.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
                continue
            else:
                Año = int(Año_de_cita)
                # Validación de rango  del año actual asta el inifinito
                if Año >= Hoy.year :
                    Año_ct = True
                else :
                    os.system("cls")
                    print('==================================')
                    print(f'Ingrese un año valido desde ({Hoy.year}).') 
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue

        # =======================================================
        # SOLICITUD DE MES
        # =======================================================
        Month_ct = False
        Mes = 0
        while not Month_ct:
            os.system("cls")
            print("--- AGENDAMIENTO DE FECHA ---")
            print("¿Qué MES quiere su cita? (1-12)")
            print(f"Ejemplo (Mes actual): {Hoy.month:02d}")
            fecha_de_citaM = input("Mes: ")

            # Validación de formato (Solo números)
            Hay_Carcteres = False
            Hay_Letras = False
            for Error in fecha_de_citaM:
                if Error in CARACTERES_DECIMALES or Error in LETRAS:
                    Hay_Carcteres = True
                    break
                    
            if Hay_Carcteres == True or fecha_de_citaM == "":
                os.system("cls")
                print('==================================')
                print('Ingrese solo números enteros para el mes.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
                continue
            else:
                Mes = int(fecha_de_citaM)
                # Validación de rango (1 a 12)
                if Año == Hoy.year:
                    if Mes >= Hoy.month and Mes <= 12:
                        Month_ct = True
                    else:
                        os.system("cls")
                        print('==================================')
                        print(f'Ingresaste un Mes no posible ({Mes}). El rango debe ser entre {Hoy.month} y 12.') 
                        print('====================================')
                        input('--- Presiona ENTER para continuar --')
                        continue

                else:
                    if Mes >= 1 and Mes <= 12:
                        Month_ct = True
                    else:
                        os.system("cls")
                        print('==================================')
                        print(f'Ingresaste un Mes no existente ({Mes}). El rango debe ser entre 1 y 12.') 
                        print('====================================')
                        input('--- Presiona ENTER para continuar --')
                        continue

        # =======================================================
        # SOLICITUD DE DÍA
        # =======================================================
        Day_ct = False
        Dia = 0
        while not Day_ct:
            os.system("cls")
            print("--- AGENDAMIENTO DE DÍA ---")
            print(f"Mes actual: {Hoy.month:02d}")
            print("¿Qué día quiere su cita? (1-28)")
            print(f"Ejemplo (Día actual): {Hoy.day:02d}")
            fecha_de_citaD = input("Día: ")
            
            # Validación de formato (Solo números)
            Hay_Carcteres = False
            Hay_Letras = False
            for Error in fecha_de_citaD:
                if Error in CARACTERES_DECIMALES or Error in LETRAS:
                    Hay_Carcteres = True
                    break

            if Hay_Carcteres or fecha_de_citaD == "":
                os.system("cls")
                print('=================================================')
                print('    Ingrese solo números enteros para el día.    ') 
                print('=================================================')
                input('--------- Presiona ENTER para continuar ---------')
                continue
            else:
                Dia = int(fecha_de_citaD)
                # Validación de rango (1 a 30) - Se mantiene el 28 por la lógica original, pero se ajusta el mensaje
                if Dia >= 1 and Dia <= 28:
                    Day_ct = True
                else:
                    os.system("cls")
                    print('==================================')
                    print(f'Ingresaste un día no existente ({Dia}). El rango debe ser entre 1 y 28 (según la validación actual).') 
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue
        
        
        
        # =======================================================
        # SOLICITUD DE HORA
        # =======================================================
        Hora_ct = False
        Hora = 0
        while not Hora_ct:
            os.system("cls")
            print("--- AGENDAMIENTO DE HORA ---")
            print("Dime a qué hora quieres tu cita (desde 8am hasta 15pm):") 
            hora_de_cita = input("Hora (Formato 24h): ")

            # Validación de formato (Solo números)
            Hay_Carcteres = False
            Hay_Letras = False
            for Error in hora_de_cita:
                if Error in CARACTERES_DECIMALES or Error in LETRAS:
                    Hay_Carcteres = True
                    break

            if Hay_Carcteres or len(hora_de_cita) == 0:
                os.system("cls")
                print('==================================')
                print('Error: Ingrese solo números enteros para la hora.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
                continue
            else:
                Hora = int(hora_de_cita)
                # Validación de rango (8 a 15)
                if Hora >= 8 and Hora <= 15:
                    Hora_ct = True
                else:
                    os.system("cls")
                    print('==================================')
                    print('Hora fuera del rango permitido (8 a 15).')
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue

        # =======================================================
        # REGISTRO Y GUARDADO DE CITA
        # =======================================================
        codigo = str(random.randint(10000, 99999))
        
        cita = {
            "Codigo": codigo,
            "Nombre": Nombres_del_paciente,
            "Apellidos": Apellidos_del_paciente,
            "Edad": edad,
            "Cita para": Cita_de_paciente,
            "Motivo": Motivo,
            "Cedula": Cedula,
            "Dia": Dia,
            "Mes": Mes,
            "Año": Año, # Se agrega el año al diccionario de cita
            "Hora": Hora, 
            "Estado": "PENDIENTE",
        }
        
        # GUARDA LA CITA EN LA LISTA GLOBAL
        citas_agendadas_lista.append(cita)
        citas_agendadas += 1
        
        os.system("cls")
        print("¡CITA AGENDADA CON ÉXITO!")
        print(f"Código de cita: {codigo}")
        print("\n--- Detalles de la cita ---")
        for clave, valor in cita.items():
            # Formateo mejorado para Fecha y Hora
            if clave == "Dia" or clave == "Mes" or clave == "Hora":
                 print(f"{clave}: {valor:02d}")
            elif clave == "Año":
                print(f"{clave}: {valor}")
            else:
                 print(f"{clave}: {valor}")
                 
        input("\nENTER para volver al menú...")
    elif Opciones_menu == 2:
        # =======================================================
        # 2. VER LISTA DE CITAS AGENDADAS
        # =======================================================
        os.system("cls")
        print("===== LISTA DE CITAS AGENDADAS =====\n")
        
        if len(citas_agendadas_lista) == 0:
            print("No hay citas agendadas.")
        else:
            # Recorre la lista e imprime cada cita
            print(f"Total de citas: {citas_agendadas}")
            print("-------------------------------")
            
            for i, cita in enumerate(citas_agendadas_lista, 1):
                print(f"--- Cita #{i} (Código: {cita['Codigo']}) ---")
                print(f"Nombre: {cita['Nombre']} {cita['Apellidos']}")
                print(f"Edad: {cita['Edad']}")
                print(f"Cita para: {cita['Cita para']}")
                # Se ajusta la impresión de la fecha para incluir el Año
                print(f"Fecha: {cita['Dia']:02d}/{cita['Mes']:02d}/{cita['Año']} - Hora: {cita['Hora']:02d}:00")
                print(f"Estado: {cita['Estado']}")
                print("-------------------------------")
            
            input("\nENTER para regresar al menú...")
    elif Opciones_menu == 3:
        while True:
            os.system("cls")
            #------PARTE DE MATHIAS (Adaptada y unificada)
            print("\n===== CONTROL DE CITAS =====")
            print("1. Registrar una cita atendida")
            print("2. Cancelar una cita")
            print("3. Ver citas programadas")
            print("4. Volver al menú principal")
            op = input("Seleccione una opción: ")
        
            # Registrar cita atendida
            if op == "1":
                os.system("cls")
                if len(citas_agendadas_lista) == 0:
                    print("No hay citas programadas.")
                    input('\n--- Presiona ENTER para continuar ---')
                    continue

                print("\n--- Citas Programadas ---")
                for i, c in enumerate(citas_agendadas_lista):
                    # Se usa cita['Apellidos'] y la fecha completa
                    print(f"{i+1}. {c['Nombre']} -{c['Apellidos']} - {c['Cita para']} - {c['Dia']:02d}/{c['Mes']:02d}/{c['Año']} a las {c['Hora']:02d}:00")

                try:
                    num = int(input("Ingrese el número de la cita atendida: ")) - 1
                except ValueError:
                    print("Entrada inválida. Ingrese un número.")
                    input('\n--- Presiona ENTER para continuar ---')
                    continue


                if 0 <= num < len(citas_agendadas_lista):
                    cita_atendida = citas_agendadas_lista.pop(num)
                    # Se asume que cita['Nombre'] es el nombre del paciente
                    print(f"La cita de {cita_atendida['Nombre']} fue marcada como ATENDIDA y eliminada de programadas.")
                else:
                    print("Número inválido.")
                input('\n--- Presiona ENTER para continuar ---')

            # Cancelar cita
            elif op == "2":
                os.system("cls")
                if len(citas_agendadas_lista) == 0:
                    print("No hay citas programadas.")
                    input('\n--- Presiona ENTER para continuar ---')
                    continue

                print("\n--- Citas Programadas ---")
                for i, c in enumerate(citas_agendadas_lista):
                    # Se usa cita['Apellidos'] y la fecha completa
                    print(f"{i+1}. {c['Nombre']} -{c['Apellidos']} - {c['Cita para']} - {c['Dia']:02d}/{c['Mes']:02d}/{c['Año']} a las {c['Hora']:02d}:00")

                try:
                    num = int(input("Ingrese el número de la cita a cancelar: ")) - 1
                except ValueError:
                    print("Entrada inválida. Ingrese un número.")
                    input('\n--- Presiona ENTER para continuar ---')
                    continue

                if 0 <= num < len(citas_agendadas_lista):
                    cancelada = citas_agendadas_lista.pop(num)
                    # Se asume que cancelada['Nombre'] es el nombre del paciente
                    print(f"Cita de {cancelada['Nombre']} cancelada exitosamente.")
                else:
                    print("Número inválido.")
                input('\n--- Presiona ENTER para continuar ---')

            # Ver citas programadas
            elif op == "3":
                os.system("cls")
                if len(citas_agendadas_lista) == 0:
                    print("No hay citas.")
                else:
                    print("\n===== LISTA DE CITAS =====")
                    for i, c in enumerate(citas_agendadas_lista):
                        # Se usa cita['Apellidos'] y la fecha completa
                        print(f"{i+1}. {c['Nombre']} -{c['Apellidos']} - {c['Cita para']} - {c['Dia']:02d}/{c['Mes']:02d}/{c['Año']} a las {c['Hora']:02d}:00")
                input('\n--- Presiona ENTER para continuar ---')

            # Volver
            elif op == "4":
                os.system("cls")
                break

            else:
                os.system("cls")
                print("Opción no válida.")
                input('\n--- Presiona ENTER para continuar ---')


    elif Opciones_menu == 4:
        # Se mantienen las variables globales ya declaradas
        # todosloshistoriales = ""
        # pacientes = []   
        while True:
            os.system("cls")
            print("----------------------------------------------------")
            print("------ MENÚ PRINCIPAL HISTORIAL ------")
            print("1. Historial clínico (cliente)")
            print("2. Reportes y estadísticas (personal autorizado) - (Esta opción redirige al menú 5)")
            print("3. Salir")
            print("----------------------------------------------------")
            menu = input("Opción: ")

            if menu == "1":
                while True:
                    os.system("cls")
                    print("--------------------------------")
                    print("---- HISTORIAL CLÍNICO ----")
                    print("1. **Crear Historial (Desde Cita y Registrar Datos Clínicos)**") 
                    print("2. Ver historiales")
                    print("3. Buscar por cédula")
                    print("4. Cantidad de pacientes")
                    print("5. Volver al menú principal")
                    print("--------------------------------")

                    opcion = input("-- Opción: ")
                    os.system("cls")

                    if opcion == "1":
                        # =======================================================
                        # MODIFICACIÓN: Crear Historial desde Cita + Pedir Datos Clínicos
                        # =======================================================
                        if len(citas_agendadas_lista) == 0:
                            print("-- No hay citas agendadas para crear un historial --")
                            input('\n--- Presiona ENTER para continuar ---')
                            continue
                            
                        print("---------------------------------")
                        print("-- CREAR HISTORIAL DESDE CITA --")
                        print("-- (Se usarán datos de la cita y se solicitarán los datos clínicos) --") 
                        print("---------------------------------")
                        
                        codigo_buscado = input("Ingrese el CÓDIGO de la cita (5 dígitos) para crear el historial: ")
                        cita_encontrada = None
                        
                        for cita in citas_agendadas_lista:
                            if cita["Codigo"] == codigo_buscado:
                                cita_encontrada = cita
                                break
                        
                        if cita_encontrada is None:
                            print("-- Cita no encontrada. Verifique el código. --")
                            input('\n--- Presiona ENTER para continuar ---')
                            continue
                            
                        # Usar datos de la cita como base
                        nombre = cita_encontrada["Nombre"]
                        apellidos = cita_encontrada["Apellidos"]
                        cedula = str(cita_encontrada["Cedula"]) # Asegurar que es string
                        edad = str(cita_encontrada["Edad"]) # Asegurar que es string
                        motivo = cita_encontrada["Motivo"]
                        area_cita = cita_encontrada["Cita para"]

                        print("\n-- DATOS DE LA CITA OBTENIDOS --")
                        print(f"Nombre: {nombre} {apellidos}")
                        print(f"Cédula: {cedula}")
                        print(f"Edad: {edad}")
                        print(f"Motivo (Cita): {motivo}")
                        print(f"Tipo de Cita/Área: {area_cita}")
                        print("----------------------\n")
                        
                        # --- INICIO DE DATOS SOLICITADOS (RESTAURADOS) ---
                        print("-- INGRESE DATOS CLÍNICOS Y ADMINISTRATIVOS --")
                        telefono = input("Teléfono: ")
                        direccion = input("Dirección: ")

                        # Elección de Área Médica (similar a la lógica original)
                        print("\n---------------------------------")
                        print("Áreas Médicas (Seleccione la atendida):")
                        print("1. Medicina general")
                        print("2. Control medico")
                        print("3. Revision de medicamentos")
                        print("4. Otra")
                        print("---------------------------------")
                        area_op = input("Seleccione área: ")

                        if area_op == "1":
                            area = "Medicina general"
                        elif area_op == "2":
                            area = "Control medico"
                        elif area_op == "3":
                            area = "Revision de medicamentos"
                        else:
                            area = input("Especifique otra área: ")

                        diagnostico = input("Diagnóstico: ")
                        alergias = input("Alergias: ")
                        enfermedades = input("Enfermedades previas: ")
                        cirugias = input("Cirugías: ")
                        medicacion = input("Medicación actual: ")
                        # --- FIN DE DATOS SOLICITADOS (RESTAURADOS) ---


                        # Validación de cédula (ya validada en la cita)
                        if not (len(cedula) == 10 and cedula.isdigit()):
                            print("Error: la cédula debe tener 10 números (Error interno)")
                            input('\n--- Presiona ENTER para continuar ---')
                            continue

                        # Validación de edad (ya validada en la cita)
                        if edad.isdigit():
                            edad_num = int(edad)
                            if not (0 <= edad_num <= 120):
                                print("Error: edad inválida (Error interno)")
                                input('\n--- Presiona ENTER para continuar ---')
                                continue
                        else:
                            print("Error: edad inválida (Error interno)")
                            input('\n--- Presiona ENTER para continuar ---')
                            continue

                        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

                        historial = f"""
---------------------------------------
-- HISTORIAL REGISTRADO --
Código de Cita: {codigo_buscado}
Fecha: {fecha}
Nombre: {nombre} {apellidos}
Cédula: {cedula}
Edad: {edad}
Teléfono: {telefono}
Dirección: {direccion}
Motivo de Cita: {motivo}
Área de Atención: {area}
Diagnóstico: {diagnostico}
Alergias: {alergias}
Enfermedades previas: {enfermedades}
Cirugías: {cirugias}
Medicación actual: {medicacion}
---------------------------------------
"""

                        todosloshistoriales # Se usa global para modificar la variable fuera del scope local
                        todosloshistoriales += historial

                        pacientes # Se usa global para modificar la variable fuera del scope local
                        pacientes.append({
                            "cedula": cedula,
                            "nombre": nombre,
                            "apellidos": apellidos,
                            "edad": edad_num,
                            "area": area,
                            "diagnostico": diagnostico
                        })

                        print("-- Historial guardado correctamente --")
                        input('\n--- Presiona ENTER para continuar ---')

                    elif opcion == "2":
                        print("----------------------------")
                        print("-- MOSTRAR HISTORIALES --")
                        print("----------------------------")
                        if todosloshistoriales == "":
                            print("-- No hay historiales aún --")
                        else:
                            print(todosloshistoriales)
                        input('\n--- Presiona ENTER para continuar ---')

                    elif opcion == "3":
                        print("-------------------------")
                        print("-- BUSCAR POR CÉDULA --")
                        print("-------------------------")
                        buscar = input("Ingrese la cédula: ")
                        
                        # Búsqueda más precisa en la lista de pacientes, aunque el código original buscaba en la cadena
                        encontrado = False
                        if buscar in todosloshistoriales:
                            # Se mantiene la lógica original de búsqueda en la cadena, aunque es rudimentaria
                            partes = todosloshistoriales.split("---------------------------------------")
                            for h in partes:
                                # Se verifica que la cédula esté en la parte y que no sea una parte vacía
                                if buscar in h and h.strip() != "":
                                    print("---------------------------------------" + h + "---------------------------------------")
                                    encontrado = True
                        
                        if not encontrado:
                            print("-- No se encontró esa cédula --")
                        
                        input('\n--- Presiona ENTER para continuar ---')

                    elif opcion == "4":
                        cantidad = todosloshistoriales.count("-- HISTORIAL REGISTRADO --")
                        print(f"-- Total pacientes: {cantidad} --")
                        input('\n--- Presiona ENTER para continuar ---')

                    elif opcion == "5":
                        break

                    else:
                        print("-- Opción inválida --")
                        input('\n--- Presiona ENTER para continuar --')

            elif menu == "2":
                 # Simula volver al menú principal para que el flujo vaya a Opciones_menu=5
                Opciones_menu = 5
                break 

            elif menu == "3":
                # Rompe el bucle del menú 4 y regresa al principal.
                break 

            else:
                print("-- Opción inválida --")
                input('\n--- Presiona ENTER para continuar ---')

        # Si en el menú 4 se eligió la opción 2, se ejecuta el bloque 5
        if Opciones_menu == 5:
            os.system("cls")
            print("-------------------------------------------")
            print("--- ACCESO SOLO PERSONAL AUTORIZADO ---")
            print("-------------------------------------------")
            usuarios = {
              "admin": "admin123",
              "psico": "psico123",
              "enfer": "enfer123",
              "odonto": "odonto123"
            }

            user = input("Usuario: ")
            clave = input("Contraseña: ")

            if user not in usuarios or usuarios[user] != clave:
                os.system("cls")
                print("--------------------")
                print(" ACCESO DENEGADO ")
                print("--------------------")
                input('\n--- Presiona ENTER para continuar ---')
                continue # Vuelve al bucle del menú principal si falla el login
            
            os.system("cls")
            print("--------------------")
            print(" Acceso permitido ")
            print("--------------------")
            input('\n--- Presiona ENTER para continuar ---')
            while True:
                os.system("cls")
                print("------------------------------------")
                print("---- REPORTES Y ESTADÍSTICAS ----")
                print("------------------------------------")
                print("1. Pacientes por área")
                print("2. Diagnósticos registrados")
                print("3. Listado completo interno")
                print("4. Volver al menú principal")

                op = input("Opción: ")
                os.system("cls")

                if op == "1":
                    print("--------------------------")
                    print("-- PACIENTES POR ÁREA --")
                    print("--------------------------")
                    conteo = {}

                    for p in pacientes:
                        area = p["area"]
                        conteo[area] = conteo.get(area, 0) + 1

                    for area, cant in conteo.items():
                        print(f"{area}: {cant} pacientes")
                    input('\n--- Presiona ENTER para continuar ---')

                elif op == "2":
                    print("--------------------")
                    print("-- DIAGNÓSTICOS --")
                    print("--------------------")
                    diagnos = {}

                    for p in pacientes:
                        d = p["diagnostico"]
                        diagnos[d] = diagnos.get(d, 0) + 1

                    for d, cant in diagnos.items():
                        print(f"{d}: {cant} casos")
                    input('\n--- Presiona ENTER para continuar ---')

                elif op == "3":
                    print("-------------------------")
                    print("-- REGISTROS INTERNOS --")
                    print("-------------------------")
                    if len(pacientes) == 0:
                        print("--No hay registros aún --")
                    else:
                        for p in pacientes:
                            print(p)
                    input('\n--- Presiona ENTER para continuar ---')

                elif op == "4":
                    break

                else:
                    print("-- Opción inválida --")
                    input('\n--- Presiona ENTER para continuar ---')
    # Se añade la lógica del menú 5 aquí, por si se accede directamente desde el menú principal
    elif Opciones_menu == 5:
        os.system("cls")
        print("-------------------------------------------")
        print("--- ACCESO SOLO PERSONAL AUTORIZADO ---")
        print("-------------------------------------------")
        usuarios = {
          "admin": "admin123",
          "psico": "psico123",
          "enfer": "enfer123",
          "odonto": "odonto123"
        }

        user = input("Usuario: ")
        clave = input("Contraseña: ")

        if user not in usuarios or usuarios[user] != clave:
          os.system("cls")
          print("--------------------")
          print(" ACCESO DENEGADO ")
          print("--------------------")
          input('\n--- Presiona ENTER para continuar ---')
          continue
          
        os.system("cls")
        print("--------------------")
        print(" Acceso permitido ")
        print("--------------------")
        input('\n--- Presiona ENTER para continuar ---')
        while True:
          os.system("cls")
          print("------------------------------------")
          print("---- REPORTES Y ESTADÍSTICAS ----")
          print("------------------------------------")
          print("1. Pacientes por área")
          print("2. Diagnósticos registrados")
          print("3. Listado completo interno")
          print("4. Volver al menú principal")

          op = input("Opción: ")
          os.system("cls")

          if op == "1":
            print("--------------------------")
            print("-- PACIENTES POR ÁREA --")
            print("--------------------------")
            conteo = {}

            for p in pacientes:
                area = p["area"]
                conteo[area] = conteo.get(area, 0) + 1

            for area, cant in conteo.items():
                print(f"{area}: {cant} pacientes")
            input('\n--- Presiona ENTER para continuar ---')

          elif op == "2":
            print("--------------------")
            print("-- DIAGNÓSTICOS --")
            print("--------------------")
            diagnos = {}

            for p in pacientes:
                d = p["diagnostico"]
                diagnos[d] = diagnos.get(d, 0) + 1

            for d, cant in diagnos.items():
                print(f"{d}: {cant} casos")
            input('\n--- Presiona ENTER para continuar ---')

          elif op == "3":
            print("-------------------------")
            print("-- REGISTROS INTERNOS --")
            print("-------------------------")
            if len(pacientes) == 0:
                print("--No hay registros aún --")
            else:
                for p in pacientes:
                    print(p)
            input('\n--- Presiona ENTER para continuar ---')

          elif op == "4":
            break

          else:
            print("-- Opción inválida --")
            input('\n--- Presiona ENTER para continuar ---')
    # Se añade un else para opciones de menú inválidas
    else:
        os.system("cls")
        print("Opción de menú no válida. Ingrese un número del 1 al 5.")
        input('\n--- Presiona ENTER para continuar ---')