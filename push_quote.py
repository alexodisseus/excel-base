import model

import pandas as pd

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'asd/titulo.xlsx'

# Carregando a planilha do Excel em um DataFrame do pandas
dados_excel = pd.read_excel(nome_arquivo)


"""
dados_excel = pd.read_excel(nome_arquivo, sheet_name='COTISTAS')
# Substitua 'indice_da_linha' pelo índice real da linha que você deseja acessar
coluna_especifica = dados_excel['Nome']
"""

q = dados_excel.shape[0]

for x in range(0,q):
	numero = dados_excel.at[x, 'Numero']
	Situacao = dados_excel.at[x, 'Situação']
	Cotista = dados_excel.at[x, 'Cotista']
	Cotas = dados_excel.at[x, 'Cotas']

	Data_Aquis = dados_excel.at[x, 'Data_Aquis']
	Data_Aquis = str(Data_Aquis)
	Data_Aquis = Data_Aquis.split(" ")
	Data_Aquis = Data_Aquis[0]

	Cotista2 = dados_excel.at[x, 'Cotista2']
	Cotista2 = str(Cotista2)
	Cotista2 = Cotista2.split('.')
	Cotista2 = Cotista2[0]


	
	print(numero)
	print(Situacao)
	print(Data_Aquis)
	print(Cotista2)
	
	print(Cotas)
	print(Cotista)
	
	
	if Situacao == "T":
		model.push_quote(numero, Situacao,Data_Aquis, Cotista, Cotas, Cotista2)
		

#Numero	
#Situação	
#Cotista	
#Cotas	
#Data_Aquis	
#Mes_Transf	
#Ano_Transf	
#Cotista2
