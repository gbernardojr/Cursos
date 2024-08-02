
##Transcrição dos vídeos da trilha 01 - Introduction to Data Analytics on Google Cloud

###Entenda o ciclo de vida da análise de dados no Google Cloud

Este módulo do curso Introdução à análise de dados no Google Cloud examina o fluxo de trabalho de análise de dados do Google Cloud e descreve as fontes de dados e os métodos de armazenamento do Google Cloud.
Capturar, gerenciar e usar dados é essencial para redefinir as experiências do cliente e criar novo valor.
Para analisar e obter insights dos seus dados, é fundamental que você entenda o ciclo de vida da análise de dados no Google Cloud.
O ciclo de vida da análise de dados fornece uma estrutura para organizar as diferentes etapas envolvidas na análise de dados.
Essa estrutura pode ajudar a garantir que as etapas necessárias sejam tomadas e na ordem correta.
Armazenar, gerenciar e organizar seus dados é a base da análise de dados no Google Cloud.
Nesta seção, você aprenderá a: Detalhar e descrever um fluxo de trabalho de análise de dados no Google Cloud.
Compare e contraste fontes de dados e métodos de armazenamento disponíveis no Google Cloud.
E compare como diferentes tipos de dados podem ser usados para análise de dados versus aprendizado de máquina.

Os dados são um ingrediente essencial para impulsionar a inovação e a diferenciação, e são a chave para extrair valor da inteligência artificial.
Os dados vêm de várias fontes e entradas diferentes, incluindo sistemas operacionais, fontes da web, mídias sociais e Internet das Coisas, ou IoT.
Os dados também podem ser estruturados ou não estruturados.
Para gerar insights, você precisa combinar e dar sentido a diferentes tipos de dados, independentemente do estado em que se encontram ou de como foram criados.
O Google Cloud fornece soluções integradas, abrangentes e sem servidor para cada etapa do ciclo de vida da análise de dados.
O ciclo de vida da análise de dados é o processo de coleta, armazenamento, processamento e análise de dados para extrair insights.
É uma parte essencial de qualquer empresa que queira tomar decisões informadas com base em dados.
O ciclo de vida da análise de dados é um processo iterativo.
Muitas vezes, você alternará entre diferentes etapas à medida que aprende mais sobre seus dados e o que deseja alcançar com eles.
Vamos explorar as etapas do ciclo de vida da análise de dados.
O primeiro passo é ingerir dados na nuvem.
Durante esta etapa, as ferramentas de ingestão e processamento do Google Cloud ajudam a quebrar os silos de dados e aumentar o tempo de obtenção de insights.
Produtos como Pub/Sub, Dataflow, Dataproc e Cloud Data Fusion são usados para ingerir e processar dados em tempo real e em lote.
O Cloud Data Fusion é um serviço de integração de dados totalmente gerenciado e prioritário na nuvem.
Esta ferramenta de extração, transformação e carregamento (ETL) sem código integra dados entre fontes locais e na nuvem.
Pub/Sub e Dataflow são serviços de análise de streaming.
Pub/Sub é para ingestão e mensagens, e Dataflow é para análise e processamento.
Depois que os dados são ingeridos, eles precisam ser processados.
O Dataproc pode ser usado para processar dados em lote, o Dataflow para transmitir dados ou o Cloud Data Fusion para integrar dados de várias fontes.
Depois que os dados forem ingeridos e processados, o próximo passo é armazená-los com segurança.
As soluções de armazenamento também precisam ser dimensionadas junto com seus dados.
As opções de armazenamento do Google Cloud incluem bancos de dados, data lakes e data warehouses.
Os produtos de armazenamento do Google Cloud incluem: Cloud Storage, Cloud SQL, Cloud Spanner, Bigtable, Firestore, AlloyDB para PostgreSQL e BigQuery.
Cloud SQL, Cloud Spanner e AlloyDB para PostgreSQL são bancos de dados relacionais, enquanto Bigtable e Firestore são bancos de dados NoSQL.
O BigQuery é a solução de data warehouse do Google Cloud.
Depois que seus dados forem ingeridos, processados e armazenados, eles poderão ser analisados.
Este curso se concentra no estágio de análise do ciclo de vida da análise de dados.
O BigQuery está no centro da análise de dados no Google Cloud.
O BigQuery é um data warehouse elástico, flexível, seguro e confiável que funciona em todas as nuvens e se adapta aos seus dados.
Este data warehouse totalmente gerenciado pode ser usado para analisar dados por meio de comandos SQL.
O BigQuery é profundamente integrado aos serviços analíticos e de processamento de dados do Google Cloud, o que permite que você crie um data warehouse que priorize a nuvem.
Além do BigQuery, você pode analisar dados e visualizar resultados usando o Looker e o Looker Studio.
Neste curso, você explorará o BigQuery, o Looker e o Looker Studio.
Os dados também são a chave para desbloquear o valor do aprendizado de máquina no Google Cloud.
O principal produto da plataforma de desenvolvimento de aprendizado de máquina é o Vertex AI, que inclui: AutoML, Vertex AI Workbench e TensorFlow.
Esses produtos revelam insights que somente grandes quantidades de dados podem fornecer.
O conhecimento do ciclo de vida da análise de dados ajudará você a identificar os dados certos, prepará-los para análise e extrair insights deles.


