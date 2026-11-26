# ✍️ Exercício Prático: Engenharia de Prompt para Tomada de Decisão Estratégica em People Analytics

## 📌 Contexto do Desafio
O Comitê Executivo da **Hashtag Eletro** solicitou à diretoria de RH uma recomendação de **desligamento estratégico de 3 colaboradores** para otimização do orçamento de pessoal e melhoria do clima organizacional.

O Diretor de RH não deseja apenas uma lista ordenada das menores notas de avaliação. Ele precisa de uma visão executiva fundamentada no **impacto real e na responsabilidade de cada cargo** na organização.

Como especialista em People Analytics, seu objetivo é **desenvolver o prompt ideal** para que uma inteligência artificial analise a base de dados tratada dos 215 funcionários ativos e entregue essa recomendação com embasamento estratégico.

---

## 🧠 Etapa 1: Reflexão Crítica (Antes de Criar o Prompt)
Antes de redigir o prompt, analise as seguintes questões estratégicas de negócio:

1. **Efeito Multiplicador da Liderança:** O impacto de um desempenho insatisfatório de um Estagiário ou Analista é equivalente ao de um Coordenador ou Gerente? De que maneira uma liderança desmotivada afeta a produtividade da equipe?
2. **Retorno sobre o Investimento da Folha (ROI):** Como ponderar a nota de desempenho em relação ao custo salarial do colaborador? Por exemplo, qual o impacto relativo de um salário de R$ 16.600,00 com avaliação 6,0 versus um salário de R$ 6.200,00 com avaliação 6,0?
3. **Diretrizes para a IA:** Quais regras, restrições e formatos de saída devem ser incluídos no prompt para evitar respostas genéricas baseadas apenas na menor nota absoluta?

---

## 🎯 Etapa 2: Construção do Prompt Ideal
Elabore o seu prompt estruturado para ser executado em uma ferramenta de IA (como ChatGPT, Copilot ou Gemini). O seu prompt deve conter obrigatoriamente os seguintes blocos:

* **[Persona / Papel]:** Atribuir um papel especialista à IA (ex.: *Consultor Especialista em People Analytics e Reestruturação Organizacional*).
* **[Contexto e Objetivo]:** Explicar o objetivo principal (recomendar os 3 desligamentos estratégicos prioritários).
* **[Critérios e Regras de Negócio]:**
  * Instruir a IA a considerar a **responsabilidade do cargo** (efeito multiplicador e impacto do líder sobre o time).
  * Instruir a IA a avaliar o **custo-benefício financeiro** (salários elevados combinados com notas baixas ou medianas).
  * Definir a nota de corte para a análise (ex.: avaliações iguais ou inferiores a 6,0).
* **[Formato de Saída Exigido]:** Solicitar uma tabela comparativa dos colaboradores indicados e justificativas individuais em tom executivo.

---

## 🧪 Etapa 3: Validação e Teste do Prompt
1. Insira a base de dados tratada (ou a tabela resumida) juntamente com o prompt criado no modelo de IA de sua escolha.
2. Verifique os 3 nomes recomendados pela IA:
   * A IA identificou **líderes de alto custo e baixo desempenho** ou apenas listou as menores notas absolutas?
   * As justificativas apresentadas têm fundamentação suficiente para serem apresentadas ao CEO?
3. Caso a resposta não atinja o nível esperado, ajuste o prompt adicionando restrições ou exemplos e faça um novo teste.

---

## 💡 Gabarito de Referência: Checklist de Estrutura do Prompt

| Componente do Prompt | Função Estratégica | Exemplo de Aplicação |
| :--- | :--- | :--- |
| **Persona** | Define a profundidade e o tom da análise | *"Atue como Consultor de People Analytics..."* |
| **Contexto** | Situa a IA no cenário da empresa | *"A Hashtag Eletro precisa de 3 desligamentos..."* |
| **Regras de Negócio** | Impõe a lógica de impacto e custo | *"Considere a liderança e o alto salário..."* |
| **Formato de Saída** | Garante um entregável pronto para reunião | *"Gere uma tabela resumida e justificativas..."* |
