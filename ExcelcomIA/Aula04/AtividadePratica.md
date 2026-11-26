# 📝 **Atividade Prática: Desafio de Criação de Planilhas com IA (Método PCTS)**

### 📌 **Objetivo da Atividade**
Testar e consolidar a sua habilidade de estruturar comandos eficientes (**prompts**) para a IA Generativa (Copilot, Grok ou ChatGPT) criar estruturas de planilhas organizadas, funcionais e prontas para uso corporativo.

### 💡 **Revisão Rápida da Técnica PCTS**
Para cada uma das 5 situações abaixo, você deverá construir um prompt contendo obrigatoriamente os 4 pilares:
* **P (Pessoa):** O papel/especialidade que a IA deve assumir *(Ex: "Você é um analista de RH...", "Atue como gestor de logística...")*.
* **C (Contexto):** A explicação detalhada do cenário da empresa e do problema que precisa ser resolvido.
* **T (Tarefa):** O que exatamente a IA deve criar (quais colunas, quais dados de teste, quais regras).
* **S (Saída):** Como e em qual formato você deseja que a IA entregue a resposta *(Ex: "Crie como Tabela Oficial no Excel", "Apresente uma tabela em markdown")*.

---

## 🏢 **As 5 Situações Práticas**

---

### **Situação 1: Fluxo de Caixa Diário para a "Boutique Estilo" (Varejo)**
* **Contexto para o Aluno**: A loja de roupas femininas "Boutique Estilo" vende à vista (Dinheiro, PIX e Cartão de Débito) e a prazo (Cartão de Crédito). A proprietária está perdendo o controle do dinheiro porque mistura o faturamento diário com o pagamento de fornecedores, conta de luz e comissão das vendedoras. Ela precisa de uma planilha simples de fluxo de caixa onde possa lançar cada movimentação do dia, identificar a categoria do gasto/receita e visualizar o saldo final acumulado.
* **Desafio do Aluno**: Crie o prompt no modelo **PCTS** solicitando à IA a criação de uma estrutura de planilha de Fluxo de Caixa Diário com colunas organizadas, 5 linhas de lançamentos fictícios e indicação de saldo positivo/negativo.

---

### **Situação 2: Manutenção Preventiva de Máquinas na "MetalLupo" (Chão de Fábrica)**
* **Contexto para o Aluno**: O setor de manutenção de uma fábrica de autopeças possui 15 máquinas industriais (Tornos CNC, Prensas Hidráulicas e Soldeiras). Quando uma máquina quebra de surpresa, a linha de produção para e a empresa perde dinheiro. O chefe de manutenção quer uma planilha para monitorar os equipamentos, registrando o código da máquina, nome do equipamento, setor da fábrica, data da última manutenção, horas rodadas e a data prevista para a próxima revisão.
* **Desafio do Aluno**: Crie o prompt no modelo **PCTS** pedindo para a IA gerar uma planilha de Controle de Manutenção Preventiva, incluindo uma coluna de "Status do Alerta" (como *Normal*, *Próximo do Vencimento* ou *Urgente*) e 5 exemplos de máquinas cadastradas.

---

### **Situação 3: Controle de Horas Extras na "Expresso Rápido" (RH & Transportes)**
* **Contexto para o Aluno**: Uma empresa de logística e transportes precisa controlar a jornada de trabalho de seus 10 motoristas. O departamento de RH precisa registrar diariamente a matrícula do funcionário, nome, cargo, quantidade de horas normais trabalhadas no dia, quantidade de horas extras executadas e o valor da hora extra. O RH precisa que a planilha já traga o cálculo do valor total de horas extras a pagar a cada motorista no mês.
* **Desafio do Aluno**: Crie o prompt no modelo **PCTS** solicitando à IA a estrutura dessa planilha de Apontamento de Horas Extras, com os cabeçalhos corretos, indicação de fórmulas para multiplicar horas extras pelo valor da hora, e 5 registros simulados de motoristas.

---