Antes de aprender sobre a etapa de análise, é importante entender as diversas soluções de armazenamento que o Google Cloud oferece.
Cada aplicativo precisa armazenar dados, e diferentes aplicativos e cargas de trabalho exigem diferentes soluções de armazenamento.
Esta seção se concentra na etapa de armazenamento do ciclo de vida da análise de dados.
O Google Cloud oferece vários produtos principais de armazenamento.
Esta lista inclui: Cloud Storage, Cloud SQL, Cloud Spanner, BigQuery, Firestore, Cloud Bigtable e AlloyDB para PostgreSQL.
Dependendo do seu caso de uso, você pode usar um ou vários desses serviços para fazer o trabalho.
Antes de entrar nos detalhes de cada uma dessas opções de armazenamento, vamos diferenciar as fontes de dados.
Fontes de dados são conectores que permitem consultar dados de várias fontes.
Você pode usar fontes de dados para criar conjuntos de dados, que são coleções de dados que podem ser usados para análise e aprendizado de máquina.
As fontes de dados do Google Cloud podem ser classificadas em duas categorias: fontes de dados na nuvem são fontes de dados armazenadas no Google Cloud.
Por exemplo, você pode se conectar a um bucket do Cloud Storage ou a um banco de dados do Cloud SQL.
Fontes de dados externas podem ser armazenadas no local ou em outro provedor de nuvem.
Por exemplo, você pode se conectar a um bucket do Amazon S3 ou a um banco de dados do Microsoft SQL Server.
Você pode criar uma conexão de fonte de dados usando o console do Google Cloud, o Cloud SDK ou a Google Cloud API.
Quais são alguns benefícios de usar fontes de dados do Google Cloud?
Primeiro, as fontes de dados do Google Cloud oferecem acesso centralizado aos seus dados, o que facilita a localização e a análise de dados, independentemente de onde estejam armazenados.
As fontes de dados do Google Cloud também ajudam você a integrar dados de diferentes fontes.
Essa integração pode ser útil para criar data warehouses e data lakes.
Discutiremos essas opções de armazenamento neste curso.
Eles também podem ser usados para analisar seus dados, para que você possa identificar tendências, fazer previsões e tomar melhores decisões de negócios.
Por fim, em geral, as fontes de dados podem ser usadas para visualizar seus dados, para ajudar você a comunicar suas descobertas a outras pessoas e tornar seus dados mais acionáveis.
Agora que você sabe o que são fontes de dados e os benefícios de usar fontes de dados do Google Cloud, vamos explorar opções de armazenamento.
A lista de opções de armazenamento inclui bancos de dados, data warehouses e data lakes.
Um banco de dados é uma coleção organizada de dados armazenados em tabelas e acessados eletronicamente a partir de um sistema de computador.
e acessados eletronicamente a partir de um sistema de computador.
O Google Cloud oferece opções de bancos de dados relacionais e não relacionais.
Bancos de dados relacionais, como Cloud SQL, Cloud Spanner e AlloyDB para PostgreSQL, armazenam e fornecem acesso a pontos de dados relacionados entre si.
Um banco de dados relacional pode estabelecer links – ou relacionamentos – entre informações unindo tabelas, e a linguagem de consulta estruturada, ou SQL, pode ser usada para consultar e manipular dados.
Esse tipo de banco de dados é altamente consistente, confiável e mais adequado para lidar com grandes quantidades de dados estruturados.
Um banco de dados não relacional, às vezes conhecido como banco de dados NoSQL, é menos estruturado em formato e não usa um formato tabular de linhas e colunas como bancos de dados relacionais.
Bancos de dados não relacionais seguem um modelo de dados flexível, o que os torna ideais para armazenar dados que mudam sua organização com frequência ou para aplicativos que manipulam diversos tipos de dados.
Bigtable é um produto de banco de dados não relacional.
Enquanto um banco de dados é projetado para capturar dados para armazenamento, recuperação e uso, um data warehouse é projetado para analisar dados.
Um data warehouse é um sistema empresarial usado para análise e geração de relatórios de dados estruturados e semiestruturados de diversas fontes.
O BigQuery é a oferta de data warehouse do Google Cloud.
Este curso se concentra na análise de dados no BigQuery e na visualização deles com o Looker e o Looker Studio.
Um data lake é um repositório projetado para ingerir, armazenar, explorar, processar e analisar qualquer tipo ou volume de dados brutos, independentemente da fonte.
Ele pode armazenar diferentes tipos de dados em seu formato original, ignorando limites de tamanho e sem muito pré-processamento ou adição de estrutura.
Os data lakes geralmente consistem em muitos produtos diferentes, dependendo da natureza dos dados ingeridos.
Data warehouses e data lakes devem ser considerados ferramentas complementares em vez de concorrentes.
Embora ambos armazenem dados em alguma capacidade, cada um é otimizado para usos diferentes.
Diferentes tipos de dados têm diferentes propósitos e usos.
Dados estruturados, ou seja, dados organizados em linhas e colunas, são mais adequados para análise de dados.
Esse tipo de dado é adequado para análise estatística e outras técnicas usadas em análise de dados.
O aprendizado de máquina pode usar dados estruturados e não estruturados.
Dados não estruturados são dados que não se encaixam perfeitamente em uma tabela ou planilha.
Esse tipo de dado pode ser texto, imagens ou áudio.
Algoritmos de aprendizado de máquina podem aprender com dados não estruturados para identificar padrões e fazer previsões.

> Quiz: Understand the data analytics lifecycle on Google Cloud

Isso nos leva ao final desta seção sobre o ciclo de vida da análise de dados.
Vamos reservar um momento para revisar o que foi abordado.
Esta seção começou com uma introdução ao ciclo de vida da análise de dados, incluindo quais produtos e serviços do Google Cloud são mais adequados para cada etapa.
A próxima seção abordou métodos de armazenamento, fontes de dados e tipos de dados para análise no Google Cloud.
Você aprendeu quais soluções de armazenamento são melhores para seus casos de uso e como os dados podem ser usados para análise em vez de aprendizado de máquina.
No próximo módulo deste curso, você aprenderá mais sobre como encontrar dados e usar comandos SQL básicos no BigQuery para extrair insights.

### Explore dados e extraia insights usando o BigQuery

