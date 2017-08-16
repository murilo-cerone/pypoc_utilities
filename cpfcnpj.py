def calc_cpf(cpf_parte):
	if len(cpf_parte)!=9:
		print(cpf_parte+" nao possui 9 digitos!")
		return -1
		
	aux=[11,10,9,8,7,6,5,4,3,2]
	soma=0
	for i in range(0,9):
		soma=soma+(int(cpf_parte[i])*aux[i+1])
	resto=soma%11
	if resto<2:
		digito1=0
	else:
		digito1=11-resto
	
	soma=0
	for i in range(0,10):
		if i==9:
			soma=soma+digito1*aux[i]
		else:
			soma=soma+(int(cpf_parte[i])*aux[i])
	resto=soma%11
	if resto<2:
		digito2=0
	else:
		digito2=11-resto
	
	cpf = cpf_parte+str(digito1)+str(digito2)
	
	return cpf
	
def calc_cnpj(cnpj_parte):
	if(len(cnpj_parte)!=12):
		print(cnpj_parte+" nao possui 12 digitos!")
		return -1
	
	aux=[6,5,4,3,2,9,8,7,6,5,4,3,2]
	soma=0
	for i in range(0,12):
		soma=soma+(int(cnpj_parte[i])*aux[i+1])
	resto=soma%11
	if resto<2:
		digito1=0
	else:
		digito1=11-resto
	
	soma=0
	for i in range(0,13):
		if i==12:
			soma=soma+digito1*aux[i]
		else:
			soma=soma+(int(cnpj_parte[i])*aux[i])
	
	resto=soma%11
	if resto<2:
		digito2=0
	else:
		digito2=11-resto
	
	
	return cnpj_parte+str(digito1)+str(digito2)
	
def valida_cpf(cpf):
		comeco=cpf[:9]
		calculado=calc_cpf(comeco)
		if calculado==cpf:
			return True
		else:
			return False


def print_cpf(cpf):
	if len(cpf)==11:
		return cpf[0:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[9:]
	else:
		return cpf

def valida_cnpj(cnpj):
	if len(cnpj)==14:
		comeco=cnpj[:12]
		calculado=calc_cnpj(comeco)
		if calculado==cnpj:
			return True
		else:
			return False
	else:
		return False
		
def print_cnpj(cnpj):
	if len(cnpj)==14:
		return cnpj[0:2]+"."+cnpj[2:5]+"."+cnpj[5:8]+"/"+cnpj[8:12]+"-"+cnpj[12:]
	else:
		return cnpj