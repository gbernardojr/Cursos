## 📑 Plano de Aula 10 - Implementação Final e Integração

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Projeto (Desenvolvimento de Aplicação).

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Implementar o ChatGPT em aplicações reais de chatbot usando suas bibliotecas e APIs.
* **Capacidade Socioemocional:** Demonstrar autonomia na escolha de ferramentas e tecnologias de integração.
* **Conhecimento:** Bibliotecas oficiais (OpenAI Python/Node.js), integração de frontend e backend, variáveis de ambiente e segurança na implementação.

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Alinhamento** | Revisão do fluxo: Usuário -> Frontend -> Backend -> API OpenAI -> Resposta. |
| **60 min** | **Teoria Técnica** | Uso de SDKs oficiais vs. Requests puros. Boas práticas de tratamento de erros em produção. |
| **20 min** | **Intervalo** | Pausa para café. |
| **120 min** | **Laboratório 9** | Integração da API em uma interface (ex: formulário Web simples ou App de console robusto). |
| **10 min** | **Encerramento** | Briefing sobre a Aula 11 (Testes e Redes Neurais). |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 10)

#### **Slide 1: A Arquitetura de uma App com IA**

* **Explicação:** Mostre que o segredo não é a IA sozinha, mas como ela se conecta aos dados da empresa. Explique que o Backend serve como um "filtro" de segurança antes de mandar a pergunta para a OpenAI.

#### **Slide 2: Bibliotecas Oficiais (SDKs)**

* **Explicação:** Apresente a biblioteca `openai` para Python ou Node.js. Mostre como ela facilita a vida do dev ao gerenciar a conexão e o formato das respostas automaticamente.

#### **Slide 3: Tratamento de Erros em Tempo Real**

* **Explicação:** No mundo real, a internet cai ou a API demora. Ensine a implementar:
* **Timeouts:** Não deixar o usuário esperando para sempre.
* **Loading States:** Mostrar que a IA está "pensando".
* **Try/Catch:** Evitar que o app quebre se a API retornar erro.



#### **Slide 4: Segurança e Variáveis de Ambiente (.env)**

* **Explicação:** Reforce o conceito da Aula 7. Mostre como carregar chaves de API sem deixá-las expostas no código fonte.

---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para aplicar a **Capacidade de Implementação** da Metodologia SENAI:

1. **O Desafio:** "Crie uma interface simples (pode ser via Streamlit ou HTML/JS) onde o usuário digita um código bugado e o sistema devolve a versão corrigida."
2. **A Missão:** O aluno deve:
* Criar o servidor (Backend).
* Integrar com a chave de API.
* Criar o "Prompt de Sistema" que garanta que a IA se comporte como um revisor de código.


3. **Resultado:** O aluno deve mostrar o sistema funcionando fora do ambiente de teste da OpenAI (Playground), rodando como um software independente.

---

### ✅ Critério de Avaliação

* O aluno conseguiu realizar a integração completa (entrada de usuário -> processamento da IA -> saída no sistema)?
* O código de integração está organizado e utiliza as bibliotecas recomendadas?