Olá e bem-vindo a este módulo sobre exploração de dados e extração de insights usando o BigQuery.
O BigQuery está no centro da análise no Google Cloud.
O BigQuery é um data warehouse totalmente gerenciado.
Um data warehouse é um grande armazenamento, contendo terabytes e petabytes de dados coletados de uma ampla variedade de fontes dentro de uma organização, que são usados para orientar decisões de gerenciamento.
Há três seções neste módulo.
Primeiro, você aprenderá tudo sobre o BigQuery, a solução de data warehouse do Google Cloud.
Em seguida, você aprenderá como o BigQuery funciona e como obter insights dos seus dados.
Por fim, você aprenderá como o BigQuery organiza dados para facilitar a análise para analistas de dados.
Ao longo do caminho, você verá o conteúdo de demonstração da interface do usuário do BigQuery.
Preparar?
Vamos começar!

Vamos começar com uma introdução ao BigQuery para analistas de dados.
Nesta seção, apresentamos o BigQuery, a solução de data warehouse do Google, discutimos seus recursos e usos e concluímos com uma demonstração.
O que queremos dizer quando afirmamos que o BigQuery é um data warehouse totalmente gerenciado?
Isso significa que o BigQuery cuida da infraestrutura subjacente, para que você possa se concentrar no uso de consultas SQL para responder a perguntas comerciais sem se preocupar com implantação, escalabilidade e segurança.
Neste ponto, é útil considerar qual é a principal diferença entre um data warehouse e um data lake.
Um data lake é apenas um conjunto de dados brutos, desorganizados e não classificados, que não tem finalidade específica.
Por outro lado, um data warehouse contém dados estruturados e organizados, que podem ser usados para consultas avançadas.
Como um data warehouse, o BigQuery pode armazenar dados transformados para insights de negócios.
As fontes de dados alimentam um data lake e são processadas em seu data warehouse para análise e geração de relatórios.
É claro que o objetivo do BigQuery não é apenas salvar dados; é analisá-los e ajudar a tomar decisões comerciais.
O BigQuery é otimizado para executar consultas analíticas em grandes conjuntos de dados.
Ele pode executar consultas em terabytes de dados em segundos e petabytes em minutos.
Esse desempenho permite que você analise grandes conjuntos de dados com eficiência e obtenha insights quase em tempo real.
Para lhe dar uma ideia da escala de dados com os quais o BigQuery pode trabalhar: um cliente do Google Cloud tem mais de 350 PB de dados armazenados no BigQuery.
Outros clientes executaram consultas em mais de 10 trilhões de linhas e consultas simultâneas em mais de 100 trilhões de linhas de vários clientes.
E outro cliente executou 10.000 consultas simultâneas ao mesmo tempo.
Então, como é uma arquitetura típica de solução de data warehouse?
O BigQuery é o mecanismo de análise que fica no final do pipeline de dados.
Ele armazena dados recebidos e permite que você faça análises e crie modelos.
O BigQuery é, na verdade, dois serviços em um: é um mecanismo de consulta SQL rápido e também uma camada de armazenamento totalmente gerenciada para carregar e armazenar seus conjuntos de dados.
O BigQuery maximiza a flexibilidade separando os recursos de computação que analisam seus dados de suas opções de armazenamento.
Você pode armazenar e analisar seus dados no BigQuery ou usar o BigQuery para avaliar seus dados onde eles estão.
Consultas federadas permitem que você leia dados de fontes externas, enquanto o streaming oferece suporte a atualizações contínuas de dados.
Ferramentas poderosas como o BigQuery ML e o BI Engine permitem que você analise e entenda esses dados.
Vamos dar uma olhada em alguns dos principais recursos do BigQuery.
Primeiro, o BigQuery fornece dois serviços em um.
É um lugar para armazenar e analisar petabytes de dados, com recursos integrados como aprendizado de máquina, análise geoespacial e inteligência empresarial.
O BigQuery é uma solução sem servidor totalmente gerenciada, o que significa que você não precisa se preocupar em provisionar nenhum recurso ou gerenciar servidores no backend, mas focar apenas no uso de consultas SQL para responder às perguntas da sua organização no frontend.
Se você nunca escreveu SQL antes, não se preocupe.
Este curso fornece recursos e laboratórios para ajudar.
O BigQuery tem um modelo de preços flexível sob demanda, no qual você paga pelo número de bytes de dados que sua consulta processa e por qualquer armazenamento de tabela permanente.
Se você preferir ter uma fatura fixa todo mês, também pode assinar o preço de computação de capacidade, no qual você tem uma quantidade reservada de recursos para uso.
Os dados no BigQuery são criptografados em repouso por padrão, sem nenhuma ação necessária do cliente.
Por criptografia em repouso, queremos dizer a criptografia usada para proteger dados armazenados em um disco, incluindo unidades de estado sólido ou mídia de backup.
E, por fim, o BigQuery tem recursos integrados de aprendizado de máquina para que você possa escrever modelos de ML diretamente no BigQuery usando SQL.
Além disso, se você decidir usar outras ferramentas profissionais, como o Vertex AI do Google Cloud, para treinar seu ML modelos, você pode exportar conjuntos de dados do BigQuery diretamente para o Vertex AI para uma integração perfeita em todo o ciclo de vida dos dados para IA.
Agora é hora de fazer login na interface de usuário do BigQuery para demonstrar como você pode consultar Terabytes de dados em segundos.
Primeiramente, vamos abrir o BigQuery, que pode ser encontrado no menu de navegação.
Veja como é a interface do usuário do BigQuery.
Cada recurso no Google Cloud existe dentro de um projeto, que você pode visualizar aqui.
Além da segurança e do controle de acesso, um projeto é o que vincula o uso de um recurso a um cartão de crédito: ele torna um recurso faturável.
O BigQuery tem vários conjuntos de dados públicos que qualquer pessoa pode consultar.
Um deles são todos os metadados de páginas públicas da Wikipédia.
Em seguida, vamos simplesmente colar e executar uma consulta SQL para ver o quão rápido o BigQuery pode
escaneie e processe 10 bilhões de linhas procurando pela palavra “Google” no título da página da Wikipédia.
O mecanismo de análise escalável e distribuído do BigQuery permite que você consulte terabytes em segundos e petabytes em minutos.
A consulta inclui filtragem, agrupamento e ordenação em um conjunto de dados que contém 10 bilhões de registros e é executada de forma rápida e eficiente no BigQuery.
No BigQuery, os dados são armazenados dentro de conjuntos de dados.
Conjuntos de dados contêm tabelas e tabelas contêm colunas.
O acesso aos dados no BigQuery é controlado em muitos níveis, desde o projeto e o conjunto de dados até a tabela, coluna e linha individuais.
Um slot do BigQuery é uma CPU virtual usada pelo BigQuery para executar consultas SQL.
O BigQuery calcula automaticamente quantos slots cada consulta requer, dependendo do tamanho e da complexidade da consulta.
Ao contrário de muitos sistemas de gerenciamento de banco de dados relacional, você não precisa provisionar recursos antes de usar o BigQuery.
O BigQuery aloca recursos de armazenamento e consulta dinamicamente com base em seus padrões de uso.
Os recursos de armazenamento são alocados conforme você os consome e desalocados conforme você remove dados ou descarta tabelas.
Os recursos de consulta são alocados de acordo com o tipo e a complexidade da consulta.
Cada consulta usa um certo número de slots, que são unidades de computação que compreendem uma certa quantidade de CPU e RAM.
Não há compromisso de uso mínimo.
O serviço aloca e cobra pelos recursos com base no seu uso real.
Por padrão, todos os clientes do BigQuery têm acesso a 2.000 slots para operações de consulta.
Você também pode reservar um número fixo de vagas para seu projeto.

