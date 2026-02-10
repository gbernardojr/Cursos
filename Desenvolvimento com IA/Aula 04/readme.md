## 📑 Plano de Aula 04 - Depuração de Código (Debug) com IA

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Situação-Problema (Resolução de Erros).

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Corrigir erros em scripts, builds e deploys com ChatGPT.
* **Capacidade Socioemocional:** Demonstrar resiliência emocional ao lidar com falhas e persistência na busca de soluções.
* **Conhecimento:** Identificação de bugs, interpretação de Stack Trace (rastreamento de erro) e análise de logs.

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Contextualização** | Discussão sobre o tempo gasto em "caça aos bugs" no dia a dia do dev. |
| **60 min** | **Teoria Técnica** | Como fornecer contexto de erro para a IA: Colando o erro + código fonte. |
| **20 min** | **Intervalo** | Pausa para café. |
| **90 min** | **Laboratório 3** | Atividade "O Código Quebrado": Alunos recebem scripts com erros de lógica e sintaxe para corrigir. |
| **40 min** | **Check-list** | Criação de um roteiro mental: "O que perguntar à IA quando o código não roda?". |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 4)

#### **Slide 1: O Ciclo do Bug**

* **Explicação:** Mostre que o bug faz parte do desenvolvimento. A diferença é que agora temos um assistente que leu bilhões de linhas de código e conhece os erros mais comuns de cada linguagem.

#### **Slide 2: Como pedir ajuda (Contexto de Erro)**

* **Explicação:** Enfatize que colar apenas o erro não basta. O prompt ideal deve conter:
1. O código que gerou o erro.
2. A mensagem de erro completa (Stack Trace).
3. O que o aluno esperava que acontecesse.



#### **Slide 3: Tipos de Erros que a IA resolve bem**

* **Explicação:**
* **Sintaxe:** Parênteses faltando, erros de indentação.
* **Lógica:** Loops infinitos, condições que nunca são atendidas.
* **Ambiente:** Erros de biblioteca faltando ou versões incompatíveis.



#### **Slide 4: Validando a correção**

* **Explicação:** Importante! A IA pode sugerir uma correção que quebra outra parte do código. Ensine o aluno a perguntar: "Esta correção impacta o desempenho ou a segurança?".

---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para aplicar a **Situação-Problema** proposta na metodologia:

1. **O Desafio:** Entregue aos alunos um script em Python ou C# que deveria realizar um cálculo simples (ex: média de notas), mas que possui um erro "silencioso" (o código roda, mas o resultado está errado).
2. **Uso da IA:** Peça para eles usarem o ChatGPT para realizar o **"Rubber Duck Debugging"** (técnica do patinho de borracha), explicando para a IA o que o código faz até que ela aponte o erro de lógica.
3. **Resultado Esperado:** O aluno deve apresentar o código corrigido e explicar *por que* o erro estava acontecendo, garantindo que ele aprendeu com a correção da IA.

---

### ✅ Critério de Avaliação

* O aluno conseguiu identificar a causa raiz do erro utilizando os insights da IA?
* A solução proposta corrigiu o problema sem gerar novos erros de sintaxe?
