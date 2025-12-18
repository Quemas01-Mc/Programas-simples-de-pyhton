def sistema_de_descuentos():
    gasto = float(input("¿Cuánto fue su gasto total?: "))
    print("Seleccione su tipo de cliente:")
    print("1: VIP")
    print("2: Cliente normal")
    tipo_cliente = int(input("Ingrese su opción (1 o 2): "))
    descuento_aplicado = 0

    if tipo_cliente == 1:
        intentos = False
        while not intentos:
            Usuarios = ["Pedro", "juan"]
            Contraseñas = ["Pedro123", "juan123"]
            
            print("--- Validación de Usuario Premium ---")
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")

            if usuario in Usuarios and contraseña in Contraseñas :
                    print("Validación exitosa! Eres usuario Premium.")
                    descuento_aplicado = 0.20  
                    intentos = True
            else:
                print("El usuario no existe.")

            if intentos:
                print("¿Desea intentar de nuevo?")
                print("1. Sí   2. No")
                salir = input("Seleccione: ")
                if salir == "2":
                    print("Saliendo del ingreso VIP...")
                    intentos = True
    
    elif tipo_cliente == 2:
        print("Aplicando tarifa de cliente normal.")
        descuento_aplicado = 0.0  
    else:
        print("Opción no válida, se procesará sin descuento.")

    monto_descuento = gasto * descuento_aplicado
    total_final = gasto - monto_descuento

    print("-" * 30)
    print(f"Resumen de compra:")
    print(f"Gasto inicial: ${gasto:.2f}")
    print(f"Descuento aplicado: {descuento_aplicado * 100}% (-${monto_descuento:.2f})")
    print(f"Total a pagar: ${total_final:.2f}")
    print("-" * 30)

print("--- Bienvenido a la tienda  de  +++++++ ---")
sistema_de_descuentos()