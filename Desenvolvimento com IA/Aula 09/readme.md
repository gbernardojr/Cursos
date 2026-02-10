## 📑 Plano de Aula 09 - Desenvolvimento de Chatbots e NLP

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Projeto Prático (Desenvolvimento de Protótipo).

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Criar um chatbot personalizado utilizando o processamento de linguagem natural (NLP).
* **Capacidade Socioemocional:** Resolver problemas complexos ao lidar com fluxos de conversação ambíguos.
* **Conhecimento:** Fundamentos de NLP, Gestão de Contexto (Histórico de Chat), Engenharia de Diálogo e UX para Chatbots.

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Conceituação** | O que faz um bot parecer "humano"? Discussão sobre intenção e contexto. |
| **60 min** | **Teoria Técnica** | Como gerenciar o histórico de mensagens para a IA não "esquecer" o que foi dito. |
| **20 min** | **Intervalo** | Pausa para networking. |
| **90 min** | **Laboratório 8** | Construção de um script que simula um chat contínuo (loop de entrada/saída). |
| **40 min** | **Teste de UX** | Teste de "Stress": Tentar confundir o bot do colega para ver como ele reage. |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 9)

#### **Slide 1: O que é NLP na prática?**

* **Explicação:** NLP é a ponte. É como a máquina transforma o "texto bagunçado" do humano em algo estruturado. Explique conceitos como **Tokenização** (visto na Aula 1) e **Análise de Sentimento**.

#### **Slide 2: A Memória do Chatbot (State Management)**

* **Explicação:** A API da OpenAI "esquece" tudo a cada nova chamada. Para o bot ter memória, o desenvolvedor precisa reenviar as perguntas e respostas anteriores a cada nova interação.
* **Dica:** Mostre como a lista de mensagens no JSON cresce a cada turno.

#### **Slide 3: Personas e o System Prompt**

* **Explicação:** O "System Prompt" é o que define o comportamento do bot.
* **Exemplo:** "Você é um assistente técnico da SENAI-SP. Seja cordial, use termos técnicos e não responda sobre assuntos fora da tecnologia."

#### **Slide 4: Fluxos de Diálogo e Fallbacks**

* **Explicação:** O que o bot faz quando não entende? Ensine a programar mensagens de erro elegantes (Fallbacks) para que o usuário não fique sem resposta.

---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para aplicar a **Resolução de Problemas Complexos** da Metodologia SENAI:

1. **O Desafio:** "Seu chatbot de suporte está gastando muitos tokens porque o histórico de conversa está ficando grande demais."
2. **A Missão:** Os alunos devem pesquisar e implementar uma estratégia de **"Summarization"** (Resumo).
* *Como?* Quando a conversa chegar a 10 mensagens, peça para a IA resumir os pontos principais e use esse resumo como o novo contexto, "limpando" as mensagens antigas.


3. **Ação:** Implementar esse "limite de memória" no script do laboratório.

---

### ✅ Critério de Avaliação

* O chatbot consegue manter o contexto de uma conversa por pelo menos 3 interações seguidas?
* O aluno definiu uma Persona clara no *System Prompt* que restringe o escopo de atuação do bot?

