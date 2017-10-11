#BLOQUE DE DEFINICIONES
#FUNCIONES

#ALGORITMO DIA SEMANA: http://eseprimo.blogspot.cl/2005/04/de-la-semana-fue.html

#1
#Funcion que transforma el año a string, agregando 0 a la izquierda de ser necesario para que tenga un largo de 4
#Entrada: Numero correspondiente al anio
#Salida: String del anio
def determinarDigitos(ano):
	digitosAno = str(ano)
	if len(digitosAno) == 4:
		return digitosAno
	if len(digitosAno) == 3:
		digitosAno = "0" + digitosAno
		return digitosAno
	if len(digitosAno) == 2:
		digitosAno = "00" + digitosAno
		return digitosAno
	if len(digitosAno) == 1:
		digitosAno = "000" + digitosAno
		return digitosAno

#2
#Funcion que determina el coeficiente del siglo al que pertenece el anio de acuerdo al algoritmo para determinar el dia de la semana
#Entrada: Numero correspondiente al anio al anio ingresado
#Salida: Numero correspondiente al siglo que pertence ese anio
def coefSiglo(ano):
	inicioSiglo = 0
	finSiglo = 99
	coefi = 39
	while not(inicioSiglo <= ano and finSiglo >= ano):
		if inicioSiglo == 1900 and finSiglo == 1999:
			coefi = coefi - 1
		else:
			coefi = coefi - 2
		inicioSiglo = finSiglo + 1
		finSiglo = inicioSiglo + 99
	
	return coefi

#3
#Funcion que determina apartir del anio ingresado, el segundo coeficiente del algoritmo para obtener el dia de la semana
#Entrada: Numero correspondiente al anio ingresado
#Salida: Numero correspondiente al segundo coeficiente del algoritmo
def coefAno(ano):
	digitosAno = determinarDigitos(ano)
	digitosAno = digitosAno[2] + digitosAno[3]
	ultimoDigitos = int(digitosAno)
	coef = ultimoDigitos / 4
	coef = coef + ultimoDigitos
	return coef

#4
#Funcion que determina el tercer coeficiente, a partir del mes y anio ingresado, del algoritmo para obtener el dia de la semana
#Entrada: -Numero correspondiente al mes ingresado
#	  -Numero correspondiente al anio ingresado
#Salida: Numero correspondiente al coeficiente determinado por el algoritmo
def coefBisiesto(mes , ano):
	if esBisiesto(ano) and (mes == 1 or mes == 2):
		return -1
	else:
		return 0

#5
#Funcion que determinar el cuarto coeficiente a partir del mes, correspondiente al algoritmo para obtener el dia de la semana
#Entrada: Numero correspondiente al mes ingresado
#Salida: Numero correspondiente al coeficiente determinado por el algoritmo
def coefMes(mes):
	if mes == 1 or mes == 10:
		return 6
	if mes == 4 or mes == 7:
		return 5
	if mes == 2 or mes == 3 or mes == 11:
		return 2
	if mes == 5:
		return 0
	if mes == 6:
		return 3
	if mes == 9 or mes == 12:
		return 4
	if mes == 8:
		return 1

#6
#Funcion que determina el dia de acuerdo al coeficiente resultante del algoritmo para obtener el dia de la semana
#Entrada: Numero correspondiente al coeficiente resultante del algoritmo
#Salida: String correspondiente al nombre del dia de la semana
def coefDeterminarDia(numero):
	if numero == 1:
		return "Lunes"
	if numero == 2:
		return "Martes"
	if numero == 3:
		return "Miercoles"
	if numero == 4:
		return "Jueves"
	if numero == 5:
		return "Viernes"
	if numero == 6:
		return "Sabado"
	if numero == 0:
		return "Domingo"

#7
#Funcion que realiza el proceso para obtener el dia de la semana a partir del algoritmo
#Entrada: -Numero correspondiente al dia ingresado
#	  -Numero correspondiente al mes ingresado
#	  -Numero correspondiente al anio ingresado
#Salida: String con el nombre del dia de la semana de la fecha ingresa
def diaSemana(dia , mes, ano):
	A = coefSiglo(ano)
	B = coefAno(ano)
	C = coefBisiesto(mes, ano)
	D = coefMes(mes)
	E = dia
	coef = A + B + C + D + E
	coef = coef % 7
	dia = coefDeterminarDia(coef)
	return dia

#8
#Funcion que respodne a la consulta si un anio es bisiesto, retornando un booleano a dicha consulta
#Entrada: Numero correspondiente al anio que se desea consultar
#Salida: Booleano -True: si es un anio bisiesto
#		  -False: si no es un anio bisiesto
def esBisiesto(ano):
	if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
		return True
	else: 
		return False

