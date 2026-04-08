install.packages("readr") # Necessário para ler arquivos CSV

install.packages("readxl") # Necessário para ler arquivos XLSX


# Carregando os pacotes
# library(readr)
# library(readxl)

# Ler arquivo CSV com a função read.csv()

dados <- read.csv("C:/Users/samco/OneDrive/LP/Repositorios DEV/EBAC_Estudos/EBAC/Estatistica/ESPORTISTAS_MOD7.csv", sep=";") # nolint

# Visualizar os dados
head(dados)

# 1 - MÉDIA

mean(dados$Ganhos_Totais) # O operador $ é usado para acessar uma coluna específica em um dataframe.

# Mesma operação mas agrupando por esporte

aggregate(Ganhos_Totais ~ Esporte, data = dados, FUN = mean)
# aggragate é semelhante ao groupby no python
# ~ especifica que queremos agrupar os dados por esporte e calcular a média dos ganhos totais para cada grupo
# FUN = mean especifica que queremos calcular a média dos valores em cada grupo


# 2 - MEDIANA

median(dados$Ganhos_Totais)

aggregate(Ganhos_Totais ~ Esporte, data = dados, FUN = median)

# 3 - MODA

calcular_moda <- function(x) {
  unique_x <- unique(x) # Obtém os valores únicos
  contagem <- tabulate(match(x, unique_x)) # Conta a frequência de cada valor
  moda <- unique_x[which.max(contagem)]
  return(moda) 
}

calcular_moda(dados$Ganhos_Totais)

# 4 - DESVIO PADRÃO

aggregate(Ganhos_Totais ~ Esporte, data = dados, FUN = sd)