# Introdução à Análise de Dados no Google Cloud

### Módulo 1: Entenda o Ciclo de Vida da Análise de Dados no Google Cloud

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

Aqui está o manual com o texto solicitado sobre exploração de dados e extração de insights usando o BigQuery:

---

## Módulo 2: Explore Dados e Extraia Insights Usando o BigQuery

### Introdução

Olá e bem-vindo a este módulo sobre exploração de dados e extração de insights usando o BigQuery. O BigQuery está no centro da análise no Google Cloud. O BigQuery é um data warehouse totalmente gerenciado. Um data warehouse é um grande armazenamento, contendo terabytes e petabytes de dados coletados de uma ampla variedade de fontes dentro de uma organização, que são usados para orientar decisões de gerenciamento. 

Este módulo é dividido em três seções:
1. **Introdução ao BigQuery**: Conheça a solução de data warehouse do Google Cloud, seus recursos e uma demonstração da plataforma.
2. **Funcionamento do BigQuery**: Entenda como o BigQuery organiza dados e realiza consultas.
3. **Organização de Dados no BigQuery**: Descubra como o BigQuery facilita a análise de dados para analistas.

Vamos começar!

### 1. Introdução ao BigQuery

#### O que é o BigQuery?

O BigQuery é um data warehouse totalmente gerenciado, o que significa que ele cuida da infraestrutura subjacente, permitindo que você se concentre no uso de consultas SQL para responder a perguntas comerciais. Diferente de um data lake, que contém dados brutos e desorganizados, o BigQuery armazena dados estruturados e organizados, prontos para consultas avançadas.

#### Recursos do BigQuery

- **Desempenho**: O BigQuery é otimizado para consultas analíticas em grandes conjuntos de dados. Ele pode processar terabytes de dados em segundos e petabytes em minutos.
- **Armazenamento e Consultas**: O BigQuery combina um mecanismo de consulta SQL rápido com uma camada de armazenamento totalmente gerenciada.
- **Consultas Federadas e Streaming**: Permite a leitura de dados de fontes externas e atualizações contínuas.
- **Aprendizado de Máquina**: Recursos integrados de aprendizado de máquina permitem que você crie modelos diretamente no BigQuery usando SQL.

#### Interface do BigQuery

- **Acesso**: O BigQuery está disponível no menu de navegação do Google Cloud.
- **Projetos e Conjuntos de Dados**: Cada recurso no Google Cloud está vinculado a um projeto. O BigQuery organiza dados em conjuntos de dados e tabelas, e cada tabela contém colunas.

### 2. Como o BigQuery Funciona

#### Armazenamento e Consultas

- **Serviço de Armazenamento**: Gerencia automaticamente os dados, organizando-os em tabelas altamente compactadas.
- **Serviço de Consulta**: Executa consultas interativas ou em lote enviadas por meio do console, da ferramenta de linha de comando bq ou da API REST. Conectores estão disponíveis para integração com outros serviços, como Dataproc.

#### Desempenho e Custos

- **Recursos Dinâmicos**: O BigQuery aloca recursos de armazenamento e consulta dinamicamente, com base na demanda.
- **Slots**: Cada consulta utiliza um número de slots, unidades de computação que incluem CPU e RAM.

#### Boas Práticas

- **Controle de Dados**: Selecione apenas as colunas necessárias para reduzir o volume de dados processados e controlar os custos.
- **Exploração Inicial**: Comece explorando conjuntos de dados de forma ampla e depois refine suas consultas.

### 3. Organização de Dados no BigQuery

#### Estrutura de Dados

- **Projetos, Conjuntos de Dados e Tabelas**: Utilize esses níveis para estruturar suas informações logicamente e controlar o acesso.
- **Armazenamento em Colunas**: O BigQuery processa colunas em vez de linhas, permitindo compactação e leitura eficientes.

#### Exemplos Práticos

- **Consulta SQL**: Execute consultas para contar registros ou calcular estatísticas, filtrando e agrupando dados conforme necessário.

#### Laboratório BigQuery: Qwik Start – Console

1. **Adicionar Dados**: Selecione conjuntos de dados públicos.
2. **Executar Consultas**: Realize consultas para analisar dados, como a duração de aluguéis ou distância percorrida por bicicletas.

### Quiz

**Recapitulando**:
- Introdução ao BigQuery e suas funcionalidades.
- Como obter insights dos dados e executar consultas básicas.
- Organização e estrutura de dados no BigQuery.

---