#9
#Funcion que a partir del dia que inicia el mes devuelve la cantidad a rellenar en la primera lista correspondiente de los dias de dicho mes
#Entrada: String correspondiente al dia en que inicia el mes
#Salida: Numero correspondiente a la catidad a desplzarse antes de colocar el primer dia del mes
def determinarDezplazamiento(inicioMes):
	if inicioMes == "Lunes":
		return 0
	if inicioMes == "Martes":
		return 1
	if inicioMes == "Miercoles":
		return 2
	if inicioMes == "Jueves":
		return 3
	if inicioMes == "Viernes":
		return 4
	if inicioMes == "Sabado":
		return 5
	if inicioMes == "Domingo":
		return 6

#10
#Funcion que rellena con guiones los primeros dias de la semana que no corresponde a dicho mes
#Entrada: -Calendario: Lista de lista correspondiente a la matriz del mes
#	  -Mes: Numero correspondiente al mes ingresado
#	  -diaInicial: String correspondiente al dia de al semana con el que comienza el mes
#Salida: Lista de lista correspondiente al calendario, rellenado con los guiones necesarios en la primera fila de los dias de la semana
def rellenarPrincipio(calendario, mes, diaInicial):
	i = 0
	desplazamiento = determinarDezplazamiento(diaInicial)
	while i < desplazamiento:
		calendario[1].append(" -")
		i+=1
	return calendario

#11
#Funcion que a partir del mes y si es bisiesto, determinar la cantidad de dias que este posee
#Entrada: Mes: Numero correspondiente al mes ingresado
#	  esBi: Booleano que indica que el mes es bisiesto o no
#Salida: Numero que indica la cantidad de dias que posee el mes   
def calcularDiasMes(mes, esBi):
	if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
		return 31
	if mes == 4 or mes == 6 or mes == 9 or mes == 11:
		return 30
	if mes == 2:
		if esBi:
			return 29
		else: 
			return 28

#12
#Funcion que transforma el numero del dia a string y lo agrega a la matriz del calendario
#Entrada: calendario: lista de lista correspondiente a la matriz del calendario
#	  numeroDelDia: Numero correspondiente al dia que se desea agregar
#	  pos: Numero que indica la posicion de la lista de la matriz que se desea agregar el dia
#Salida: lista de lista correspondiente al calendario con el dia agregado en la posicion correspondiente
def agregarDia(calendario, numeroDelDia, pos):
	if numeroDelDia < 10:
		numeroAgregado = " "+str(numeroDelDia)
	else:
		numeroAgregado = str(numeroDelDia)
	calendario[pos].append(numeroAgregado)
	return calendario

#13
#Funcion que agrega todo los dias del mes a la lista de lista correspondiente a la matriz del calendario
#Entrada: -Calendario: Lista de lista correspondiente a la matriz del mes
#	  -mes: numero del es ingresado
#	  -esBi: booleano que indica si el "mes" es bisiesto
#Salida: Lista de lista correspondiente a la matriz del mes con los dias agregados
def rellenarDias(calendario, mes, esBi):
	diasDelMes = calcularDiasMes(mes, esBi)
	numeroDia = 1
	i = 1
	while numeroDia <= diasDelMes:
		if len(calendario[i]) == 7:
			i+=1
		calendario = agregarDia(calendario, numeroDia, i)
		numeroDia +=1
	return calendario

#14
#Funcion que rellena con guiones los elementos restantes de la matriz, para que las listas posean una simetria en la cantidad de elementos
#Entrada: Calendario: lista de lista correspondiente a la matriz del mes con los dias ya agregados
#Salida: lista de lista correspondiente a la matriz rellenada completamente
def rellenarFinal(calendario):
	i = 0
	while i < 7:
		if len(calendario[i]) == 7:
			i+=1
		else:
			calendario[i].append(" -")
	return calendario

#15
#Funcion que rellena de princio a fin la lista de lista correspondiente a la matriz del mes
#Entrada: diaInicial: String con el nombre del dia de la semana que inicia el "mes"
#	  mes: Numero que indica que el mes ingresado
#	  esBi: Booleano que indica si el "mes" es bisiesto o no
#	  calendario: Lista de lista correspondiente a la matriz del mes sin rellenar
#Salida: Lista de lista correspondiente a la matriz del mes rellena con lso dias y guiones necesarios
def rellenarCalendario(diaInicial, mes, esBi, calendario):
	calendario = rellenarPrincipio(calendario, mes, diaInicial)
	calendario = rellenarDias(calendario, mes, esBi)
	calendario = rellenarFinal(calendario) 
	return calendario

