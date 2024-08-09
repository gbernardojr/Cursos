# Compreendendo o Ciclo de Vida da Análise de Dados no Google Cloud

Este módulo do curso "Introdução à Análise de Dados no Google Cloud" explora o fluxo de trabalho de análise de dados no Google Cloud, abordando as fontes de dados e os métodos de armazenamento disponíveis. Capturar, gerenciar e utilizar dados é fundamental para aprimorar a experiência do cliente e gerar valor. 

Para extrair insights significativos dos dados, é crucial entender o ciclo de vida da análise de dados no Google Cloud. Este ciclo fornece uma estrutura organizada das diferentes etapas envolvidas na análise de dados, garantindo que todas as fases sejam executadas de forma sequencial e eficaz. A gestão adequada do armazenamento, organização e processamento de dados é a base da análise no Google Cloud.

### Objetivos de Aprendizagem

Nesta seção, você irá:

- Detalhar e descrever o fluxo de trabalho de análise de dados no Google Cloud.
- Comparar as fontes de dados e métodos de armazenamento disponíveis no Google Cloud.
- Avaliar como diferentes tipos de dados são utilizados em análise de dados e aprendizado de máquina.

### Importância dos Dados

Os dados são fundamentais para a inovação e diferenciação, e são essenciais para extrair valor da inteligência artificial. Eles provêm de várias fontes, como sistemas operacionais, fontes da web, mídias sociais e Internet das Coisas (IoT), e podem ser estruturados ou não estruturados.

Para gerar insights, é necessário integrar e interpretar diferentes tipos de dados, independentemente de seu formato ou origem. O Google Cloud oferece soluções integradas, abrangentes e sem servidor para cada etapa do ciclo de vida da análise de dados.

### Etapas do Ciclo de Vida da Análise de Dados

1. **Ingestão de Dados**
   - Ferramentas do Google Cloud, como Pub/Sub, Dataflow, Dataproc e Cloud Data Fusion, facilitam a ingestão e o processamento de dados em tempo real e em lote. O Cloud Data Fusion é um serviço ETL sem código que integra dados de fontes locais e na nuvem. Pub/Sub e Dataflow são usados para análise de streaming, enquanto Dataproc é adequado para processamento de dados em lote.

2. **Armazenamento de Dados**
   - Após a ingestão e processamento, os dados precisam ser armazenados de forma segura e escalável. As opções de armazenamento do Google Cloud incluem:
     - **Bancos de Dados**: Cloud SQL, Cloud Spanner, AlloyDB para PostgreSQL (relacionais); Bigtable, Firestore (NoSQL).
     - **Data Warehouses**: BigQuery.
     - **Data Lakes**: Armazenamento de dados brutos, sem pré-processamento significativo.

3. **Análise de Dados**
   - O BigQuery, um data warehouse altamente elástico e gerenciado, é central para a análise de dados no Google Cloud. Ele permite a execução de consultas SQL e é integrado a outros serviços analíticos e de processamento. Além do BigQuery, o Looker e o Looker Studio são ferramentas úteis para visualização e análise dos dados.

4. **Aprendizado de Máquina**
   - O Vertex AI é a principal plataforma de aprendizado de máquina do Google Cloud, oferecendo ferramentas como AutoML, Vertex AI Workbench e TensorFlow. Esses produtos permitem a análise de grandes volumes de dados para gerar insights e fazer previsões.

### Soluções de Armazenamento no Google Cloud

O Google Cloud oferece uma variedade de produtos de armazenamento adequados para diferentes casos de uso:

- **Bancos de Dados Relacionais**: Cloud SQL, Cloud Spanner, AlloyDB para PostgreSQL. Esses bancos organizam dados em tabelas e utilizam SQL para consultas.
- **Bancos de Dados Não Relacionais (NoSQL)**: Bigtable, Firestore. Estes bancos oferecem modelos de dados flexíveis para dados estruturados e não estruturados.
- **Data Warehouse**: BigQuery, projetado para análise e relatórios de dados estruturados e semiestruturados.
- **Data Lakes**: Repositórios que armazenam dados em seu formato original, sem limite de tamanho e com pouca estruturação prévia.

