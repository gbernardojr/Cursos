=========================================
Conjunto de dados de compartilhamento de bicicletas
=========================================

Hadi Fanaee-T

Laboratório de Inteligência Artificial e Apoio à Decisão (LIAAD), Universidade do Porto
INESC Porto, Campus da FEUP
Rua Dr. Roberto Frias, 378
4200 - 465 Porto, Portugal


========================================
Fundo
==========================================

Os sistemas de compartilhamento de bicicletas são uma nova geração de aluguel de bicicletas tradicionais, onde todo o processo, desde a adesão, aluguel e devolução, se tornou automático. Por meio desses sistemas, o usuário pode facilmente alugar uma bicicleta em um local específico e devolvê-la em outro. Atualmente, existem cerca de 500 programas de compartilhamento de bicicletas em todo o mundo, que abrangem mais de 500 mil bicicletas. Atualmente, existe grande interesse nesses sistemas devido ao seu importante papel no trânsito, questões ambientais e de saúde.

Além das interessantes aplicações reais dos sistemas de compartilhamento de bicicletas, as características dos dados gerados por esses sistemas os tornam atraentes para a pesquisa. Ao contrário de outros serviços de transporte, como ônibus ou metrô, a duração da viagem, a posição de partida e chegada são registradas explicitamente nesses sistemas. Esse recurso transforma o sistema de compartilhamento de bicicletas em uma rede virtual de sensores que pode ser usada para detectar a mobilidade na cidade. Portanto, espera-se que a maioria dos eventos importantes na cidade possa ser detectada por meio do monitoramento desses dados.

==========================================
Conjunto de Dados
===========================================
O processo de aluguel de bicicletas compartilhadas está altamente correlacionado com as configurações ambientais e sazonais. Por exemplo, condições climáticas, precipitação, dia da semana, estação do ano, hora do dia, etc., podem afetar os comportamentos de aluguel. O conjunto de dados principal está relacionado ao registro histórico de dois anos correspondente aos anos de 2011 e 2012 do sistema Capital Bikeshare, Washington D.C., EUA, que está disponível publicamente em http://capitalbikeshare.com/system-data. Agregamos os dados a cada duas horas e diariamente e, em seguida,
extraímos e adicionamos as informações meteorológicas e sazonais correspondentes. As informações meteorológicas foram extraídas de http://www.freemeteo.com.

==========================================
Tarefas associadas
============================================

- Regressão:
Predição da contagem de aluguel de bicicletas por hora ou dia com base nas configurações ambientais e sazonais.

- Detecção de Eventos e Anomalias:
A contagem de bicicletas alugadas também está correlacionada a alguns eventos na cidade, facilmente rastreáveis ​​por meio de mecanismos de busca.
Por exemplo, uma consulta como "2012-10-30 Washington D.C." no Google retorna resultados relacionados ao Furacão Sandy. Alguns dos eventos importantes são
identificados em [1]. Portanto, os dados também podem ser usados ​​para validação de algoritmos de detecção de anomalias ou eventos.

==========================================
Arquivos
===========================================

- Readme.txt
- hour.csv: contagens de compartilhamento de bicicletas agregadas por hora. Registros: 17.379 horas
- day.csv - contagens de compartilhamento de bicicletas agregadas por dia. Registros: 731 dias

=========================================
Características do conjunto de dados
==========================================
Tanto hour.csv quanto day.csv possuem os seguintes campos, exceto hr, que não está disponível em day.csv

- instant: índice de registro
- dteday: data
- season: estação (1:primavera, 2:verão, 3:outono, 4:inverno)
- yr: ano (0:2011, 1:2012)
- mnth: mês (1 a 12)
- hr: hora (0 a 23)
- holiday: previsão do tempo, se o dia é feriado ou não (extraído de http://dchr.dc.gov/page/holiday-schedule)
- weekday: dia da semana
- workingday: se o dia não for fim de semana nem feriado, será 1, caso contrário, será 0.
+ weathersit:
- 1: Céu limpo, Poucas nuvens, Parcialmente nublado, Parcialmente nublado
- 2: Neblina + Nublado, Neblina + Nuvens isoladas, Neblina + Poucas nuvens, Neblina
- 3: Neve leve, Chuva leve + Trovoada + Nuvens isoladas, Chuva leve + Nuvens isoladas
- 4: Chuva forte + Paletes de gelo + Trovoada + Neblina, Neve + Nevoeiro
- temp: Temperatura normalizada em graus Celsius. Os valores são divididos por 41 (máx.)
- atemp: Temperatura ambiente normalizada em graus Celsius. Os valores são divididos por 50 (máx.)
- hum: Umidade normalizada. Os valores são divididos por 100 (máx.)
- windspeed: Velocidade do vento normalizada. Os valores são divididos em 67 (máx.)
- casual: contagem de usuários casuais
- registered: contagem de usuários registrados
- cnt: contagem total de bicicletas alugadas, incluindo casuais e registradas

=========================================
Licença
===========================================
O uso deste conjunto de dados em publicações deve ser citado na seguinte publicação:

[1] Fanaee-T, Hadi, e Gama, João, "Event labeling combined ensemble detectors and background knowledge", Progress in Artificial Intelligence (2013): pp. 1-15, Springer Berlin Heidelberg, doi:10.1007/s13748-013-0040-3.

@article{
ano={2013},
issn={2192-6352},
periódico={Progresso em Inteligência Artificial},
doi={10.1007/s13748-013-0040-3},
título={E
