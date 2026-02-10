O framework **CTIF** (**Context, Task, Instruction, Format**) é uma das metodologias mais eficazes de **Engenharia de Prompt**. Um prompt não é apenas uma "pergunta", mas uma estrutura de dados enviada para um modelo probabilístico.

Se você pula uma dessas etapas, a IA precisa "adivinhar" sua intenção, o que aumenta a chance de alucinação.

---

## 🏗️ Os 4 Pilares do CTIF

### 1. Context (Contexto)

É o "quem sou eu" ou "em que situação estamos". Aqui você define a **Persona** da IA e o cenário. Sem contexto, a IA responde de forma genérica.

* **O que incluir:** Papel profissional, restrições de ambiente, tecnologias envolvidas e público-alvo.
* *Exemplo:* "Você é um desenvolvedor Sênior especializado em segurança de sistemas (Cybersecurity) para o setor bancário."

### 2. Task (Tarefa)

É a ação principal. Deve começar com um **verbo de ação** claro. Seja específico sobre o que deve ser feito.

* **O que incluir:** O objetivo central da interação.
* *Exemplo:* "Analise este script em Python em busca de vulnerabilidades de SQL Injection."

### 3. Instruction (Instrução/Diretriz)

São as "regras do jogo". Aqui você define o que a IA **deve** e **não deve** fazer, quais critérios seguir e passos intermediários.

* **O que incluir:** Limitações, passos lógicos, bibliotecas específicas a serem usadas e tom de voz.
* *Exemplo:* "Não utilize bibliotecas externas. Siga as diretrizes da OWASP. Explique o risco de cada falha encontrada antes de sugerir a correção."

### 4. Format (Formato)

É a estrutura da saída. Como você quer receber o dado para que ele seja útil imediatamente no seu fluxo de trabalho?

* **O que incluir:** JSON, Markdown, Tabela, Lista, Código, Tom de voz (formal/informal).
* *Exemplo:* "Retorne a resposta em uma tabela Markdown contendo as colunas: 'Linha do Erro', 'Nível de Risco' e 'Sugestão de Código'."

---

## 🚀 Exemplo Prático: Comparação

### Prompt Sem Framework (Amador):

> "Faz um código de login para mim."

* **Resultado:** A IA vai gerar um código aleatório (pode ser PHP, Java ou Python), possivelmente inseguro e sem explicação.

### Prompt Com CTIF (Profissional):

* **C:** Você é um instrutor de backend do SENAI.
* **T:** Crie um sistema de login simples.
* **I:** Use Python com o framework Flask. Foque em segurança, utilizando hash para senhas (library `werkzeug`). Comente cada linha do código para iniciantes.
* **F:** Forneça o código em um bloco de código único, seguido por uma lista em tópicos com os pré-requisitos de instalação.

---

## 💡 Por que o CTIF funciona matematicamente?

Como discutimos sobre **Tokens e Embeddings**, o CTIF funciona porque ele "ancora" o vetor da IA em uma região específica do espaço latente.

* Ao dar o **Contexto**, você fecha o campo de busca da IA.
* Ao dar as **Instruções**, você cria barreiras de probabilidade, impedindo que ela gere tokens que fujam da regra.

---

### 🛠️ Aplicação na Aula 02 do SENAI

Ao aplicar este framework, os alunos desenvolvem a capacidade socioemocional de **Organização e Atenção aos Detalhes**. Um programador que domina o CTIF gasta 5 minutos escrevendo um prompt, mas economiza 2 horas de refatoração manual.

Abaixo, apresento um prompt "cru" (muito comum entre iniciantes) e o seu desafio é reestruturá-lo usando os pilares do **CTIF**.

---

### 🔴 O Prompt Ruim (Cenário de Problema)

> *"Faz uma função em JavaScript que calcula desconto de produto para um e-commerce. Quero que seja rápido."*

**Por que este prompt é perigoso?**

1. Não define o tipo de desconto (fixo ou percentual).
2. Não trata erros (ex: preço negativo).
3. "Rápido" é subjetivo: pode significar poucas linhas ou alta performance.

---

### 🟢 O Desafio: Aplicando o CTIF

Sua missão é preencher os campos abaixo para que a IA entregue um código profissional e pronto para produção:

* **C (Context):** (Dica: Defina a IA como um desenvolvedor Full Stack experiente).
* **T (Task):** (Dica: O que exatamente a função deve receber e retornar?).
* **I (Instruction):** (Dica: Quais regras de validação usar? Deve usar ES6? Deve documentar com JSDoc?).
* **F (Format):** (Dica: Apenas o código? Explicação técnica em tópicos?).

---

### 💡 Minha sugestão de Resolução (Para comparação)

Se eu fosse aplicar o framework para esse caso no laboratório, eu escreveria assim:

> **C:** Atue como um Desenvolvedor Senior Backend especializado em Node.js.
> **T:** Escreva uma função em JavaScript (ES6+) para cálculo de descontos em um carrinho de compras.
> **I:** A função deve receber o `valorOriginal` e a `porcentagemDesconto`. Implemente uma validação: se o desconto for maior que 100% ou o valor for menor que zero, a função deve retornar um erro claro. Use nomes de variáveis semânticos.
> **F:** Forneça o código formatado com comentários JSDoc e, logo abaixo, 3 exemplos de chamadas de função (testes simples).

---

### 🧠 Reflexão para o Aluno

Ao comparar os dois, note como o segundo remove a **ambiguidade**. Para a IA, menos ambiguidade significa menos "palpites" probabilísticos e mais precisão lógica.
