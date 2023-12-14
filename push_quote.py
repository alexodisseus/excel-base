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
	

	SujeitoIR = dados_excel.at[x, 'SujeitoIR']
	codigo = dados_excel.at[x, 'Código']

	cod = int(codigo)

	'''
	print(SujeitoIR)
	print(cod)
	'''
	
	model.push_imposto(cod , SujeitoIR)
		

#Numero	
#Situação	
#Cotista	
#Cotas	
#Data_Aquis	
#Mes_Transf	
#Ano_Transf	
#Cotista2
