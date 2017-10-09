#BLOQUE DE DEFINICIONES
#FUNCIONES

#ALGORITMO DIA SEMANA: http://eseprimo.blogspot.cl/2005/04/de-la-semana-fue.html
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

def coefAno(ano):
	digitosAno = determinarDigitos(ano)
	digitosAno = digitosAno[2] + digitosAno[3]
	ultimoDigitos = int(digitosAno)
	coef = ultimoDigitos / 4
	coef = coef + ultimoDigitos
	return coef

def coefBisiesto(mes , ano):
	digitosAno = determinarDigitos(ano)
	digito1 = int(digitosAno[2])
	digito2 = int(digitosAno[3])
	coef = digito1 + digito2
	if coef % 4 == 0 and (mes == 1 or mes == 2):
		return -1
	else:
		return 0

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

def esBisiesto(ano):
	digitosAno = determinarDigitos(ano)
	digito1 = int(digitosAno[2])
	digito2 = int(digitosAno[3])
	coef = digito1 + digito2
	if coef % 4 == 0:
		return True
	else: 
		return False

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

def rellenarPrincipio(calendario, mes, diaInicial):
	i = 0
	desplazamiento = determinarDezplazamiento(diaInicial)
	while i < desplazamiento:
		calendario[1].append(" -")
		i+=1
	return calendario

def calcularDiasMes(mes, esBi):
	if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
		return 31
	if mes == 4 or mes == 6 or mes == 9 or mes == 11:
		return 30
	if mes == 2:
		if esBisiesto:
			return 29
		else: 
			return 28

def agregarDia(calendario, numeroDelDia, pos):
	if numeroDelDia < 10:
		numeroAgregado = " "+str(numeroDelDia)
	else:
		numeroAgregado = str(numeroDelDia)
	calendario[pos].append(numeroAgregado)
	return calendario

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

def rellenarFinal(calendario):
	i = 0
	while i < 7:
		if len(calendario[i]) == 7:
			i+=1
		else:
			calendario[i].append(" -")
	return calendario

def rellenarCalendario(diaInicial, mes, esBi, calendario):
	calendario = rellenarPrincipio(calendario, mes, diaInicial)
	calendario = rellenarDias(calendario, mes, esBi)
	calendario = rellenarFinal(calendario) 
	return calendario

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

def ejecutarMenu():
        print "\n\nQue desea hacer: \n"
        print "1) Mostrar dia de semana segun fecha"
        print "2) Visualizar mes"
        print "3) Salir"

        opcion= input("0pcion: ")

        return opcion

def ejecutarOpcion(opcion):
        if opcion == 1:
                print "\nPor favor ingrese la fecha"
                dia = input("Dia: ")
                mes = input("Mes: ")
                ano = input("Anio: ")

                diaSem = diaSemana(dia, mes, ano)
                print "El dia de la semana es: " , diaSem
                opcion=ejecutarMenu()
                ejecutarOpcion(opcion)
                
        elif opcion == 2:
                print "\nPor favor ingrese el mes y el anio"
                mes = input("Mes: ")
                ano = input("Anio: ")
                print "\n"
                visualizarMes(mes, ano)

                opcion=ejecutarMenu()
                ejecutarOpcion(opcion)

        elif opcion == 3:
                return

        else:
                print "\n\n\n\nPor favor ingrese una opcion valida"
                opcion=ejecutarMenu()
                ejecutarOpcion(opcion)
                

#BLOQUE PRINCIPAL
#ENTRADA
print "\nBienvenid@ a 'nombre que le quieran poner a su programa' \n"
opcion=ejecutarMenu()
#PROCESO
ejecutarOpcion(opcion)
#SALIDA
#aun no hay salidas