Esta seção é um pouco mais técnica e explora como o BigQuery funciona.
Vamos começar discutindo como os dois serviços do BigQuery, análise e armazenamento, trabalham juntos para impulsionar sua inovação orientada por dados.
A rede interna de alta velocidade do Google conecta os dois serviços.
Essa rede super rápida é o que nos permite separar computação e armazenamento.
Então, o que cada serviço faz?
A resposta curta é que os serviços são totalmente gerenciados para que usuários como você e eu não precisa se preocupar com a forma como o BigQuery armazena dados em disco ou dimensiona automaticamente as máquinas para consultas grandes.
Dito isso, é um ótimo exercício de aprendizado entender como os serviços realizam sua mágica para que possamos entender melhor o que está acontecendo.
O primeiro é o serviço de armazenamento BigQuery.
O serviço de armazenamento gerencia automaticamente os dados que você ingere na plataforma.
O BigQuery organiza tabelas de dados em unidades chamadas conjuntos de dados.
Esses conjuntos de dados têm como escopo seu projeto do Google Cloud.
Ao referenciar uma tabela na linha de comando em consultas SQL ou em código, você faz referência a ela usando a construção: project.dataset.table.
As tabelas são armazenadas como colunas altamente compactadas no sistema de arquivos Colossus do Google, o que proporciona durabilidade e disponibilidade.
O serviço de armazenamento oferece suporte à ingestão de dados em massa e à ingestão de streaming.
Portanto, ele pode trabalhar com grandes quantidades de dados e também com fluxos de dados em tempo real.
O serviço de consulta executa consultas interativas ou em lote que são enviadas por meio do console, da interface da Web do BigQuery, da ferramenta de linha de comando bq ou da API REST.
A API REST é suportada por sete linguagens de programação.
Lembre-se de que na demonstração anterior usamos a interface da Web do BigQuery para enviar a consulta.
Há conectores para outros serviços, como o Dataproc, que simplificam a criação de fluxos de trabalho complexos entre o BigQuery e outros serviços de processamento de dados do Google Cloud.
O serviço de consulta também pode executar trabalhos de consulta em dados contidos em outros locais, como tabelas em arquivos CSV hospedados no Cloud Storage ou dados no Planilhas Google.
Antes de ficar muito animado com a execução de consultas em seus dados no Planilhas Google, você deve saiba que o BigQuery é mais eficiente ao trabalhar com dados contidos em seu próprio serviço de armazenamento.
O serviço de armazenamento e o serviço de consulta trabalham juntos para organizar internamente os dados e tornar as consultas eficientes em grandes conjuntos de dados de petabytes.
Eles até otimizam o processamento da sua consulta depois que você a envia.
Um dos controles mais importantes que você tem sobre o consumo de recursos e custos é controlar a quantidade de dados processados.
Em geral, você só deseja selecionar as colunas de dados que realmente deseja processar e retornar.
Uma prática recomendada é começar de forma ampla ao explorar o conjunto de dados e depois se concentrar nos campos e linhas essenciais dos quais você precisa.
Explorar seu conjunto de dados com SQL é o primeiro passo para descobrir insights ocultos.
Vamos retornar brevemente à interface do usuário do BigQuery e ver outro exemplo.
Aqui estamos executando uma consulta para contar o número total de viagens feitas no conjunto de dados público para viagens de bicicletas compartilhadas em São Francisco.
Muitas vezes há incerteza quanto à qualidade dos dados em seu conjunto de dados, então você pode usar SQL para explorar e filtrar anomalias.
Aqui, filtramos registros de clientes que não continham uma data de nascimento definindo member_birth_year IS NOT NULL como filtro.
Também aplicamos a cláusula group by para agrupar os resultados pelo nome da estação inicial.
A cláusula order by ajuda a classificar os resultados, enquanto o limite mostra apenas os 5 principais resultados.

> Laboratório BigQuery: Qwik Start – Console

