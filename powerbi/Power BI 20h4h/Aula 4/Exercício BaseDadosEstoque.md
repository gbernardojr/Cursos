# Exercício

Abra no Power BI o arquivo BaseDadosEstoque.xlsx

### Monte o dashboard respondendo as seguintes perguntas:

01) QUAL A QUANTIDADE TOTAL SAIU DO ESTQOUE?
02) QUAL A QUANTIDADE TOTAL ENTROU NO ESTQOUE?
03) QUAL A QUANTIDADE DE PRODUTOS GERAL HÁ NO ESTOQUE?
04) QUAL A QUANTIDADE DE ENTRADA POR LOJA?
05) QUAL A QUANTIDADE DE SAÍDA POR LOJA?
06) QUAL A QUANTIDADE DE ENTRADA POR CATEGORIA?
07) QUAL A QUANTIDADE DE SAÍDA POR CATEGORIA?
08) QUAL A QUANTIDADE DE ENTRADA POR SUBCATEGORIA?
09) QUAL A QUANTIDADE DE SAÍDA POR SUBCATEGORIA?
10) QUAL A QUANTIDADE DE ENTRADA POR PRODUTO?
11) QUAL A QUANTIDADE DE SAÍDA POR PRODUTO?


### Fórmulas

> Total Entrada = CALCULATE(SUM(BaseEstoque[Movimentação]),FILTER(BaseEstoque,BaseEstoque[Tipo]="E"))

> Total Saida = CALCULATE(SUM(BaseEstoque[Movimentação]),FILTER(BaseEstoque,BaseEstoque[Tipo]="S")) * -1

> Lucro = Produto[Preço Unit] - Produto[Custo Unit]

> % Lucro = Produto[Lucro] / Produto[Custo Unit]
