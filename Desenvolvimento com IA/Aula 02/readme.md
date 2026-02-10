## 📑 Plano de Aula 02 - Engenharia de Prompt e Prática Inicial

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Aula Prática em Laboratório com Demonstração Guiada.

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Estruturar e codificar soluções utilizando inteligências artificiais.
* **Capacidade Socioemocional:** Demonstrar atenção aos detalhes na formulação de instruções.
* **Conhecimento:** Engenharia de Prompt: Comandos, estruturação de contexto e técnicas de interação.

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Recapitulando** | Breve revisão da Aula 1 e verificação de acesso das contas (OpenAI/ChatGPT) dos alunos. |
| **60 min** | **Demonstração** | Exposição dos pilares de um bom Prompt: Contexto, Tarefa, Instruções e Formato de Saída. |
| **20 min** | **Intervalo** | Pausa para descanso. |
| **90 min** | **Laboratório 1** | Exercício guiado: Criar prompts para gerar funções simples em diferentes linguagens (Python, JS, etc). |
| **40 min** | **Desafio Rápido** | "O Prompt de Ouro": Alunos devem criar um prompt que gere um código e o respectivo teste unitário. |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 2)

#### **Slide 1: O que é Engenharia de Prompt?**

* **Explicação:** Defina como a arte de "programar em linguagem natural". Explique que o resultado da IA é 10% algoritmo e 90% a qualidade da pergunta.

#### **Slide 2: A Anatomia de um Prompt Profissional**

* **Explicação:** Mostre o framework **CTIF**:
1. **Contexto:** Quem a IA deve ser? (Ex: "Atue como um desenvolvedor Senior Backend").
2. **Tarefa:** O que ela deve fazer? (Ex: "Crie uma função de validação de CPF").
3. **Instruções:** Quais as regras? (Ex: "Use Python 3.10, sem bibliotecas externas").
4. **Formato:** Como deve entregar? (Ex: "Retorne apenas o código e um exemplo de uso").



#### **Slide 3: Técnicas Avançadas (Few-Shot Prompting)**

* **Explicação:** Explique que dar exemplos à IA aumenta drasticamente a assertividade.
* **Exemplo:** "Aqui está um exemplo de como eu documento minhas funções: [Exemplo]. Agora, documente esta nova função seguindo o mesmo padrão."

#### **Slide 4: Zero-Shot vs. Chain of Thought**

* **Explicação:** * **Zero-Shot:** Pedir a resposta direto.
* **Chain of Thought (Cadeia de Pensamento):** Pedir para a IA "pensar passo a passo". Isso reduz erros de lógica em códigos complexos.



#### **Slide 5: Lidando com Alucinações no Código**

* **Explicação:** Instrua os alunos a sempre incluírem: "Se você não tiver certeza de qual biblioteca usar, me avise, não invente uma".

---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para que o aluno sinta a "dor" do mercado e a solução da IA, faça o seguinte exercício no Laboratório:

1. **O Problema Vago:** Peça para eles digitarem apenas: *"Crie um sistema de login"*.
2. **O Resultado:** Eles verão que a IA traz algo genérico, talvez em uma linguagem que eles não usam.
3. **O Refinamento:** Agora peça para aplicarem o framework **CTIF**: *"Atue como desenvolvedor Python. Crie um sistema de login usando Flask e SQLite. Foque na segurança da senha usando Werkzeug. Retorne o código comentado em português."*
4. **A Conclusão:** Comparem os dois resultados. O segundo economiza horas de ajuste manual.

---

### ✅ Critério de Avaliação

* O aluno consegue estruturar um prompt que contenha Persona, Contexto e Saída formatada?
* O código gerado atende aos requisitos técnicos solicitados no prompt?

