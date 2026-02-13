import pandas as pd


df = pd.read_csv(r'C:\Users\samco\OneDrive\LP\Repositorios DEV\EBAC_Estudos\EBAC\Tratamento_dados\clientesruim.csv')

pd.set_option('display.width', None)
print(df.head()) 

#REMOVER DADOS(inplace=True faz as mudanças diretoo no seu dataframe sem criar outro)
df.drop(labels='pais', axis=1, inplace=True) # Axis1 = Coluna
df.drop(labels=2, axis=0, inplace=True) #Axis0 = Linha

#NORMALIZAR CAMPOS DE TEXTO
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

#CONVERTER TIPOS DE DADOS
df['idade'] = df['idade'].astype(int)

#TRATAR VALORES NULOS/AUSENTES
print('Valores nulos:\n', df.isnull().sum()) #Mostrar campos com valores nulos

df_fillna = df.fillna(0) #Substitui valores nulos por 0
df_dropna = df.dropna() #Remove registros com valores nulos
df_dropna4 = df.dropna(thresh=4) #Manter registros com no mínimo 4 valores não nulos
df = df.dropna(subset=['cpf']) #Remover registros com cpf nulo, apenas esta está executando no dataframe de fato


print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum().sum()) #.sum().sum() soma todos os valores que estão separados em uma linha para ver o total
print('Qtd de registros nulos com dropna:', df_dropna.isnull().sum().sum())
print('Qtd de registros nulos com dropna4:', df_dropna4.isnull().sum().sum())
print('Qtd de registros nulos com CPF:', df.isnull().sum().sum())
 
df.fillna(value={'estado': 'Desconhecido'}, inplace=True) #Todo campo do estado que for nulo vai substituir por desconhecido
df['endereco'] = df['endereco'].fillna('Endereço não informado') #Outra forma de fazer(criando novo campo no df), substitiu enderecos nulos pela string endereco nao informado
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean()) #Transformar idades nulas na média de todas as idades

#TRATAR FORMATO DOS DADOS
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') #errors=coerce = se tiver erro gera o valor nulo

#TRATAR VALORES DUPLICADOS
print('Quantidade de registros atual: ', df.shape[0]) #shape[0] mostra so as linhas
df.drop_duplicates(subset='cpf', inplace=True) #Removendo cpfs duplicados
print('Quantidade de registros removendo duplicatas: ', len(df))

print('Dados Limpos:\n', df)


#SALVAR DATAFRAME
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome','cpf','idade','data','endereco','estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo Dataframe: \n', pd.read_csv('clientes_limpeza.csv'))

