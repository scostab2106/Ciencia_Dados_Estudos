import pandas as pd


df = pd.read_csv(r'C:\Users\samco\OneDrive\LP\Repositorios DEV\EBAC_Estudos\EBAC\Tratamento_dados\clientesruim.csv')



# Verificar os primeiros registros
print(df.head().to_string())

# Verificar os últimos registros
print(df.tail().to_string())

# Verificar quantidade de linhas e colunas
print('Qtd: ', df.shape)

# Verificar tipos de dados
print('Tipo dos dados', df.dtypes)

# Checagem de valores nulos
print('Valores nulos: \n', df.isnull().sum())

 
