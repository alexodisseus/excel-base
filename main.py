import model

import pandas as pd

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'asd/cotistas.xlsx'

# Carregando a planilha do Excel em um DataFrame do pandas
dados_excel = pd.read_excel(nome_arquivo)


"""
dados_excel = pd.read_excel(nome_arquivo, sheet_name='COTISTAS')
# Substitua 'indice_da_linha' pelo índice real da linha que você deseja acessar
coluna_especifica = dados_excel['Nome']
"""

q = dados_excel.shape[0]

for x in range(0,q):
	nome = dados_excel.at[x, 'Nome']
	codigo = dados_excel.at[x, 'Código']
	endereço = dados_excel.at[x, 'Endereço']
	Documento = dados_excel.at[x, 'Documento']
	Documento = str(Documento)
	Cidade = dados_excel.at[x, 'Cidade']
	Estado = dados_excel.at[x, 'Estado']
	Banco = dados_excel.at[x, 'Banco']
	Banco = str(Banco)
	Agencia = dados_excel.at[x, 'Agencia']
	Agencia = str(Agencia)
	Conta = dados_excel.at[x, 'Conta']
	Conta = str(Conta)
	Cep1 = dados_excel.at[x, 'Cep1']
	print(type(Cep1))
	Cep2 = dados_excel.at[x, 'Cep2']
	"""
	if 'nan' in Cep1:
		Cep1 = 00000
	if Cep2 == 'nan':
		Cep2 = 00000
	"""
	Cep1 = str(int(Cep1))
	Cep2 = str(int(Cep2))
	
	if len(Cep1) == 4:
		Cep1 = "0"+Cep1
	if len(Cep1) == 3:
		Cep1 = "00"+Cep1
	if len(Cep1) == 2:
		Cep1 = "000"+Cep1
	
	if len(Cep2) == 1:
		Cep2 = "00"+Cep2
	if len(Cep2) == 2:
		Cep2 = "0"+Cep2

	cep = Cep1+"-"+str(Cep2)
	rua = endereço.split(",")
	if len(rua)>1:
		numero_rua = rua[1]
	else:
		numero_rua = ''


	print(nome.strip())
	print(Documento.replace('_x0000_', ''))


	print(int(codigo))
	print(rua[0])
	print(str(numero_rua))
	print(cep)
	print(Cidade)
	print(Estado)
	print(Banco.replace('nan', ''))
	print(Agencia.replace('nan', ''))
	print(Conta.replace('nan', ''))







	model.push_shareholder(nome.strip() , '' , Documento.replace('_x0000_', ''), '', '' , '' , str(int(codigo)) , rua[0] , str(numero_rua) ,cep , Cidade , Estado , Banco.replace('nan', '') , Agencia.replace('nan', '') , Conta.replace('nan', ''))

# Obtendo a quantidade de linhas usando a propriedade shape



#Código	
#Nome	
#Endereço	
#Cidade	
#Estado	
#Cep1	
#Cep2	
#FisJur	
#SujeitoIR	
#Documento	
#Banco	
#Agencia	
#Conta	
#CodFolha	
#Implantado	
#Pagamento



