# Aula 3: Decisões Compostas e Matemática Financeira no Excel (`SE`, `PGTO` e `TAXA`)

Seja bem-vindo à **Aula 3**! Após dominar a estrutura da planilha, a lógica de travamento de células e as primeiras funções básicas, agora daremos um salto em direção à **lógica avançada de tomada de decisão** e à **matemática financeira aplicada ao mercado corporativo**.

Nesta aula, você aprenderá a criar regras com múltiplos critérios e a construir ferramentas práticas de simulação de crédito e cálculo de juros.

---

## 1. A Função `SE()` com 3 Opções (Condições Aninhadas)

Na aula anterior, vimos a função `SE()` avaliando apenas duas possibilidades (Verdadeiro ou Falso). No mundo real, contudo, as decisões frequentemente possuem **três ou mais cenários**. 

Para resolver isso, utilizamos a **Função `SE()` Aninhada** (inserindo uma nova função `SE()` dentro do argumento `valor_se_falso` da primeira).

### 🔹 Sintaxe Básica (3 Opções):
```excel
=SE(condição_1; resultado_1; SE(condição_2; resultado_2; resultado_3))
```

### 💡 Exemplo Prático: Classificação de Desempenho / Notas
Imagine que a empresa precise classificar a avaliação dos funcionários em três faixas:
* **Nota >= 8,0**: *"Excelente"*
* **Nota entre 5,0 e 7,9**: *"Satisfatório"*
* **Nota < 5,0**: *"Necessita Treinamento"*

**Fórmula aplicada na célula `B2`**:
```excel
=SE(A2 >= 8; "Excelente"; SE(A2 >= 5; "Satisfatório"; "Necessita Treinamento"))
```
*(O Excel avalia a primeira condição. Se for falsa, passa para a segunda; se também for falsa, assume automaticamente a terceira opção).*

---

## 2. Calculadora de Financiamento: A Função `PGTO()`

A função `PGTO()` calcula o **valor da prestação mensal** de um empréstimo ou financiamento com base em uma taxa de juros constante e um número fixo de parcelas.

### 🔹 Sintaxe:
```excel
=PGTO(taxa; nper; vp)
```
* **`taxa`**: Taxa de juros por período (ex.: se a taxa for ao ano e o pagamento for mensal, divide-se por 12).
* **`nper`**: Número total de parcelas (períodos de pagamento).
* **`vp`**: Valor Presente (o montante total financiado).

### 💡 Exemplo Prático: Simulação de Compra de Veículo
* **Valor do Empréstimo (`vp`)**: R\$ 50.000,00 (célula `B1`)
* **Prazo (`nper`)**: 48 meses (célula `B2`)
* **Taxa de Juros Mensal (`taxa`)**: 1,5% a.m. (célula `B3`)

**Fórmula da Parcela Mensal**:
```excel
=-PGTO(B3; B2; B1)
```
*(Nota: Inserimos o sinal negativo `-` antes da função porque o Excel trata pagamentos e saídas de caixa como valores negativos. O sinal `-` converte o resultado para um valor positivo legível).*

---

## 3. Auditando Empréstimos: A Função `TAXA()`

Muitas vezes, lojas ou instituições financeiras divulgam o valor da parcela e o total de meses, mas omitem a **taxa de juros real** que está sendo cobrada no contrato. A função `TAXA()` é a ferramenta perfeita para o **auditor de dados** descobrir essa porcentagem.

### 🔹 Sintaxe:
```excel
=TAXA(nper; pgto; vp)
```
* **`nper`**: Quantidade de parcelas.
* **`pgto`**: Valor da prestação mensal (deve entrar como número negativo, pois representa saída de caixa).
* **`vp`**: Valor total que foi financiado/recebido.

### 💡 Exemplo Prático: Descobrindo a Taxa Embutida
Um fornecedor oferece um maquinário no valor de **R\$ 20.000,00** para ser pago em **24 parcelas de R\$ 1.050,00**. Qual é a taxa de juros mensal cobrada?

**Fórmula aplicada no Excel**:
```excel
=TAXA(24; -1050; 20000)
```
* **Resultado**: O Excel retornará a taxa de juros exata de aproximadamente **2,02% ao mês**.

---

🎯 **Objetivo ao final desta aula**: Você será capaz de construir uma planilha completa de simulação financeira, permitindo calcular o valor exato das parcelas de um financiamento, auditar contratos descobrindo taxas ocultas e automatizar classificações de risco ou desempenho com três níveis de decisão!