### Comparação de Dados

Dados estruturados, organizados em linhas e colunas, são ideais para análises estatísticas e técnicas tradicionais. Dados não estruturados, como texto, imagens e áudio, podem ser utilizados por algoritmos de aprendizado de máquina para identificar padrões e fazer previsões.

## Explore dados e extraia insights usando o BigQuery

Olá e bem-vindo a este módulo sobre exploração de dados e extração de insights usando o BigQuery. O BigQuery está no centro da análise no Google Cloud. O BigQuery é um **data warehouse** totalmente gerenciado. Um data warehouse é um grande armazenamento, contendo terabytes e petabytes de dados coletados de uma ampla variedade de fontes dentro de uma organização, que são usados para orientar decisões de gerenciamento. 

Há três seções neste módulo. Primeiro, você aprenderá tudo sobre o BigQuery, a solução de data warehouse do Google Cloud. Em seguida, você aprenderá como o BigQuery funciona e como obter insights dos seus dados. Por fim, você aprenderá como o BigQuery organiza dados para facilitar a análise para analistas de dados. Ao longo do caminho, você verá o conteúdo de demonstração da interface do usuário do BigQuery. Preparar? Vamos começar!

### Introdução ao BigQuery

Vamos começar com uma introdução ao BigQuery para analistas de dados. Nesta seção, apresentamos o BigQuery, a solução de data warehouse do Google, discutimos seus recursos e usos e concluímos com uma demonstração. 

**O que queremos dizer quando afirmamos que o BigQuery é um data warehouse totalmente gerenciado?** Isso significa que o BigQuery cuida da infraestrutura subjacente, para que você possa se concentrar no uso de consultas SQL para responder a perguntas comerciais sem se preocupar com implantação, escalabilidade e segurança.

Neste ponto, é útil considerar qual é a principal diferença entre um **data warehouse** e um **data lake**. Um data lake é apenas um conjunto de dados brutos, desorganizados e não classificados, que não tem finalidade específica. Por outro lado, um data warehouse contém dados estruturados e organizados, que podem ser usados para consultas avançadas. Como um data warehouse, o BigQuery pode armazenar dados transformados para insights de negócios. As fontes de dados alimentam um data lake e são processadas em seu data warehouse para análise e geração de relatórios. É claro que o objetivo do BigQuery não é apenas salvar dados; é analisá-los e ajudar a tomar decisões comerciais. 

O BigQuery é otimizado para executar consultas analíticas em grandes conjuntos de dados. Ele pode executar consultas em terabytes de dados em segundos e petabytes em minutos. Esse desempenho permite que você analise grandes conjuntos de dados com eficiência e obtenha insights quase em tempo real. Para lhe dar uma ideia da escala de dados com os quais o BigQuery pode trabalhar: um cliente do Google Cloud tem mais de **350 PB** de dados armazenados no BigQuery. Outros clientes executaram consultas em mais de **10 trilhões de linhas** e consultas simultâneas em mais de **100 trilhões de linhas** de vários clientes. E outro cliente executou **10.000 consultas simultâneas** ao mesmo tempo. 

**Então, como é uma arquitetura típica de solução de data warehouse?** O BigQuery é o mecanismo de análise que fica no final do pipeline de dados. Ele armazena dados recebidos e permite que você faça análises e crie modelos. O BigQuery é, na verdade, dois serviços em um: é um mecanismo de consulta SQL rápido e também uma camada de armazenamento totalmente gerenciada para carregar e armazenar seus conjuntos de dados. O BigQuery maximiza a flexibilidade separando os recursos de computação que analisam seus dados de suas opções de armazenamento. Você pode armazenar e analisar seus dados no BigQuery ou usar o BigQuery para avaliar seus dados onde eles estão. Consultas federadas permitem que você leia dados de fontes externas, enquanto o streaming oferece suporte a atualizações contínuas de dados. Ferramentas poderosas como o BigQuery ML e o BI Engine permitem que você analise e entenda esses dados.

