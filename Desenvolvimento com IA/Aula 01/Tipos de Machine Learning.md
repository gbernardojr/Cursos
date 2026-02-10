## 1. Aprendizado Supervisionado (Supervised Learning)

É o tipo mais comum. Nele, a IA aprende com um conjunto de dados que já contém a **resposta correta** (rótulos ou *labels*). É como um aluno estudando com um livro que tem o gabarito no final.

### Subclassificações:

* **Classificação:** O objetivo é prever uma categoria (discreta).
* *Exemplo:* Filtro de Spam (é spam ou não é?), diagnóstico de doenças (doente ou saudável).


* **Regressão:** O objetivo é prever um valor numérico contínuo.
* *Exemplo:* Prever o preço de uma casa com base na metragem, prever a temperatura de amanhã.



> **Exemplo Prático:** Você fornece ao algoritmo 10.000 fotos de peças industriais, marcando quais estão "defeituosas" e quais estão "boas". Após o treino, ele classifica novas peças sozinho.

---

## 2. Aprendizado Não Supervisionado (Unsupervised Learning)

Aqui, a IA recebe dados **sem rótulos**. Ela não sabe o que é o quê. O objetivo é que ela encontre **padrões, estruturas ou grupos** escondidos por conta própria.

### Subclassificações:

* **Agrupamento (Clustering):** Junta dados que possuem características semelhantes.
* *Exemplo:* Segmentação de clientes (grupo que compra eletrônicos vs. grupo que compra roupas).


* **Associação:** Descobre regras que descrevem seus dados.
* *Exemplo:* "Quem compra pão, também costuma comprar manteiga" (sistemas de recomendação de mercado).


* **Redução de Dimensionalidade:** Simplifica dados complexos mantendo as informações essenciais.
* *Exemplo:* Comprimir uma imagem ou simplificar um banco de dados com centenas de colunas.



> **Exemplo Prático:** Você joga o histórico de compras de uma loja no algoritmo sem dizer nada. Ele identifica sozinho que existem 3 perfis diferentes de consumidores.

---

## 3. Aprendizado por Reforço (Reinforcement Learning)

Não há dados prévios. A IA aprende através da **interação com um ambiente**. Ela toma decisões e recebe uma **recompensa** (se for bom) ou uma **punição** (se for ruim). O objetivo é maximizar a recompensa total ao longo do tempo.

### Subclassificações:

* **Baseado em Valor (Value-based):** A IA tenta encontrar a ação que gera o maior valor futuro (ex: Q-Learning).
* **Baseado em Política (Policy-based):** A IA foca em aprender diretamente a melhor estratégia ou "caminho" a seguir.
* **Model-Based vs Model-Free:** Se a IA tenta criar um mapa interno do ambiente ou se ela apenas reage ao que vê no momento.

> **Exemplo Prático:** Um robô aprendendo a andar. Cada passo à frente é um ponto positivo; cair no chão é um ponto negativo. Após milhões de tentativas, ele "descobre" a marcha perfeita.

> <img width="2048" height="1593" alt="image" src="https://github.com/user-attachments/assets/7c6147e4-035e-49f5-9760-22c82a9e25cd" />


---

## 📊 Quadro Comparativo para Slide

| Tipo | Dados de Entrada | Objetivo | Exemplo |
| --- | --- | --- | --- |
| **Supervisionado** | Rotulados (com resposta) | Mapear entrada -> saída | Prever preço de venda |
| **Não Supervisionado** | Não rotulados (sem resposta) | Descobrir padrões ocultos | Agrupar clientes vips |
| **Por Reforço** | Interação viva (Ambiente) | Aprender uma sequência de ações | Dirigir carro autônomo |

---

### 💡 Por que o programador de IA precisa saber isso?

Muitas vezes, antes de usar a **IA Generativa** (Aula 01), você precisa tratar os dados.

* Se você quer que a IA entenda se um código é "seguro" ou "vulnerável", você usará **Supervisionado**.
* Se você tem milhares de logs de erro e não sabe por onde começar, usará **Não Supervisionado** para agrupá-los por similaridade.