## Modulo 3: Tomando Decisões Baseadas em Dados Usando o Looker

---

### Introdução

Bem-vindo ao manual sobre como tomar decisões baseadas em dados usando o Looker. Esta ferramenta poderosa permite que você analise, visualize e compartilhe dados de maneira eficaz, capacitando sua equipe a tomar decisões fundamentadas em informações precisas.

---

### O que é Looker?

O Looker é uma plataforma de análise de dados que ajuda a:

- **Acessar e revisar dados** coletados pela empresa.
- **Responder perguntas sobre dados** em tempo real.
- **Manter-se atualizado** sobre o status do negócio.
- **Usar dados para orientar a tomada de decisões**.

---

### Processo Comum de Análise de Dados no Looker

1. **Identificação das Perguntas de Dados**
   - Exemplo: Quantas vendas foram feitas na semana passada? Qual é a demografia dos seus usuários?

2. **Identificação dos Dados Necessários**
   - Exemplo: Dados sobre pedidos, remessas, origem dos usuários.

3. **Análise dos Dados**
   - No Looker, isso é feito através da "exploração", onde você combina dimensões e medidas para encontrar respostas.

4. **Interpretação dos Resultados**
   - Exemplo: Identificar o sucesso de uma campanha de marketing e defender mais campanhas semelhantes.

---

### Explorando Dados no Looker

1. **Interface do Looker**

   - **Explorar**: A interface principal para criar relatórios e fazer perguntas sobre seus dados.
   - **Seletor de Campos**: Localizado no painel lateral esquerdo, onde os campos são agrupados em visualizações.
   - **Dimensões e Medidas**:
     - **Dimensões**: Atributos ou características dos dados (ex: data, preço, status do envio).
     - **Medidas**: Cálculos realizados em linhas de dados (ex: contagem de pedidos).

2. **Criação de Visualizações**

   - Adicione dimensões e medidas para responder a perguntas específicas.
   - Exemplo: Para saber quantos pedidos foram feitos, adicione a dimensão "data do pedido" e a medida "contagem".

3. **Ajuste de Visualizações**

   - Escolha o tipo de visualização adequado (gráfico de colunas, linhas, etc.).
   - Personalize as visualizações, como adicionar rótulos de valor.

4. **Filtragem de Resultados**

   - Use filtros para restringir resultados com base em critérios específicos (ex: cidades na Califórnia).

5. **Uso de Pivôs**

   - Transforme dimensões em colunas para criar matrizes de dados.
   - Exemplo: Adicione a dimensão "faixa etária" para comparar dados por idade.

---

### Compartilhamento de Dados

1. **No Looker**

   - **Salvar como Look**: Relatório ou visualização único salvo.
   - **Salvar em Painel**: Série de relatórios salvos em uma página.
   - **Exportar Dados**: Em formatos como CSV, PDF, ou PNG.
   - **Enviar Dados**: Por e-mail ou criar cronogramas de envio.

2. **No Looker Studio**

   - **Compartilhamento**: Semelhante ao Google Drive, onde você pode definir permissões para visualização ou edição.
   - **Visualização**: Criar gráficos usando dados do Looker e personalizá-los conforme necessário.
   - **Integração**: Conectar ao Looker usando o conector Looker no Looker Studio.

---

### Visualizações no Looker Studio

- **Gráficos de Barras**: Comparar dados entre categorias.
- **Gráficos de Linhas**: Mostrar mudanças ao longo do tempo.
- **Gráficos de Área**: Similar aos gráficos de linhas, mas com a área abaixo da linha preenchida.
- **Gráficos de Pizza/Rosca**: Mostrar proporções relativas.
- **Gráficos de Dispersão**: Mostrar a relação entre duas variáveis.
- **Mapas de Calor e Mapas**: Mostrar a distribuição e localização geográfica dos dados.

---

### Laboratório

1. **No Looker**

   - **Explorar Dados**: Use a interface Explore para consultar e selecionar dados.
   - **Criar Visualizações**: Selecione o tipo de visualização apropriado.
   - **Salvar Consultas**: Adicione a um painel.

2. **No Looker Studio**

   - **Criar Relatório**: Obtenha um conjunto de dados, adicione gráficos e estilize o relatório.

---

### Conclusão

Você agora possui uma compreensão abrangente de como usar o Looker e o Looker Studio para análise de dados. Através da exploração de dados, criação de visualizações e compartilhamento de informações, você está pronto para tomar decisões baseadas em dados e compartilhar descobertas com sua equipe.

---


