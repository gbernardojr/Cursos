# Caso de Uso: Controle de Empréstimos Pessoais

Você trabalha como assistente financeiro em uma instituição bancária e precisa criar uma planilha para controlar os empréstimos pessoais dos clientes. Cada cliente faz um empréstimo com valor e prazo definidos, e a cada mês o banco cobra uma parcela fixa de acordo com o valor financiado e a taxa de juros. Seu objetivo é calcular o valor das parcelas mensais, acompanhar os pagamentos, calcular o saldo devedor de cada cliente e gerar relatórios de vencimentos.

## Informações para Construção das Tabelas:

### 1. Cadastro de Clientes
- Cada cliente possui um nome, data do empréstimo, valor financiado, taxa de juros mensal e prazo em meses.
- Com essas informações, você deve calcular o valor da parcela mensal utilizando a função **PGTO()**, que recebe como parâmetros: taxa de juros, número de períodos (meses) e o valor financiado.

### 2. Controle de Pagamentos
- A cada mês, o cliente realiza um pagamento, que será registrado com a data e o valor pago. É necessário calcular o saldo devedor após o pagamento. O saldo devedor será o valor financiado menos o valor pago até o momento.
- A função **SE()** será usada para verificar se o pagamento foi suficiente para cobrir a parcela mensal ou se há diferença a ser paga.

### 3. Vencimentos
- A cada mês, você precisa controlar as datas de vencimento das parcelas. As datas de vencimento podem ser calculadas a partir da data do empréstimo (adicionando os meses correspondentes).
- A função de **subtração de datas** será usada para calcular o número de dias de atraso do pagamento em relação à data de vencimento.

### 4. Relatório de Pagamentos
- Para cada cliente, você precisa calcular o total de pagamentos realizados e somar os pagamentos feitos até o momento utilizando a função **SOMASE()**. Caso o cliente tenha feito pagamentos parciais, você precisa identificar a diferença entre o valor das parcelas e o total pago até o momento.

## Tarefas:

### 1. Cálculo da Parcela Mensal com PGTO()
- Crie uma fórmula que calcule o valor da parcela mensal utilizando a função **PGTO()**, com base no valor financiado, taxa de juros mensal e prazo em meses.
- Lembre-se de que a fórmula do **PGTO()** tem a seguinte estrutura:  
  `=PGTO(taxa_juros; nº_de_periodos; valor_financiado)`

### 2. Controle de Pagamentos e Saldo Devedor
- Para controlar os pagamentos, crie uma fórmula utilizando a função **SE()** para verificar se o pagamento realizado foi igual, maior ou menor que o valor da parcela mensal.
- Caso o pagamento seja inferior, calcule a diferença e adicione ao saldo devedor.
- Utilize a subtração de datas para calcular o número de dias de atraso entre a data de vencimento e a data de pagamento.

### 3. Relatório de Pagamentos Acumulados
- Utilize a função **SOMASE()** para somar os pagamentos feitos até determinado mês. A fórmula será semelhante a:  
  `=SOMASE(intervalo_de_datas; "condição"; intervalo_de_pagamentos)`

### 4. Relatório de Vencimentos
- Crie uma fórmula para calcular a data de vencimento de cada parcela, considerando a data de início do empréstimo e o prazo em meses. Utilize a função **DATA()** ou **EDATE()** para adicionar os meses à data de início do empréstimo.

---

## Passos para Desenvolvimento:

1. **Cadastro de Clientes**: Crie uma tabela com os seguintes campos: Nome do Cliente, Data do Empréstimo, Valor Financiado, Taxa de Juros Mensal e Prazo em Meses.
2. **Cálculo da Parcela Mensal**: Com base nas informações do cliente, calcule a parcela mensal utilizando a função **PGTO()**.
3. **Controle de Pagamentos**: Crie uma tabela de pagamentos com as colunas: Data de Pagamento, Valor Pago, Saldo Devedor.
4. **Relatório de Vencimentos**: Calcule a data de vencimento de cada parcela mensal.
5. **Relatório de Pagamentos Acumulados**: Utilize a função **SOMASE()** para gerar o total de pagamentos realizados até determinado mês.

---

## Objetivo:

- Calcular corretamente o valor das parcelas mensais.
- Controlar os pagamentos e o saldo devedor dos clientes.
- Gerar relatórios de vencimentos e pagamentos acumulados.
- Trabalhar com a subtração de datas e funções financeiras para um controle eficiente de empréstimos.

Este exercício ajudará os alunos a praticar o uso das funções **PGTO()**, **SE()**, **SOMASE()** e subtração de datas, além de aplicar conceitos de finanças no Excel.