Além dos tempos rápidos de execução de consultas, lembre-se de que o BigQuery também gerencia o armazenamento e os metadados dos seus conjuntos de dados.
Vamos discutir como o BigQuery organiza dados para facilitar a exploração e a análise.
Quais são alguns motivos para estruturar suas informações em conjuntos de dados, projetos e tabelas?
Esses múltiplos escopos — projeto, conjunto de dados e tabela — podem ajudar você a estruturar suas informações logicamente.
Você pode usar vários conjuntos de dados para separar tabelas pertencentes a diferentes domínios analíticos e pode usar o escopo em nível de projeto para isolar conjuntos de dados uns dos outros de acordo com as necessidades do seu negócio.
Você pode alinhar projetos ao faturamento e usar conjuntos de dados para controle de acesso.
Você armazena dados em tabelas separadas com base em considerações de esquema lógico.
Cada tabela tem um esquema.
Você pode inserir o esquema manualmente por meio do console do Google Cloud ou fornecendo um arquivo JSON.
Formatos de arquivo como Avro, Parquet, ORC, Firestore export ou Datastore export são autodescritivos, então o BigQuery infere automaticamente o esquema da tabela a partir dos dados de origem.
O BigQuery é chamado de "armazenamento em colunas", o que significa que ele foi projetado para processar colunas, não linhas.
Como o BigQuery lê apenas as colunas relevantes para executar uma consulta, ele é otimizado para leituras altas de data warehouses.
Como cada coluna tem dados do mesmo tipo, o BigQuery pode compactar os dados da coluna com muito mais eficiência.
Cada coluna é automaticamente compactada, criptografada e replicada para oferecer suporte à disponibilidade e durabilidade dos dados no BigQuery.
O BigQuery armazena dados em um formato amplamente distribuído.
O mesmo vale para o Google Cloud Storage e é o que alimenta aplicativos como Gmail, Ads e muitos outros produtos do Google.
O BigQuery otimiza automaticamente o balanceamento e o particionamento desses fragmentos de dados no back-end.
Como alternativa, você também pode particionar e agrupar suas tabelas com base em seus padrões de acesso para controlar custos e tornar suas consultas mais eficientes.
Vamos demonstrar mais uma vez como usar SQL no BigQuery para analisar dados.
Após esta demonstração, você terá experiência prática em um laboratório.
A primeira coisa que faremos é adicionar alguns dados.
Vamos clicar em Adicionar dados e selecionar Conjuntos de dados públicos.
E neste caso queremos analisar os dados de viagens de bicicleta do New York Citi, então vamos procurar esse conjunto de dados e clicar em Exibir conjunto de dados.
No console do BigQuery, você vê dois projetos no painel esquerdo, um chamado ID do projeto do Qwiklabs e outro chamado bigquery-public-data.
Vamos rolar para baixo e encontrar nossa tabela.
E então selecionaremos a tabela e depois a guia Visualizar para examinar as colunas e os dados.
Em seguida, vamos executar uma nova consulta.
Esta consulta nos informará a duração típica dos 10 aluguéis só de ida mais comuns.
Vamos executar mais uma consulta, desta vez para encontrar a distância total percorrida por cada bicicleta no conjunto de dados.
Observe que, neste caso, estamos extraindo dados de algumas tabelas de dados diferentes (citybike_trips e citibike_stations) e unindo as tabelas para obter os resultados pretendidos.

> Quiz: Explore data and extract insights using BigQuery

Você chegou ao final deste módulo sobre o BigQuery, o data warehouse empresarial totalmente gerenciado do Google para análise e armazenamento.
Vamos recapitular brevemente o que você aprendeu.
Primeiro, você recebeu uma introdução ao BigQuery, incluindo uma breve demonstração da plataforma.
Em seguida, você aprendeu como obter insights dos seus dados com o BigQuery, incluindo como acessar os dados necessários e executar consultas básicas.
Por fim, você aprendeu mais sobre armazenamento e organização do BigQuery.
Ao longo do caminho, você viu demonstrações e participou de alguns laboratórios.
Na próxima seção, você aprenderá sobre o Looker, a ferramenta de análise e visualização de dados do Google Cloud.
 
### Tome decisões baseadas em dados usando o Looker

Bem-vindo a esta seção no Looker, onde você aprende os fundamentos da análise, visualização e compartilhamento de dados usando a plataforma Looker.
Com o Looker, você pode ativar e usar os dados analisados para capacitar suas equipes a tomar decisões eficazes e baseadas em dados.
Então, o que é Looker?
O Looker é uma ferramenta poderosa que ajuda você a: Acessar e revisar os dados coletados pela sua empresa.
Responda a perguntas sobre dados em tempo real.
Mantenha-se atualizado sobre o status do seu negócio.
E use dados para orientar a tomada de decisões.
Vamos examinar o processo comum de análise de dados no Looker.
Primeiro, identifique as perguntas de dados que você deseja responder.
Talvez você seja analista de um varejista de comércio eletrônico.
Algumas perguntas padrão incluem: Quantas vendas foram feitas na semana passada?
Qual é a demografia dos seus usuários ou clientes?
Qual é o status de envio de todos os pedidos?
O próximo passo é identificar os dados necessários para responder às suas perguntas.
Referindo-se ao nosso exemplo anterior de comércio eletrônico, se você quiser determinar o status de envio de todos
pedidos, você precisa de dados sobre pedidos, remessas e talvez informações adicionais, como dados do centro de distribuição.
Se você estiver analisando seus usuários, talvez queira dados sobre a origem desses usuários, como origem do tráfego e localização.
Em seguida, é hora de analisar os dados.
No Looker, a análise de dados é chamada de “exploração”.
Depois de identificar suas perguntas de dados e os dados necessários, você estará pronto para combinar dimensões e medidas no Looker para encontrar as respostas.
Você aprenderá mais sobre dimensões e medidas neste curso.
Por fim, interprete os resultados.
Depois de analisar e visualizar os dados, você pode obter insights, agir e tomar decisões baseadas em dados.
Referindo-se ao exemplo do comércio eletrônico, talvez você tenha descoberto que uma grande porcentagem de seus clientes foi direcionada ao seu site por meio de uma campanha recente criada pela sua equipe de marketing.
Ao usar dados para mostrar o sucesso da campanha, você pode defender mais campanhas semelhantes no futuro para aumentar as vendas.
Nesta seção, você aprenderá a: Manipular um observador. Explorar para responder a perguntas baseadas em dados.
Crie uma visualização apropriada à situação para destacar a resposta para uma pergunta baseada em dados.
E compartilhe visualizações com outras pessoas.
Vamos começar!

