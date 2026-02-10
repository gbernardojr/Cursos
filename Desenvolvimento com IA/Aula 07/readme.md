## 📑 Plano de Aula 07 - Implementação Técnica via API

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Aula Prática (Laboratório) com Demonstração de Fluxo.

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Implementar o ChatGPT em aplicações usando suas bibliotecas e APIs.
* **Capacidade Socioemocional:** Demonstrar autonomia na resolução de problemas de conectividade e autenticação.
* **Conhecimento:** Introdução à API da OpenAI, Documentação oficial, Autenticação (API Keys), Endpoints de Chat Completion e JSON.

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Contexto** | Diferença entre o ChatGPT (Produto) e a API (Motor). Por que empresas usam a API? |
| **60 min** | **Teoria Técnica** | Explorando a documentação oficial. Conceitos de *Headers*, *Payload* e *API Keys*. |
| **20 min** | **Intervalo** | Pausa para café. |
| **90 min** | **Laboratório 6** | Configuração de ambiente (Python/Node) e realização da primeira chamada de API. |
| **40 min** | **Desafio** | Alterar parâmetros como `temperature` e `max_tokens` para observar mudanças na resposta. |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 7)

#### **Slide 1: O Ecossistema da API**

* **Explicação:** Mostre que a API permite que qualquer software (um app mobile, um site ou um sistema de estoque) "converse" com o cérebro do GPT. Explique o modelo de custo (Pay-per-token).

#### **Slide 2: Segurança e API Keys**

* **Explicação:** Este é o ponto mais crítico. Ensine que a **API Key é uma senha**.
* **Dica Prática:** Nunca submeter a chave ao GitHub. Use arquivos `.env` (variáveis de ambiente).

#### **Slide 3: O Objeto JSON de Requisição**

* **Explicação:** Mostre a estrutura de uma chamada:
* **Model:** (Ex: gpt-3.5-turbo).
* **Messages:** Onde definimos o `system` (quem a IA é), `user` (pergunta) e `assistant` (histórico).



#### **Slide 4: Parâmetros de Controle (A "Mão" do Dev)**

* **Explicação:** * **Temperature:** 0 (preciso/robótico) a 2 (criativo/caótico). Para código, usamos valores baixos (0.1 a 0.3).
* **Max Tokens:** Limita o tamanho da resposta para controlar custos.



---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para aplicar a **Metodologia SENAI**, vamos simular uma falha comum:

1. **O Problema:** O aluno tentará rodar o código e receberá um erro (Ex: *401 Unauthorized* ou *429 Too Many Requests*).
2. **A Mediação:** Não dê a resposta. Peça para ele colar o código de erro no ChatGPT ou olhar a documentação e descobrir o que o código HTTP significa.
3. **Resultado:** O aluno aprende a interpretar o "diálogo" entre sistemas (Client-Server), uma competência essencial de Backend.

---

### ✅ Critério de Avaliação

* O aluno conseguiu gerar uma resposta da API dentro de um script local (ex: rodando no VS Code)?
* O aluno utilizou variáveis de ambiente para proteger sua chave de API?

