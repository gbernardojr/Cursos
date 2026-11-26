# 📝 Atividade Prática: Construção de Calculadoras Financeiras no Excel (`PGTO` e `TAXA`)

### 📌 **Objetivo da Atividade**
Desenvolver duas ferramentas de simulação financeira no Microsoft Excel: uma **Calculadora de Financiamento** para prever o valor das parcelas mensais e uma **Calculadora de Auditoria de Taxa** para identificar juros embutidos em contratos comerciais.

---

## 🏢 Parte 1: Calculadora de Financiamento (Função `PGTO`)

### **Cenário da Empresa**
A diretoria da empresa **Comercial Vendas S.A.** deseja adquirir um novo veículo comercial para a equipe de entregas no valor de **R\$ 60.000,00**. A instituição financeira oferece duas opções de financiamento com taxa de juros de **1,8% ao mês**:
* **Opção A**: Pagamento em 24 meses.
* **Opção B**: Pagamento em 48 meses.

---

### 🛠️ **Passo a Passo da Construção no Excel**

1. Abra uma nova planilha no Excel e monte a seguinte estrutura a partir da célula `A1`:

|   | A | B |
| :-: | :--- | :--- |
| **1** | **SIMULADOR DE FINANCIAMENTO** | |
| **2** | Valor do Veículo (VP) | 60000 |
| **3** | Taxa de Juros Mensal (Taxa) | 1,8% |
| **4** | Prazo (Meses - NPER) | 24 |
| **5** | **Valor da Parcela Mensal** | *[Inserir Fórmula]* |
| **6** | **Custo Total do Financiamento** | *[Inserir Fórmula]* |
| **7** | **Total Pago em Juros** | *[Inserir Fórmula]* |

2. **Inserção das Fórmulas**:
   * Na célula **`B5`** (Valor da Parcela), insira a fórmula da função `PGTO`:
     ```excel
     =-PGTO(B3; B4; B2)
     ```
     *(Nota: Lembre-se de utilizar o sinal negativo `-` antes da função para exibir o valor positivo).*
   * Na célula **`B6`** (Custo Total), multiplique o valor da parcela pelo número de meses:
     ```excel
     =B5 * B4
     ```
   * Na célula **`B7`** (Total de Juros), subtraia o valor original do veículo do custo total:
     ```excel
     =B6 - B2
     ```

---

### ❓ **Perguntas de Análise (Responda na Planilha)**

1. Qual é o valor da parcela mensal no prazo de **24 meses**? Qual o total pago em juros nessa opção?
2. Altere a célula `B4` para **48 meses**. O que acontece com o valor da parcela mensal e com o total pago em juros ao final do contrato?
3. Como auditor financeiro, qual opção você recomendaria para a diretoria da empresa e por quê?

---

## 🔍 Parte 2: Calculadora de Auditoria de Taxa de Juros (Função `TAXA`)

### **Cenário da Empresa**
O setor de compras recebeu uma proposta de um fornecedor para adquirir um novo servidor no valor à vista de **R\$ 25.000,00**. O fornecedor informou que pode parcelar o equipamento em **36 vezes fixas de R\$ 980,00**, alegando que a "taxa de juros é super baixa", mas não declarou o percentual exato no contrato.

Você foi encarregado de auditar o contrato e descobrir a taxa de juros mensal cobrada.

---

### 🛠️ **Passo a Passo da Construção no Excel**

1. Na mesma pasta de trabalho (ou em uma nova aba), monte a seguinte tabela a partir da célula `A1`:

|   | A | B |
| :-: | :--- | :--- |
| **1** | **AUDITORIA DE CONTRATO - TAXA DE JUROS** | |
| **2** | Valor à Vista do Equipamento (VP) | 25000 |
| **3** | Quantidade de Parcelas (NPER) | 36 |
| **4** | Valor da Parcela Mensal (PGTO) | 980 |
| **5** | **Taxa de Juros Mensal Calculada** | *[Inserir Fórmula]* |
| **6** | **Taxa de Juros Anual Equivalente** | *[Inserir Fórmula]* |

2. **Inserção das Fórmulas**:
   * Na célula **`B5`** (Taxa Mensal), insira a função `TAXA`:
     ```excel
     =TAXA(B3; -B4; B2)
     ```
     *(Nota: O valor da parcela em `B4` deve entrar com o sinal negativo `-` indicando saída de caixa).*
   * Formate a célula `B5` para exibir como **Porcentagem (`%`)** com 2 casas decimais.
   * Na célula **`B6`** (Taxa Anual aproximada), multiplique a taxa mensal por 12:
     ```excel
     =B5 * 12
     ```

---

### ❓ **Perguntas de Análise (Responda na Planilha)**

1. Qual é a taxa de juros mensal exata cobrada pelo fornecedor?
2. Se a empresa conseguir um empréstimo bancário com taxa de **1,5% ao mês** para comprar o equipamento à vista, vale a pena aceitar o parcelamento do fornecedor? Justifique mostrando a diferença de valores.

---

## 📊 Gabarito de Verificação para o Professor

| Calculadora | Parâmetro | Resultado Esperado |
| :--- | :--- | :--- |
| **Parte 1 (`PGTO`) - 24 meses** | Parcela Mensal | **R\$ 3.099,98** |
| | Total em Juros | **R\$ 14.399,44** |
| **Parte 1 (`PGTO`) - 48 meses** | Parcela Mensal | **R\$ 1.890,71** |
| | Total em Juros | **R\$ 30.754,08** |
| **Parte 2 (`TAXA`)** | Taxa Mensal | **2,06% a.m.** |
| | Taxa Anual Simples | **24,72% a.a.** |

---
