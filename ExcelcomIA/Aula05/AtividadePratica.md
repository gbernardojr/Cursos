
# 📊 **Atividade Prática: Construção de Dashboard de Indicadores no Excel com IA**

### 📌 **Objetivo da Atividade**
Utilizar o assistente de IA Generativa para analisar a base de dados histórica da Lotofácil, extrair estatísticas e padrões relevantes, e estruturar os componentes visuais para um **Dashboard Executivo de Indicadores**.

---

## 🎯 **As 10 Questões do Exercício**

---

### **1. Ranking de Frequência das Dezenas**
* **Pergunta para Análise**: Quais são as 5 dezenas mais sorteadas ("quentes") e as 5 menos sorteadas ("frias") em todo o histórico da Lotofácil?
* **Prompt Sugerido para a IA**: *"Analise as colunas de 'Bola1' a 'Bola15' de todos os concursos. Conte a frequência total de cada número de 1 a 25 e ordene do mais sorteado ao menos sorteado."*
* **Elemento no Dashboard**: Gráfico de Barras Horizontais com destaque de cores para os TOP 5 e BOTTOM 5.

---

### **2. Proporção de Números Pares e Ímpares**
* **Pergunta para Análise**: Qual é o padrão de paridade mais comum por concurso (ex.: 8 ímpares e 7 pares) e qual a porcentagem de ocorrência de cada combinação?
* **Prompt Sugerido para a IA**: *"Crie uma coluna calculada identificando a quantidade de números pares e ímpares sorteados em cada concurso. Crie uma tabela de frequência percentual dessas combinações."*
* **Elemento no Dashboard**: Gráfico de Rosca ou Pizza mostrando a distribuição percentual dos padrões de paridade.

---

### **3. Presença de Números Primos**
* **Pergunta para Análise**: Em média, quantos números primos (2, 3, 5, 7, 11, 13, 17, 19, 23) são sorteados por concurso e qual a distribuição dessa quantidade?
* **Prompt Sugerido para a IA**: *"Contabilize quantos números primos aparecem em cada concurso entre as 15 bolas sorteadas. Calcule a média geral e a frequência de cada quantidade de primos."*
* **Elemento no Dashboard**: Cartão KPI com a média de primos e Gráfico de Colunas da distribuição.

---

### **4. Intervalo da Soma Total das Dezenas**
* **Pergunta para Análise**: Qual é a soma total das 15 dezenas mais frequente por sorteio, e quais foram os valores máximo e mínimo registrados?
* **Prompt Sugerido para a IA**: *"Some as 15 bolas de cada concurso para obter a 'Soma do Concurso'. Calcule a média, valor mínimo, valor máximo e agrupe as somas em faixas de 10 em 10 para ver a distribuição."*
* **Elemento no Dashboard**: Gráfico de Área/Linhas para a curva de distribuição e Cartões de KPI para Soma Mínima, Média e Máxima.

---

### **5. Concentração Geográfica dos Ganhadores (15 Acertos)**
* **Pergunta para Análise**: Quais são os 10 estados (UF) com o maior número de apostas contempladas na faixa principal de 15 acertos?
* **Prompt Sugerido para a IA**: *"Extraia as siglas dos estados da coluna 'Cidade / UF' quando houver ganhadores de 15 acertos e some a quantidade total de ganhadores por UF."*
* **Elemento no Dashboard**: Gráfico de Barras dos TOP 10 Estados ou Mapa de Calor Geográfico.

---

### **6. Evolução Financeira e Arrecadação ao Longo do Tempo**
* **Pergunta para Análise**: Como evoluiu a Arrecadação Total e o valor do prêmio de 15 acertos ano a ano desde a criação da loteria?
* **Prompt Sugerido para a IA**: *"Agrupe os dados por ano a partir da coluna 'Data Sorteio'. Calcule a soma da 'Arrecadacao Total' e a média do 'Rateio 15 acertos' para cada ano."*
* **Elemento no Dashboard**: Gráfico de Linhas Combinado (Arrecadação vs. Valor do Prêmio Médio).

---

### **7. Taxa de Acúmulo do Prêmio Principal**
* **Pergunta para Análise**: Quantos concursos terminaram sem nenhum ganhador na faixa de 15 acertos (acumulados) e qual porcentagem isso representa no total de jogos?
* **Prompt Sugerido para a IA**: *"Filtre os concursos onde 'Ganhadores 15 acertos' é igual a 0. Calcule o total de concursos acumulados e o percentual em relação ao total de linhas."*
* **Elemento no Dashboard**: Cartão KPI de % de Jogos Acumulados e Indicador do Total de Concursos Acumulados.

---

### **8. Análise de Padrão do Volante: Moldura vs. Miolo**
* **Pergunta para Análise**: Qual é a média de dezenas sorteadas na "Moldura" (borda do bilhete: 1 a 5, 6, 10, 11, 15, 16, 20 a 25) comparada ao "Miolo" (centro: 7, 8, 9, 12, 13, 14, 17, 18, 19)?
* **Prompt Sugerido para a IA**: *"Classifique as 25 dezenas entre 'Moldura' e 'Miolo'. Para cada concurso, conte quantas bolas saíram em cada grupo e calcule a média histórica."*
* **Elemento no Dashboard**: Gráfico de Barras Comparativo (Média de Dezenas na Moldura vs. Miolo).

---

### **9. Recordes da Lotofácil (Maiores Prêmios)**
* **Pergunta para Análise**: Qual foi o maior prêmio individual já pago para 15 acertos, em qual concurso ocorreu e qual foi a arrecadação desse dia?
* **Prompt Sugerido para a IA**: *"Identifique a linha com o maior valor na coluna 'Rateio 15 acertos'. Retorne o número do concurso, data, valor do rateio, quantidade de ganhadores e arrecadação total."*
* **Elemento no Dashboard**: Painel de Destaque (Cards de Recordes) com Valor Recorde, Concurso e Data.

---

### **10. Comportamento Recente (Últimos 20 Concursos)**
* **Pergunta para Análise**: Quais dezenas estão em alta ("tendência") nos últimos 20 concursos em comparação com a sua média histórica?
* **Prompt Sugerido para a IA**: *"Filtre os últimos 20 concursos ordenados por data/concurso. Calcule a frequência de cada dezena nesse período curto e compare com a frequência relativa histórica."*
* **Elemento no Dashboard**: Tabela Dinâmica Interativa / Matriz de Calor de Tendências Recentes.

---
