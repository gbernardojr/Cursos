## 📑 Plano de Aula 11 - Testes, Avaliação e Redes Neurais

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Pesquisa Aplicada e Aula Prática.

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Avaliar o desempenho do modelo e realizar o ajuste fino necessário; Avaliar redes neurais e métricas de sucesso.
* **Capacidade Socioemocional:** Demonstrar resiliência emocional ao lidar com resultados inesperados do modelo.
* **Conhecimento:** Métricas de avaliação (Precisão, Recall, F1-Score), Testes A/B em Prompts, Introdução às Redes Neurais (Pesos e Viés).

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Contexto** | Discussão: "Como saber se a resposta da IA é realmente boa ou se apenas parece boa?". |
| **60 min** | **Teoria Técnica** | Introdução às Redes Neurais: Como os neurônios digitais se conectam. Métricas de avaliação. |
| **20 min** | **Intervalo** | Pausa para café. |
| **90 min** | **Laboratório 10** | Execução de testes de consistência. Comparação entre o modelo original e o personalizado. |
| **40 min** | **Ajuste Fino** | Alteração de hiperparâmetros (temperatura, top_p) para otimizar os resultados. |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 11)

#### **Slide 1: Por dentro da Rede Neural**

* **Explicação:** Explique que a rede neural funciona por camadas. Cada camada extrai uma característica do texto (ex: gramática, tom de voz, lógica de programação). Use a analogia das camadas de cebola: quanto mais fundo, mais específico é o entendimento.

#### **Slide 2: Métricas de Sucesso - Além do "Gostei"**

* **Explicação:** Ensine que em produção usamos métricas:
* **Precisão:** Das respostas que a IA deu, quantas estavam certas?
* **Recall:** De todas as respostas certas possíveis, quantas a IA conseguiu encontrar?
* **F1-Score:** O equilíbrio entre as duas acima.



#### **Slide 3: Teste A/B de Prompts**

* **Explicação:** Mostre como comparar duas versões do mesmo sistema.
* *Versão A:* Prompt curto.
* *Versão B:* Prompt com exemplos (Few-shot).
* **Tarefa:** Rodar 10 testes em cada e tabular qual falhou menos.



#### **Slide 4: O Ciclo de Melhoria Contínua**

* **Explicação:** O trabalho do dev de IA não acaba no deploy. É um ciclo: Testar -> Analisar Erro -> Ajustar Prompt/Dataset -> Testar novamente.

---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para aplicar a **Avaliação de Modelos** conforme a metodologia:

1. **O Desafio:** "Seu chatbot de código está sugerindo funções que usam bibliotecas desatualizadas (Depreciadas)."
2. **A Missão:** Os alunos devem analisar o "Viés" do modelo (ele foi treinado com dados antigos).
3. **Ação:** Eles devem criar um **"Gold Standard"** (um conjunto de 5 perguntas e 5 respostas perfeitas) e testar se o modelo atual passa nesse teste. Se não passar, devem sugerir um ajuste no *System Prompt* para forçar o uso de versões novas.

---

### ✅ Critério de Avaliação

* O aluno consegue explicar a diferença entre um modelo com erro de lógica e um modelo com alucinação por falta de dados?
* O aluno realizou o ajuste de pelo menos dois hiperparâmetros (ex: temperatura) e documentou a diferença nos resultados?

