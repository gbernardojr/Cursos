## 🛠️ Atividade: Mapeamento de Modelos de IA vs. Casos de Uso Reais

Esta tabela serve como gabarito para o instrutor ou como material de estudo para os alunos.

### 1. Aprendizado Supervisionado (Supervised Learning)

*Foco: Previsão baseada em dados históricos rotulados.*

| Caso de Uso Real | Subclassificação | Descrição do Funcionamento |
| --- | --- | --- |
| **Score de Crédito Bancário** | **Regressão** | O modelo analisa histórico de renda e dívidas para prever um número (0 a 1000) que representa o risco de inadimplência. |
| **Classificação de Imagens Médicas** | **Classificação** | Treinado com milhares de exames rotulados como "Normal" ou "Anomalia" para auxiliar radiologistas. |
| **Estimativa de Tempo de Entrega (ETA)** | **Regressão** | Aplicativos de delivery usam dados de entregas passadas, clima e trânsito para prever os minutos restantes. |
| **Detecção de Fraude em Cartão** | **Classificação** | O sistema marca uma transação como "Suspeita" ou "Legítima" com base no perfil de gasto do usuário. |

---

### 2. Aprendizado Não Supervisionado (Unsupervised Learning)

*Foco: Descoberta de estruturas e padrões em dados ocultos.*

| Caso de Uso Real | Subclassificação | Descrição do Funcionamento |
| --- | --- | --- |
| **Sistemas de Recomendação (Streaming)** | **Associação** | Identifica que usuários que assistiram ao filme "A" também gostaram do filme "B", sem que ninguém tenha rotulado essa conexão previamente. |
| **Agrupamento de Clientes (Marketing)** | **Clustering (Agrupamento)** | Divide a base de dados em grupos (ex: "Clientes Econômicos", "Clientes Premium", "Clientes Esporádicos") para campanhas focadas. |
| **Análise de Genoma** | **Clustering** | Agrupa sequências de DNA semelhantes para identificar ancestralidade ou propensão a características genéticas. |
| **Limpeza de Ruído em Áudio** | **Redução de Dimensionalidade** | Remove frequências irrelevantes de uma gravação, mantendo apenas os componentes essenciais da voz humana. |

---

### 3. Aprendizado por Reforço (Reinforcement Learning)

*Foco: Tomada de decisão sequencial e otimização de processos.*

| Caso de Uso Real | Subclassificação | Descrição do Funcionamento |
| --- | --- | --- |
| **Logística de Armazéns Robóticos** | **Model-Free** | Robôs em centros de distribuição aprendem o caminho mais curto para pegar um produto sem colidir com outros, recebendo "pontos" por eficiência. |
| **Otimização de Semáforos Inteligentes** | **Baseado em Valor** | A IA ajusta o tempo do sinal verde para maximizar o fluxo de veículos (recompensa) e minimizar o tempo de espera (punição). |
| **Sistemas de Trading de Alta Frequência** | **Baseado em Política** | Algoritmos que decidem o momento exato de comprar ou vender ações para maximizar o lucro diário da carteira. |
| **Treinamento de Jogadores Não-Jogáveis (NPCs)** | **Deep Reinforcement** | Bots em jogos complexos (como Dota 2 ou StarCraft) que aprendem estratégias de combate enfrentando a si mesmos milhões de vezes. |

<img width="2048" height="1593" alt="image" src="https://github.com/user-attachments/assets/6272351c-778b-4ee8-9440-cc78cbe67d4a" />

---

### 💡 Sugestão Didática para o Instrutor (Desafio de Aula)

Peça para os alunos escolherem **um** desses casos e desenharem no quadro (ou explicarem) o seguinte:

1. **Input:** O que entra de dados?
2. **Processamento:** Qual o tipo de IA?
3. **Output:** O que o sistema entrega no final?