Vamos começar visualizando a interface do Looker e detalhando os principais componentes usados para exploração de dados.
No Looker, o Explorar é uma interface de criação de relatórios e um portal para fazer perguntas usando seus dados.
Os explores são selecionados pelos desenvolvedores do Looker em uma linguagem de modelos proprietária chamada LookML.
Os Explores aos quais você teve acesso estão listados na seção Explorar.
Este exemplo do Explore contém dados de comércio eletrônico.
O painel lateral esquerdo exibe o seletor de campos, onde os campos são agrupados em grupos chamados visualizações.
Os dois campos principais para explorar dados no Looker são dimensões e medidas.
Dimensões são atributos ou características dos seus dados.
Cada coluna em uma tabela de banco de dados é uma dimensão no Looker.
Por exemplo, esta tabela de banco de dados exibe dados de pedidos.
Cada coluna na tabela exibe um atributo para o pedido, como a data em que o pedido foi feito, o preço de venda e o status do envio.
No Looker, todas essas colunas são dimensões.
Medidas são cálculos realizados em várias linhas de dados.
Assim, medidas são agregados de atributos de dados ou dimensões.
Talvez você queira saber quantos pedidos foram feitos na semana passada.
Sempre que você tiver uma pergunta como "quantos", provavelmente você vai querer procurar uma medida com a palavra count ou number (nesse caso, count).
Para encontrar a resposta a essa pergunta sobre dados, você deve primeiro agrupar os dados por dimensão — neste caso, a data do pedido — e depois adicionar uma medida de contagem.
Muitas vezes, você precisa combinar dimensões e medidas para responder às suas perguntas sobre dados.
Essas dimensões e medidas também podem abranger diversas visualizações.
Vejamos outro exemplo, desta vez analisando dados do usuário.
Observe que as dimensões no seletor de campos são listadas em ordem alfabética, e algumas dimensões são agrupadas, como Data de criação.
Use a função de pesquisa para encontrar rapidamente a dimensão que você está procurando.
Neste exemplo, o objetivo é identificar quais cidades têm mais usuários, então comece por
adicionando a dimensão da cidade e depois a medida de contagem para ver quantos usuários estão em cada cidade.
Defina um limite de linhas para 10 para ver as 10 principais cidades.
Depois que tudo estiver definido, clique em Executar para exibir as 10 principais cidades com base no número de usuários.
Vamos dar um passo adiante e ajustar a visualização.
Há várias opções de visualização diferentes para escolher.
Neste exemplo, provavelmente faz sentido exibir a visualização como um gráfico de colunas.
Você também pode adicionar rótulos ao lado de cada barra para ver o valor total da barra.
Clique em Editar e ative Rótulos de Valor na aba Valores.
Cada coluna no gráfico agora tem seu valor exibido.
Agora, o gráfico de colunas que mostra as 10 principais cidades com mais usuários está completo.
Em seguida, vamos filtrar os resultados.
Os filtros restringem os resultados retornados com base em critérios específicos, para que você possa se concentrar em um subconjunto dos seus dados com base nas características desejadas.
Um recurso importante dos filtros é que eles não excluem nada do banco de dados; eles são aplicados apenas aos dados que o Looker exibe na tela.
Você pode filtrar dimensões e medidas.
O exemplo a seguir demonstra como filtrar uma dimensão.
Talvez os resultados da nossa consulta anterior – exibindo cidades nos Estados Unidos – sejam muito amplos e
em vez disso, você deseja restringir os resultados para mostrar apenas cidades no estado da Califórnia.
Você pode restringir os resultados adicionando um filtro para o estado da Califórnia.
Depois de executar a consulta novamente, os resultados serão filtrados para exibir apenas as 10 principais cidades da Califórnia.
A técnica de exploração final abordada nesta seção é o pivô.
Os pivôs permitem que você transforme uma dimensão selecionada em várias colunas, o que cria uma matriz de seus dados.
Talvez, além da dimensão da cidade, você queira adicionar a dimensão da faixa etária para agrupar seus usuários por idade.
Após a execução da consulta, a tabela não mostra os resultados pretendidos.
Por exemplo, Los Angeles aparece em várias linhas, e apenas quatro das 10 principais cidades são exibidas.
É aqui que um pivô pode ser útil.
Girar a tabela pela dimensão Faixa etária traz a faixa etária para o topo da tabela, e agora todas as faixas etárias e cidades ficam visíveis.
Quando você gira em uma dimensão, cada valor possível exclusivo dessa dimensão se torna seu próprio cabeçalho de coluna.
Todas as medidas são então repetidas sob cada cabeçalho de coluna.
Depois de dinamizar os resultados, você pode facilmente comparar resultados por diferentes agrupamentos e identificar possíveis lacunas, sem afetar seus dados subjacentes.
Vamos voltar à interface de usuário do Looker e usar outro exemplo para demonstrar como os pivôs funcionam.
Na Exploração de Itens do Pedido, a medida Preço Total de Venda é adicionada.
Em seguida, as dimensões Categoria de Produto e Departamento são adicionadas para agrupar os resultados por essas características.
Após a execução da consulta, os dois departamentos aparecem em várias linhas.
Esta tabela pode se tornar mais útil e fácil de ler adicionando um pivô.
Ao girar na dimensão do departamento, o departamento é colocado no topo da tabela, de modo que, quando você executa a consulta novamente, cada departamento é exibido em uma única coluna.
Se você notar algum insight ou tendência interessante em seus dados, você pode salvar suas descobertas em um painel ou como um Look.
Um Look é um relatório ou visualização único e salvo.
As aparências geralmente respondem a uma pergunta de dados individual e podem ser adicionadas a um painel.
Um painel é uma série de relatórios salvos, todos em uma página.
Um painel apresenta as respostas para diversas perguntas sobre dados e geralmente é onde os exploradores de dados armazenam suas descobertas.
Explorações, visuais e painéis podem ser compartilhados com outras pessoas.
Você aprenderá mais sobre compartilhamento de dados neste curso.

