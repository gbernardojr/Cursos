# Introdução à Análise de Dados no Google Cloud

## Entenda o Ciclo de Vida da Análise de Dados no Google Cloud

---

#### Introdução

Este módulo do curso "Introdução à Análise de Dados no Google Cloud" examina o fluxo de trabalho de análise de dados do Google Cloud e descreve as fontes de dados e os métodos de armazenamento disponíveis. Capturar, gerenciar e usar dados é essencial para redefinir as experiências do cliente e criar novo valor. Para analisar e obter insights dos seus dados, é fundamental entender o ciclo de vida da análise de dados no Google Cloud. O ciclo de vida da análise de dados fornece uma estrutura para organizar as diferentes etapas envolvidas na análise de dados, ajudando a garantir que as etapas necessárias sejam tomadas e na ordem correta.

---

#### 1. O Ciclo de Vida da Análise de Dados

O ciclo de vida da análise de dados é o processo de coleta, armazenamento, processamento e análise de dados para extrair insights. É um processo iterativo, onde frequentemente se alterna entre as diferentes etapas conforme se aprende mais sobre os dados e os objetivos desejados. Vamos explorar as etapas do ciclo de vida:

1. **Ingestão de Dados:**
   - **Objetivo:** Capturar dados e prepará-los para processamento.
   - **Ferramentas:** Pub/Sub (ingestão e mensagens), Dataflow (análise e processamento em tempo real e em lote), Dataproc (processamento de dados em lote), e Cloud Data Fusion (integração de dados ETL).

2. **Processamento de Dados:**
   - **Objetivo:** Processar os dados ingeridos para prepará-los para análise.
   - **Ferramentas:** Dataproc (processamento em lote), Dataflow (processamento em tempo real), Cloud Data Fusion (integração de dados).

3. **Armazenamento de Dados:**
   - **Objetivo:** Armazenar dados com segurança e dimensioná-los conforme necessário.
   - **Opções:**
     - **Bancos de Dados Relacionais:** Cloud SQL, Cloud Spanner, AlloyDB para PostgreSQL.
     - **Bancos de Dados NoSQL:** Bigtable, Firestore.
     - **Data Warehouse:** BigQuery.
   
4. **Análise de Dados:**
   - **Objetivo:** Analisar os dados para obter insights.
   - **Ferramentas:** BigQuery (data warehouse elástico e flexível), Looker e Looker Studio (visualização de dados).

5. **Aprendizado de Máquina:**
   - **Objetivo:** Utilizar dados para treinar modelos e extrair insights avançados.
   - **Ferramentas:** Vertex AI (inclui AutoML, Vertex AI Workbench e TensorFlow).

---

#### 2. Fontes de Dados e Métodos de Armazenamento

**Fontes de Dados:**
- **Fontes de Dados na Nuvem:** Armazenadas no Google Cloud, como Cloud Storage e Cloud SQL.
- **Fontes de Dados Externas:** Armazenadas fora do Google Cloud, como Amazon S3 e Microsoft SQL Server.

**Benefícios das Fontes de Dados do Google Cloud:**
- Acesso centralizado aos dados.
- Integração de dados de diferentes fontes.
- Melhoria na criação de data warehouses e data lakes.
- Facilitação na visualização e comunicação de descobertas.

**Métodos de Armazenamento:**
1. **Bancos de Dados Relacionais:**
   - **Exemplos:** Cloud SQL, Cloud Spanner, AlloyDB para PostgreSQL.
   - **Características:** Dados estruturados, consistência alta, ideal para dados estruturados e consultas SQL.

2. **Bancos de Dados Não Relacionais (NoSQL):**
   - **Exemplos:** Bigtable, Firestore.
   - **Características:** Dados menos estruturados, modelo de dados flexível, ideal para dados que mudam frequentemente.

3. **Data Warehouse:**
   - **Exemplo:** BigQuery.
   - **Características:** Análise de dados estruturados e semiestruturados de diversas fontes, projetado para análise e relatórios.

4. **Data Lake:**
   - **Características:** Armazenamento de dados brutos em seu formato original, sem limites de tamanho, adequado para análise de grandes volumes de dados diversos.

---

#### 3. Tipos de Dados

**Dados Estruturados:**
- Organizados em linhas e colunas, adequados para análise estatística e técnicas de análise de dados.

**Dados Não Estruturados:**
- Incluem texto, imagens e áudio. Utilizados em aprendizado de máquina para identificar padrões e fazer previsões.

---

#### Quiz: Entenda o Ciclo de Vida da Análise de Dados no Google Cloud

1. Qual é o primeiro passo no ciclo de vida da análise de dados no Google Cloud?
2. Quais ferramentas são usadas para processamento de dados em lote e em tempo real?
3. Cite duas opções de armazenamento de dados no Google Cloud e suas características.
4. O que é um data lake e como ele difere de um data warehouse?
5. Como o Vertex AI pode ser utilizado no ciclo de vida da análise de dados?

---

#### Conclusão

Nesta seção, você aprendeu sobre o ciclo de vida da análise de dados no Google Cloud, incluindo ingestão, processamento, armazenamento e análise de dados. Exploramos também as opções de armazenamento, fontes de dados e os tipos de dados que podem ser analisados. No próximo módulo, você aprenderá mais sobre como encontrar dados e usar comandos SQL básicos no BigQuery para extrair insights.

---

