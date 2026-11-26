# 🏢 MEMORANDO INTERNO

**DE:** Diretoria de Recursos Humanos (Diretor de RH – Hashtag Eletro)  
**PARA:** Equipe de People Analytics & Business Intelligence (Alunos do Curso)  
**DATA:** 24 de Novembro de 2026  
**ASSUNTO:** Diagnóstico Estratégico da Força de Trabalho e Folha de Pagamento — Exercício Prático  

---

### Prezada Equipe de People Analytics,

Estamos em fase final de elaboração do **Planejamento Estratégico do próximo ciclo** da Hashtag Eletro. Para subsidiar a reunião do Comitê Executivo com o nosso CEO, preciso de um diagnóstico analítico aprofundado sobre a nossa base de **215 colaboradores ativos**.

Recebemos a extração bruta do sistema legado do RH (arquivo CSV `BaseFuncionarios_-_Ativos_(2).csv`). Notei que os dados precisam de tratamento prévio antes de responder às demandas da diretoria.

Solicito que a equipe execute o **ETL (tratamento e limpeza dos dados)** e responda com precisão às **11 perguntas estratégicas** organizadas nos **4 Blocos de Análise** descritos a seguir.

---

### 🛠️ Etapa Prévia Obrigatória: ETL e Tratamento de Dados (Power Query / Fórmulas)

Antes de responder às perguntas, vocês deverão realizar a preparação da base de dados:

1. **Limpeza de Cabeçalho:** Remover as 2 primeiras linhas de metadados do sistema para fixar os nomes corretos das colunas na linha 3 (`Cadastro RH`, `Nome Completo`, `Genero`, etc.).
2. **Separação de Atributos (`Cargo - Area`):** Dividir a coluna `Cargo - Area` em duas colunas distintas: **Nível Hierárquico** (Estagiário, Analista, Coordenador, Gerente, Diretor) e **Departamento/Área** (Administrativo, Comercial, Financeiro, Logística, Operações).
3. **Tratamento Geográfico (`Endereço Sede`):** Extrair a **Cidade** e o **Estado (UF)** a partir do endereço completo da unidade da sede.
4. **Padronização de Tipos:** Converter a `Avaliação do Funcionário` (formato texto com decimal em vírgula, ex: `9,6`) para número decimal de modo a permitir cálculos de média, e ajustar as datas (`Data de Nascimento` e `Data de Contratacao`) para o formato de data nativo.
5. **Criação de Colunas Calculadas:**
   * **Custo Total Mensal do Colaborador:** $\text{Salario} + \text{VR} + \text{VT}$
   * **Idade do Colaborador:** Idade em anos completos a partir da `Data de Nascimento`.
   * **Tempo de Empresa (Tenure):** Tempo de casa em anos completos a partir da `Data de Contratacao`.

---

### 📊 BLOCO 1: Gestão Orçamentária, Custos e Benefícios (Comp & Ben)

> *Objetivo: Entender o impacto financeiro direto da folha de pagamento e dos benefícios por unidade e nível hierárquico.*

1. **Custo Global da Folha:** Qual é o nosso custo total mensal com a folha de pagamento (somando Salário Base, VR e VT)? Qual é o peso percentual específico dos benefícios (VR + VT) no orçamento total de pessoal?
2. **Distribuição e Custo Regional:** Qual das nossas unidades regionais (SP, RJ, PE, BA, GO, MG, PR, RS) concentra a maior massa salarial e o maior custo de benefícios? Monte um ranking das unidades do maior para o menor custo total.
3. **Comprometimento Orçamentário por Nível:** Quanto do orçamento mensal de salários está comprometido com cargos de liderança (Coordenadores, Gerentes e Diretores) em comparação com cargos operacionais/iniciais (Estagiários e Analistas)?

---

### 🎯 BLOCO 2: Performance Analytics & Gestão de Talentos

> *Objetivo: Identificar padrões de desempenho, relação com tempo de casa e mapear os talentos da empresa.*

4. **Desempenho por Departamento:** Qual é a média da `Avaliação do Funcionário` por área/departamento (Administrativo, Comercial, Financeiro, Logística e Operações)? Qual departamento necessita de um plano de ação prioritário devido às menores notas?
5. **Tenure vs. Performance:** Colaboradores com mais tempo de casa têm notas de avaliação significativamente superiores aos recém-contratados, ou existe estagnação no desempenho ao longo dos anos?
6. **Mapeamento de High Performers:** Quantos e quem são os colaboradores que possuem avaliação **igual ou superior a 9,0**? Em quais cargos e unidades eles estão concentrados?

---

### ⚖️ BLOCO 3: Diversidade, Equidade Salarial e Demografia

> *Objetivo: Avaliar a distribuição demográfica e identificar potenciais disparidades salariais de gênero.*

7. **Equidade Salarial por Cargo e Gênero:** Ao comparar homens (`M`) e mulheres (`F`) que ocupam o **mesmo cargo no mesmo departamento**, há diferença relevante na média salarial? Identifique se existe algum desvio que necessite de adequação salarial.
8. **Representatividade na Liderança:** Qual é o percentual de mulheres ocupando cargos de liderança (Coordenadora, Gerente e Diretora) frente ao total de lideranças da empresa? Esse número reflete a proporção geral de gênero da base?
9. **Perfil Etário da Empresa:** Qual é a idade média dos nossos colaboradores? Como está distribuído o perfil etário por faixa (ex.: *Até 25 anos*, *26 a 35 anos*, *36 a 45 anos*, *Mais de 45 anos*)?

---

### 🔮 BLOCO 4: Simulação de Cenários e Resumo Executivo com IA

> *Objetivo: Projetar impactos orçamentários com modelos de simulação e utilizar ferramentas de IA para sintetizar decisões.*

10. **Simulação de Reajuste e Benefícios (Cenário "What-If"):** 
    * A diretoria estuda conceder um **reajuste salarial de 8% exclusivamente para a equipe Comercial** (Estagiários, Analistas, Coordenadores e Gerentes Comercial).
    * Além disso, pretende **equalizar o VR de todos os funcionários da empresa para um valor fixo de R\$ 550,00**.
    * **Pergunta:** Qual será o novo custo total mensal da empresa e qual será o acréscimo orçamentário em Reais (R\$) e em percentual (%)?
11. **Resumo Executivo para a Diretoria (Desafio Copilot/ChatGPT):**
    * Com base em todas as análises realizadas acima, utilize a IA para elaborar um **Relatório Executivo de 1 página** contendo:
      * Resumo dos principais números da empresa.
      * As 3 principais fragilidades ou riscos identificados na base.
      * 3 recomendações estratégicas fundamentadas em dados para o CEO.

---

Conto com a pontualidade e o rigor analítico de vocês para a entrega desses resultados ao final do nosso workshop.

Atenciosamente,

**Diretoria de Recursos Humanos**  
*Hashtag Eletro*
