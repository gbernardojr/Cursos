## 📑 Plano de Aula 06 - Preparação de Dados e Treinamento Personalizado

**Unidade Curricular:** IA Generativa Aplicada à Programação – ChatGPT
**Carga Horária da Aula:** 4 horas
**Estratégia de Ensino:** Pesquisa Aplicada e Aula Prática.

### 🎯 Capacidades e Conhecimentos

* **Capacidade Técnica:** Aplicar o processo de treinamento personalizado do ChatGPT através de API, incluindo a coleta e pré-processamento de dados.
* **Capacidade Socioemocional:** Demonstrar autogestão na organização de volumes de dados e atenção aos detalhes.
* **Conhecimento:** Modelos personalizados, preparação de datasets (JSONL), ajuste de parâmetros (Fine-tuning) e ética no tratamento de dados.

---

### 🕒 Cronograma de Atividades

| Tempo | Etapa | Descrição da Atividade (Ações do Docente) |
| --- | --- | --- |
| **30 min** | **Introdução** | Explicação: Quando o "Prompt" não é suficiente e precisamos de "Fine-tuning". |
| **60 min** | **Teoria Técnica** | Estrutura de dados para IA: O formato JSONL (Prompt vs. Completion). |
| **20 min** | **Intervalo** | Pausa para café. |
| **90 min** | **Laboratório 5** | Atividade "Data Prep": Alunos devem converter uma FAQ de empresa em um dataset de treino. |
| **40 min** | **Validação** | Uso de ferramentas de verificação de sintaxe para garantir que o dataset está pronto. |

---

### 🖥️ Estrutura da Apresentação (Slides da Aula 6)

#### **Slide 1: Fine-tuning vs. Few-shot Prompting**

* **Explicação:** Use a analogia: *Few-shot* é dar um exemplo na hora da prova. *Fine-tuning* é fazer o aluno (IA) estudar um livro inteiro antes da prova. O treinamento personalizado economiza tokens e garante um "tom de voz" constante.

#### **Slide 2: O Ciclo do Treinamento**

* **Explicação:** Mostre as etapas:
1. **Coleta:** Juntar logs, manuais ou códigos.
2. **Limpeza:** Remover informações sensíveis (LGPD) e erros.
3. **Formatação:** Transformar tudo em pares de "Pergunta e Resposta" no padrão JSONL.



#### **Slide 3: O Formato JSONL**

* **Explicação:** Mostre como a máquina "lê" o arquivo. Cada linha é um objeto independente.
* **Exemplo:** `{"prompt": "Como faço deploy no servidor X?", "completion": "O comando padrão é sudo deploy --env production"}`

#### **Slide 4: Parâmetros de Ajuste (Hyperparameters)**

* **Explicação:** Explique de forma simples o que é *Epochs* (quantas vezes a IA lê os dados) e *Learning Rate* (o quão rápido ela tenta aprender). Use a analogia de um estudante: ler rápido demais pode causar confusão; ler devagar demais demora muito.

---

### 💡 Dicas para o Instrutor (Conexão SENAI)

Para seguir a **Metodologia SENAI**, foque na **Qualidade dos Dados**:

1. **O Desafio:** Entregue aos alunos um arquivo de texto "sujo" (com gírias, erros ortográficos e informações irrelevantes).
2. **A Missão:** Eles devem usar o próprio ChatGPT para ajudar a limpar esses dados e formatá-los em um arquivo JSONL perfeito.
3. **Reflexão Ética:** Discuta com a turma: "Se treinarmos a IA com códigos que têm falhas de segurança, o que a nossa IA personalizada vai gerar?". Isso reforça a capacidade socioemocional de responsabilidade técnica.

---

### ✅ Critério de Avaliação

* O aluno conseguiu estruturar corretamente um arquivo JSONL com pelo menos 10 entradas consistentes?
* O aluno identificou e removeu dados sensíveis ou incorretos do dataset original?