Vamos dar uma olhada em alguns dos principais recursos do BigQuery:

- **Dois serviços em um:** É um lugar para armazenar e analisar petabytes de dados, com recursos integrados como aprendizado de máquina, análise geoespacial e inteligência empresarial.
- **Solução sem servidor:** Totalmente gerenciada, você não precisa se preocupar em provisionar recursos ou gerenciar servidores no backend, apenas no uso de consultas SQL no frontend.
- **Modelo de preços flexível:** Sob demanda ou com uma fatura fixa mensal, pagando pelo número de bytes processados e armazenamento de tabela permanente.
- **Criptografia em repouso:** Dados criptografados por padrão, sem ação necessária do cliente.
- **Aprendizado de máquina integrado:** Modelos de ML podem ser escritos diretamente no BigQuery usando SQL e integrados com ferramentas como o Vertex AI.

Agora é hora de fazer login na interface de usuário do BigQuery para demonstrar como você pode consultar terabytes de dados em segundos. Primeiramente, vamos abrir o BigQuery, que pode ser encontrado no menu de navegação. Veja como é a interface do usuário do BigQuery. Cada recurso no Google Cloud existe dentro de um projeto, que você pode visualizar aqui. Além da segurança e do controle de acesso, um projeto é o que vincula o uso de um recurso a um cartão de crédito: ele torna um recurso faturável.

O BigQuery tem vários conjuntos de dados públicos que qualquer pessoa pode consultar. Um deles são todos os metadados de páginas públicas da Wikipédia. Em seguida, vamos simplesmente colar e executar uma consulta SQL para ver o quão rápido o BigQuery pode escanear e processar **10 bilhões de linhas** procurando pela palavra “Google” no título da página da Wikipédia. O mecanismo de análise escalável e distribuído do BigQuery permite que você consulte terabytes em segundos e petabytes em minutos. A consulta inclui filtragem, agrupamento e ordenação em um conjunto de dados que contém **10 bilhões de registros** e é executada de forma rápida e eficiente no BigQuery.

No BigQuery, os dados são armazenados dentro de conjuntos de dados. Conjuntos de dados contêm tabelas e tabelas contêm colunas. O acesso aos dados no BigQuery é controlado em muitos níveis, desde o projeto e o conjunto de dados até a tabela, coluna e linha individuais. Um slot do BigQuery é uma CPU virtual usada pelo BigQuery para executar consultas SQL. O BigQuery calcula automaticamente quantos slots cada consulta requer, dependendo do tamanho e da complexidade da consulta. Ao contrário de muitos sistemas de gerenciamento de banco de dados relacional, você não precisa provisionar recursos antes de usar o BigQuery. O BigQuery aloca recursos de armazenamento e consulta dinamicamente com base em seus padrões de uso. Os recursos de armazenamento são alocados conforme você os consome e desalocados conforme você remove dados ou descarta tabelas. Os recursos de consulta são alocados de acordo com o tipo e a complexidade da consulta. Cada consulta usa um certo número de slots, que são unidades de computação que compreendem uma certa quantidade de CPU e RAM. Não há compromisso de uso mínimo. O serviço aloca e cobra pelos recursos com base no seu uso real. Por padrão, todos os clientes do BigQuery têm acesso a **2.000 slots** para operações de consulta. Você também pode reservar um número fixo de vagas para seu projeto.

### Como o BigQuery Funciona

Esta seção é um pouco mais técnica e explora como o BigQuery funciona. Vamos começar discutindo como os dois serviços do BigQuery, análise e armazenamento, trabalham juntos para impulsionar sua inovação orientada por dados. A rede interna de alta velocidade do Google conecta os dois serviços. Essa rede super rápida é o que nos permite separar computação e armazenamento. 

