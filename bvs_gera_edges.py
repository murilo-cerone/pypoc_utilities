import random

id=100
fhand=open('edges.ope','w')
for i in range(1,10):
	#print("CPF de id: "+str(i))
	numero_empresas=random.randint(1,7)
	for j in range(1,numero_empresas):
		id=id+1
		empresa=random.randint(11,29)
		#print("socio/a da :" +str(empresa))
		linha=str(id)+","+str(i)+","+str(empresa)+",socio,"+" "+",,,,"
		fhand.write(linha+"\n")
		print(linha)

fhand.close()