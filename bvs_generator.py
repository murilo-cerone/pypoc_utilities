import cpfcnpj as dg
import random

status_pessoa=["negativada","nao negativada"]
status_cnpj=["ativa","inativa"]
status_empresa=["ok","acao na justica","recuperacao judicial"]

#<id>,<atributo>,<tipo_atributo>,<string>,<numero>,<timestamp>

fhand=open("entidades.opv",'w')

for i in range(1,10):
	id=i
	cpf_base=370000000+i
	cpf=dg.calc_cpf(str(cpf_base))
	print(str(id)+",cpf,1,"+str(cpf)+",,")
	l1=str(id)+",cpf,1,"+str(cpf)+",,"
	nome="pf"+str(i)
	print(str(id)+",nome,1,"+nome+",,")
	l2=str(id)+",nome,1,"+nome+",,"
	x=random.random()
	if 10*x<1:
		status=status_pessoa[0]
	else:
		status=status_pessoa[1]
	print(str(id)+",status,1,"+status+",,")
	l3=str(id)+",status,1,"+status+",,"
	fhand.write(l1+"\n")
	fhand.write(l2+"\n")
	fhand.write(l3+"\n")
	
	
for i in range(1,20):
	id=i+10
	cnpj_base=str(11000000+int(i+100*random.random()))+str("0001")
	cnpj=dg.calc_cnpj(cnpj_base)
	print(str(id)+",cnpj,1,"+str(cnpj)+",,")
	l1=str(id)+",cnpj,1,"+str(cnpj)+",,"
	x=random.random()
	if 10*x<0.5:
		status=status_cnpj[1]
	else:
		status=status_cnpj[0]
	print(str(id)+",atividade,1,"+status+",,")
	l2=str(id)+",atividade,1,"+status+",,"
	
	x=random.random()
	if 10*x<0.5:
		status=status_empresa[2]
	elif 10*x>=0.5 and 10*x<1:
		status=status_empresa[1]
	else:
		status=status_empresa[0]
	
	print(str(id)+",situacao,1,"+status+",,")
	l3=str(id)+",situacao,1,"+status+",,"
	fhand.write(l1+"\n")
	fhand.write(l2+"\n")
	fhand.write(l3+"\n")
	
	
fhand.close()