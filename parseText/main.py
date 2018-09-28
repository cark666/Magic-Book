
conjuros_lista = open('./leer/lista_conjuros.txt', mode='r', encoding='utf-8')
archivo_nuevo=''
nivel =-1
conjuros = 0
posicion= -1
longitud= 0
pos_inicial = -1
pos_final = -1
subcadena = ''
cuenta_dos=0
file = ''
paladin_file=''
while True: 
	linea = conjuros_lista.readline()  # lee línea
	if not linea: 
		break  # Si no hay más se rompe bucle
	if linea.find('Conjuros de bardo') != -1:
		archivo_nuevo = 'bardo.txt'	
		file = open(archivo_nuevo, "w")
	if linea.find('Conjuros de brujo') != -1:
		archivo_nuevo = 'brujo.txt'		
		file.close
		file = open(archivo_nuevo, "w")
	if linea.find('Conjuros de clérigo') != -1:
		archivo_nuevo = 'clérigo.txt'
		file.close
		file = open(archivo_nuevo, "w")		
	if linea.find('Conjuros de druida') != -1:
		archivo_nuevo = 'druida.txt'
		file.close
		file = open(archivo_nuevo, "w")	
	if linea.find('Conjuros de explorador ') != -1:
		archivo_nuevo = 'explorador.txt'
		file.close
		file = open(archivo_nuevo, "w")		
	if linea.find('Conjuros de hechicero') != -1:
		archivo_nuevo = 'hechicero.txt'
		file.close
		file = open(archivo_nuevo, "w")	
	if linea.find('Conjuros de mago') != -1:
		archivo_nuevo = 'mago.txt'
		file.close
		file = open(archivo_nuevo, "w")	
	if linea.find('Conjuros de paladín') != -1:
		archivo_nuevo = 'paladin.txt'	
		file.close
		file = open(archivo_nuevo, "w")
	if linea.find('Conjuros de Chaman') != -1:
		archivo_nuevo = 'chaman.txt'	
		file.close
		file = open(archivo_nuevo, "w")	

	if archivo_nuevo != '':
		if linea.find('Trucos (nivel 0)') != -1:
			longitud = len('Trucos (nivel 0)')
			posicion = linea.find('Trucos (nivel 0)') + longitud
			subcadena = linea[posicion:]	
		if linea.find('Trucos (nivel 0)') == -1:
			subcadena = linea
		
	count = -1;		
	for x in subcadena:
		count = count + 1
		
		if(x.isupper()):		
			cuenta_dos = cuenta_dos + 1
			
			if cuenta_dos == 1:
				pos_inicial = count
					
			if cuenta_dos > 1:
				
				pos_final = count
				file.write(subcadena[pos_inicial:pos_final] +' \n' )
				pos_inicial = count

		if count == len(subcadena)-1:

			file.write(subcadena[pos_inicial:len(subcadena)-1] +' \n' )
			if archivo_nuevo.find('chaman.txt') != -1:
				print("cierrate")
				file.close


conjuros_lista.close
