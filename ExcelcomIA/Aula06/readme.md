# Aula 6: Diagnóstico Estratégico de RH com IA Generativa (Caso Hashtag Eletro)

Seja bem-vindo à **Aula 6**! Neste encontro, colocaremos em prática todas as competências desenvolvidas ao longo do curso para resolver um grande desafio corporativo real de **People Analytics**. 

Utilizando a base de dados oficial da **Hashtag Eletro** (`BaseFuncionarios - Ativos.xlsx`), assumiremos o papel de analistas estratégicos para diagnosticar a situação financeira, a distribuição demográfica e a performance dos **215 colaboradores ativos** da empresa.

---

## 🏢 1. O Desafio Corporativo do Memorando do RH

A Diretoria de Recursos Humanos da Hashtag Eletro convocou a equipe de analytics para subsidiar a reunião de planejamento estratégico com o CEO. O objetivo é transformar uma base de dados bruta extraída do sistema legado de RH em um **Relatório Executivo de Tomada de Decisão**.

Nesta aula, **100% das etapas — desde a limpeza de dados até a simulação financeira — serão solicitadas ao assistente de Inteligência Artificial** através da **Técnica PCTS** (**P**essoa, **C**ontexto, **T**arefa e **S**aída).

---

## 🛠️ 2. Etapa Prévia Obrigatória: ETL e Tratamento de Dados via Prompts

Antes de responder às perguntas da diretoria, é necessário tratar os dados despadronizados. Instruiremos a IA a gerar as fórmulas do Excel ou passos no Power Query para:

1. **Limpeza de Cabeçalho**: Remover as 2 primeiras linhas de metadados para fixar a linha 3 como cabeçalho oficial.
2. **Separação de Atributos (`Cargo - Area`)**: Dividir em duas colunas separadas — **Nível Hierárquico** (*Estagiário, Analista, Coordenador, Gerente, Diretor*) e **Departamento/Área** (*Administrativo, Comercial, Financeiro, Logística, Operações*).
3. **Tratamento Geográfico**: Extrair a **Cidade** e o **Estado (UF)** do endereço da sede.
4. **Padronização de Tipos**: Converter a nota de Avaliação (ex: `9,6`) para número decimal e ajustar as datas de nascimento e contratação.
5. **Colunas Calculadas**: Criar as métricas de **Custo Total Mensal** (\\(\text{Salário} + \text{VR} + \text{VT}\\)), **Idade** e **Tempo de Empresa (Tenure)**.

> **Exemplo de Prompt PCTS para ETL**:
> *"Atue como um Engenheiro de Dados especialista em Excel (Pessoa). Tenho uma base bruta de RH na aba 'Ativos' com a coluna 'Cargo - Area' contendo valores como 'Analista - Comercial' e a coluna de avaliação em texto com vírgula (Contexto). Escreva a fórmula ou o passo a passo no Power Query para dividir 'Cargo - Area' em duas colunas distintas ('Nível' e 'Departamento') e converter a nota em número decimal calculável (Tarefa). Apresente o resultado no formato de tabela pronta para copiar e colar (Saída)."*

---

## 📊 3. Os 4 Blocos de Análise Estratégica com Prompts PCTS

---

### 🔹 BLOCO 1: Gestão Orçamentária, Custos e Benefícios (Comp & Ben)
* **Objetivo**: Avaliar o custo total da folha de pagamento, o peso dos benefícios e a distribuição regional por unidade.

> **Prompt PCTS 1.1 (Custo Global e Benefícios)**:
> *"Atue como Analista Financeiro de RH (P). Com base na coluna calculada de Custo Total Mensal (Salário + VR + VT) dos 215 funcionários (C), crie as fórmulas no Excel para calcular o custo total acumulado da folha e a porcentagem exata que os benefícios (VR + VT) representam sobre esse orçamento (T). Apresente os resultados em um quadro resumo executivo em Reais e Porcentagem (S)."*

