#Funcines
def aviso():
	clear()
	sistema = os.uname()
	#Aviso sobre necesidad de paquetes
	print('|\t*********************************************************\t|')
	print('|\tEste software necesita los siguientes paquetes:          \t|')
	print('|\t (pip) (xerox) (xclip en linux)                          \t|')
	print('|\t                                                         \t|')
	print('|\t                                                         \t|')
	#Identifica el os
	if "ubuntu" in str(sistema.version).lower():
		print			 ('|\tPresione s para instalarlos automaticamente en Ubuntu    \t|')
		respuesta = input('|\tPresione enter para continuar sin instalarlos            \t|')
		if respuesta.lower() == 's':
			os.system("sudo apt install python3-pip")
			os.system("sudo apt install xclip")
			os.system("pip install xerox")
	elif "fedora" in str(sistema.version).lower():
		print			 ('|\tPresione s para instalarlos automaticamente en fedora    \t|')
		respuesta = input('|\tPresione enter para continuar sin instalarlos            \t|')
		if respuesta.lower() == 's':
			os.system("sudo dnf install python3-pip")
			os.system("sudo dnf install xclip")
			os.system("pip install xerox")
	elif "windows" in str(sistema.version).lower():
		print			 ('|\tPresione s para instalarlos automaticamente en Windows   \t|')
		respuesta = input('|\tPresione enter para continuar sin instalarlos            \t|')
		if respuesta.lower() == 's':
			os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
			os.system("python3 get-pip.py")
	else:
		print('|\tAsegurese de instalarlos antes de ejecutar el programa   \t|')
		print('|\tPresione s para salir                                    \t|')
		respuesta = input('|\tPresione enter para continuar                            \t|')
		

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def help():
	print('|\t******************* -anlleguizamongu- *******************\t|')
	print('|\t                                                         \t|')
	print('|\tÉste software le permitira encriptar o desencriptar el   \t|')
	print('|\ttexto que usted desee usando el cifrado de Cesar.        \t|')
	print('|\tTambien en caso de que lo requiera, tendra una explicaci-\t|')
	print('|\ton sencilla de su funcionamineto                         \t|')
	print('|\t                                                         \t|')
	print('|\tLas opciones son las siguientes:                         \t|')
	print('|\t                                                         \t|')
	print('|\tE / e: Para encriptar un texto.                          \t|')
	print('|\tD / d: Para desencriptar un texto.                       \t|')
	print('|\tO / o: Para ver este menú nuevamente.                    \t|')
	print('|\tX / x: Para una explicacion y ejemplo.                   \t|')
	print('|\tS / s: Le permitira salir del programa. CTRL+C tambien.  \t|')
	print('|\t                                                         \t|')
	print('|\tAlgunos caracteres no pueden ser encriptados             \t|')
	print('|\t                                                         \t|')
	print('|\tAl momento de ingresar una llave, si no ingresa ningun   \t|')
	print('|\tvalor, se usará la llave por defecto 3 o la ingresada    \t|')
	print('|\tanteriormente. Esta debe ser un numero entre 0 y 27.     \t|')
	print('|\t                                                         \t|')
	print('|\tPresione Enter para continuar                            \t|')
	input('|\t*********************************************************\t|')
	clear()

def inicio():
	clear()
	print('|\t*********************************************************\t|')
	print('|\t**** Bienvenido al software de encriptacion de Cesar ****\t|')
	print('|\t*********************************************************\t|')
	print('|\t                                                         \t|')
	print('|\t            (O/o para ver todas las opciones)            \t|')
	print('|\t                                                         \t|')
	print('|\t*************** ¿Que tarea desea realizar? **************\t|')

def menu():
	while True:
		inicio()
		tarea = input('|\t(e/d/o/x/s)                                             \t|: ')
		if	(tarea=='e' or tarea == 'E'):
			clear()
			llave('|\t********************* Encriptacion **********************\t|')
			encriptar()

		elif(tarea=='d' or tarea == 'D'):
			clear()
			llave('|\t******************** Desencriptacion ********************\t|')
			desencriptar()

		elif(tarea=='o' or tarea == 'O'):
			clear()
			help()

		elif(tarea=='x' or tarea == 'X'):
			clear()
			print_alfabeto()

		elif(tarea=='s' or tarea == 'S'):
			break
		else:
			input('|\tOpcion no valida. Intente nuevamente                     \t|')
			clear()

def llave(head):
	global key
	while True:
		print(head)
		nkey = input('|\tIngrese la llave a usar:                                 \t|: ')
		if nkey == '':
			print(f'|\tSe usará la llave por defecto {key}                        \t\t|')
			return
		try:
			nkey = int(nkey)
			if nkey > 27 or nkey < 0:
				input('|\tNumero fuera de rango, debe estar entre 0 y 27           \t|')
				clear()
			else:	
				key = nkey
				print(f'|\tSe usará la llave: {key}                                 \t\t|')
				break
		except ValueError:
			input('|\t¡No es un numero entero! Intenta nuevamente               \t|')
			clear()