#16
#Funcion que imprime el titulo del mes que se visualizara por pantalla
#Entrada: mes: Numero correspondiente al mes ingresado
#	  ano: Numero correspondiente al anio ingresado
#Salida: ---
def imprimirTituloMes(mes, ano):
	anio = determinarDigitos(ano)
	if mes == 1:
		print "-----------ENERO---------",anio,"-----------"
	if mes == 2:
		print "-----------FEBRERO-------",anio,"-----------"
	if mes == 3:
		print "-----------MARZO---------",anio,"-----------"
	if mes == 4:
		print "-----------ABRIL---------",anio,"-----------"
	if mes == 5:
		print "-----------MAYO----------",anio,"-----------"
	if mes == 6:
		print "-----------JUNIO---------",anio,"-----------"
	if mes == 7:
		print "-----------JULIO---------",anio,"-----------"
	if mes == 8:
		print "-----------AGOSTO--------",anio,"-----------"
	if mes == 9:
		print "-----------SEPTIEMBRE----",anio,"-----------"
	if mes == 10:
		print "-----------OCTUBRE-------",anio,"-----------"
	if mes == 11:
		print "-----------NOVIEMBRE-----",anio,"-----------"
	if mes == 12:
		print "-----------DICIEMBRE-----",anio,"-----------"
	return

#17
#Funcion que imprime las listas de la matriz para visualizar por pantalla el mes
#Entarda: mes: Numero correspondiente al mes ingresado
#	  ano: Numero correspondiente al anio ingresado
#Salida: ---
def visualizarMes(mes, ano):
	calendario = [[' L',' M',' M',' J',' V',' S',' D'],[],[],[],[],[],[]]
	diaInicial = diaSemana(1, mes, ano)
	esBi = esBisiesto(ano)
	calendario = rellenarCalendario(diaInicial, mes, esBi, calendario)
	i = 0
	imprimirTituloMes(mes, ano)
	while i < 7:
		print calendario[i]
		i+=1
	return

#18
#Funcion que imprime la opciones por pantalla y solicita el ingreso de una de ella
#Entrada: ---
#Retorna: Numero correspondiente a la opcion escogida
def ejecutarMenu():
        print "\n\nQue desea hacer: \n"
        print "1) Mostrar dia de semana segun fecha"
        print "2) Visualizar mes"
        print "3) Salir"

        opcion= raw_input("0pcion: ")

        return opcion

#19
#Funcion que recibe la opcion y ejecuta el caso necesario para dicha opcion
#Entrada: Numero correspondiente a la opcion escogida por el usuario
#Salida: (Hasta que se ejecute la opcion 3) se retornara nada
def ejecutarOpcion(opcion):
        if opcion.isdigit():
                opcion=int(opcion)
                if opcion == 1:
                        print "\nPor favor ingrese la fecha"
                        dia = raw_input("Dia: ")
                        if dia.isdigit():
                                dia=int(dia)
                        else:
                                print "Por favor ingresar solo numeros"
                                opcion=ejecutarMenu()
                                ejecutarOpcion(opcion)
                                
                        mes = raw_input("Mes: ")
                        if mes.isdigit():
                                mes=int(mes)
                        else:
                                print "Por favor ingresar solo numeros"
                                opcion=ejecutarMenu()
                                ejecutarOpcion(opcion)

                        ano = raw_input("Anio: ")
                        if ano.isdigit():
                                ano=int(ano)
                        else:
                                print "Por favor ingresar solo numeros"
                                opcion=ejecutarMenu()
                                ejecutarOpcion(opcion)

                        diaSem = diaSemana(dia, mes, ano)
                        print "El dia de la semana es: " , diaSem
                        opcion=ejecutarMenu()
                        ejecutarOpcion(opcion)
                        
                elif opcion == 2:
                        print "\nPor favor ingrese el mes y el anio"
                        mes = raw_input("Mes: ")
                        if mes.isdigit():
                                mes=int(mes)
                        else:
                                print "Por favor ingresar solo numeros"
                                opcion=ejecutarMenu()
                                ejecutarOpcion(opcion)

                        ano = raw_input("Anio: ")
                        if ano.isdigit():
                                ano=int(ano)
                        else:
                                print "Por favor ingresar solo numeros"
                                opcion=ejecutarMenu()
                                ejecutarOpcion(opcion)

                        visualizarMes(mes, ano)

                        opcion=ejecutarMenu()
                        ejecutarOpcion(opcion)

                elif opcion == 3:
                        return

                else:
                        print "\n\n\n\nPor favor ingrese una opcion valida"
                        opcion=ejecutarMenu()
                        ejecutarOpcion(opcion)
        else:
                print "Por favor ingresar solo numeros"
                opcion=ejecutarMenu()
                ejecutarOpcion(opcion)
                

#BLOQUE PRINCIPAL
#ENTRADA
print "\nBienvenid@ a Agenda USACH \n"
opcion=ejecutarMenu()
#PROCESO
ejecutarOpcion(opcion)
#SALIDA
#aun no hay salidas
