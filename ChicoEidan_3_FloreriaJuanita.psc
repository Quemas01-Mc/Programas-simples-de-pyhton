Algoritmo ChicoEidan_2_FloreriaJuanita
	Definir Flores Como Entero
	Definir amarilla Como Entero
	Definir azul Como Entero
	Definir rojas Como Entero
	Escribir '........................'
	Escribir 'Bienvenido ala floreria'
	Escribir '........................'
	Escribir 'Como te llamas:'
	Escribir '........................'
	Leer Nombre
	Repetir
		Escribir '..........................'
		Escribir 'Que flores deseas comprar:'
		Escribir '............................'
		Escribir '1.Flores rojas : $4.30'
		Escribir '2.Flores amarillas : $5.90'
		Escribir '3.Flores azules : $2.40'
		Escribir '.............................'
		Leer Flores
		Escribir '..............................'
		Si Flores=1 Entonces
			Escribir 'Cuantas flores quieres llevar :'
			Escribir '................................'
			Leer rojas
			TotalR <- rojas*4.30
		FinSi
		Si Flores=2 Entonces
			Escribir 'Cuantas flores quieres llevar :'
			Escribir '................................'
			Leer azul
			TotalR <- azul*5.90
		FinSi
		Si Flores=3 Entonces
			Escribir 'Cuantas flores quieres llevar :'
			Escribir '................................'
			Leer amarillas
			TotalR <- amarillas*2.40
		FinSi
		Si TotalR>50 Entonces
			Escribir '................................'
			Escribir 'Se le aplico un descuento'
			Escribir '................................'
			Descuento <- TotalR*0.1
			Td <- TotalR-Descuento
			Escribir 'El total de su compra :  ', Td
			Escribir '........................................'
			Escribir 'Muchas gracias por su compra', Nombre
			Escribir '........................................'
		SiNo
			Escribir 'El total de su compra :  ', TotalR
			Escribir '........................................'
			Escribir "Muchas gracias por su compra : ", Nombre
			Escribir '........................................'
		FinSi
		Escribir 'Quieres comprar algo mas s/n'
		Escribir '........................................'
		Leer Op
	Hasta Que Op='n'
	Escribir '......................................'
	Escribir '-Gracias por comprar en la floreria -'
	Escribir '......................................'
FinAlgoritmo
