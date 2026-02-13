import pandas as pd
from scipy import stats

pd.set_option('display.width', None) #Removendo limitações de tamanho no display

df = pd.read_csv(r'C:\Users\samco\OneDrive\LP\Repositorios DEV\EBAC_Estudos\EBAC\Tratamento_dados\clientes_limpeza.csv') #lendo o dataframe com o pandas e armazenando na variável df

df_filtro_basico = df[df['idade'] > 100] #Filtrando idades maiores que 100 do df e armazenando na variável filtro_basico

print('Filtro básico \n', df_filtro_basico[['nome', 'idade']])

#IDENTIFICAR OUTLIERS COM Z-score
z_scores = stats.zscore(df['idade']) #Faz os cálculo do quão longe os valores estão da média no campo idade
outliers_z = df[z_scores >= 3] #Armazena em uma variável para visualização os valores de zscore que são iguais ou maiores que 3
print('Outliers pelo Z-score: \n', outliers_z)

#FILTRAR OUTLIERS COM Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)] #Armazena em uma variável os valores do campo idade que possuem desvio padrão <3

#IDENTIFICAR OUTLIERS COM IQR
Q1 = df['idade'].quantile(0.25) #Pega o primeiro quadrante os 25%
Q3 = df['idade'].quantile(0.75) #Pega o terceiro quadrante os 75%
IQR = Q3 - Q1 

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('Limites IQR: ', limite_baixo, limite_alto) #Os limites estão bagunçados, então é bom definir

limite_baixo = 9
limite_alto = 90

#MOSTRANDO OUTLIERS COM IQR 
outliers_iqr = df[(df['idade'] <= limite_baixo) | (df['idade'] >= limite_alto)] #Armazenando na variável os outliers
print('Outliers pelo IQR: \n', outliers_iqr)

#FILTRANDO OUTLIERS COM IQR 
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)] #Armazenando os valores sem ouliers em uma variável

#FILTRAR ENDERECOS INVÁLIDOS
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço invalido' if len(x.split('\n')) < 3 else x) #Para cada valor do endereço escreve 'Endereco invalido' se houver menos de 3 campos entre Ns.(split vai dividir os campos a partir do \n e o len é pra contar a quantidade)

#TRATAR CAMPOS DE TEXTO
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x) #Para cada valor do nome registrar nome invalido se a quantidade de caracteres foi maior que 50 (isinstance(x, str) trata se o campo é do valor texto)
print('Quantidade de registros com nomes grandes: ', (df['nome'] == 'Nome inválido').sum()) #Soma todos os campos que estão com 'Nome inválid' e mostra

print('Dados com Outliers tratados: \n', df) #Exibe o dataframe tratado

#SALVAR DATAFRAME
df.to_csv('clientes_remove_outliers.csv', index=False)





