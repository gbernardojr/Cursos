# Cenário do Mundo Real: E-commerce "TechGadget" - Transformação Digital

## **Contexto Empresarial**
A **TechGadget** é uma empresa de e-commerce que vende dispositivos eletrônicos e acessórios. Eles estão migrando sua infraestrutura de dados para o Azure para melhorar a experiência do cliente, otimizar operações e obter insights de negócio.

---

## **1. PROBLEMA INICIAL (ANTES DO AZURE)**

A TechGadget opera com:
- **Sistema legado:** SQL Server no local para transações
- **Dados espalhados:** Planilhas Excel, arquivos CSV, logs de servidor
- **Relatórios manuais:** Equipe gera relatórios manualmente no Excel
- **Site lento:** Recomendações básicas baseadas em regras simples
- **Falta de visibilidade:** Não conseguem prever demanda ou analisar comportamento

---

## **2. ARQUITETURA DE SOLUÇÃO NO AZURE (MODULAR)**

### **MÓDULO 1: Dados Transacionais (Dados Relacionais)**
**Cenário:** Processamento de pedidos em tempo real

- **Azure SQL Database** para:
  - Tabela `Clientes` (chave primária: ClienteID)
  - Tabela `Pedidos` (chave estrangeira para Clientes)
  - Tabela `Produtos` 
  - Processa 1.000 transações/minuto durante picos de venda
  - **SQL básico usado:** `INSERT` para novos pedidos, `SELECT JOIN` para histórico

```sql
-- Exemplo: Pedido em tempo real
INSERT INTO Pedidos (ClienteID, ProdutoID, Quantidade, Data)
VALUES (12345, 67890, 2, GETDATE());
```

### **MÓDULO 2: Dados Não Estruturados (Dados Não Relacionais)**
**Cenário:** Armazenamento de múltiplos formatos de dados

- **Azure Blob Storage** para:
  - Fotos dos produtos enviadas pelos fornecedores
  - Manuais de produto em PDF
  - Vídeos de demonstração
  - Logs do servidor web

- **Azure Cosmos DB (API SQL)** para:
  - Carrinhos de compra abandonados (documentos JSON)
  - Sessões de usuário no site
  - Perfis de cliente enriquecidos

```json
// Documento no Cosmos DB
{
  "sessionId": "sess_789",
  "userId": "12345",
  "pagesVisited": ["/smartphones", "/headphones"],
  "cartItems": [
    {"productId": "P123", "viewedAt": "2024-01-15T10:30:00Z"}
  ],
  "lastActivity": "2024-01-15T10:45:00Z"
}
```

- **Azure Table Storage** para:
  - Metadados das imagens (nome, tamanho, tipo)
  - Configurações do sistema

### **MÓDULO 3: Pipeline de Dados (ETL/ELT)**
**Cenário:** Consolidação diária de dados para análise

- **Azure Data Factory** orquestra o pipeline diário:
  1. **Extract:** Pega dados do Azure SQL (pedidos), Blob Storage (logs), Cosmos DB (sessões)
  2. **Transform:** Limpa e padroniza dados
  3. **Load:** Envia para Azure Synapse Analytics

- **Processamento Batch (noturno):**
  - Consolidar vendas do dia
  - Calcular métricas de negócio
  - Atualizar estoques previstos

- **Processamento em Tempo Real:**
  - **Azure Stream Analytics** processa:
    - Cliques em tempo real no site
    - Adições ao carrinho
  - Aciona **Azure Functions** para:
    - Recomendações personalizadas
    - Alertas de fraude (múltiplas tentativas de pagamento)

### **MÓDULO 4: Analytics e Business Intelligence**
**Cenário:** Tomada de decisão baseada em dados

- **Azure Synapse Analytics** como Data Warehouse:
  - Tabelas dimensionais (`Dim_Clientes`, `Dim_Produtos`, `Dim_Tempo`)
  - Tabela de fatos (`Fato_Vendas`)
  - Consultas analíticas complexas

```sql
-- Análise: Produtos mais vendidos por região
SELECT r.Regiao, p.NomeProduto, SUM(f.Quantidade) as TotalVendido
FROM Fato_Vendas f
JOIN Dim_Clientes c ON f.ClienteID = c.ClienteID
JOIN Dim_Produtos p ON f.ProdutoID = p.ProdutoID
JOIN Dim_Regiao r ON c.RegiaoID = r.RegiaoID
GROUP BY r.Regiao, p.NomeProduto
ORDER BY TotalVendido DESC;
```

- **Power BI** para visualização:
  - Dashboard executivo: Receita, crescimento, métricas-chave
  - Relatório de vendas por categoria, região, período
  - Análise de comportamento do cliente
  - Previsão de demanda usando machine learning

### **MÓDULO 5: Data Lake Moderno**
**Cenário:** Armazenamento de todos os dados brutos

- **Azure Data Lake Storage Gen2** como repositório central:
  - Camada 1 (Bronze): Dados brutos (CSV, JSON, logs)
  - Camada 2 (Silver): Dados limpos e validados
  - Camada 3 (Gold): Dados enriquecidos prontos para análise
  
- **Azure Databricks** para:
  - Processamento avançado com Spark
  - Modelos de machine learning (recomendação)
  - Análise de sentimentos em avaliações de produtos

---

## **3. FLUXO COMPLETO DE DADOS**

```
CLIENTE NO SITE
      ↓
Azure Cosmos DB (sessão em tempo real)
      ↓
FAZ PEDIDO → Azure SQL Database (transação ACID)
      ↓
Azure Functions (processa pagamento)
      ↓
Azure Stream Analytics (análise em tempo real)
      ↓
A CADA 24 HORAS:
Azure Data Factory (orquestra ETL)
      ↓
Azure Synapse Analytics (consolida para BI)
      ↓
Power BI (dashboard executivo)
      ↓
EQUIPE DE NEGÓCIO (toma decisões)
```

---

## **4. BENEFÍCIOS OBTIDOS**

| **Tecnologia Azure** | **Benefício para TechGadget** |
|----------------------|--------------------------------|
| **Azure SQL Database** | Pedidos processados 5x mais rápido, alta disponibilidade |
| **Cosmos DB** | Recomendações personalizadas aumentaram conversão em 15% |
| **Data Factory** | Relatórios prontos às 8 AM (antes era meio-dia) |
| **Synapse Analytics** | Análise de 12 meses de dados em segundos |
| **Power BI** | Decisões baseadas em dados em tempo real |
| **Blob Storage** | Redução de 60% em custos de armazenamento de mídia |

---


Este cenário integra **todos os conceitos do DP-900** em uma narrativa coesa, mostrando como diferentes serviços Azure trabalham juntos para resolver problemas de negócio reais. Os alunos podem se identificar com a TechGadget e entender o **"porquê"** por trás de cada escolha tecnológica.