### **Situação 4: Cotação e Comparativo de Fornecedores na "Lupo Construções" (Suprimentos)**
* **Contexto para o Aluno**: O setor de compras de uma construtora vai comprar grandes quantidades de cimento e aço para uma nova obra. Eles receberam propostas de 3 fornecedores diferentes, mas estão em dúvida sobre qual escolher porque um tem o menor preço, mas cobra o frete mais caro e demora mais para entregar. A equipe de compras precisa de uma planilha comparativa de cotação onde possa inserir os dados dos fornecedores, o preço unitário do insumo, o custo do frete, o prazo de entrega (em dias) e a nota de avaliação da qualidade do fornecedor.
* **Desafio do Aluno**: Crie o prompt no modelo **PCTS** pedindo para a IA criar uma Matriz Comparativa de Cotação de Fornecedores que facilite a decisão do comprador, incluindo dados de teste de 3 fornecedores concorrentes.

---

### **Situação 5: Vistoria e Controle de Frota na "Locadora Frota Segura" (Logística de Veículos)**
* **Contexto para o Aluno**: Uma locadora de veículos comerciais faz a vistoria dos carros na entrega e na devolução do cliente. A empresa precisa registrar a placa do veículo, modelo, nome do cliente que alugou, quilometragem inicial (na saída), quilometragem final (na devolução), nível do tanque de combustível e se o veículo retornou com alguma avaria/risco na lataria. 
* **Desafio do Aluno**: Crie o prompt no modelo **PCTS** solicitando à IA uma planilha de Vistoria e Controle de Devolução de Frotas, calculando a quilometragem total percorrida e trazendo colunas de verificação para cobranças adicionais (combustível ou avarias).

---

## 📋 **Modelo de Entrega do Aluno**

O aluno deverá responder a cada situação seguindo esta estrutura padronizada:

```text
==================================================
RESPOSTA DA SITUAÇÃO [Número]
==================================================
P (Pessoa): [Descreva a pessoa/papel da IA]
C (Contexto): [Explique o cenário e problema]
T (Tarefa): [Descreva a tarefa detalhada]
S (Saída): [Especifique o formato da resposta esperada]

PROMPT COMPLETO UNIFICADO:
"[Escreva o texto final do prompt exatamente como seria enviado para a IA]"
==================================================
```

---

## 👨‍🏫 **Gabarito / Exemplo de Resposta Esperada (Para Orientação do Professor)**

Abaixo está um exemplo de como deve ser a resposta ideal para a **Situação 2 (Manutenção Preventiva)**:

> * **Pessoa**: Atue como um engenheiro de manutenção industrial e especialista em organização de dados operacionais no Excel.
> * **Contexto**: Trabalho no setor de manutenção da fábrica "MetalLupo". Precisamos controlar a manutenção de 15 máquinas industriais para evitar paradas não planejadas na linha de produção.
> * **Tarefa**: Crie uma estrutura de planilha para Controle de Manutenção Preventiva contendo as colunas: `Código_Máquina`, `Equipamento`, `Setor`, `Data_Última_Revisão`, `Horas_Trabalhadas`, `Próxima_Revisão` e `Status_Alerta`. Preencha com 5 exemplos de máquinas industriais fictícias (ex: Tornos, Prensas, Soldeiras) com dados coerentes.
> * **Saída**: Gere a tabela diretamente como Tabela Oficial do Excel (ou no formato de tabela simples para copiar e colar), aplicando uma lógica visual para que o status exiba termos como "Normal", "Revisão Próxima" ou "Atrasado".
>
> **PROMPT UNIFICADO FINAL**:
> *"Você é um engenheiro de manutenção industrial e especialista em Microsoft Excel. Estou organizando o setor de manutenção da fábrica MetalLupo para monitorar 15 máquinas industriais e evitar paradas indesejadas na produção. Crie uma planilha de Controle de Manutenção Preventiva contendo as colunas: Código_Máquina, Equipamento, Setor, Data_Última_Revisão, Horas_Trabalhadas, Próxima_Revisão e Status_Alerta. Preencha a planilha com 5 linhas de dados fictícios e seguros de máquinas (como Tornos CNC e Prensas) e forneça o resultado formatado como Tabela Oficial para uso no Excel."*

---
