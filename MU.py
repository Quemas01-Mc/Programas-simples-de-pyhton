import os
import datetime
import random

# =======================================================
# 1. INICIALIZACIÓN GLOBAL (NECESARIO PARA GUARDAR DATOS)
# =======================================================

# Lista principal que almacenará TODOS los diccionarios de cita
citas_agendadas_lista = []
citas_agendadas = 0 
citalis = "PENDIENTE"

# Definiciones de caracteres para validación (Fuera de los bucles para mejor práctica)
LETRAS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMEROS = '0123456789'
CARACTERES_DECIMALES = '.,'

# Definición de mensajes de error de longitud (como solicitaste)
MENSAJE_EXCESO = "¡Error! Ingresaste más de diez números."
MENSAJE_DEFECTO = "¡Error! Ingresaste menos de diez números."

# =======================================================
# BUCLE PRINCIPAL DEL PROGRAMA (MENÚ)
# =======================================================

while True:
    os.system("cls")
    print("--- MENÚ PRINCIPAL ---")
    print("1. Reservación de citas")
    print("2. Ver lista de citas agendadas")
    print("3. Salir")
    Opciones_del_menu = input("Pon un número: ").strip()

    if not Opciones_del_menu.isdigit():
        os.system("cls")
        print('==================================')
        print('Ingresaste un dato inválido. Solo números (1, 2 o 3).') 
        print('====================================')
        input('--- Presiona ENTER para continuar --')
        continue

    Opciones_del_menu = int(Opciones_del_menu)

    if Opciones_del_menu == 1:
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
            Nombres_del_paciente = input("Nombres: ").strip()
            
            Hay_errores = False
            for Error in Nombres_del_paciente:
                if Error in NUMEROS:
                    Hay_errores = True
                    break
            
            if Hay_errores == True or len(Nombres_del_paciente) == 0:
                os.system("cls")
                print('==================================')
                print('Ingresaste números o el campo está vacío. Solo letras.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
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
            Apellidos_del_paciente = input("Apellidos: ").strip()
            
            Hay_errores = False
            for Error in Apellidos_del_paciente:
                if Error in NUMEROS:
                    Hay_errores = True
                    break
            
            if Hay_errores == True or len(Apellidos_del_paciente) == 0:
                os.system("cls")
                print('==================================')
                print('Ingresaste números o el campo está vacío. Solo letras.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
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
            Edad_input = input("Edad: ").strip()
            
            Hay_Caracteres = False
            Hay_Letras = False
            
            for Error in Edad_input:
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
                input('--- Presiona ENTER para continuar --')
                continue
            elif Hay_Letras == True:
                os.system("cls")
                print('==================================')
                print('Ingresaste letras, solo números.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
                continue
            elif len(Edad_input) == 0:
                os.system("cls")
                print('==================================')
                print('El campo de edad no puede estar vacío.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
                continue
            else:
                edad = int(Edad_input)
                if edad > 0 and edad < 120: # Límite superior razonable para edad
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
            Especialidad_input = input("Opción: ").strip()

            if not Especialidad_input.isdigit():
                 Especialidad = 0
            else:
                 Especialidad = int(Especialidad_input)

            if Especialidad == 1:
                Cita_de_paciente = "Medicina general"
                break
            elif Especialidad == 2:
                Cita_de_paciente = "Control medico"
                break
            elif Especialidad == 3:
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
        Motivo = input("Motivo: ").strip()

        # =======================================================
        # SOLICITUD DE CÉDULA (CON VALIDACIÓN DE LONGITUD DE 10)
        # =======================================================
        ci = False
        while not ci:
            os.system("cls") 
            print("------------------------------------------")
            print("Ingrese su cédula (debe tener 10 dígitos y solo números):") 
            print("__________________________________________")
            Cedula = input("Cédula: ").strip()
            
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
                print('==================================')
                print('La cédula solo debe contener números enteros, sin letras ni símbolos.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
                continue
            
            # Validación de longitud (exactamente 10)
            else:
                longitud = len(Cedula)
                
                if longitud == 10:
                    ci = True
                elif longitud < 10:
                    os.system("cls")
                    print('==================================')
                    print(MENSAJE_DEFECTO)
                    print(f"Faltan {10 - longitud} números.")
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue
                else: # longitud > 10
                    os.system("cls")
                    print('==================================')
                    print(MENSAJE_EXCESO)
                    print(f"Sobran {longitud - 10} números.")
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue
        
        # =======================================================
        # SOLICITUD DE FECHA (DÍA)
        # =======================================================
        Day_ct = False
        Hoy = datetime.datetime.now()
        Dia = 0
        while not Day_ct:
            os.system("cls")
            print("--- AGENDAMIENTO DE FECHA ---")
            print(f"Mes actual: {Hoy.month:02d}")
            print("¿Qué DÍA quiere su cita? (1-30)")
            print(f"Ejemplo (Día actual): {Hoy.day:02d}")
            fecha_de_citaD = input("Día: ").strip()
            
            # Validación de formato (Solo números)
            Hay_Carcteres = False
            Hay_Letras = False
            for Error in fecha_de_citaD:
                if Error in CARACTERES_DECIMALES or Error in LETRAS:
                    Hay_Carcteres = True
                    break

            if Hay_Carcteres or len(fecha_de_citaD) == 0:
                os.system("cls")
                print('==================================')
                print('Error: Ingrese solo números enteros para el día.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
                continue
            else:
                Dia = int(fecha_de_citaD)
                # Validación de rango (1 a 30)
                if Dia >= 1 and Dia <= 30:
                    Day_ct = True
                else:
                    os.system("cls")
                    print('==================================')
                    print(f'Ingresaste un día no existente ({Dia}). El rango debe ser entre 1 y 30.') 
                    print('====================================')
                    input('--- Presiona ENTER para continuar --')
                    continue
        
        # =======================================================
        # SOLICITUD DE FECHA (MES)
        # =======================================================
        Day_ct = False # Usamos la misma bandera, pero es mejor definir una nueva (Month_ct)
        Month_ct = False
        Mes = 0
        while not Month_ct:
            os.system("cls")
            print("--- AGENDAMIENTO DE FECHA ---")
            print("¿Qué MES quiere su cita? (1-12)")
            print(f"Ejemplo (Mes actual): {Hoy.month:02d}")
            fecha_de_citaM = input("Mes: ").strip()

            # Validación de formato (Solo números)
            Hay_Carcteres = False
            Hay_Letras = False
            for Error in fecha_de_citaM:
                if Error in CARACTERES_DECIMALES or Error in LETRAS:
                    Hay_Carcteres = True
                    break
                    
            if Hay_Carcteres or len(fecha_de_citaM) == 0:
                os.system("cls")
                print('==================================')
                print('Error: Ingrese solo números enteros para el mes.') 
                print('====================================')
                input('--- Presiona ENTER para continuar --')
                continue
            else:
                Mes = int(fecha_de_citaM)
                # Validación de rango (1 a 12)
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
        # SOLICITUD DE HORA
        # =======================================================
        Hora_ct = False
        Hora = 0
        while not Hora_ct:
            os.system("cls")
            print("--- AGENDAMIENTO DE HORA ---")
            print("Dime a qué HORA quieres tu cita (desde 8am hasta 15pm):") 
            hora_de_cita = input("Hora (Formato 24h): ").strip()

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
            else:
                 print(f"{clave}: {valor}")
                 
        input("\nENTER para volver al menú...")

    # =======================================================
    # 2. VER LISTA DE CITAS AGENDADAS
    # =======================================================
    elif Opciones_del_menu == 2:
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
                print(f"Fecha: {cita['Dia']:02d}/{cita['Mes']:02d} - Hora: {cita['Hora']:02d}:00")
                print(f"Estado: {cita['Estado']}")
                print("-------------------------------")
                
        input("\nENTER para regresar al menú...")