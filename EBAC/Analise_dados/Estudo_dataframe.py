import pandas as pd

#Lista de dicionários
dados = [
    {'nome' : 'Ana', 'idade' : 25, 'cidade' : 'Guará'},
    {'nome' : 'Carlos', 'idade' : 29, 'cidade' : 'Aparecida'},
    {'nome' : 'Jones', 'idade' : 30, 'cidade' : 'Joanesburgo'}
]

#Dataframe
dataframe = pd.DataFrame(dados)
print('DataFrame \n', dataframe)

#Selecionar coluna
print(dataframe['nome'])

#Selecionar várias colunas
print(dataframe[['nome','idade']])

#Selecionar linhas pelo índice
print('Primeira Linha \n', dataframe.iloc[0])

#Adicionar novas colunas
dataframe['salario'] = [4100, 3600, 5200]

#Adicionar novo registro
dataframe.loc[len(dataframe)] = {
    'nome':'Samuel',
    'idade' : 25,
    'cidade' : 'RJ',
    'Salário' : '10000'
}

#Removendo uma coluna
dataframe.drop(labels='salario', axis = 1, inplace=True)

#Filtrando pessoas com mais de 29 anos
filtro_idade = dataframe[dataframe['idade'] >= 30]
print('Filtro \n', filtro_idade)

#Salvando o DataFrame em CSV
dataframe.to_csv(path_or_buf='dados.csv', index = False)

#Lendo um arquivo CSV
dataframe_lido = pd.read_csv('dados.csv')
print('\n Leitura do CSV \n', dataframe_lido)






