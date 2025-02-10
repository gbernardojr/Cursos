## 🎯 **Exercício: Decisão Estratégica com Power BI**
**Cenário:**  
Você é um analista de negócios de uma rede de lojas de eletrônicos que está estudando o desempenho das filiais em diferentes cidades. A empresa quer definir uma estratégia para o próximo trimestre e precisa decidir **se deve investir em marketing para aumentar as vendas, cortar custos ou fechar uma filial com baixo desempenho**.  

---

### 📊 **Dados fornecidos**  
Os alunos devem trabalhar com um conjunto de dados que inclua:  

1. **Vendas**  
   - Data da venda  
   - Filial (Cidade)  
   - Produto  
   - Quantidade vendida  
   - Receita gerada  

2. **Custos Operacionais**  
   - Filial  
   - Custo fixo mensal  
   - Custo variável  

3. **Satisfação do Cliente**  
   - Filial  
   - Nota média de avaliação dos clientes  

---

### 🏆 **Desafio proposto**  
Com base nesses dados, os alunos devem criar um **dashboard analítico** que ajude a responder:  

1. **Qual filial tem o melhor e o pior desempenho em vendas?**  
2. **Qual o impacto dos custos sobre a rentabilidade de cada filial?**  
3. **Há uma relação entre satisfação do cliente e o volume de vendas?**  
4. **Qual filial deveria receber investimento em marketing e qual poderia ser fechada?**  

---

### 🔧 **Passos para resolver o exercício**  

1️⃣ **Importar e tratar os dados**  
- Carregar os arquivos no Power BI.  
- Criar relacionamentos entre tabelas.  
- Verificar se os dados precisam de limpeza.  

2️⃣ **Criar as medidas no DAX**  
- **Receita Total:** `SUM(Vendas[Receita gerada])`  
- **Lucro:** `SUM(Vendas[Receita gerada]) - SUM(Custos[Total de Custos])`  
- **Média de Satisfação:** `AVERAGE(Satisfação[Nota])`  
- **Margem de Lucro (%):** `(Lucro / Receita Total) * 100`  

3️⃣ **Construir visualizações**  
- **Gráfico de colunas** comparando Receita, Lucro e Custos por filial.  
- **Mapa geográfico** mostrando a distribuição das filiais e suas receitas.  
- **Gráfico de dispersão** comparando Satisfação do Cliente x Receita.  
- **Tabela dinâmica** para acompanhar os principais indicadores.  

4️⃣ **Tomada de decisão**  
Os alunos devem apresentar suas conclusões e decidir:  
- Qual filial **deve receber mais investimento**?  
- Qual filial **deve reduzir custos**?  
- Qual filial **não é rentável e pode ser fechada**?  

---

### 🎤 **Apresentação final**  
No final da atividade, cada grupo deve apresentar sua análise e defender sua decisão, explicando quais indicadores usaram para embasar a escolha.  

