Aqui está o conteúdo formatado em Markdown:

```markdown
# Caso de Uso Simplificado: Gestão de um Petshop no Excel

## Cenário
Você é o gestor de um petshop e precisa organizar informações sobre os produtos, serviços, clientes e vendas. O objetivo é criar uma planilha simples e funcional, utilizando fórmulas como **SE()**, **PROCV()**, **SOMASE()** e cálculos entre datas.

---

## Estrutura da Planilha

### 1. Produtos
- **Colunas**: Código, Nome, Preço, Estoque.

### 2. Serviços
- **Colunas**: Código, Nome, Preço.

### 3. Clientes
- **Colunas**: Código, Nome, Data de Cadastro.

### 4. Vendas e Serviços Prestados
- **Colunas**: Data, Código do Cliente, Tipo (Produto ou Serviço), Código do Item, Quantidade, Total.

---

## Atividades

### 1. Fórmula SE()
Na tabela **Vendas e Serviços Prestados**, crie uma fórmula para verificar se o campo `Quantidade` está vazio. Caso esteja vazio, exiba "Quantidade inválida"; caso contrário, exiba "OK".

**Exemplo** (na célula correspondente à validação da quantidade):
```excel
=SE(E2=""; "Quantidade inválida"; "OK")
```

### 2. Fórmula PROCV()
- Na tabela **Vendas e Serviços Prestados**, use **PROCV()** para buscar o preço do produto ou serviço com base no `Código do Item`.

**Exemplo**:
```excel
=PROCV(D2; Produtos!A:D; 3; FALSO)
```

### 3. Fórmula SOMASE()
- Crie uma célula para calcular o total de vendas realizadas em um período. Use a fórmula **SOMASE()** para somar os valores da coluna `Total` que correspondem a um intervalo de datas.

**Exemplo**:
```excel
=SOMASE(A:A; ">="&G1; F:F)
```
*(G1 é a célula onde você insere a data inicial.)*

### 4. Cálculo entre Datas
- Na tabela **Clientes**, adicione uma coluna chamada "Dias como Cliente". Subtraia a `Data de Cadastro` da data atual para calcular o tempo desde o cadastro.

**Exemplo**:
```excel
=HOJE()-C2
```

---

## Desafios Adicionais

1. **Valor Total do Estoque**
   Crie uma coluna na tabela **Produtos** para calcular o valor total do estoque.

   **Fórmula**:
   ```excel
   =B2*C2
   ```

2. **Alerta de Estoque Baixo**
   Gere um alerta usando **formatação condicional** para destacar os produtos com estoque inferior a 5 unidades.

---

## Resultado Esperado
O aluno deverá criar uma planilha simples com funcionalidades úteis, desenvolvendo habilidades básicas no uso das fórmulas.
```

Você pode copiar e colar esse texto diretamente no GitHub para que o formato fique limpo e organizado.