É hora de outro laboratório!
Nas lições anteriores, discutimos como usar dimensões, medidas, filtros e pivôs para encontrar respostas para perguntas baseadas em dados.
Agora, vamos colocar em prática o que você aprendeu e usar a interface do Looker para explorar dados.
Neste laboratório, você: Usará a interface Explore para acessar dados publicados por desenvolvedores do LookML.
Trabalhe com dimensões e medidas para consultar e selecionar dados.
Selecione o tipo de visualização apropriado para melhor exibir seus dados.
E salve uma consulta do Explore em um painel.
Vamos começar.

> Análise de dados do Looker: Qwik Start

Além do Looker, você pode usar o Looker Studio para visualizar seus dados.
O Looker fornece ferramentas analíticas poderosas para analisar dados e criar relatórios.
O Looker Studio apresenta menos funcionalidades analíticas e se concentra mais em uma interface simples e fácil de usar para visualização de dados.
O Looker Studio oferece vários recursos que facilitam o compartilhamento e a colaboração em relatórios.
Você pode publicar relatórios na web e também incorporá-los em outros aplicativos.
Os benefícios de usar o Looker Studio para visualizações de dados incluem: Uma interface de arrastar e soltar que facilita a criação de relatórios e painéis.
Vários relatórios e painéis, incluindo gráficos, diagramas e tabelas.
Recursos poderosos que permitem criar relatórios com aparência profissional, como a capacidade de adicionar filtros e detalhar os dados.
Colaboração em tempo real em relatórios e painéis.
E recursos de segurança que permitem controlar quem tem acesso aos seus dados.
O Looker e o Looker Studio podem ser integrados usando o conector Looker para o Looker Studio.
Essa integração permite que você se conecte a qualquer instância do Looker hospedada no Google Cloud e crie relatórios e painéis usando dados do Looker.
O conector Looker é apenas um dos muitos conectores diferentes disponíveis no Looker Studio.
Para usar o conector Looker, você deve primeiro habilitar a integração na sua instância do Looker.
Depois que a integração for habilitada, você pode criar um novo relatório no Looker Studio e selecionar o conector Looker como sua fonte de dados.
Em seguida, você será solicitado a inserir a URL da sua instância do Looker e selecionar um Explore.
Depois de selecionar um Explorar, você pode começar a criar seu relatório usando dados do Looker.
Para criar uma visualização apropriada à situação em um relatório no Looker Studio, você precisa considerar o seguinte: primeiro, com que tipo de dados você está trabalhando?
Segundo, que insights você está tentando comunicar?
O que você está tentando comunicar influenciará o tipo de opção de visualização que você escolher.
E, finalmente, para qual público você está criando o relatório?
O público pode influenciar a maneira como você estiliza e organiza seu relatório.
A seguir, vamos examinar as opções de visualização mais comuns no Looker Studio.
Os gráficos de barras são uma ótima maneira de comparar dados entre diferentes categorias.
Gráficos de linhas são uma ótima maneira de mostrar como os dados mudam ao longo do tempo.
Os gráficos de área são semelhantes aos gráficos de linhas, mas a área abaixo da linha é preenchida.
Os gráficos de pizza são úteis para mostrar as proporções relativas de diferentes categorias.
Os gráficos de rosca são semelhantes aos gráficos de pizza, mas deixam um buraco no centro.
Os gráficos de dispersão são uma ótima maneira de mostrar a relação entre duas variáveis.
Mapas de calor são usados para mostrar a distribuição de dados.
E, por fim, os mapas mostram dados que estão localizados geograficamente.
Além disso, você também pode criar visualizações personalizadas com o Looker Studio.
Vamos demonstrar como criar um gráfico simples no Looker Studio usando dados do Looker.
Neste exemplo, o Looker já foi conectado como fonte de dados usando o conector Looker.
Um relatório no Looker Studio é o mesmo que um painel no Looker e consiste em um ou vários gráficos.
Gráficos são maneiras de visualizar dimensões e métricas.
Você pode criar um gráfico no Looker Studio clicando em Adicionar um gráfico na barra de ferramentas e selecionando o tipo de gráfico que deseja usar.
Vamos supor que você trabalha em uma loja de comércio eletrônico e deseja visualizar a contagem de pedidos de cada categoria no ano passado.
Um gráfico de linhas ou um gráfico de área seria uma ótima visualização para esse tipo de dados.
Depois de selecionar o gráfico desejado, ele é adicionado ao relatório.
Em seguida, personalize os dados, como você faria no Looker, adicionando dimensões para a data de criação do pedido e a categoria do produto.
A data de criação é um intervalo de datas, por isso é adicionada como a dimensão do intervalo de datas.
E os dados serão divididos por categoria de produto, então especifique a categoria Produtos como a dimensão de divisão.
O gráfico exibe atualmente todos os dados de pedidos dos últimos anos.
Para limitar os resultados — neste caso, ao ano passado — adicione um filtro.
E agora o gráfico exibe a contagem de pedidos por data, divididos por categoria, no ano passado.
Por fim, na aba de estilo, você pode personalizar os diferentes componentes do gráfico, como rótulos, cores e fontes, ou pode alternar para uma visualização completamente diferente.

Você chegou ao segundo laboratório desta seção.
Neste laboratório, você usará o Looker Studio para visualizar resultados de consultas e criar relatórios e painéis atraentes.
Neste laboratório, você: criará um relatório obtendo um conjunto de dados público do BigQuery, adicionará um gráfico e estilizará um relatório.
Vamos começar.

> Looker Studio: Qwik Start

