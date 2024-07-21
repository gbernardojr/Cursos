#Webscraping com Power BI

## Utilizar o dashboard do Brasileirão e criar as medidas

> Total CA = CALCULATE(SUM(TABELA[CARTÃO AMARELO]),ALL(TABELA))

> Total CV = CALCULATE(SUM(TABELA[CARTÃO VERMELHO]),ALL(TABELA))

> CA = SUM(TABELA[CARTÃO AMARELO])

> CV = SUM(TABELA[CARTÃO VERMELHO])

> % CA = [CA] / [Total CA]

> % CV = [CV] / [Total CV]