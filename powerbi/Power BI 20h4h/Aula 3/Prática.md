#Webscraping com Power BI

Utilizar o site da CBF onde contém a tabela do Brasileirão

https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2024

## Utilizar o dashboard do Brasileirão e criar as medidas

> Pontos Máximos = 114

> Limite de Rebaixamento = 47

> Total CA = CALCULATE(SUM(TABELA[CARTÃO AMARELO]),ALL(TABELA))

> Total CV = CALCULATE(SUM(TABELA[CARTÃO VERMELHO]),ALL(TABELA))

> CA = SUM(TABELA[CARTÃO AMARELO])

> CV = SUM(TABELA[CARTÃO VERMELHO])

> % CA = [CA] / [Total CA]

> % CV = [CV] / [Total CV]