O valor do Looker e do Looker Studio não termina na análise e visualização de dados.
Compartilhar relatórios e painéis com outras pessoas melhora a colaboração, permite a tomada de decisões baseada em dados e aumenta a transparência.
Os dados podem ser compartilhados tanto do Looker quanto do Looker Studio.
Nesta lição, você aprenderá os benefícios e as desvantagens de cada um.
Primeiro, vamos explorar o compartilhamento de dados do Looker.
Compartilhar dados no Looker melhora a comunicação e a colaboração, o que leva a uma tomada de decisão mais rápida e maior eficiência.
Além disso, o Looker fornece um repositório centralizado de dados, o que garante que os dados sejam precisos, consistentes e fáceis de encontrar.
O Looker também é escalável e pode ser integrado a outras fontes de dados e aplicativos.
No entanto, também há algumas desvantagens em usar o Looker para compartilhar dados.
Primeiro, o Looker armazena dados na nuvem, o que significa que eles são potencialmente vulneráveis a violações de segurança.
No entanto, o Looker oferece vários recursos de segurança que podem ajudar a proteger dados, como criptografia e controle de acesso.
Em segundo lugar, o Looker é uma plataforma paga, e o custo pode ser um fator para algumas organizações.
Por fim, o Looker é uma plataforma relativamente complexa e, às vezes, pode haver uma curva de aprendizado íngreme.
Como alternativa, você pode usar o Looker Studio para compartilhar dados.
Os benefícios de usar o Looker Studio incluem: Facilidade de uso: O Looker Studio é uma plataforma amigável que facilita o compartilhamento de dados.
Os usuários podem criar e compartilhar painéis e relatórios com outras pessoas e também incorporá-los em sites e aplicativos.
Flexibilidade: o Looker Studio oferece vários recursos que permitem personalizar as experiências de compartilhamento de dados.
Por exemplo, você pode controlar quem tem acesso aos dados e também definir permissões para diferentes tipos de dados.
E, por fim, a segurança: o Looker Studio oferece recursos de segurança que ajudam a proteger os dados, como criptografia e controle de acesso.
No entanto, o Looker Studio é, no geral, uma plataforma menos poderosa que o Looker e não oferece o conjunto completo de recursos que o Looker oferece.
Por exemplo, o Looker Studio não oferece suporte para modelagem avançada de dados ou aprendizado de máquina.
O Looker Studio também não se integra com tantas fontes de dados quanto o Looker.
A falta de integrações pode dificultar o compartilhamento de dados de diversas fontes.
Em última análise, a melhor plataforma para compartilhamento de dados depende das necessidades específicas da organização.
O Looker é uma boa escolha para organizações que precisam de uma plataforma poderosa e escalável para compartilhamento de dados.
O Looker Studio é uma boa escolha para organizações que buscam uma plataforma fácil de usar.
Agora que você entende os benefícios e as desvantagens do compartilhamento de dados com o Looker e o Looker Studio, vamos examinar como compartilhar dados no Looker.
Isso é frequentemente chamado de “entrega de dados”.
Este Explore exibe os resultados de uma consulta.
No menu Configurações, você pode compartilhar seus insights baseados em dados de algumas maneiras diferentes.
Primeiro, você pode salvá-lo como um relatório, chamado Look, ou em um painel, exibindo vários relatórios.
Como alternativa, para exportar dados apenas uma vez, você pode baixá-los ou enviá-los.
O download extrai os dados para seu próprio computador.
O Looker oferece suporte para download em diferentes formatos de arquivo, incluindo CSV, um arquivo zip de um ou mais CSVs, um PDF ou um PNG.
O envio permite que você entregue os dados para outro lugar.
O destino mais popular é o e-mail; por exemplo, você pode enviar o painel por e-mail para você mesmo e seu gerente.
Para enviar os dados mais de uma vez, crie um cronograma e defina a frequência com que o relatório será enviado a outras pessoas.
O agendamento é basicamente o mesmo que o envio, exceto pela frequência de entrega, como diária ou semanal.
Isso é útil se você quiser que uma planilha com os dados do Look seja entregue automaticamente na sua caixa de entrada, digamos, toda sexta-feira à tarde no final da sua semana de trabalho.
Por fim, para enviar a outros os dados mais recentes, você pode simplesmente clicar em Compartilhar, copiar o URL e enviá-lo para as pessoas que precisam vê-lo.
Com as permissões corretas, esses indivíduos podem visualizar os dados.
Em seguida, vamos fazer a transição para o compartilhamento de dados no Looker Studio.
O Looker Studio foi criado com base no Google Drive, para que você possa compartilhar seus relatórios e fontes de dados da mesma forma que compartilha documentos, planilhas e slides.
Assim como no Google Drive, os usuários recebem permissão para editar ou visualizar os dados compartilhados.
Você pode compartilhar um relatório no Looker Studio a partir da página inicial do Looker Studio ou do próprio relatório.
A partir do relatório, além de compartilhar, você pode agendar uma entrega, obter um link para o relatório ou baixá-lo.
O compartilhamento no Looker Studio é muito semelhante ao do Google Drive.
Você pode escolher se deseja que os destinatários possam visualizar ou editar o relatório.
Basta clicar em Enviar para compartilhar o relatório.
Os dados podem ser visualizados e compartilhados tanto no Looker quanto no Looker Studio.
O que é certo para você e sua equipe depende das necessidades específicas da sua organização.

> Quiz: Making data-driven decisions using Looker

Isso nos leva ao final deste módulo sobre como tomar decisões baseadas em dados usando o Looker.
Agora você está pronto para começar a analisar, visualizar e compartilhar dados usando o Looker e o Looker Studio.
Vamos recapitular o que você aprendeu.
Primeiro, você recebeu uma introdução à exploração de dados no Looker, incluindo a manipulação do Looker Explore e o uso de dimensões, medidas, filtros e pivôs para encontrar respostas a perguntas baseadas em dados.
Depois disso, você aprendeu sobre as diversas opções de visualização disponíveis no Looker e no Looker Studio.
Você também recebeu uma demonstração de como criar um gráfico no Looker Studio.
Você também recebeu uma demonstração de como criar um gráfico no Looker Studio.
Por fim, você comparou os benefícios e as desvantagens de usar o Looker e o Looker Studio para compartilhar dados com outras pessoas e aprendeu como compartilhar dados de ambas as plataformas.


