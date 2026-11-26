# Aula 5: Análise Estatística de Grandes Volumes no Excel com IA Generativa (Estudo de Caso Mega-Sena)

Seja bem-vindo à **Aula 5**! Hoje exploraremos como utilizar a Inteligência Artificial Generativa (Grok, ChatGPT ou Copilot) como sua assistente de análise de dados para examinar o histórico completo da **Mega-Sena**, disponibilizado pela Caixa Econômica Federal.

Nesta aula, **todas as fórmulas, tabelas dinâmicas, análises de frequência e códigos de automação serão desenvolvidos pela IA** a partir dos comandos (prompts) criados por você utilizando a **Técnica PCTS** (**P**essoa, **C**ontexto, **T**arefa e **S**aída).

---

## ☄️ 1. O Desafio da Probabilidade: A Curiosidade do Meteoro

Antes de abrir a planilha, vale lembrar uma comparação estatística marcante:

* **Probabilidade de ser atingido por um meteoro/aerolito**: estimada em cerca de **1 em 1.600.000** ao longo da vida.
* **Probabilidade de acertar os 6 números da Mega-Sena (aposta simples de 6 dezenas)**: **1 em 50.063.860**.

> 💡 **Conclusão:** É cerca de **30 vezes mais provável um meteoro cair na cabeça de uma pessoa** do que ela ganhar na Mega-Sena com um bilhete único!

---

## ⚠️ 2. Nota Pedagógica Importante (Aviso de Responsabilidade)

> **Atenção:** Esta atividade possui caráter **estritamente pedagógico, acadêmico e recreativo**. O objetivo é ensinar a construção de prompts para análise estatística e tratamento de grandes volumes de dados no Excel.
> 
> **Não há incentivo ao jogo de azar.** Do ponto de vista matemático, cada sorteio é um evento completamente independente. O fato de um número ter saído mais ou menos vezes no passado **não altera em nada a probabilidade de sorteios futuros**.

---

## 📥 3. Obtenção da Base de Dados Oficial

1. Acesse o portal de Loterias da **Caixa Econômica Federal**.
2. Navegue até a página da **Mega-Sena** e clique na opção **Downloads** / **Resultado da Mega-Sena em Excel**.
3. Baixe e abra o arquivo contendo o histórico de todos os concursos realizados desde 1996.

---

## 🤖 4. Engenharia de Prompt no Excel: Guia Prático de Prompts PCTS

Em vez de escrever manualmente fórmulas complexas de contagem ou matrizes, você utilizará o assistente de IA integrado ao Excel enviando comandos estruturados.

---

### 🔹 Prompt 1: Frequência Absoluta de Cada Número (1 a 60)
**Objetivo**: Saber quantas vezes cada dezena (de 01 a 60) foi sorteada em todo o histórico.

> **Prompt PCTS**:
> *"Atue como um Especialista em Análise de Dados no Excel (Pessoa). Tenho uma planilha com todo o histórico de sorteios da Mega-Sena, onde as 6 dezenas sorteadas estão nas colunas D a I, da linha 2 até a 3000 (Contexto). Escreva a fórmula exata usando CONT.SE para contar a frequência do número 1 e me explique como aplicar para todos os números de 1 a 60 (Tarefa). Apresente o resultado no formato de uma tabela com duas colunas: 'Dezena' e 'Frequência de Sorteios' (Saída)."*

---

### 🔹 Prompt 2: Ranking dos 10 Números Mais Sorteados (Top 10)
**Objetivo**: Identificar as dezenas que mais apareceram nos sorteios.

> **Prompt PCTS**:
> *"Atue como um Analista Estatístico de BI (Pessoa). Com base na tabela de frequências das dezenas de 1 a 60 recém-criada (Contexto), indique a fórmula ou o passo a passo no Excel usando as funções MAIOR e PROCX para extrair os 10 números mais sorteados (Tarefa). Apresente o resultado em uma tabela de ranking decrescente (do 1º ao 10º lugar) e sugira o tipo de gráfico ideal para apresentar esse ranking à diretoria (Saída)."*

---

### 🔹 Prompt 3: Ranking dos Números Menos Sorteados e "Atrasados" (Bottom 10)
**Objetivo**: Descobrir os números raros e há quantos concursos um número não é sorteado.

> **Prompt PCTS**:
> *"Atue como Auditor de Dados (Pessoa). Na mesma planilha de histórico da Mega-Sena (Contexto), elabore o prompt e a lógica para identificar as 10 dezenas menos sorteadas da história e crie uma fórmula para calcular o 'atraso' (quantidade de concursos decorridos desde a última vez que o número foi sorteado) (Tarefa). Forneça a explicação passo a passo e as fórmulas prontas para copiar e colar no Excel (Saída)."*

---

### 🔹 Prompt 4: Análise de Combinações Frequentes (Duplas e Trios)
**Objetivo**: Descobrir quais pares (duplas) ou trios de números saíram juntos no mesmo concurso com maior frequência.

> **Prompt PCTS**:
> *"Atue como Engenheiro de Dados e Especialista em Power Query/VBA (Pessoa). Tenho a tabela com as 6 dezenas de cada concurso nas colunas D a I (Contexto). Escreva um código em Power Query M ou uma Macro em VBA para analisar a combinação de todas as dezenas e identificar quais duplas (2 números) e trios (3 números) mais saíram juntos nos mesmos concursos (Tarefa). Apresente o código comentado e a instrução de onde colá-lo no Excel (Saída)."*

---

### 🔹 Prompt 5: Outras Análises Estatísticas Avançadas

* **Proporção de Pares vs. Ímpares por Concurso**:
  > *"Atue como Analista de Dados (P). Crie uma coluna calculada no Excel que analise as 6 dezenas de cada concurso e classifique a distribuição entre números pares e ímpares (ex.: 3P-3I, 4P-2I) (T). Mostre a fórmula e a tabela percentual de ocorrência (S)."*

* **Soma Total das Dezenas Sorteadas (Curva Normal de Gauss)**:
  > *"Atue como Estatístico (P). Crie uma fórmula de SOMA para adicionar o valor das 6 dezenas em cada concurso e me diga qual é a faixa de soma mais frequente em toda a história da Mega-Sena (T). Apresente o resultado com uma sugestão de Histograma (S)."*

* **Distribuição Geográfica dos Prêmios por Estado (UF)**:
  > *"Atue como Gestor de BI (P). Com base na coluna de UF dos ganhadores (C), monte o passo a passo para criar uma Tabela Dinâmica exibindo a quantidade de ganhadores e o total de prêmios por estado brasileiro (T). Apresente em formato de ranking regional (S)."*

---

🎯 **Objetivo ao final desta aula**: Você dominará a criação de prompts para instruir a IA a realizar análises estatísticas complexas no Excel, auditando cada fórmula e código gerado com autonomia e pensamento crítico!

---

