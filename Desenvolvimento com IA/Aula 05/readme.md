## 📑 Plano de Aula 05 - Refatoração de Código com IA

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Estudo de Caso e Pesquisa Aplicada.

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Refatorar códigos com ChatGPT para melhorar o desempenho geral.
* **Capacidade Socioemocional:** Demonstrar pensamento analítico ao avaliar diferentes estruturas de código.
* **Conhecimento:** Refatoração de código: Legibilidade, desempenho, complexidade ciclomática e padrões de projeto (Design Patterns).

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Conceituação** | O que é código "sujo" (Dirty Code) e o impacto disso na manutenção de sistemas. |
| **60 min** | **Teoria Técnica** | Técnicas de Refatoração: Renomeação, extração de métodos e simplificação de condicionais. |
| **20 min** | **Intervalo** | Pausa para café. |
| **90 min** | **Laboratório 4** | Atividade "Extreme Makeover": Refatorar um script funcional, mas confuso, usando a IA. |
| **40 min** | **Avaliação Cruzada** | Alunos comparam o código original vs. refatorado e justificam as melhorias. |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 5)

#### **Slide 1: Refatorar != Corrigir**

* **Explicação:** Deixe claro que refatorar não é mudar o que o código faz, mas sim como ele é feito "por baixo do capô". É como reformar o motor de um carro para ele ser mais econômico sem mudar o destino da viagem.

#### **Slide 2: Indicadores de Código Ruim (Code Smells)**

* **Explicação:** Mostre como a IA identifica:
* Funções gigantescas (Long Method).
* Nomes de variáveis genéricos (ex: `var a`, `var b`).
* Código duplicado.



#### **Slide 3: Prompts para Refatoração Profissional**

* **Explicação:** Ensine o aluno a não pedir apenas "melhore este código". O prompt deve ser específico:
* "Refatore este código seguindo os princípios de **Clean Code**."
* "Simplifique estes `if/else` aninhados usando cláusulas de guarda."
* "Melhore a performance deste loop para grandes volumes de dados."



#### **Slide 4: Complexidade Ciclomática**

* **Explicação:** Explique que a IA pode ajudar a reduzir o número de caminhos que um código segue. Quanto mais simples o caminho, mais fácil é testar e menos chances de bugs no futuro.

---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para aplicar a **Pesquisa Aplicada** da Metodologia SENAI:

1. **O Desafio:** Forneça um código que utiliza muitos loops `for` aninhados (o famoso "código espaguete").
2. **Uso da IA:** Peça para os alunos solicitarem ao ChatGPT a refatoração utilizando recursos modernos da linguagem (ex: *List Comprehension* em Python ou *LINQ* em C#).
3. **A Prova Real:** Peça para a IA gerar um script de medição de tempo (`timeit`) para comparar a execução do código antigo com o novo. Isso prova tecnicamente que a refatoração melhorou o desempenho.

---

### ✅ Critério de Avaliação

* O aluno conseguiu reduzir a complexidade do código mantendo a funcionalidade original?
* O aluno justificou as mudanças feitas pela IA (ex: "foi usado o padrão Factory para facilitar a expansão")?

