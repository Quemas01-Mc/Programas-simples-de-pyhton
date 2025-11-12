Algoritmo Emco
	Limpiar Pantalla
	Escribir '======================================='
	Escribir '| -------- CASINO LA RATA  -----------|'
	Escribir '======================================='
	Escribir '-----------  Bienvenido  --------------'
	Escribir '-------- Solo mayores de edad ---------'
	Escribir '======================================='
	Escribir '-Donde vendemos mejor que otros lugares'
	Escribir '======================================='
	Escribir '¿Cual es tu nombre?'
	Escribir '---------------------------------------'
	Leer Nombre
	Limpiar Pantalla
	Escribir '======================================='
	Escribir 'Hola ', Nombre, ' ¿Qué edad tienes?'
	Escribir '---------------------------------------'
	Leer edad
	Limpiar Pantalla
	Si edad>=18 Entonces
		Bucle <- 's'
		TotalUni <- 0
		TotalCO <- 0
		TotalGa <- 0
		DineroPa <- 0
		Mientras Bucle='s' Hacer
			Escribir '¿Qué activida deseas hacer?'
			Escribir '=========== Menu ============'
			Escribir '1.Bar'
			Escribir '2.Juegos'
			Escribir '-----------------------------'
			Leer Opcion
			Limpiar Pantalla
			Según Opcion Hacer
				1:
					I <- 's'
					Mientras I='s' Hacer
						Escribir '========= Menú de Licores ========='
						Escribir '1. Martini .............. $ 2.10'
						Escribir '2. Negroni .............. $ 4.00'
						Escribir '3. Jugo de mora ......... $ 2.50'
						Escribir '==================================='
						Escribir '¿Qué deseas comprar?'
						Escribir '-----------------------------------'
						Escribir 'Puedes ganar un descuento si superas una compra de mas de 3 vevidas'
						Escribir '___________________________________________________________________'
						Leer Comprar
						Limpiar Pantalla
						Según Comprar Hacer
							1:
								Escribir 'Qué buena elección  ', Nombre, '  ¿Cuánto deseas llevar?'
								Escribir '--------------------------------------------------------'
								Leer Chi
								Unidades <- Chi
								TotalUni <- TotalUni+Unidades
								Escribir 'Quieres hacer algo mas antes de irte s/n'
								Escribir '----------------------------------------'
								Leer Bucle
								Limpiar Pantalla
								I <- 'n'
								Total <- Chi*2.10
								TotalCO <- TotalCO+Total
							2:
								Escribir 'Qué buena elección  ', Nombre, '  ¿Cuánto deseas llevar?'
								Escribir '--------------------------------------------------------'
								Leer Chi
								Unidades <- Chi
								TotalUni <- TotalUni+Unidades
								Escribir 'Quieres hacer algo mas antes de irte s/n'
								Escribir '----------------------------------------'
								Leer Bucle
								Limpiar Pantalla
								I <- 'n'
								Total <- Chi*4
								TotalCO <- TotalCO+Total
							3:
								Escribir 'Qué buena elección  ', Nombre, '  ¿Cuánto deseas llevar?'
								Escribir '--------------------------------------------------------'
								Leer Chi
								Unidades <- Chi
								TotalUni <- TotalUni+Unidades
								Escribir 'Quieres hacer algo mas antes de irte s/n'
								Escribir '----------------------------------------'
								Leer Bucle
								Limpiar Pantalla
								I <- 'n'
								Total <- Chi*2.50
								TotalCO <- TotalCO+Total
							De Otro Modo:
								Escribir '=================================='
								Escribir 'Ingresaste un numero invalido'
								Escribir ':('
								Escribir 'Intentalo de nuevo'
								Escribir '==================================='
								Escribir '-----Enter para continuar----'
								Escribir '=================================='
								Leer ok
								Bucle <- 's'
						FinSegún
					FinMientras
				2:
					Escribir '¿Cuánta plata quieres poner para apostar? ', Nombre
					Escribir '---------------------------------------------------'
					Leer dinero
					DineroPa <- dinero
					Limpiar Pantalla
					Juefo <- 's'
					Mientras Juefo='s' Hacer
						Escribir '=========================='
						Escribir '¿Qué quieres jugar?'
						Escribir '======== Menú  ==========='
						Escribir '1.Es par o impar----------'
						Escribir '2.Piedra,Papel o Tijera---'
						Escribir '3.Carrera de caballos-----'
						Escribir '__________________________'
						Leer Juego
						Limpiar Pantalla
						Según Juego Hacer
							1:
								Buc <- 's'
								Mientras Buc='s' Hacer
									Escribir 'Tu saldo es de: $', dinero
									Escribir '=========================='
									Repetir
										Escribir 'Ingresa el monto a apostar: mínimo $1, máximo $', dinero
										Escribir '======================================================='
										Leer Apuesta
									Hasta Que Apuesta>=1 Y Apuesta<=dinero
									Escribir 'Bienvenido a es par o impar'
									Escribir '==========================='
									Escribir 'Ya tengo el número pensado'
									Escribir '==========================='
									Escribir 'Dime, ¿es par o impar?'
									Escribir '==========================='
									Escribir '1.Par'
									Escribir '2.Impar'
									Escribir '___________________________'
									Leer PoI
									Según PoI Hacer
										1:
											Escribir 'Escogiste par'
											Escribir '=============='
											Elnumero <- Aleatorio(1,50)
											Si Elnumero MOD 2==0 Entonces
												Escribir 'El número fue par: ', Elnumero
												Escribir 'Ganaste'
												dinero <- Apuesta+dinero
												TotalGa <- TotalGa+dinero
												Escribir 'Ganaste en total: $', dinero
												Escribir '============================'
												Escribir '¿Quieres seguir jugando? s/n'
												Escribir '----------------------------'
												Leer Ele
												Si Ele='s' Entonces
													Buc <- 's'
													Limpiar Pantalla
												SiNo
													Escribir '======================================'
													Escribir 'Te retiras con el total de $ ', dinero
													Escribir '======================================'
													Buc <- 'n'
													Bucle <- 'n'
													Juefo <- 'n'
												FinSi
											SiNo
												Escribir 'El número fue impar: ', Elnumero
												Escribir '==============================='
												Escribir 'Perdiste $', Apuesta
												Escribir '============================='
												dinero <- dinero-Apuesta
												Escribir 'Te quedas con $', dinero
												Escribir '=============================='
												Escribir 'La casa gana'
												Escribir '=============================='
												Si dinero=0 Entonces
													Buc <- 'n'
													Bucle <- 'n'
													Juefo <- 'n'
												SiNo
													Escribir '¿Quieres seguir jugando? s/n'
													Escribir '-----------------------------'
													Leer Ele
													Si Ele='s' Entonces
														Buc <- 's'
														Limpiar Pantalla
													SiNo
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													FinSi
												FinSi
											FinSi
										2:
											Escribir 'Escogiste impar'
											Escribir '==============='
											Elnumero <- Aleatorio(1,50)
											Si Elnumero MOD 2==0 Entonces
												Escribir 'El número fue par: ', Elnumero
												Escribir '==============================='
												Escribir 'Perdiste $', Apuesta
												Escribir '==============================='
												dinero <- dinero-Apuesta
												Escribir 'Te quedas con $', dinero
												Escribir '==============================='
												Escribir 'La casa gana'
												Escribir '==============================='
												Si dinero=0 Entonces
													Buc <- 'n'
													Bucle <- 'n'
													Juefo <- 'n'
												SiNo
													Escribir '¿Quieres seguir jugando? s/n'
													Escribir '----------------------------'
													Leer Ele
													Si Ele='s' Entonces
														Buc <- 's'
														Limpiar Pantalla
													SiNo
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													FinSi
												FinSi
											SiNo
												Escribir 'El número fue impar: ', Elnumero
												dinero <- Apuesta+dinero
												TotalGa <- TotalGa+dinero
												Escribir 'Ganaste en total: $', dinero
												Escribir '============================'
												Escribir '¿Quieres seguir jugando? s/n'
												Escribir '----------------------------'
												Leer Ele
												Si Ele='s' Entonces
													Buc <- 's'
													Limpiar Pantalla
												SiNo
													Buc <- 'n'
													Bucle <- 'n'
													Juefo <- 'n'
												FinSi
											FinSi
									FinSegún
								FinMientras
							2:
								Buc <- 's'
								Mientras Buc='s' Hacer
									Limpiar Pantalla
									Escribir 'Tu saldo es de: $', dinero
									Escribir '========================='
									Repetir
										Escribir 'Ingresa el monto a apostar mínimo $1, máximo $', dinero
										Escribir '-------------------------------------------------------'
										Leer Apuesta
									Hasta Que Apuesta>=1 Y Apuesta<=dinero
									Escribir '==============='
									Escribir 'Elije entre :'
									Escribir '==============='
									Escribir '1.Piedra------|'
									Escribir '2.Tijera------|'
									Escribir '3.Papel-------|'
									Escribir '---------------'
									Leer Op
									Limpiar Pantalla
									Escribir '=============='
									Según Op Hacer
										1:
											Escribir 'Elejiste piedra'
											Escribir '==============='
											Ga <- Aleatorio(1,3)
											Según Ga Hacer
												1:
													Escribir 'Yo elegi papel'
													Escribir '==============================='
													Escribir 'Yo gane'
													Escribir '==============================='
													Escribir 'Perdiste $', Apuesta
													Escribir '==============================='
													dinero <- dinero-Apuesta
													Escribir 'Te quedas con $', dinero
													Escribir '==============================='
													Escribir 'La casa gana'
													Escribir '==============================='
													Si dinero=0 Entonces
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													SiNo
														Escribir 'Quieres seguir juegando? s/n'
														Escribir '----------------------------'
														Leer Ele
														Si Ele='s' Entonces
															Buc <- 's'
															Limpiar Pantalla
														SiNo
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														FinSi
													FinSi
												2:
													Escribir 'Yo elegi tijera'
													Escribir '============================'
													Escribir 'Tu ganaste'
													Escribir '============================'
													dinero <- dinero+Apuesta
													TotalGa <- TotalGa+dinero
													Escribir 'Ganaste en total : $', dinero
													Escribir '============================'
													Escribir 'Quieres seguir juegando? s/n'
													Escribir '-----------------------------'
													Leer Ele
													Si Ele='s' Entonces
														Buc <- 's'
													SiNo
														BBuc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													FinSi
												3:
													Escribir 'Yo elegi piedra'
													Escribir '============================'
													Escribir 'Empate'
													Escribir '============================'
													Escribir 'Nadie gana'
													Escribir '============================'
													Escribir 'Quieres seguir juegando? s/n'
													Escribir '----------------------------'
													Leer Ele
													Si Ele='s' Entonces
														Buc <- 's'
													SiNo
														Escribir 'Dinero apostado $ ', Apuesta
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													FinSi
											FinSegún
										2:
											Escribir 'Elejiste tijeras'
											Ga <- Aleatorio(1,3)
											Según Ga Hacer
												1:
													Escribir 'Yo elegi piedra'
													Escribir '=============================='
													Escribir 'Yo gane'
													Escribir '=============================='
													Escribir 'Perdiste $', Apuesta
													Escribir '=============================='
													dinero <- dinero-Apuesta
													Escribir 'Te quedas con $', dinero
													Escribir '=============================='
													Escribir 'La casa gana'
													Escribir '=============================='
													Si dinero=0 Entonces
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													SiNo
														Escribir 'Quieres seguir juegando? s/n'
														Escribir '----------------------------'
														Leer Ele
														Si Ele='s' Entonces
															Buc <- 's'
															Limpiar Pantalla
														SiNo
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														FinSi
													FinSi
												2:
													Escribir 'Yo elegi papel'
													Escribir '============================'
													Escribir 'Tu ganaste'
													Escribir '============================'
													dinero <- dinero+Apuesta
													TotalGa <- TotalGa+dinero
													Escribir 'Ganaste en total : $', dinero
													Escribir '============================'
													Escribir 'Quieres seguir juegando? s/n'
													Escribir '----------------------------'
													Leer Ele
													Si Ele='s' Entonces
														Buc <- 's'
													SiNo
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													FinSi
												3:
													Escribir 'Yo elegi tijera'
													Escribir '============================'
													Escribir 'Empate'
													Escribir '============================'
													Escribir 'Nadie gana'
													Escribir '============================'
													Escribir 'Quieres seguir juegando? s/n'
													Escribir '----------------------------'
													Leer Ele
													Si Ele='s' Entonces
														Buc <- 's'
													SiNo
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													FinSi
											FinSegún
										3:
											Escribir 'Elejiste papel'
											Ga <- Aleatorio(1,3)
											Según Ga Hacer
												1:
													Escribir 'Yo elegi tijera'
													Escribir '============================='
													Escribir 'Yo gane'
													Escribir '=============================='
													Escribir 'Perdiste $', Apuesta
													Escribir '=============================='
													dinero <- dinero-Apuesta
													Escribir 'Te quedas con $', dinero
													Escribir '=============================='
													Escribir 'La casa gana'
													Escribir '=============================='
													Si dinero=0 Entonces
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													SiNo
														Escribir 'Quieres seguir juegando? s/n'
														Escribir '----------------------------'
														Leer Ele
														Si Ele='s' Entonces
															Buc <- 's'
															Limpiar Pantalla
														SiNo
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														FinSi
													FinSi
												2:
													Escribir 'Yo elegi piedra'
													Escribir '============================'
													Escribir 'Tu ganaste'
													Escribir '============================'
													dinero <- dinero+Apuesta
													TotalGa <- TotalGa+dinero
													Escribir 'Ganaste en total : $', dinero
													Escribir '============================'
													Escribir 'Quieres seguir juegando? s/n'
													Escribir '----------------------------'
													Leer Ele
													Si Ele='s' Entonces
														Buc <- 's'
													SiNo
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													FinSi
												3:
													Escribir 'Yo elegi papel'
													Escribir '==========================='
													Escribir 'Empate'
													Escribir '==========================='
													Escribir 'Nadie gana'
													Escribir '============================'
													Escribir 'Quieres seguir juegando? s/n'
													Escribir '----------------------------'
													Leer Ele
													Si Ele='s' Entonces
														Buc <- 's'
													SiNo
														Buc <- 'n'
														Bucle <- 'n'
														Juefo <- 'n'
													FinSi
												De Otro Modo:
													Escribir '=================================='
													Escribir 'Ingresaste un numero invalido'
													Escribir ':('
													Escribir 'Intentalo de nuevo'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer ok
													Buc <- 's'
											FinSegún
										De Otro Modo:
											Escribir '=================================='
											Escribir 'Ingresaste un numero invalido'
											Escribir ':('
											Escribir 'Intentalo de nuevo'
											Escribir '==================================='
											Escribir '-----Enter para continuar----'
											Escribir '=================================='
											Leer ok
											Buc <- 's'
									FinSegún
								FinMientras
							3:
								buc3="s"
								Mientras buc3="s" Hacer
									
								
									Escribir "============================="
									Escribir 'A que caballo quieres apostar'
									Escribir "============================="
									Escribir '1.Secretariat'
									Escribir '2.Justify'
									Escribir '3.Cigar'
									Escribir "-----------------------------"
									Leer Caballo
									Según Caballo Hacer
										1:
											NombreCA <- 'Secretariat'
											ID=1
											buc3="n"
										2:
											NombreCA <- 'Justify'
											ID=2
											buc3="n"
										3:
											NombreCA <- 'Cigar'
											ID=3
											buc3="n"
										De Otro Modo:
											Escribir '=================================='
											Escribir 'Ingresaste un numero invalido'
											Escribir ':('
											Escribir 'Intentalo de nuevo'
											Escribir '==================================='
											Escribir '-----Enter para continuar----'
											Escribir '=================================='
											Leer ok
											Limpiar Pantalla
											buc3="s"
									
									FinSegún
								Fin Mientras
								Repetir
									Escribir 'Ingresa el monto a apostar: mínimo $1, máximo $', dinero
									Escribir '--------------------------------------------------------'
									Leer Apuesta
								Hasta Que Apuesta>=1 Y Apuesta<=dinero
									NUm <- 1
									Según NUm Hacer
										1:
                                            Limpiar Pantalla
											Escribir '-------|\__-------------------------------------------------------'
											Escribir ' ______|´ |)-----------------------------------------------------'
											Escribir '/  |1|   /-------------------------------------------------------'
											Escribir ' ----- |\__------------------------------------------------------'
											Escribir ' ______|´ |)-----------------------------------------------------'
											Escribir '/  |2|   /-------------------------------------------------------'
											Escribir ' ------|\__------------------------------------------------------'
											Escribir ' ______|´ |)-----------------------------------------------------'
											Escribir '/  |3|   /-------------------------------------------------------'
											Escribir '==================================='
											Escribir '-----Enter para continuar----'
											Escribir '=================================='
											Leer KI
											NUm <- Aleatorio(1,3)
											Limpiar Pantalla
											Según NUm Hacer
												1:
													Escribir '------------------------|\__-------------------------------------'
													Escribir '----------------- ______|´ |)------------------------------------'
													Escribir '-----------------/  |2|   /--------------------------------------'
													Escribir ' --------------- |\__--------------------------------------------'
													Escribir '---------- ______|´ |)-------------------------------------------'
													Escribir '----------/  |1|   /----------------------------------------------'
													Escribir ' ------|\__------------------------------------------------------'
													Escribir ' ______|´ |)-----------------------------------------------------'
													Escribir '/  |3|   /-------------------------------------------------------'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													NUm <- Aleatorio(1,3)
													Limpiar Pantalla
												2:
													Escribir '------------------------|\__-------------------------------------'
													Escribir '----------------- ______|´ |)------------------------------------'
													Escribir '-----------------/  |3|   /--------------------------------------'
													Escribir ' --------------- |\__--------------------------------------------'
													Escribir '---------- ______|´ |)-------------------------------------------'
													Escribir '----------/  |2|   /----------------------------------------------'
													Escribir ' ------|\__------------------------------------------------------'
													Escribir ' ______|´ |)-----------------------------------------------------'
													Escribir '/  |1|   /-------------------------------------------------------'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													NUm <- Aleatorio(1,3)
													Limpiar Pantalla
												3:
													Escribir '------------------------|\__-------------------------------------'
													Escribir '----------------- ______|´ |)------------------------------------'
													Escribir '-----------------/  |2|   /--------------------------------------'
													Escribir ' --------------- |\__--------------------------------------------'
													Escribir '---------- ______|´ |)-------------------------------------------'
													Escribir '----------/  |3|   /----------------------------------------------'
													Escribir ' ------|\__------------------------------------------------------'
													Escribir ' ______|´ |)-----------------------------------------------------'
													Escribir '/  |1|   /-------------------------------------------------------'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													NUm <- Aleatorio(1,3)
													Limpiar Pantalla
											FinSegún
											Según NUm Hacer
												1:
													Escribir '------------------------------------|\__--------------------------'
													Escribir '----------------------------- ______|´ |)------------------------'
													Escribir '-----------------------------/  |3|   /--------------------------'
													Escribir ' ----------------------------------------------------|\__--------'
													Escribir '-----------------------------------------------______|´ |)-------'
													Escribir '----------------------------------------------/  |1|   /---------'
													Escribir '------------------------|\__-------------------------------------'
													Escribir '----------------- ______|´ |)------------------------------------'
													Escribir '-----------------/  |2|   /--------------------------------------'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													NUm <- Aleatorio(1,3)
													Limpiar Pantalla
												2:
													Escribir '------------------------------------|\__--------------------------'
													Escribir '----------------------------- ______|´ |)------------------------'
													Escribir '-----------------------------/  |1|   /--------------------------'
													Escribir ' ----------------------------------------------------|\__--------'
													Escribir '-----------------------------------------------______|´ |)-------'
													Escribir '----------------------------------------------/  |3|   /---------'
													Escribir '------------------------|\__-------------------------------------'
													Escribir '----------------- ______|´ |)------------------------------------'
													Escribir '-----------------/  |2|   /--------------------------------------'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													NUm <- Aleatorio(1,3)
													Limpiar Pantalla
												3:
													Escribir '------------------------------------|\__--------------------------'
													Escribir '----------------------------- ______|´ |)------------------------'
													Escribir '-----------------------------/  |1|   /--------------------------'
													Escribir ' ----------------------------------------------------|\__--------'
													Escribir '-----------------------------------------------______|´ |)-------'
													Escribir '----------------------------------------------/  |3|   /---------'
													Escribir '------------------------|\__-------------------------------------'
													Escribir '----------------- ______|´ |)------------------------------------'
													Escribir '-----------------/  |2|   /--------------------------------------'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													NUm <- Aleatorio(1,3)
													Limpiar Pantalla
											FinSegún
											Según NUm Hacer
												1:
													Escribir '------------------------------------|\__--------------------------'
													Escribir '----------------------------- ______|´ |)------------------------'
													Escribir '-----------------------------/  |3|   /--------------------------'
													Escribir ' ----------------------------------------------------|\__--------'
													Escribir '-----------------------------------------------______|´ |)-------'
													Escribir '----------------------------------------------/  |2|   /---------'
													Escribir '-------------------------------------------------------------|\__'
													Escribir '-------------------------------------------------------______|´ |)'
													Escribir '------------------------------------------------------/  |1|   /'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													Ga <- 1
													Limpiar Pantalla
												2:
													Escribir '------------------------------------|\__--------------------------'
													Escribir '----------------------------- ______|´ |)------------------------'
													Escribir '-----------------------------/  |2|   /--------------------------'
													Escribir ' ----------------------------------------------------|\__--------'
													Escribir '-----------------------------------------------______|´ |)-------'
													Escribir '----------------------------------------------/  |1|   /---------'
													Escribir '-------------------------------------------------------------|\__'
													Escribir '-------------------------------------------------------______|´ |)'
													Escribir '------------------------------------------------------/  |3|   /'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													Ga <- 3
													Limpiar Pantalla
												3:
													Escribir '------------------------------------|\__--------------------------'
													Escribir '----------------------------- ______|´ |)------------------------'
													Escribir '-----------------------------/  |1|   /--------------------------'
													Escribir ' ----------------------------------------------------|\__--------'
													Escribir '-----------------------------------------------______|´ |)-------'
													Escribir '----------------------------------------------/  |3|   /---------'
													Escribir '-------------------------------------------------------------|\__'
													Escribir '-------------------------------------------------------______|´ |)'
													Escribir '------------------------------------------------------/  |2|   /'
													Escribir '==================================='
													Escribir '-----Enter para continuar----'
													Escribir '=================================='
													Leer KI
													Ga <- 2
													Limpiar Pantalla
											FinSegún
											Según Ga Hacer
												1:
													Escribir "========================"
													Escribir "El ganador fue Secretariat"
													Escribir "========================"
													Escribir "Tu escojiste a ",NombreCa
													Escribir "========================"
													Si ID=1 Entonces
														Escribir"Ganaste felizidades"
														Escribir "==================="
														dinero <- dinero+Apuesta
														TotalGa <- TotalGa+dinero
														Escribir 'Ganaste en total : $', dinero
														Escribir '============================'
														Escribir 'Quieres seguir juegando? s/n'
														Escribir '----------------------------'
														Leer Ele
														Si Ele='s' Entonces
															Juefo="s"
														SiNo
															Buc3="n"
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														FinSi
														
													SiNo
														Escribir 'Perdiste $', Apuesta
														Escribir '=============================='
														dinero <- dinero-Apuesta
														Escribir 'Te quedas con $', dinero
														Escribir '=============================='
														Escribir 'La casa gana'
														Escribir '=============================='
														Si dinero=0 Entonces
															Buc3="n"
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														SiNo
															Escribir 'Quieres seguir juegando? s/n'
															Escribir '----------------------------'
															Leer Ele
															Si Ele='s' Entonces
																Juefo="s"
																Limpiar Pantalla
															SiNo
																Buc3="n"
																Buc <- 'n'
																Bucle <- 'n'
																Juefo <- 'n'
															FinSi
														FinSi
														
														
													Fin Si
 												2:
													Escribir "========================"
													Escribir "El ganador fue Justify"
													Escribir "========================"
													Escribir "Tu escojiste a ",NombreCa
													Escribir "========================"
													Si ID=2 Entonces
														Escribir"Ganaste felizidades"
														Escribir "==================="
														dinero <- dinero+Apuesta
														TotalGa <- TotalGa+dinero
														Escribir 'Ganaste en total : $', dinero
														Escribir '============================'
														Escribir 'Quieres seguir juegando? s/n'
														Escribir '----------------------------'
														Leer Ele
														Si Ele='s' Entonces
															Juefo="s"
														SiNo
															Buc3="n"
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														FinSi
													SiNo
														Escribir 'Perdiste $', Apuesta
														Escribir '=============================='
														dinero <- dinero-Apuesta
														Escribir 'Te quedas con $', dinero
														Escribir '=============================='
														Escribir 'La casa gana'
														Escribir '=============================='
														Si dinero=0 Entonces
															Buc3="n"
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														SiNo
															Escribir 'Quieres seguir juegando? s/n'
															Escribir '----------------------------'
															Leer Ele
															Si Ele='s' Entonces
																Juefo="s"
																Limpiar Pantalla
															SiNo
																Buc3="n"
																Buc <- 'n'
																Bucle <- 'n'
																Juefo <- 'n'
															FinSi
														FinSi
														
														
													Fin Si
												3:
													Escribir "========================"
													Escribir "El ganador fue Cigar"
													Escribir "========================"
													Escribir "Tu escojiste a ",NombreCa
													Escribir "========================"
													Si ID=3 Entonces
														Escribir"Ganaste felizidades"
														Escribir "==================="
														dinero <- dinero+Apuesta
														TotalGa <- TotalGa+dinero
														Escribir 'Ganaste en total : $', dinero
														Escribir '============================'
														Escribir 'Quieres seguir juegando? s/n'
														Escribir '----------------------------'
														Leer Ele
														Si Ele='s' Entonces
															Juefo="s"
														SiNo
															Buc3="n"
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														FinSi
														
													SiNo
														Escribir 'Perdiste $', Apuesta
														Escribir '=============================='
														dinero <- dinero-Apuesta
														Escribir 'Te quedas con $', dinero
														Escribir '=============================='
														Escribir 'La casa gana'
														Escribir '=============================='
														Si dinero=0 Entonces
															Buc3="n"
															Buc <- 'n'
															Bucle <- 'n'
															Juefo <- 'n'
														SiNo
															Escribir 'Quieres seguir juegando? s/n'
															Escribir '----------------------------'
															Leer Ele
															Si Ele='s' Entonces
																Juefo="s"
																Limpiar Pantalla
															SiNo
																Buc3="n"
																Buc <- 'n'
																Bucle <- 'n'
																Juefo <- 'n'
															FinSi
														FinSi
														
													Fin Si
											FinSegún
									FinSegún
								
							De Otro Modo:
								Escribir '=================================='
								Escribir 'Ingresaste un numero invalido'
								Escribir ':('
								Escribir 'Intentalo de nuevo'
								Escribir '==================================='
								Escribir '-----Enter para continuar----'
								Escribir '=================================='
								Leer ok
								Juefo <- 's'
						FinSegún
					FinMientras
				De Otro Modo:
					Escribir '=================================='
					Escribir 'Ingresaste un numero invalido'
					Escribir ':('
					Escribir 'Intentalo de nuevo'
					Escribir '==================================='
					Escribir '-----Enter para continuar----'
					Escribir '=================================='
					Leer ok
					Bucle <- 's'
			FinSegún
		FinMientras
		Si TotalUni>=3 Entonces
			Limpiar Pantalla
			Descuento <- TotalCO*0.1
			td <- TotalCO-Descuento
			Limpiar Pantalla
			Escribir 'El total a pagar del bar es:  $', TotalCO
			Escribir '========================================'
			Escribir 'El total a pagar del casino es $', DineroPa
			Escribir '======================================='
			Escribir 'Como quieres pagar tu consumo :'
			Escribir '================================'
			Escribir '1.Efectivo'
			Escribir '2.Tarjeta'
			Escribir '-------------------------------'
			Leer Pago
			Si Pago=1 Entonces
				PagoET <- 'Efectivo'
			SiNo
				PagoET <- 'Tarjeta'
			FinSi
			Limpiar Pantalla
			Escribir '===================================='
			Escribir '------- FACTURA DE COMPRA ----------'
			Escribir '===================================='
			Escribir 'Cliente: ', Nombre
			Escribir '------------------------------------'
			Escribir 'Productos: ', TotalUni, ' bebidas '
			Escribir 'Subtotal: $', TotalCO
			Escribir '------------------------------------'
			Escribir 'TOTAL A PAGAR: $', TotalCO
			Escribir 'Método de Pago:', PagoET
			Escribir '======================================='
			Escribir '--------- Apuestas echas --------------'
			Escribir "Dinero apostado : $",DineroPa
			Escribir 'Total de dinero ganado : $', TotalGa
			Escribir 'Te retiras con el total de $ ', dinero
			Escribir '===================================='
			Escribir '      ¡Gracias por visitarnos!'
			Escribir '===================================='
		SiNo
			Limpiar Pantalla
			Escribir 'El total a pagar del bar es:  $', TotalCO
			Escribir '========================================'
			Escribir 'El total a pagar del casino es $', DineroPa
			Escribir '======================================='
			Escribir 'Como quieres pagar tu consumo :'
			Escribir '================================'
			Escribir '1.Efectivo'
			Escribir '2.Tarjeta'
			Escribir '-------------------------------'
			Leer Pago
			Si Pago=1 Entonces
				PagoET <- 'Efectivo'
			SiNo
				PagoET <- 'Tarjeta'
			FinSi
			Limpiar Pantalla
			Escribir '===================================='
			Escribir '------- FACTURA DE COMPRA ----------'
			Escribir '===================================='
			Escribir 'Cliente: ', Nombre
			Escribir '------------------------------------'
			Escribir 'Productos: ', TotalUni, ' bebidas '
			Escribir 'Subtotal: $', TotalCO
			Escribir '------------------------------------'
			Escribir 'TOTAL A PAGAR: $', TotalCO
			Escribir 'Método de Pago:', PagoET
			Escribir '======================================='
			Escribir '--------- Apuestas echas --------------'
			Escribir "Dinero apostado : $",DineroPa
			Escribir 'Total de dinero ganado : $', TotalGa
			Escribir 'Te retiras con el total de $ ', dinero
			Escribir '===================================='
			Escribir '      ¡Gracias por visitarnos!'
			Escribir '===================================='
		FinSi
	SiNo
		Escribir '--------------------------------------------------------------------'
		Escribir 'Lo siento, ', Nombre, ' pero no tienes la edad necesaria para ingresar'
		Escribir ':('
		Escribir '--------------------------------------------------------------------'
		Limpiar Pantalla
	FinSi
	Escribir 'Esperamos su regreso ', Nombre
	Escribir '================================'
FinAlgoritmo