def print_alfabeto():
	global alfabeto
	global tildes
	global digitos
	global caracteres
	global key

	alf  = '|'
	nAlf = '|'
	til  = '|'
	ntil = '|'
	num	 = '|'
	nnum = '|'
	car	 = '|'
	ncar = '|'

	#Muestra el desplazamiento en todos los alfabetos
	for i in range(0,27):
		alf = alf + alfabeto[i] + '|'
		nAlf = nAlf + alfabeto[(i+key)%27] + '|'
		if i <10:
			til  = til  + tildes[i] + '|'
			ntil = ntil + tildes[(i+key)%10] + '|'
			num  = num  + digitos[i] + '|'
			nnum = nnum + digitos[(i+key)%10] + '|'
		else:
			til  = til  + '░' + '|'
			ntil = ntil + '░' + '|'
			num	 = num  + '░' + '|'
			nnum = nnum + '░' + '|'
		if i < 23:
			car  = car  + caracteres[i] + '|'
			ncar = ncar + caracteres[(i+key)%23] + '|'
		else:
			car  = car  + '░' + '|'
			ncar = ncar + '░' + '|'

	print('|\t*********************** Alfabeto ************************\t|')
	print(f'|\tLlave actual: {key}                                     \t\t|')
	print('|\t ┌-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┬-┐ \t|')
	print('|\t |1|2|3|4|5|6|7|8|9|1|1|1|1|1|1|1|1|1|1|2|2|2|2|2|2|2|2| \t|')
	print('|\t | | | | | | | | | |0|1|2|3|4|5|6|7|8|9|0|1|2|3|4|5|6|7| \t|')
	print('|\t |-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-| \t|')
	print(f'|\t {alf} \t|')
	print('|\t |-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-| \t|')
	print(f'|\t {nAlf} \t|')
	print('|\t |-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-| \t|')
	print(f'|\t {til} \t|')
	print('|\t |-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-| \t|')
	print(f'|\t {ntil} \t|')
	print('|\t |-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-| \t|')
	print(f'|\t {num} \t|')
	print('|\t |-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-| \t|')
	print(f'|\t {nnum} \t|')
	print('|\t |-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-| \t|')
	print(f'|\t {car} \t|')
	print('|\t |-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-┼-| \t|')
	print(f'|\t {ncar} \t|')
	print('|\t └-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┴-┘ \t|')
	return

def encriptar():
	global alfabeto
	#Ingreso de texto
	print('|\tIngrese el texto a procesar:                            \t|')
	texto = input('|\t')
	cifrado = ''
	#Recorre cada caracter en la cadena suministrada
	for c in texto:
		#Guarda el estado de mayuscula por cada caracter
		mayus = False
		if c.isupper(): mayus = True
		c = c.lower()
		#Busca el elemento en la lista del alfabeto
		if c in alfabeto:					#Reemplaza el simbolo							
			indice = alfabeto.index(c)
			nc = alfabeto[(indice+key)%27]
			if mayus : nc = nc.capitalize() #Vuelve a colocarlo en mayuscula
			cifrado=cifrado+nc
		elif c in tildes: 					#Cifra el tilde con el mismo metodo
			indice = tildes.index(c)
			nc = tildes[(indice+key)%10]
			cifrado=cifrado+nc
		elif c in digitos:					#Cifra el numero con el mismo metodo
			indice = digitos.index(c)
			nc = digitos[(indice+key)%10]
			cifrado=cifrado+nc
		elif c in caracteres:				#Cifra el caracter con el mismo metodo
			indice = caracteres.index(c)
			nc = caracteres[(indice+key)%23]
			cifrado=cifrado+nc
		else:
			cifrado=cifrado+c				#Si no esta coloca el mismo simbolo
	xerox.copy(cifrado)
	if len(texto) <= 57:
		texto	= texto.ljust(57) + '\t|'
		cifrado = cifrado.ljust(57) + '\t|'

	print_alfabeto()
	print('|\t*********************** Resultado ***********************\t|')
	print('|\tTexto original:                                          \t|')
	print(f'|\t{texto}')
	print('|\tTexto procesado:                                         \t|')
	print(f'|\t{cifrado}')
	print('|\t                                                         \t|')
	print('|\tTexto procesado copiado en el portapapeles.              \t|')
	input('|\tPresione Enter para continuar                            \t|')
	return

def desencriptar():
	global key
	#Al ser el mismo proceso inverso, solo invierto el valor de la key
	key = key * -1
	encriptar()
	key = key * -1
	return

#Variables
alfabeto	= [ 'a','b','c','d','e','f','g','h','i',
	    	 'j','k','l','m','n','ñ','o','p','q',
			 'r','s','t','u','v','w','x','y','z']
digitos		= ['1','2','3','4','5','6','7','8','9','0']
tildes		= ['á','é','í','ó','ú','ä','ë','ï','ö','ü']
caracteres	= ['|','_','+','-','*','/','\\','\'','"','=',
	      	   '.',',',':',';','(',')','¿' ,'?' ,'¡','!',
			   '#','$','&']

key = 3
texto_ejemplo = 'Esto es un texto de ejemplo'

#Main
import os
aviso()
import xerox
menu()
clear()
exit()