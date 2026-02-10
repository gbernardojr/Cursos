# 🚀 Do Texto à Resposta: A Jornada do Dado na IA

### 1. A Camada de Entrada (Tokenização)

O texto é fatiado em **Tokens** (pedaços de significado).

* **O que a IA vê:** Não são letras, mas IDs numéricos.
* **Fato Curioso:** A indentação e os espaços no código também são tokens e ocupam "espaço" na memória da IA.

---

### 2. A Camada de Significado (Embeddings)

Os IDs numéricos são convertidos em **Vetores** em um mapa matemático (Espaço Latente).

* **Geometria Semântica:** Palavras com sentidos próximos (ex: `Python` e `Código`) ficam fisicamente perto no mapa.
* **Cálculo:** A IA entende o mundo através de distâncias e ângulos entre esses pontos.

---

### 3. A Camada de Contexto (Atenção / Self-Attention)

A IA olha para a frase inteira ao mesmo tempo para resolver ambiguidades.

* **O "Peso":** A palavra "Banco" é puxada para o setor de "Móveis" ou "Finanças" dependendo das outras palavras ao redor.
* **Conexão:** É aqui que a IA entende que o `if` que ela está escrevendo agora depende da `variável` que você defini os 10 linhas acima.

---

### 4. A Camada de Decisão (Predição Probabilística)

Após entender o contexto, a IA calcula qual é o **próximo token mais provável**.

* **Não é mágica, é estatística:** Ela não "sabe" a resposta, ela calcula qual peça de código melhor completa o padrão que você iniciou.
* **Temperatura:** Define se a IA deve ser conservadora (escolher sempre o mais provável) ou criativa (arriscar tokens menos óbvios).

---

### 📋 Resumo para o Aluno SENAI:

| Etapa | Nome Técnico | O que acontece? |
| --- | --- | --- |
| **1** | **Tokenização** | Quebra o texto em pedaços e IDs. |
| **2** | **Embedding** | Dá significado matemático (coordenadas). |
| **3** | **Attention** | Entende a relação entre as palavras da frase. |
| **4** | **Inference** | Gera a resposta token por token. |

---

**Com este infográfico, fechamos o Ciclo de Fundamentos da Aula 01!**