**Então, o que cada serviço faz?** A resposta curta é que os serviços são totalmente gerenciados para que usuários como você e eu não precisem se preocupar com a forma como o BigQuery armazena dados em disco ou dimensiona automaticamente as máquinas para consultas grandes. Dito isso, é um ótimo exercício de aprendizado entender como os serviços realizam sua mágica para que possamos entender melhor o que está acontecendo.

O primeiro é o serviço de **armazenamento BigQuery**. O serviço de armazenamento gerencia automaticamente os dados que você ingere na plataforma. O BigQuery organiza tabelas de dados em unidades chamadas conjuntos de dados. Esses conjuntos de dados têm como escopo seu projeto do Google Cloud. Ao referenciar uma tabela na linha de comando em consultas SQL ou em código, você faz referência a ela usando a construção: `project.dataset.table`. As tabelas são armazenadas como colunas altamente compactadas no sistema de arquivos Colossus do Google, o que proporciona durabilidade e disponibilidade. O serviço de armazenamento oferece suporte à ingestão de dados em massa e à ingestão de streaming. Portanto, ele pode trabalhar com grandes quantidades de dados e também com fluxos de dados em tempo real.

O serviço de **consulta** executa consultas interativas ou em lote que são enviadas por meio do console, da interface da Web do BigQuery, da ferramenta de linha de comando `bq` ou da API REST. A API REST é suportada por sete linguagens de programação. Lembre-se de que na demonstração anterior usamos a interface da Web do BigQuery para enviar a consulta. Há conectores para outros serviços, como o Dataproc, que simplificam a criação de fluxos de trabalho complexos entre o BigQuery e outros serviços de processamento de dados do Google Cloud. O serviço de consulta também pode executar trabalhos de consulta em dados contidos em outros locais, como tabelas em arquivos CSV hospedados no Cloud Storage ou dados no Planilhas Google. Antes de ficar muito animado com a execução de consultas em seus dados no Planilhas Google, você deve saber que o BigQuery é mais eficiente ao trabalhar com dados contidos em seu próprio serviço de armazenamento. 

O serviço de armazenamento e o serviço de consulta trabalham juntos para organizar intern

amente os dados e tornar as consultas eficientes em grandes conjuntos de dados de petabytes. Eles até otimizam o processamento da sua consulta depois que você a envia. Um dos controles mais importantes que você tem sobre o consumo de recursos e custos é controlar a quantidade de dados processados. Em geral, você só deseja selecionar as colunas de dados que realmente deseja processar e retornar. Uma prática recomendada é começar de forma ampla ao explorar o conjunto de dados e depois se concentrar nos campos e linhas essenciais dos quais você precisa. Explorar seu conjunto de dados com SQL é o primeiro passo para descobrir insights ocultos. 

Vamos retornar brevemente à interface do usuário do BigQuery e ver outro exemplo. Aqui estamos executando uma consulta para contar o número total de viagens feitas no conjunto de dados público para viagens de bicicletas compartilhadas em São Francisco. Muitas vezes há incerteza quanto à qualidade dos dados em seu conjunto de dados, então você pode usar SQL para explorar e filtrar anomalias. Aqui, filtramos registros de clientes que não continham uma data de nascimento definindo `member_birth_year IS NOT NULL` como filtro. Também aplicamos a cláusula `GROUP BY` para agrupar os resultados pelo nome da estação inicial. A cláusula `ORDER BY` ajuda a classificar os resultados, enquanto o `LIMIT` mostra apenas os 5 principais resultados.

### Laboratório BigQuery: Qwik Start – Console

