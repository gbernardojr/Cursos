# Aula 2: Fundamentos do Excel, Referências e Primeiras Funções

Seja bem-vindo à **Aula 2**! Após compreendermos o papel da Inteligência Artificial e da Engenharia de Prompt no ambiente corporativo, chegamos ao momento de dominar a estrutura essencial da ferramenta onde tudo acontece: o **Microsoft Excel**.

Neste encontro, você aprenderá como o Excel organiza as informações visualmente, como realizar cálculos matemáticos com precisão e como aplicar suas primeiras funções automáticas para solucionar problemas reais do dia a dia.

---

## 1. A Estrutura Básica: O que é o Excel?

O Microsoft Excel é uma planilha eletrônica estruturada em forma de grade (ou matriz). Para trabalhar de forma eficiente, é fundamental entender os três elementos básicos dessa grade:

* **Colunas**: Identificadas por **letras** na vertical (A, B, C...).
* **Linhas**: Identificadas por **números** na horizontal (1, 2, 3...).
* **Células**: O cruzamento exato entre uma coluna e uma linha (ex.: **A1**, **B5**, **C10**). É dentro da célula que inserimos textos, números ou fórmulas.

---

## 2. Lógica de Endereçamento: Referência Relativa vs. Referência Absoluta

Um dos conceitos mais importantes para evitar erros em planilhas é entender como o Excel interpreta o endereço de uma célula ao copiar ou arrastar uma fórmula:

* **Endereço Relativo (`A1`)**: Quando você copia a fórmula para a linha de baixo, o Excel ajusta automaticamente o endereço (virando `A2`, `A3`...). É o comportamento padrão do Excel.
* **Endereço Absoluto (`$A$1`)**: Utiliza o símbolo de cifrão (`$`) para **travar** a coluna e a linha. Ao arrastar a fórmula, o endereço fixado **não muda**. É ideal para calcular impostos, taxas fixas ou margens que estão isoladas em uma única célula. *(Dica: Pressione a tecla **F4** para aplicar o travamento rapidamente).*

---

## 3. Operações Matemáticas Fundamentais

No Excel, **toda fórmula deve começar obrigatoriamente com o sinal de igual (`=`)**. Sem ele, o sistema interpreta o conteúdo apenas como texto comum.

Os operadores matemáticos básicos utilizados são:

| Operação | Sinal no Excel | Exemplo de Fórmula | Resultado Esperado |
| :--- | :---: | :--- | :--- |
| **Adição** | `+` | `=A1 + B1` | Soma os valores das duas células |
| **Subtração** | `-` | `=A1 - B1` | Subtrai o valor de B1 do valor de A1 |
| **Multiplicação** | `*` | `=A1 * B1` | Multiplica os valores |
| **Divisão** | `/` | `=A1 / B1` | Divide o valor de A1 por B1 |
| **Exponenciação** | `^` | `=A1 ^ 2` | Eleva o valor de A1 ao quadrado |

---

## 4. Suas Primeiras Funções Automáticas

As funções são fórmulas pré-programadas no Excel que simplificam cálculos complexos. Nesta aula, veremos as três principais:

### 🔹 `SOMA()`
Soma rapidamente um intervalo contínuo de células sem a necessidade de somar item por item.
* **Sintaxe**: `=SOMA(A1:A10)` *(Soma todas as células de A1 até A10)*.

### 🔹 `MÉDIA()`
Calcula a média aritmética dos valores de um intervalo selecionado.
* **Sintaxe**: `=MÉDIA(B1:B12)` *(Soma os valores de B1 a B12 e divide pela quantidade de itens)*.

### 🔹 `SE()`
Uma das funções condicionais mais poderosas do Excel. Ela avalia se uma condição é verdadeira ou falsa e retorna um resultado diferente para cada caso.
* **Sintaxe**: `=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)`
* **Exemplo Prático**: 
  ```excel
  =SE(C2 >= 7; "Aprovado"; "Reprovado")
  ```
  *(Se a nota na célula C2 for maior ou igual a 7, o Excel exibe "Aprovado"; caso contrário, exibe "Reprovado").*

---

🎯 **Objetivo ao final desta aula**: Você será capaz de construir sua própria planilha do zero, realizar cálculos de faturamento e margem, fixar células corretamente com o cifrão (`$`) e automatizar diagnósticos com a função `SE()`.
