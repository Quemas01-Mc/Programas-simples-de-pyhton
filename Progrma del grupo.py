import os
import datetime
import random
citas = []   
control = {} 
citas_agendadas = 0

print("_________________________________")
print("---------- BIENVENIDO -----------")
print("---------------------------------")
print("- A la Agendación de Citas Médicas -") 
print("---------------------------------")
print("¿A qué nombre se realizará la cita médica?") 
print("_________________________________")
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
 print("_____________________________")
 Opciones_del_menu=int(input("Escribe un número: ")) 
 os.system("cls")
 if Opciones_del_menu == 1:
    print("RESERVACIÓN DE CITAS") 
    print("---------------------------------")
    print(f"Hola {Nombre_del_paciente}, ¿qué edad tienes?") 
    
    Edad=int(input("Ingrese su edad: "))
    while True:
     print("Elija el tipo de cita")
     print("1.Medicina general")
     print("2.Control medico")
     print("3.Revision de medicamentos")
     Especialidad=int(input(""))
     if Especialidad == 1 :
        Cita_de_paciente = "Medicina general"
        break
     if Especialidad == 2 :
        Cita_de_paciente = "Control medico"
        break
     if Especialidad == 3 :
        Cita_de_paciente = "Revision de medicamentos"
        break
     else:
        print('\n==================================')
        print(' Ingresaste un dato inválido (Cédula).') 
        print(':(')
        print('Inténtalo de nuevo.')
        print('===================================')
        print('----- Presiona ENTER para continuar ----')
        print('==================================')
        input()
        os.system("cls")
        continue 
    
    print("\n---------------------------------")
    print("¿Cuál es su motivo para agendar esta cita?") 
    Motivo=input("Motivo: ")
    while True:        
            print("\nIngrese su cédula:") 
            Cedula=input("Cédula: ")
            
            contador = 0
            for Numero in Cedula:
                contador+=1
            
            if contador == 10: 
                Hoy= datetime.datetime.now()
                
                print("\n--- AGENDAMIENTO DE FECHA ---")
                
                print("¿Qué día quiere su cita?")
                print(f"Ejemplo (Día actual): {Hoy.day:02d}")

                fecha_de_citaD=int(input("Día: "))
                
                
                print("\n¿Qué mes quiere su cita?")
                print(f"Ejemplo (Mes actual): {Hoy.month:02d}")
                
                fecha_de_citaM=int(input("Mes: "))

               
                if Hoy.day <= fecha_de_citaD and Hoy.month <= fecha_de_citaM:
                    print("\nDime a qué hora quieres tu cita (desde 8am hasta 15pm):") 
                    
                    hora_de_cita=int(input("Hora (Formato 24h): "))
                    if hora_de_cita >= 8 and hora_de_cita <= 15:
                        codigo = str(random.randint(10000, 99999))

                        cita = {
                     "codigo": codigo,
                     "nombre": Nombre_del_paciente,
                     "edad": Edad,
                     "Cita para ": Cita_de_paciente,
                     "motivo": Motivo,
                     "cedula": Cedula,
                     "dia": fecha_de_citaD,
                     "mes": fecha_de_citaM,
                     "hora": hora_de_cita,
                      
                    }
                        print("\n¡CITA AGENDADA CON ÉXITO!")
                        print(f"Código de cita: {codigo}")
                        print(f"Detalles: {fecha_de_citaD:02d}/{fecha_de_citaM:02d} a las {hora_de_cita:02d}:00.")
                        citas_agendadas =+1
                        citalis = "PENDIENTE"
                        input("\nENTER para volver al menú...")
                        break
                    else:
                        print('\n==================================')
                        print('Hora fuera del rango permitido (8 a 15).')
                        print('Inténtalo de nuevo.')
                        print('==================================')
                        input()
                        os.system("cls")
                        continue 
                else:
                    print('\n==================================')
                    print(' Fecha inválida o anterior a la actual.')
                    print('Inténtalo de nuevo.')
                    print('==================================')
                    input()
                    os.system("cls")
                    continue
            
            else:
                
                print('\n==================================')
                print(' Ingresaste un dato inválido (Cédula).') 
                print(':(')
                print('Inténtalo de nuevo.')
                print('===================================')
                print('----- Presiona ENTER para continuar ----')
                print('==================================')
                input()
                os.system("cls")
                continue 
 if Opciones_del_menu == 2:
    os.system("cls")
    print("===== LISTA DE CITAS AGENDADAS =====\n")
    if citas_agendadas == 0:
        print("No hay citas agendadas")
    else :
        print(f"Código: {codigo}")
        print(f"Nombre: {Nombre_del_paciente}")
        print(f"Fecha: {fecha_de_citaD}/{fecha_de_citaM} \nHora: {hora_de_cita}")
        print(f"Motivo: {Motivo}")
        print(f"Estado: {citalis}")
        print(f"Cita para : {Cita_de_paciente}")
        print(f"Cédula :{Cedula}")
        print("-------------------------------")
        input("\nENTER para regresar al menú...")     
 if Opciones_del_menu == 3:
    print("===== CONTROL DE CITA =====")
    Bucle_Codigo = "s"
    while Bucle_Codigo == "s":
     codigo = input("Ingrese el código de la cita: ")

    if codigo not in control:
        while True :
         print("Código no encontrado.")
         input("ENTER para continuar...")
         print("Quiere regresar al menu")
         print("1.Si")
         print("2.NO")
         Opciones_del_control=int(input("Ingrese un numero : 1/2  "))
         if Opciones_del_control == 1 :
             Bucle_menu = "s"
             Bucle_Codigo="n"
             break
         if Opciones_del_control == 2 :
             Bucle_menu = "n"
             Bucle_Codigo ="s"
             break
         else :
             print("Numero invalido")
             input("ENTER para continuar...")
    

    print("\nCita encontrada:")
    print(f"Nombre: {Nombre_del_paciente}")
    print(f"Fecha: {fecha_de_citaD}/{fecha_de_citaM}  Hora: {hora_de_cita}:00")
    print(f"Estado actual: {citalis}")

    print("\nCambiar estado a:")
    print("1. Realizada")
    print("2. Cancelada")
    print("3. Pendiente")

    opcion_cambio_de_estado = input("Seleccione estado: ")

    if opcion_cambio_de_estado == "1":
        citalis = "REALIZADA"
    elif opcion_cambio_de_estado == "2":
        citalis = "CANCELADA"
    elif opcion_cambio_de_estado == "3":
        citalis = "PENDIENTE"
    else:
        print("Opción no válida.")

    print("\nEstado actualizado.")
    input("ENTER para continuar...")
 if Opciones_del_menu == 4:
  print ("-------------------------------")
  print ("---- Historial Clínico ----")
  print ("-------------------------------")
  todos_los_historiales = ""

  def registrar_paciente():
    global todos_los_historiales

    print("---- REGISTRO DEL HISTORIAL ----")

    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    edad = input("Edad: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    sexo = input("Sexo: ")
    nacimiento = input("Fecha de nacimiento: ")

    motivo = input("Motivo de consulta: ")
    diagnostico = input("Diagnóstico: ")
    tratamiento = input("Tratamiento: ")
    alergias = input("Alergias: ")
    enfermedades = input("Enfermedades previas: ")
    cirugias = input("Cirugías: ")
    medicacion = input("Medicación actual: ")

    fecha = datetime.datetime.now().strftime("%d/%m/%Y")
    hora = datetime.datetime.now().strftime("%H:%M:%S")

    historial = "---- HISTORIAL MÉDICO ----"
    historial += "Fecha: " + fecha + "  Hora: " + hora + "\n"
    historial += "Nombre: " + nombre + "\n"
    historial += "Cédula: " + cedula + "\n"
    historial += "Edad: " + edad + "\n"
    historial += "Teléfono: " + telefono + "\n"
    historial += "Dirección: " + direccion + "\n"
    historial += "Sexo: " + sexo + "\n"
    historial += "Nacimiento: " + nacimiento + "\n"
    historial += "Motivo: " + motivo + "\n"
    historial += "Diagnóstico: " + diagnostico + "\n"
    historial += "Tratamiento: " + tratamiento + "\n"
    historial += "Alergias: " + alergias + "\n"
    historial += "Enfermedades previas: " + enfermedades + "\n"
    historial += "Cirugías: " + cirugias + "\n"
    historial += "Medicación actual: " + medicacion + "\n"
    historial += "------------------------------\n"

   
    todos_los_historiales = todos_los_historiales + historial

    print("\nHistorial guardado correctamente :3\n")


  def mostrar_historiales():
    if todos_los_historiales == "":
        print("\nNo hay historiales registrados.\n")
    else:
        print("\n===== TODOS LOS HISTORIALES =====\n")
        print(todos_los_historiales)


  def buscar_por_cedula():
    cedula = input("\nIngrese la cédula: ")

    if "Cédula: " + cedula in todos_los_historiales:
        print("\nEl paciente existe en los registros.\n")
    else:
        print("\nNo se encontró ningún paciente.\n")


  def cantidad_atendidos():
   
    conteo = todos_los_historiales.count("HISTORIAL MÉDICO")
    print("\nPacientes atendidos:", conteo, "\n")



while True:
    print("---- AGENDA MÉDICA ----")
    print("1. Registrar historial")
    print("2. Ver historiales")
    print("3. Buscar por cédula")
    print("4. Cantidad de pacientes")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar_paciente()
    elif opcion == "2":
        mostrar_historiales()
    elif opcion == "3":
        buscar_por_cedula()
    elif opcion == "4":
        cantidad_atendidos()
    elif opcion == "5":
        print("Saliendo... :3")
        break
    else:
        print("Opción inválida\n")


if Opciones_del_menu == 5:
    print()
