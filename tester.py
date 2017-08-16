import cpfcnpj as dg

cpf=dg.calc_cpf("101023987")
print(cpf)
print(dg.valida_cpf(cpf))
print(dg.print_cpf(cpf))

cnpj = dg.calc_cnpj("112223330001")
print(cnpj)
print(dg.valida_cnpj(cnpj))
print(dg.print_cnpj(cnpj))
