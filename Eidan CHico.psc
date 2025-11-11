Algoritmo Emco
	Limpiar Pantalla
	Escribir '::::::::::::::::::::::::::::'
	Escribir '--Bienvenido a la licorería--'
	Escribir '::::::::::::::::::::::::::::'
	Escribir '¿Qué edad tienes?'
	Escribir '::::::::::::::::::::::::::::'
	Leer edad
	Escribir '::::::::::::::::::::::::::::'
	Escribir '¿Cual es tu nombre?'
	Leer Nombre
	Limpiar Pantalla
	Si edad>=18 Entonces
		Bucle="s"
		Mientras Bucle="s" Hacer
		Escribir '¿Qué quieres hacer hoy?'
		Escribir '::::::::::::Menu::::::::::::'
		Escribir '1.Dulces y Licores'
		Escribir '2.Juegos'
		Escribir '::::::::::::::::::::::::::::'
		Leer Opcion
		Limpiar Pantalla
		Según Opcion Hacer
			1:
				I <- 's'
				Mientras I='s' Hacer
					Escribir ':::::::::Menú:::::::::::'
					Escribir '1.Gomitas.........$1.10'
					Escribir '2.Whisky.............$4'
					Escribir '3.Pilsener........$2.50'
					Escribir ':::::::::::::::::::::::'
					Escribir '¿Qué deseas comprar?'
					Escribir ':::::::::::::::::::::::'
					Leer Comprar
					Limpiar Pantalla
					Según Comprar Hacer
						1:
							Escribir 'Qué buena elección  ', Nombre, '  ¿Cuánto deseas llevar?'
							Escribir '::::::::::::::::::::::::::::::::::::::::'
							Leer Gom
							Si Gom>=30 Entonces
								Limpiar Pantalla
								Total <- Gom*1.10
								Descuento <- Total*0.1
								Td <- Total-Descuento
								Escribir 'Acabas de ganar un descuento ', Nombre
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'El total a pagar es: $', Td
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Como quieres pagar :'
								Escribir '::::::::::::::::::::::::::::'
								Escribir '1.Efectivo'
								Escribir '2.Targeta'
								Escribir '::::::::::::::::::::::::::::'
								Leer Pago
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Gracias por su compra'
								Bucle="n"
							SiNo
								Limpiar Pantalla
								Total <- Gom*1.10
								Escribir 'El total a pagar es:  $', Total
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Como quieres pagar :'
								Escribir '::::::::::::::::::::::::::::'
								Escribir '1.Efectivo'
								Escribir '2.Targeta'
								Escribir '::::::::::::::::::::::::::::'
								Leer Pago
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Gracias por su compra'
								Bucle="n"
							FinSi
							I <- 'n'
						2:
							Escribir 'Qué buena elección  ', Nombre, '  ¿Cuánto deseas llevar?'
							Escribir '::::::::::::::::::::::::::::::::::::::::'
							Leer Cho
							Si Cho>=30 Entonces
								Limpiar Pantalla
								Total <- Cho*4
								Descuento <- Total*0.1
								Td <- Total-Descuento
								Escribir 'Acabas de ganar un descuento ', Nombre
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'El total a pagar es: $', Td
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Como quieres pagar :'
								Escribir '::::::::::::::::::::::::::::'
								Escribir '1.Efectivo'
								Escribir '2.Targeta'
								Escribir '::::::::::::::::::::::::::::'
								Leer Pago
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Gracias por su compra'
								Bucle="n"
							SiNo
								Limpiar Pantalla
								Total <- Cho*4
								Escribir 'El total a pagar es:  $', Total
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Como quieres pagar :'
								Escribir '::::::::::::::::::::::::::::'
								Escribir '1.Efectivo'
								Escribir '2.Targeta'
								Escribir '::::::::::::::::::::::::::::'
								Leer Pago
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Gracias por su compra'
								Bucle="n"
							FinSi
							I <- 'n'
						3:
							Escribir 'Qué buena elección  ', Nombre, '  ¿Cuánto deseas llevar?'
							Escribir '::::::::::::::::::::::::::::::::::::::::'
							Leer Chi
							Si Chi>=30 Entonces
								Limpiar Pantalla
								Total <- Chi*2.50
								Descuento <- Total*0.1
								Td <- Total-Descuento
								Escribir 'Acabas de ganar un descuento ', Nombre
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'El total a pagar es: $', Td
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Como quieres pagar :'
								Escribir '::::::::::::::::::::::::::::'
								Escribir '1.Efectivo'
								Escribir '2.Targeta'
								Escribir '::::::::::::::::::::::::::::'
								Leer Pago
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Gracias por su compra'
								Bucle="n"
							SiNo
								Limpiar Pantalla
								Total <- Chi*2.50
								Escribir 'El total a pagar es:  $', Total
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Como quieres pagar :'
								Escribir '::::::::::::::::::::::::::::'
								Escribir '1.Efectivo'
								Escribir '2.Targeta'
								Escribir '::::::::::::::::::::::::::::'
								Leer Pago
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'Gracias por su compra'
								Bucle="n"
							FinSi
							I <- 'n'
						De Otro Modo:
							Escribir 'Pusiste mal el número, intenta otra vez'
							I <- 's'
					FinSegún
				FinMientras
			2:
				Escribir '¿Cuánta plata quieres poner para apostar? ', Nombre
				Escribir ':::::::::::::::::::::::::::::::::::::::'
				Leer dinero
				Juefo="s"
				Mientras Juefo="s" Hacer
				Escribir ':::::::::::::::::::::::'
				Escribir '¿Qué quieres jugar?'
				Escribir '::::::::Menú:::::::::::::'
				Escribir '1.Es par o impar'
				Escribir ':::::::::::::::::::::::'
				Leer Juego
				Limpiar Pantalla
				Según Juego Hacer
					1:
						Buc <- 's'
						Mientras Buc='s' Hacer
							Escribir 'Tu saldo es de: $', dinero
							Escribir '::::::::::::::::::::::::::::'
							Repetir
								Escribir 'Ingresa el monto a apostar: mínimo $1, máximo $', dinero
								Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::'
								Leer Apuesta
							Hasta Que Apuesta>=1 Y Apuesta<=dinero
							Escribir 'Bienvenido a es par o impar'
							Escribir ':::::::::::::::::::::::::::'
							Escribir 'Ya tengo el número pensado'
							Escribir ':::::::::::::::::::::::::::'
							Escribir 'Dime, ¿es par o impar?'
							Escribir ':::::::::::::::::::::::::::'
							Escribir '1.Par'
							Escribir '2.Impar'
							Escribir ':::::::::::::::::::::::::::'
							Leer PoI
							Según PoI Hacer
								1:
									Escribir 'Escogiste par'
									Escribir ':::::::::::::::'
									Elnumero <- Aleatorio(1,50)
									Si Elnumero MOD 2==0 Entonces
										Escribir 'El número fue par: ', Elnumero
										Escribir 'Ganaste'
										dinero <- Apuesta+dinero
										Escribir 'Ganaste en total: $', dinero
										Escribir ':::::::::::::::::::::'
										Escribir '¿Quieres seguir jugando? s/n'
										Escribir '::::::::::::::::::::::::::::::'
										Leer Ele
										Si Ele='s' Entonces
											Buc <- 's'
											Limpiar Pantalla
										SiNo
											Escribir ':::::::::::::::::::::::::::::::::'
											Escribir 'Te retiras con el total de $ ', dinero
											Escribir ':::::::::::::::::::::::::::::::::'
											Buc <- 'n'
											Bucle="n"
											Juefo="n"
										FinSi
									SiNo
										Escribir 'El número fue impar: ', Elnumero
										Escribir '::::::::::::::::::::::::::::::'
										Escribir 'Perdiste $', Apuesta
										Escribir '::::::::::::::::::::::::::::::'
										dinero <- dinero-Apuesta
										Escribir 'Te quedas con $', dinero
										Escribir '::::::::::::::::::::::::::::::'
										Escribir 'La casa gana'
										Escribir '::::::::::::::::::::::::::::::'
										Si dinero=0 Entonces
											Buc <- 'n'
											Bucle="n"
											Juefo="n"
										SiNo
											Escribir '¿Quieres seguir jugando? s/n'
											Escribir '::::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
												Limpiar Pantalla
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::'
												Escribir 'Te retiras con el total de $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::'
												Buc <- 'n'
												Bucle="n"
												Juefo="n"
											FinSi
										FinSi
									FinSi
								2:
									Escribir 'Escogiste impar'
									Escribir ':::::::::::::::'
									Elnumero <- Aleatorio(1,50)
									Si Elnumero MOD 2==0 Entonces
										Escribir 'El número fue par: ', Elnumero
										Escribir '::::::::::::::::::::::::::::::'
										Escribir 'Perdiste $', Apuesta
										Escribir '::::::::::::::::::::::::::::::'
										dinero <- dinero-Apuesta
										Escribir 'Te quedas con $', dinero
										Escribir '::::::::::::::::::::::::::::::'
										Escribir 'La casa gana'
										Escribir '::::::::::::::::::::::::::::::'
										Si dinero=0 Entonces
											Buc <- 'n'
											Bucle="n"
											Juefo="n"
										SiNo
											Escribir '¿Quieres seguir jugando? s/n'
											Escribir '::::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
												Limpiar Pantalla
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::'
												Escribir 'Te retiras con el total de $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::'
												Buc <- 'n'
												Bucle="n"
												Juefo="n"
											FinSi
										FinSi
									SiNo
										Escribir 'El número fue impar: ', Elnumero
										dinero <- Apuesta+dinero
										Escribir 'Ganaste en total: $', dinero
										Escribir ':::::::::::::::::::::'
										Escribir '¿Quieres seguir jugando? s/n'
										Escribir '::::::::::::::::::::::::::::::'
										Leer Ele
										Si Ele='s' Entonces
											Buc <- 's'
											Limpiar Pantalla
										SiNo
											Escribir ':::::::::::::::::::::::::::::::::'
											Escribir 'Te retiras con el total de $ ', dinero
											Escribir ':::::::::::::::::::::::::::::::::'
											Buc <- 'n'
											Bucle="n"
											Juefo="n"
										FinSi
									FinSi
								De Otro Modo:
									Escribir 'Pusiste mal el número, intenta de nuevo'
									Buc <- 's'
							FinSegún
						FinMientras
					De Otro Modo:
						Escribir 'Pusiste mal el número, intenta de nuevo'
						Juefo="s"
				FinSegún
			FinMientras	
			De Otro Modo:
				Escribir 'Pusiste mal el número, intenta otra vez'
				Bucle="s"
		FinSegún
	     FinMientras
		Escribir '::::::::::::::::::::::'
		Escribir 'Esperamos su regreso ', Nombre
	SiNo
		Escribir 'Lo siento, pero no tienes la edad necesaria para ingresar'
	FinSi
FinAlgoritmo
