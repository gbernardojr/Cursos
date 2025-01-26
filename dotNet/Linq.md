O LINQ (**Language-Integrated Query**) é uma funcionalidade poderosa do .NET que permite realizar consultas diretamente em coleções de dados (como arrays, listas, ou até bancos de dados) de maneira elegante, legível e semelhante a SQL.

Ele foi projetado para que você possa manipular e consultar dados de maneira consistente, independentemente da fonte (ex.: objetos em memória, banco de dados, XML, etc.).

---

## **Conceitos Básicos do LINQ**

1. **Consulta baseada em objetos:**
   Você pode usar LINQ para consultar coleções como listas, arrays, ou outros objetos que implementam as interfaces **IEnumerable** ou **IQueryable**.

2. **Sintaxe de LINQ:**
   Existem duas formas principais de usar LINQ:
   - **Sintaxe de consulta** (similar a SQL).
   - **Sintaxe de método** (usando métodos como `.Where()`, `.Select()`, `.OrderBy()`).

3. **Principais operações do LINQ:**
   - **Filtrar:** Usando `Where`.
   - **Selecionar:** Usando `Select`.
   - **Ordenar:** Usando `OrderBy` ou `OrderByDescending`.
   - **Agrupar:** Usando `GroupBy`.
   - **Juntar:** Usando `Join`.

---

### **Exemplo Simples: Filtrar uma Lista**

#### Sem LINQ:
```csharp
List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
List<int> numerosPares = new List<int>();

foreach (var numero in numeros)
{
    if (numero % 2 == 0)
    {
        numerosPares.Add(numero);
    }
}

foreach (var numeroPar in numerosPares)
{
    Console.WriteLine(numeroPar);
}
```

#### Com LINQ (sintaxe de método):
```csharp
List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
var numerosPares = numeros.Where(n => n % 2 == 0);

foreach (var numeroPar in numerosPares)
{
    Console.WriteLine(numeroPar);
}
```

---

## **Estrutura da Sintaxe**

### **Sintaxe de Consulta** (parecida com SQL):
```csharp
var resultado = from item in colecao
                where condicao
                orderby criterio
                select item;
```

### **Sintaxe de Método** (mais usada na prática):
```csharp
var resultado = colecao.Where(item => condicao)
                       .OrderBy(item => criterio)
                       .Select(item => transformacao);
```

---

## **Exemplos Práticos com LINQ**

### **1. Filtrando Dados com `Where`**
#### Cenário:
Você tem uma lista de nomes e deseja filtrar os que começam com a letra "A".

```csharp
List<string> nomes = new List<string> { "Ana", "Bruno", "Carlos", "Alice", "Amanda" };

// LINQ - Método
var nomesComA = nomes.Where(nome => nome.StartsWith("A"));

foreach (var nome in nomesComA)
{
    Console.WriteLine(nome);
}
```

**Saída:**
```
Ana
Alice
Amanda
```

---

### **2. Selecionando e Transformando Dados com `Select`**
#### Cenário:
Você tem uma lista de números e deseja gerar uma lista com seus quadrados.

```csharp
List<int> numeros = new List<int> { 1, 2, 3, 4, 5 };

// LINQ - Método
var quadrados = numeros.Select(n => n * n);

foreach (var quadrado in quadrados)
{
    Console.WriteLine(quadrado);
}
```

**Saída:**
```
1
4
9
16
25
```

---

### **3. Ordenando Dados com `OrderBy` e `OrderByDescending`**
#### Cenário:
Você tem uma lista de nomes e deseja ordená-los em ordem alfabética.

```csharp
List<string> nomes = new List<string> { "Carlos", "Ana", "Bruno", "Alice" };

// LINQ - Ordem crescente
var nomesOrdenados = nomes.OrderBy(nome => nome);

foreach (var nome in nomesOrdenados)
{
    Console.WriteLine(nome);
}
```

**Saída:**
```
Alice
Ana
Bruno
Carlos
```

---

### **4. Agrupando Dados com `GroupBy`**
#### Cenário:
Você tem uma lista de palavras e deseja agrupá-las pela primeira letra.

```csharp
List<string> palavras = new List<string> { "Ana", "Bruno", "Carlos", "Alice", "Amanda" };

// LINQ - Agrupamento
var grupos = palavras.GroupBy(palavra => palavra[0]);

foreach (var grupo in grupos)
{
    Console.WriteLine($"Palavras que começam com '{grupo.Key}':");
    foreach (var palavra in grupo)
    {
        Console.WriteLine($"  {palavra}");
    }
}
```

**Saída:**
```
Palavras que começam com 'A':
  Ana
  Alice
  Amanda
Palavras que começam com 'B':
  Bruno
Palavras que começam com 'C':
  Carlos
```

---

## **Aplicando LINQ no Sistema de Agendamento**

Vamos usar LINQ para listar consultas de forma ordenada e filtrada.

```csharp
public void ListarConsultasPorData(DateTime data)
{
    var consultasNoDia = Consultas
        .Where(c => c.DataHora.Date == data.Date)
        .OrderBy(c => c.DataHora);

    Console.WriteLine($"Consultas em {data.ToShortDateString()}:");
    foreach (var consulta in consultasNoDia)
    {
        Console.WriteLine($"  {consulta.DataHora}: {consulta.Medico.Nome} com {consulta.Paciente.Nome} ({consulta.Status})");
    }
}
```

### Exemplo de Uso:
```csharp
// Listar consultas de uma data específica
agendamento.ListarConsultasPorData(new DateTime(2025, 01, 28));
```

---

## **Vantagens do LINQ**
1. **Legibilidade:** Código mais limpo e fácil de entender.
2. **Produtividade:** Muitas operações comuns (filtro, ordenação, agrupamento) ficam simples de implementar.
3. **Flexibilidade:** Você pode aplicar LINQ a diversas fontes de dados.
