## 📑 Plano de Aula 08 - Processamento de Dados e Avaliação de Modelos

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Pesquisa Aplicada e Aula Prática (Laboratório).

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Realizar o ajuste de parâmetros e avaliação do modelo e redes neurais.
* **Capacidade Socioemocional:** Demonstrar pensamento analítico ao interpretar métricas de erro e precisão.
* **Conhecimento:** Coleta e pré-processamento de dados para treinamento, métricas de sucesso (Loss, Accuracy) e avaliação de redes neurais.

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Recapitulando** | Revisão dos arquivos JSONL criados na Aula 06 e preparação para o "Upload". |
| **60 min** | **Teoria Técnica** | Como a IA avalia o próprio aprendizado? Explicação sobre *Training Loss* e *Validation Loss*. |
| **20 min** | **Intervalo** | Pausa para café. |
| **90 min** | **Laboratório 7** | Simulação de treinamento: Submissão do dataset e monitoramento do progresso via CLI ou Dashboard. |
| **40 min** | **Análise Crítica** | Teste do modelo treinado: "A IA respondeu conforme o dataset ou ignorou as instruções?". |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 8)

#### **Slide 1: O que acontece durante o Processamento?**

* **Explicação:** Mostre que o servidor da OpenAI está ajustando os "pesos" das conexões neurais para que, ao receber o seu prompt específico, a resposta saia exatamente como no seu exemplo.

#### **Slide 2: Entendendo as Métricas de Erro (Loss)**

* **Explicação:** Use um gráfico simples. A "Loss" (Perda) é a distância entre a resposta da IA e a resposta correta.
* **O objetivo:** Quanto menor a Loss ao final do treino, mais "inteligente" o modelo ficou naquele assunto específico.

#### **Slide 3: Overfitting – O perigo de decorar**

* **Explicação:** Explique que se a IA ler os dados vezes demais (muitas *epochs*), ela pode "decorar" as frases em vez de aprender o conceito. Isso é o *Overfitting*. Se você mudar uma vírgula na pergunta, ela trava.

#### **Slide 4: Teste de Validação (O "Pente Fino")**

* **Explicação:** Ensine a técnica de separar 10% dos dados para não treinar a IA com eles. Depois do treino, usamos esses 10% para ver se ela acerta algo que "nunca viu antes".

---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para aplicar a **Avaliação de Modelos** conforme a metodologia:

1. **O Cenário:** A IA foi treinada para ser um suporte técnico de uma linguagem de programação específica, mas está respondendo de forma grosseira ou incompleta.
2. **A Missão:** Os alunos devem identificar se o problema está:
* No **Volume de Dados** (Poucos exemplos).
* Na **Qualidade** (Dados contraditórios no dataset).
* Nos **Parâmetros** (Temperatura muito alta na hora de testar).


3. **Ação:** Proponha que eles façam um "Ajuste Fino do Ajuste Fino", corrigindo 3 linhas do dataset e explicando por que aquela mudança é necessária.

---

### ✅ Critério de Avaliação

* O aluno identifica corretamente se um modelo está apresentando *Overfitting* ou se precisa de mais dados?
* O aluno demonstra compreensão sobre como os parâmetros de treinamento influenciam o resultado final?
