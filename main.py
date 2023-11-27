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


nome = dados_excel.at[0, 'Nome']

print(nome)

# Obtendo a quantidade de linhas usando a propriedade shape
quantidade_linhas = dados_excel.shape[0]
print("Quantidade de linhas:", quantidade_linhas)



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