> **Prompt PCTS 1.2 (Ranking Regional de Custos por UF)**:
> *"Atue como Gestor de BI (P). Utilizando a coluna de UF da sede (SP, RJ, PE, BA, GO, MG, PR, RS) (C), mostre como criar uma Tabela Dinâmica que ordene as unidades do maior para o menor custo total com pessoal, destacando a região líder em orçamento (T). Apresente no formato de tabela de ranking e sugira o gráfico ideal para a diretoria (S)."*

---

### 🔹 BLOCO 2: Performance Analytics & Gestão de Talentos
* **Objetivo**: Identificar gargalos de desempenho por departamento e mapear os colaboradores de alta performance (*High Performers*).

> **Prompt PCTS 2.1 (Média de Desempenho por Área)**:
> *"Atue como Consultor de T&D (P). Com as colunas de 'Departamento' e 'Avaliação do Funcionário' (C), crie uma fórmula usando MÉDIASES para calcular a nota média de cada uma das 5 áreas (Administrativo, Comercial, Financeiro, Logística e Operações) (T). Indique qual departamento possui a menor média e necessita de um plano de ação imediato (S)."*

> **Prompt PCTS 2.2 (Mapeamento de High Performers)**:
> *"Atue como Especialista em Talent Management (P). Na base tratada de 215 colaboradores (C), elabore o prompt e a fórmula usando FILTRO ou CONT.SE para identificar e listar todos os colaboradores com avaliação igual ou superior a 9,0, indicando em quais cargos e cidades estão concentrados (T). Exiba o resultado em uma lista organizada por nível hierárquico (S)."*

---

### 🔹 BLOCO 3: Diversidade, Equidade Salarial e Demografia
* **Objetivo**: Investigar paridade salarial de gênero no mesmo cargo, representatividade na liderança e faixa etária da empresa.

> **Prompt PCTS 3.1 (Equidade Salarial por Cargo e Gênero)**:
> *"Atue como Auditor de Compliance e ESG (P). Analisando os salários de homens (M) e mulheres (F) que ocupam o mesmo cargo no mesmo departamento (C), construa uma estrutura de análise no Excel para comparar as médias salariais de cada grupo e identificar se existem disparidades não justificadas (T). Apresente uma tabela comparativa lado a lado com a diferença percentual (S)."*

> **Prompt PCTS 3.2 (Mulheres na Liderança)**:
> *"Atue como Analista de D&I (P). Considerando os cargos de liderança (Coordenadora, Gerente e Diretora) (C), crie as fórmulas para calcular o percentual de mulheres na liderança frente ao total de líderes da empresa e compare com a proporção geral de gênero da base (T). Responda em formato de diagnóstico com percentuais (S)."*

---

### 🔹 BLOCO 4: Simulação de Cenários ("What-If") e Resumo Executivo
* **Objetivo**: Projetar o impacto orçamentário de reajustes salariais e utilizar a IA para sintetizar o relatório final ao CEO.

> **Prompt PCTS 4.1 (Simulação de Reajuste e VR)**:
> *"Atue como Diretor Financeiro (P). A empresa estuda conceder 8% de reajuste salarial exclusivo para a equipe Comercial e equalizar o VR de todos os 215 funcionários para R\$ 550,00 fixos (C). Crie uma fórmula de simulação 'What-If' que calcule o novo custo mensal total da empresa, o acréscimo bruto em R\$ e a variação percentual em relação ao custo atual (T). Apresente os três indicadores em um painel comparativo (S)."*

> **Prompt PCTS 4.2 (Relatório Executivo de 1 Página com IA)**:
> *"Atue como Chief Human Resources Officer (CHRO) da Hashtag Eletro (P). Com base em todos os resultados obtidos nas análises de orçamento, performance, equidade salarial e simulação financeira (C), elabore um Relatório Executivo de 1 página para o CEO contendo: 1) Resumo dos números principais, 2) As 3 principais fragilidades/riscos identificados, e 3) 3 recomendações estratégicas fundamentadas em dados (T). Formate em texto executivo de alto impacto (S)."*

---

🎯 **Objetivo ao final desta aula**: O aluno dominará a condução de um projeto completo de People Analytics no Excel impulsionado por IA, aprendendo a limpar dados, investigar hipóteses de negócios, realizar simulações financeiras e apresentar recomendações estratégicas para o C-Level.

---

