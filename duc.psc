Algoritmo Licoreria
	Limpiar Pantalla
	Escribir '::::::::::::::::::::::::::::'
	Escribir '--Bienvendio ala licoreria--'
	Escribir '::::::::::::::::::::::::::::'
	Escribir 'Que edad tienes ?'
	Escribir '::::::::::::::::::::::::::::'
	Leer edad
	Escribir '::::::::::::::::::::::::::::'
	Limpiar Pantalla
	Si edad>=18 Entonces
		Escribir 'Que quieres hacer hoy ?'
		Escribir '::::::::::::::::::::::::::::'
		Escribir '1.Dulces y Licores'
		Escribir '2.Juegos'
		Escribir '::::::::::::::::::::::::::::'
		Leer Opcion
		Limpiar Pantalla
		Según Opcion Hacer
			1:
				I <- 's'
				Mientras I='s' Hacer
					Escribir ':::::::::Menu:::::::::::'
					Escribir '1.Gomitas.........$1.10'
					Escribir '2.whisky.............$4'
					Escribir '3.Pilsener........$2.50'
					Escribir ':::::::::::::::::::::::'
					Escribir 'Que deseas comprar ?'
					Escribir ':::::::::::::::::::::::'
					Leer Comprar
					Limpiar Pantalla
					Según Comprar Hacer
						1:
							Escribir 'Que buena elecion cuanto deseas llevar ?'
							Escribir '::::::::::::::::::::::::::::::::::::::::'
							Leer Gom
							Si Gom>=30 Entonces
								Total <- Gom*1.10
								Descuento <- Total*0.1
								Td <- Total-Descuento
								Escribir 'Acaba de ganar un descuento'
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'El total a pagar es : $', Td
							SiNo
								Total <- Gom*1.10
								Escribir 'El total a pagar es :  $', Total
							FinSi
							I <- n
						2:
							Escribir 'Que buena elecion cuanto deseas llevar ?'
							Escribir '::::::::::::::::::::::::::::::::::::::::'
							Leer Cho
							Si Cho>=30 Entonces
								Total <- Cho*4
								Descuento <- Total*0.1
								Td <- Total-Descuento
								Escribir 'Acaba de ganar un descuento'
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'El total a pagar es : $', Td
							SiNo
								Total <- Cho*4
								Escribir 'El total a pagar es :  $', Total
							FinSi
							I <- n
						3:
							Escribir 'Que buena elecion cuanto deseas llevar ?'
							Escribir '::::::::::::::::::::::::::::::::::::::::'
							Leer Chi
							Si Chi>=30 Entonces
								Total <- Chi*2.50
								Descuento <- Total*0.1
								Td <- Total-Descuento
								Escribir 'Acaba de ganar un descuento'
								Escribir '::::::::::::::::::::::::::::'
								Escribir 'El total a pagar es : $', Td
							SiNo
								Total <- Chi*2.50
								Escribir 'El total a pagar es :  $', Total
							FinSi
							I <- n
						De Otro Modo:
							Escribir 'Puso mal el numero intente otra vez'
							I <- 's'
					FinSegún
				FinMientras
			2:
				Escribir 'Cuanta plata quieres poner para apostar'
				Escribir ':::::::::::::::::::::::::::::::::::::::'
				Leer dinero
				Escribir ':::::::::::::::::::::::'
				Escribir 'Que quieres juegar ?'
				Escribir '::::::::Menu:::::::::::::'
				Escribir '1.Piedra,Papel o Tijera'
				Escribir '2.Es par o inpar'
				Escribir ':::::::::::::::::::::::'
				Leer Juego
				Limpiar Pantalla
				Según Juego Hacer
					1:
						Buc <- 's'
						Mientras Buc='s' Hacer
							Limpiar Pantalla
							Escribir 'Tu saldo es de: $', dinero
							Escribir ':::::::::::::::::::::::.::'
							Repetir
								Escribir 'Ingresa el monto a apostar mínimo $1, máximo $', dinero
								Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::::'
								Leer Apuesta
							Hasta Que Apuesta>=1 Y Apuesta<=dinero
							Escribir ':::::::::::::::'
							Escribir 'Elije entre :'
							Escribir ':::::::::::::::'
							Escribir '1.Piedra'
							Escribir '2.Tijera'
							Escribir '3.Papel'
							Escribir ':::::::::::::::'
							Leer Op
							Limpiar Pantalla
							Escribir '::::::::::::::::'
							Según Op Hacer
								1:
									Escribir 'Elejiste piedra'
									Escribir ':::::::::::::::'
									Ga <- Aleatorio(1,3)
									Según Ga Hacer
										1:
											Escribir 'Yo elegi papel'
											Escribir '::::::::::::::::'
											Escribir 'Yo gane'
											Escribir '::::::::::::::::'
											Escribir 'Perdiste $', Apuesta
											Escribir '::::::::::::::::::::::::::::::'
											dinero <- dinero-Apuesta
											Escribir 'Te quedas con $', dinero
											Escribir '::::::::::::::::::::::::::::::'
											Escribir 'La casa gana'
											Escribir '::::::::::::::::::::::::::::::'
											Si dinero=0 Entonces
												Buc <- 'n'
											SiNo
												Escribir 'Quieres seguir juegando? s/n'
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
												FinSi
											FinSi
										2:
											Escribir 'Yo elegi tijera'
											Escribir '::::::::::::::::'
											Escribir 'Tu ganaste'
											Escribir '::::::::::::::::'
											dinero <- dinero+Apuesta
											Escribir 'Ganaste en total : $', dinero
											Escribir ':::::::::::::::::::::'
											Escribir 'Quieres seguir juegando? s/n'
											Escribir '::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::'
												Escribir 'Te retiras con el total de $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::'
												Buc <- 'n'
											FinSi
										3:
											Escribir 'Yo elegi piedra'
											Escribir '::::::::::::::::'
											Escribir 'Empate'
											Escribir '::::::::::::::::'
											Escribir 'Nadie gana'
											Escribir '::::::::::::::::'
											Escribir 'Quieres seguir juegando? s/n'
											Escribir '::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::'
												Escribir 'Te retiras con el total de dinero ganado $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::'
												Escribir 'Dinero apostado $ ', Apuesta
												Buc <- 'n'
											FinSi
									FinSegún
								2:
									Escribir 'Elejiste tijeras'
									Ga <- Aleatorio(1,3)
									Según Ga Hacer
										1:
											Escribir 'Yo elegi piedra'
											Escribir '::::::::::::::::'
											Escribir 'Yo gane'
											Escribir '::::::::::::::::'
											Escribir 'Perdiste $', Apuesta
											Escribir '::::::::::::::::::::::::::::::'
											dinero <- dinero-Apuesta
											Escribir 'Te quedas con $', dinero
											Escribir '::::::::::::::::::::::::::::::'
											Escribir 'La casa gana'
											Escribir '::::::::::::::::::::::::::::::'
											Si dinero=0 Entonces
												Buc <- 'n'
											SiNo
												Escribir 'Quieres seguir juegando? s/n'
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
												FinSi
											FinSi
										2:
											Escribir 'Yo elegi papel'
											Escribir '::::::::::::::::'
											Escribir 'Tu ganaste'
											Escribir '::::::::::::::::'
											dinero <- dinero+Apuesta
											Escribir 'Ganaste en total : $', dinero
											Escribir ':::::::::::::::::::::'
											Escribir 'Quieres seguir juegando? s/n'
											Escribir '::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::'
												Escribir 'Te retirasa con el total de $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::'
												Buc <- 'n'
											FinSi
										3:
											Escribir 'Yo elegi tijera'
											Escribir '::::::::::::::::'
											Escribir 'Empate'
											Escribir '::::::::::::::::'
											Escribir 'Nadie gana'
											Escribir '::::::::::::::::'
											Escribir 'Quieres seguir juegando? s/n'
											Escribir '::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::'
												Escribir 'Te retirasa con el total de dinero ganado $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::'
												Escribir 'Dinero apostado $ ', Apuesta
												Buc <- 'n'
											FinSi
									FinSegún
								3:
									Escribir 'Elejiste papel'
									Ga <- Aleatorio(1,3)
									Según Ga Hacer
										1:
											Escribir 'Yo elegi tijera'
											Escribir '::::::::::::::::'
											Escribir 'Yo gane'
											Escribir '::::::::::::::::'
											Escribir 'Perdiste $', Apuesta
											Escribir '::::::::::::::::::::::::::::::'
											dinero <- dinero-Apuesta
											Escribir 'Te quedas con $', dinero
											Escribir '::::::::::::::::::::::::::::::'
											Escribir 'La casa gana'
											Escribir '::::::::::::::::::::::::::::::'
											Si dinero=0 Entonces
												Buc <- 'n'
											SiNo
												Escribir 'Quieres seguir juegando? s/n'
												Escribir '::::::::::::::::::::::::::::::'
												Leer Ele
												Si Ele='s' Entonces
													Buc <- 's'
													Limpiar Pantalla
												SiNo
													Escribir ':::::::::::::::::::::::::::::::::'
													Escribir 'Te retirasa con el total de $ ', dinero
													Escribir ':::::::::::::::::::::::::::::::::'
													Buc <- 'n'
												FinSi
											FinSi
										2:
											Escribir 'Yo elegi piedra'
											Escribir '::::::::::::::::'
											Escribir 'Tu ganaste'
											Escribir '::::::::::::::::'
											dinero <- dinero+Apuesta
											Escribir 'Ganaste en total : $', dinero
											Escribir ':::::::::::::::::::::'
											Escribir 'Quieres seguir juegando? s/n'
											Escribir '::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::'
												Escribir 'Te retirasa con el total de $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::'
												Buc <- 'n'
											FinSi
										3:
											Escribir 'Yo elegi papel'
											Escribir '::::::::::::::::'
											Escribir 'Empate'
											Escribir '::::::::::::::::'
											Escribir 'Nadie gana'
											Escribir '::::::::::::::::'
											Escribir 'Quieres seguir juegando? s/n'
											Escribir '::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::'
												Escribir 'Te retirasa con el total de dinero ganado $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::'
												Escribir 'Dinero apostado $ ', Apuesta
												Buc <- 'n'
											FinSi
									FinSegún
							FinSegún
						FinMientras
					2:
						Buc <- 's'
						Mientras Buc='s' Hacer
							Escribir 'Tu saldo es de: $', dinero
							Escribir '::::::::::::::::::::::::::::'
							Repetir
								Escribir 'Ingresa el monto a apostar mínimo $1, máximo $', dinero
								Escribir ':::::::::::::::::::::::::::::::::::::::::::::::::::::'
								Leer Apuesta
							Hasta Que Apuesta>=1 Y Apuesta<=dinero
							Escribir 'Bienvenido a es par o inpar'
							Escribir ':::::::::::::::::::::::::::'
							Escribir 'Ya tengo el numero pensado'
							Escribir ':::::::::::::::::::::::::::'
							Escribir 'Dime es par o inpar'
							Escribir ':::::::::::::::::::::::::::'
							Escribir '1.Par'
							Escribir '2.Inpar'
							Escribir ':::::::::::::::::::::::::::'
							Leer PoI
							Según PoI Hacer
								1:
									Escribir 'Escojiste par '
									Elnumero <- Aleatorio(1,50)
									Si Elnumero MOD 2==0 Entonces
										Escribir 'El numero fue par  ', Elnumero
										Escribir 'Ganaste'
										dinero <- Apuesta+dinero
										Escribir 'Ganaste en total : $', dinero
										Escribir ':::::::::::::::::::::'
										Escribir 'Quieres seguir juegando? s/n'
										Escribir '::::::::::::::::::::::::::::::'
										Leer Ele
										Si Ele='s' Entonces
											Buc <- 's'
											Limpiar Pantalla
										SiNo
											Escribir ':::::::::::::::::::::::::::::::::'
											Escribir 'Te retirasa con el total de $ ', dinero
											Escribir ':::::::::::::::::::::::::::::::::'
											Buc <- 'n'
										FinSi
									SiNo
										Escribir 'El numero fue inpar  ', Elnumero
										Escribir '::::::::::::::::::::::::::::::'
										Escribir 'Perdiste $', dinero
										Escribir '::::::::::::::::::::::::::::::'
										dinero <- dinero-Apuesta
										Escribir 'Te quedas con $', dinero
										Escribir '::::::::::::::::::::::::::::::'
										Escribir 'La casa gana'
										Escribir '::::::::::::::::::::::::::::::'
										Si dinero=0 Entonces
											Buc <- 'n'
										SiNo
											Escribir 'Quieres seguir juegando? s/n'
											Escribir '::::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
												Limpiar Pantalla
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::'
												Escribir 'Te retirasa con el total de $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::'
												Buc <- 'n'
											FinSi
										FinSi
									FinSi
								2:
									Escribir 'Escojiste inpar'
									Elnumero <- Aleatorio(1,50)
									Si Elnumero MOD 2==0 Entonces
										Escribir 'El numero fue par ', Elnumero
										Escribir '::::::::::::::::::::::::::::::'
										Escribir 'Perdiste $', dinero
										Escribir '::::::::::::::::::::::::::::::'
										dinero <- dinero-Apuesta
										Escribir 'Te quedas con $', dinero
										Escribir '::::::::::::::::::::::::::::::'
										Escribir 'La casa gana'
										Escribir '::::::::::::::::::::::::::::::'
										Si dinero=0 Entonces
											Buc <- 'n'
										SiNo
											Escribir 'Quieres seguir juegando? s/n'
											Escribir '::::::::::::::::::::::::::::::'
											Leer Ele
											Si Ele='s' Entonces
												Buc <- 's'
												Limpiar Pantalla
											SiNo
												Escribir ':::::::::::::::::::::::::::::::::'
												Escribir 'Te retirasa con el total de $ ', dinero
												Escribir ':::::::::::::::::::::::::::::::::'
												Buc <- 'n'
											FinSi
										FinSi
									SiNo
										Escribir 'El numero fue inpar ', Elnumero
										dinero <- Apuesta+dinero
										Escribir 'Ganaste en total : $', dinero
										Escribir ':::::::::::::::::::::'
										Escribir 'Quieres seguir juegando? s/n'
										Escribir '::::::::::::::::::::::::::::::'
										Leer Ele
										Si Ele='s' Entonces
											Buc <- 's'
											Limpiar Pantalla
										SiNo
											Escribir ':::::::::::::::::::::::::::::::::'
											Escribir 'Te retirasa con el total de $ ', dinero
											Escribir ':::::::::::::::::::::::::::::::::'
											Buc <- 'n'
										FinSi
									FinSi
							FinSegún
						FinMientras
					De Otro Modo:
						Escribir 'Puso mal el numero intente de nuevo'
						Buc <- 's'
				FinSegún
			De Otro Modo:
				Escribir 'Puso mal el numero intentar otra vez'
		FinSegún
	SiNo
		Escribir 'Lo siento pero no tienes la edad nesesaria para ingresar'
	FinSi
FinAlgoritmo