Além dos tempos rápidos de execução de consultas, lembre-se de que o BigQuery também gerencia o armazenamento e os metadados dos seus conjuntos de dados. Vamos discutir como o BigQuery organiza dados para facilitar a exploração e a análise. Quais são alguns motivos para estruturar suas informações em conjuntos de dados, projetos e tabelas? Esses múltiplos escopos — projeto, conjunto de dados e tabela — podem ajudar você a estruturar suas informações logicamente. Você pode usar vários conjuntos de dados para separar tabelas pertencentes a diferentes domínios analíticos e pode usar o escopo em nível de projeto para isolar conjuntos de dados uns dos outros de acordo com as necessidades do seu negócio. Você pode alinhar projetos ao faturamento e usar conjuntos de dados para controle de acesso. Você armazena dados em tabelas separadas com base em considerações de esquema lógico. Cada tabela tem um esquema. Você pode inserir o esquema manualmente por meio do console do Google Cloud ou fornecendo um arquivo JSON. Formatos de arquivo como Avro, Parquet, ORC, Firestore export ou Datastore export são autodescritivos, então o BigQuery infere automaticamente o esquema da tabela a partir dos dados de origem. 

O BigQuery é chamado de **"armazenamento em colunas"**, o que significa que ele foi projetado para processar colunas, não linhas. Como o BigQuery lê apenas as colunas relevantes para executar uma consulta, ele é otimizado para leituras altas de data warehouses. Como cada coluna tem dados do mesmo tipo, o BigQuery pode compactar os dados da coluna com muito mais eficiência. Cada coluna é automaticamente compactada, criptografada e replicada para oferecer suporte à disponibilidade e durabilidade dos dados no BigQuery. O BigQuery armazena dados em um formato amplamente distribuído. O mesmo vale para o Google Cloud Storage e é o que alimenta aplicativos como Gmail, Ads e muitos outros produtos do Google. O BigQuery otimiza automaticamente o balanceamento e o particionamento desses fragmentos de dados no back-end. Como alternativa, você também pode particionar e agrupar suas tabelas com base em seus padrões de acesso para controlar custos e tornar suas consultas mais eficientes.

Vamos demonstrar mais uma vez como usar SQL no BigQuery para analisar dados. Após esta demonstração, você terá experiência prática em um laboratório. A primeira coisa que faremos é adicionar alguns dados. Vamos clicar em **Adicionar dados** e selecionar **Conjuntos de dados públicos**. E neste caso queremos analisar os dados de viagens de bicicleta do New York Citi, então vamos procurar esse conjunto de dados e clicar em **Exibir conjunto de dados**. No console do BigQuery, você vê dois projetos no painel esquerdo, um chamado **ID do projeto do Qwiklabs** e outro chamado **bigquery-public-data**. Vamos rolar para baixo e encontrar nossa tabela. E então selecionaremos a tabela e depois a guia **Visualizar** para examinar as colunas e os dados. Em seguida, vamos executar uma nova consulta. Esta consulta nos informará a duração típica dos 10 aluguéis só de ida mais comuns. Vamos executar mais uma consulta, desta vez para encontrar a distância total percorrida por cada bicicleta no conjunto de dados. Observe que, neste caso, estamos extraindo dados de algumas tabelas de dados diferentes (`citybike_trips` e `citibike_stations`) e unindo as tabelas para obter os resultados pretendidos.

### Quiz: Explore dados e extraia insights usando o BigQuery

Você chegou ao final deste módulo sobre o BigQuery, o data warehouse empresarial totalmente gerenciado do Google para análise e armazenamento. Vamos recapitular brevemente o que você aprendeu. Primeiro, você recebeu uma introdução ao BigQuery, incluindo uma breve demonstração da plataforma. Em seguida, você aprendeu como obter insights dos seus dados com o BigQuery, incluindo como acessar os dados necessários e executar consultas básicas. Por fim, você aprendeu mais sobre armazenamento e organização do BigQuery. Ao longo do caminho, você viu demonstrações e participou de alguns laboratórios. Na próxima seção, você aprenderá sobre o Looker, a ferramenta de análise e visualização de dados do Google Cloud.

---
