
### **1. Fundamentos da Orientação a Objetos**
A OO é um modelo baseado em **objetos** do mundo real. A ideia é dividir o sistema em partes menores, representadas por **classes**, que possuem:  
- **Propriedades**: características do objeto (atributos).  
- **Métodos**: comportamentos do objeto (ações que ele realiza).  

---

### **2. Conceitos Básicos da OO**  

1. **Classe**  
   - É o molde ou blueprint para criar objetos.  
   - Exemplo: "Carro" é a classe, enquanto "meuCarro" (um Fusca, por exemplo) é o objeto criado dessa classe.  
   
   ```csharp
   public class Carro
   {
       public string Modelo { get; set; }
       public int Ano { get; set; }

       public void Acelerar()
       {
           Console.WriteLine($"{Modelo} está acelerando.");
       }
   }
   ```

2. **Objeto**  
   - É a instância da classe. Um objeto é "concreto".  
   ```csharp
   Carro meuCarro = new Carro();
   meuCarro.Modelo = "Fusca";
   meuCarro.Ano = 1980;
   meuCarro.Acelerar();
   ```

3. **Encapsulamento**  
   - Esconde detalhes de implementação e expõe apenas o necessário.  
   - Você pode controlar o acesso às propriedades com modificadores (`private`, `public`).  

   ```csharp
   public class ContaBancaria
   {
       private decimal saldo;

       public void Depositar(decimal valor)
       {
           saldo += valor;
       }

       public decimal ConsultarSaldo()
       {
           return saldo;
       }
   }
   ```

4. **Herança**  
   - Uma classe pode "herdar" de outra, compartilhando código.  
   ```csharp
   public class Veiculo
   {
       public int Rodas { get; set; }
       public void Mover() => Console.WriteLine("O veículo está se movendo.");
   }

   public class Moto : Veiculo
   {
       public bool TemGuidão { get; set; }
   }
   ```

5. **Polimorfismo**  
   - Permite que um método tenha comportamentos diferentes dependendo do contexto.  
   - Exemplo: a mesma função pode se comportar de formas distintas em classes derivadas.  
   ```csharp
   public class Animal
   {
       public virtual void FazerSom() => Console.WriteLine("Som genérico");
   }

   public class Cachorro : Animal
   {
       public override void FazerSom() => Console.WriteLine("Latido");
   }
   ```

6. **Interface**  
   - É um contrato. Uma classe que implementa uma interface deve fornecer a lógica para todos os métodos definidos nela.  
   ```csharp
   public interface IImprimivel
   {
       void Imprimir();
   }

   public class Relatorio : IImprimivel
   {
       public void Imprimir()
       {
           Console.WriteLine("Relatório impresso.");
       }
   }
   ```

---

### **3. Como Estruturar Classes em um Projeto**
Aqui está o segredo: pense em **responsabilidades únicas** para cada classe.  

- **Classe = Responsabilidade**  
  - Pergunte: *qual é o papel dessa classe no sistema?*  
  - Exemplo:  
    - Classe `Cliente` → Gerenciar dados do cliente.  
    - Classe `Pedido` → Representar um pedido.  
    - Classe `Relatorio` → Gerar relatórios.  

- **Propriedades e Métodos**  
  - Propriedades descrevem o objeto.  
  - Métodos representam ações do objeto.  

---

### **4. Quando Usar Interfaces**
Use interfaces quando:  
1. Você quer definir **um contrato comum** para várias classes diferentes.  
   - Exemplo: Classes `PDFReport` e `HTMLReport` podem implementar a interface `IReport`.  
2. Você quer facilitar a manutenção e o teste.  

---

### **Exercício Prático Inicial**  
Vamos criar um sistema simples de cadastro de veículos. Aqui estão as classes:  
1. `Veiculo` (base): Propriedades `Marca`, `Modelo` e método `ExibirDetalhes`.  
2. `Carro` (herda `Veiculo`): Propriedade adicional `QuantidadePortas`.  
3. `Moto` (herda `Veiculo`): Propriedade adicional `Cilindradas`.  

```csharp
public class Veiculo
{
    public string Marca { get; set; }
    public string Modelo { get; set; }

    public virtual void ExibirDetalhes()
    {
        Console.WriteLine($"Marca: {Marca}, Modelo: {Modelo}");
    }
}

public class Carro : Veiculo
{
    public int QuantidadePortas { get; set; }

    public override void ExibirDetalhes()
    {
        base.ExibirDetalhes();
        Console.WriteLine($"Portas: {QuantidadePortas}");
    }
}

public class Moto : Veiculo
{
    public int Cilindradas { get; set; }

    public override void ExibirDetalhes()
    {
        base.ExibirDetalhes();
        Console.WriteLine($"Cilindradas: {Cilindradas}");
    }
}
```

Teste com:  

```csharp
Carro carro = new Carro
{
    Marca = "Fiat",
    Modelo = "Uno",
    QuantidadePortas = 4
};
carro.ExibirDetalhes();

Moto moto = new Moto
{
    Marca = "Yamaha",
    Modelo = "XT660",
    Cilindradas = 660
};
moto.ExibirDetalhes();
```

---

### **O que é o `virtual`?**
O modificador **`virtual`** em C# permite que um método definido em uma classe **base** (como `Veiculo`) possa ser **substituído** ou **sobrescrito** em classes derivadas (como `Carro` e `Moto`).  

Ele é a chave para habilitar o **polimorfismo**, ou seja, o comportamento dinâmico de métodos em tempo de execução.

---

### **Como funciona?**
- Quando um método é marcado como **`virtual`**, ele pode ser sobrescrito em uma classe derivada usando o modificador **`override`**.  
- Caso a classe derivada **não sobrescreva** o método, a implementação da classe base será utilizada.

---

### **Exemplo Prático**
No exemplo que escrevemos:  

```csharp
public class Veiculo
{
    public virtual void ExibirDetalhes()
    {
        Console.WriteLine($"Marca: {Marca}, Modelo: {Modelo}");
    }
}
```

A classe `Veiculo` define um método **`ExibirDetalhes`** com o modificador **`virtual`**. Isso significa que qualquer classe que herdar de `Veiculo` pode **sobrescrever** o comportamento desse método.  

---

### **Sobrescrita com `override`**
Quando criamos a classe `Carro`, usamos o **`override`** para alterar o comportamento do método `ExibirDetalhes`:

```csharp
public class Carro : Veiculo
{
    public int QuantidadePortas { get; set; }

    public override void ExibirDetalhes()
    {
        base.ExibirDetalhes(); // Chama o método da classe base.
        Console.WriteLine($"Portas: {QuantidadePortas}");
    }
}
```

Aqui:
- **`base.ExibirDetalhes()`** chama a implementação original da classe base (`Veiculo`).  
- Depois, adicionamos um comportamento extra específico da classe `Carro` (mostrar as portas).  

---

### **O que acontece sem o `virtual`?**
Se o método `ExibirDetalhes` não fosse marcado como **`virtual`** na classe `Veiculo`, você **não poderia sobrescrevê-lo** com `override` na classe `Carro` ou `Moto`. O compilador geraria um erro.

---

### **Polimorfismo em Ação**
Quando usamos uma variável do tipo `Veiculo` para armazenar um objeto de `Carro` ou `Moto`, o método sobrescrito será chamado **automaticamente** graças ao `virtual`:

```csharp
Veiculo veiculo1 = new Carro { Marca = "Fiat", Modelo = "Uno", QuantidadePortas = 4 };
veiculo1.ExibirDetalhes(); 
// Resultado:
// Marca: Fiat, Modelo: Uno
// Portas: 4

Veiculo veiculo2 = new Moto { Marca = "Yamaha", Modelo = "XT660", Cilindradas = 660 };
veiculo2.ExibirDetalhes();
// Resultado:
// Marca: Yamaha, Modelo: XT660
// Cilindradas: 660
```

Aqui está o poder do **polimorfismo**:
- O método chamado depende do **tipo do objeto real** (no caso, `Carro` ou `Moto`), e não do tipo da variável (`Veiculo`).

---

### **Resumo**
- **`virtual`**: Permite que um método da classe base seja sobrescrito em classes derivadas.  
- **`override`**: Usado para sobrescrever o método em uma classe derivada.  
- **Polimorfismo**: Com `virtual` e `override`, o método correto será chamado com base no tipo do objeto em tempo de execução, mesmo que a variável tenha o tipo da classe base.  

---

### **Projeto 1: Gerenciamento de Biblioteca**
**Objetivo:** Criar um sistema simples para gerenciar livros e leitores.

#### Requisitos:
1. O sistema deve armazenar informações sobre **livros** e **leitores**.
2. Cada leitor pode **emprestar** um livro.
3. Um livro pode estar **disponível** ou **emprestado**.
4. Deve haver uma funcionalidade para listar os livros disponíveis e os emprestados.

---

#### Organização das Classes:
1. **Classe Livro:**
   - Propriedades: `Titulo`, `Autor`, `Status` (Disponível/Emprestado).
   - Métodos: `Emprestar()`, `Devolver()`.

2. **Classe Leitor:**
   - Propriedades: `Nome`, `LivrosEmprestados` (lista de livros).
   - Métodos: `EmprestarLivro(Livro livro)`, `DevolverLivro(Livro livro)`.

3. **Classe Biblioteca:**
   - Propriedades: `ListaDeLivros`, `ListaDeLeitores`.
   - Métodos: `AdicionarLivro()`, `ListarLivrosDisponiveis()`, `ListarLivrosEmprestados()`.

---

#### Código:
Aqui está a implementação:

```csharp
using System;
using System.Collections.Generic;

public class Livro
{
    public string Titulo { get; set; }
    public string Autor { get; set; }
    public bool Emprestado { get; private set; }

    public Livro(string titulo, string autor)
    {
        Titulo = titulo;
        Autor = autor;
        Emprestado = false;
    }

    public void Emprestar()
    {
        if (Emprestado)
            Console.WriteLine($"O livro '{Titulo}' já está emprestado.");
        else
        {
            Emprestado = true;
            Console.WriteLine($"O livro '{Titulo}' foi emprestado com sucesso.");
        }
    }

    public void Devolver()
    {
        if (!Emprestado)
            Console.WriteLine($"O livro '{Titulo}' já está disponível.");
        else
        {
            Emprestado = false;
            Console.WriteLine($"O livro '{Titulo}' foi devolvido com sucesso.");
        }
    }
}

public class Leitor
{
    public string Nome { get; set; }
    public List<Livro> LivrosEmprestados { get; private set; }

    public Leitor(string nome)
    {
        Nome = nome;
        LivrosEmprestados = new List<Livro>();
    }

    public void EmprestarLivro(Livro livro)
    {
        if (!livro.Emprestado)
        {
            LivrosEmprestados.Add(livro);
            livro.Emprestar();
        }
        else
        {
            Console.WriteLine($"O livro '{livro.Titulo}' não está disponível.");
        }
    }

    public void DevolverLivro(Livro livro)
    {
        if (LivrosEmprestados.Contains(livro))
        {
            LivrosEmprestados.Remove(livro);
            livro.Devolver();
        }
        else
        {
            Console.WriteLine($"O leitor {Nome} não possui o livro '{livro.Titulo}'.");
        }
    }
}

public class Biblioteca
{
    public List<Livro> ListaDeLivros { get; private set; }
    public List<Leitor> ListaDeLeitores { get; private set; }

    public Biblioteca()
    {
        ListaDeLivros = new List<Livro>();
        ListaDeLeitores = new List<Leitor>();
    }

    public void AdicionarLivro(Livro livro)
    {
        ListaDeLivros.Add(livro);
    }

    public void ListarLivrosDisponiveis()
    {
        Console.WriteLine("\nLivros Disponíveis:");
        foreach (var livro in ListaDeLivros)
        {
            if (!livro.Emprestado)
                Console.WriteLine($"- {livro.Titulo} ({livro.Autor})");
        }
    }

    public void ListarLivrosEmprestados()
    {
        Console.WriteLine("\nLivros Emprestados:");
        foreach (var livro in ListaDeLivros)
        {
            if (livro.Emprestado)
                Console.WriteLine($"- {livro.Titulo} ({livro.Autor})");
        }
    }
}
```

---

#### Testando o Sistema:
No método `Main`, podemos interagir com o sistema:

```csharp
public class Program
{
    public static void Main(string[] args)
    {
        Biblioteca biblioteca = new Biblioteca();

        // Criar livros
        Livro livro1 = new Livro("O Senhor dos Anéis", "J.R.R. Tolkien");
        Livro livro2 = new Livro("1984", "George Orwell");
        Livro livro3 = new Livro("Dom Casmurro", "Machado de Assis");

        biblioteca.AdicionarLivro(livro1);
        biblioteca.AdicionarLivro(livro2);
        biblioteca.AdicionarLivro(livro3);

        // Criar leitores
        Leitor leitor1 = new Leitor("Gilberto");
        Leitor leitor2 = new Leitor("Ana");

        // Emprestar livros
        leitor1.EmprestarLivro(livro1);
        leitor2.EmprestarLivro(livro2);

        // Listar livros disponíveis e emprestados
        biblioteca.ListarLivrosDisponiveis();
        biblioteca.ListarLivrosEmprestados();

        // Devolver livro
        leitor1.DevolverLivro(livro1);

        // Listar novamente
        biblioteca.ListarLivrosDisponiveis();
        biblioteca.ListarLivrosEmprestados();
    }
}
```

---

### **O que praticamos aqui:**
1. **Divisão de responsabilidades**:
   - `Livro`: Gerencia o estado e comportamento de um livro individual.
   - `Leitor`: Gerencia as ações de um leitor sobre os livros.
   - `Biblioteca`: Centraliza a administração dos livros e leitores.

2. **Encapsulamento**: 
   - Os métodos controlam o acesso e alteração das propriedades, como `Emprestar` e `Devolver`.

3. **Listas e interação entre objetos**:
   - Usamos listas (`List<Livro>`) para gerenciar coleções.

4. **Polimorfismo em menor escala**:
   - Não usamos herança aqui, mas o conceito pode ser expandido futuramente.

---

### **Quer evoluir o projeto?**
- Podemos adicionar persistência com um banco de dados.
- Criar interfaces gráficas ou APIs.
- Explorar herança e interfaces, como criar uma interface `IMedia` para gerenciar Livros, DVDs, etc.

---

### **Separação de Responsabilidades**
1. **Método `Emprestar` na classe Livro:**
   - **Responsabilidade do Livro:** Um livro sabe se ele está disponível ou emprestado. Isso significa que a classe **Livro** é responsável por **gerenciar seu próprio estado** (disponível ou emprestado). 
   - O método `Emprestar` encapsula a lógica para verificar e alterar o estado do livro. Ele garante que um livro não seja emprestado se já estiver emprestado.

2. **Método `EmprestarLivro` na classe Leitor:**
   - **Responsabilidade do Leitor:** Um leitor sabe quais livros ele pegou emprestado. A classe **Leitor** é responsável por gerenciar a lista de livros que ele possui no momento.
   - O método `EmprestarLivro` encapsula a lógica de como um leitor interage com um livro. Ele chama o método `Emprestar` do livro para realizar a operação, mas também atualiza a lista de livros emprestados pelo leitor.

---

### **Por que separar essas responsabilidades?**
- **Coerência:** Cada classe é responsável apenas pelas operações relacionadas ao seu domínio. 
  - A classe **Livro** cuida do estado do livro.
  - A classe **Leitor** cuida do que um leitor está emprestando.
- **Reusabilidade:** O método `Emprestar` da classe **Livro** pode ser usado em outros contextos, sem depender da classe **Leitor**. Por exemplo, se no futuro você criar uma funcionalidade que empresta livros diretamente da biblioteca (sem passar pelo leitor), o método já está pronto.
- **Encapsulamento:** Cada classe controla suas próprias mudanças de estado. Isso impede que outras classes alterem diretamente as propriedades (`Emprestado`) sem passar pela lógica adequada.

---

### **Exemplo da Interação**
Quando um leitor empresta um livro, veja como as classes trabalham juntas:

1. O método `EmprestarLivro` da classe **Leitor** é chamado.
   - Ele verifica se o livro está disponível.
   - Chama o método `Emprestar` da classe **Livro**.
   - Adiciona o livro à lista de livros emprestados pelo leitor.

2. O método `Emprestar` da classe **Livro** é chamado.
   - Ele altera o estado interno do livro (`Emprestado = true`).
   - Garante que a lógica para impedir múltiplos empréstimos está aplicada.

Isso divide claramente as responsabilidades entre o leitor e o livro.

---

### **E se tivéssemos apenas um dos métodos?**
1. **Somente `Emprestar` na classe Livro:**
   - A classe **Livro** teria que gerenciar a relação com os leitores, o que não faz sentido, pois um livro não deveria saber quem o está emprestando.

2. **Somente `EmprestarLivro` na classe Leitor:**
   - A classe **Leitor** teria que alterar diretamente o estado do livro, quebrando o encapsulamento e potencialmente introduzindo inconsistências (como esquecer de marcar um livro como emprestado).

---

### **Resumo:**
A existência de ambos os métodos permite:
- Que **cada classe cuide apenas da sua responsabilidade.**
- Uma interação clara entre as classes, sem acoplamento excessivo.
- **Facilidade de manutenção e evolução**, caso novas funcionalidades sejam adicionadas no futuro.

Quando estamos projetando classes, pensar em **responsabilidades** é essencial para criar um código bem estruturado, reutilizável e fácil de manter. Vamos abordar como definir responsabilidades de maneira clara e eficiente.

---

## **Princípios para Definir Responsabilidades**
1. ### **SRP (Princípio da Responsabilidade Única)**
   - Cada classe deve ter **uma única razão para mudar**.
   - Isso significa que uma classe deve fazer apenas **uma coisa** e fazer isso bem.
   - Exemplo:
     - Uma classe **Livro** deve cuidar apenas dos dados e estado relacionados a um livro.
     - Uma classe **Leitor** deve cuidar apenas das informações e ações de um leitor.
     - Não devemos misturar responsabilidades (ex.: não colocar métodos para gerenciar leitores dentro da classe **Livro**).

---

2. ### **Pense no Mundo Real**
   - Ao projetar classes, imagine o sistema como um modelo do mundo real.
   - Pergunte-se:
     - Que **papel** essa entidade desempenha no sistema?
     - Quais **dados** e **ações** ela deveria gerenciar?
   - Exemplo:
     - Um **Livro** no mundo real tem título, autor, e estado (emprestado ou disponível).
     - Um **Leitor** tem nome, documentos e uma lista de livros que pegou emprestados.

---

3. ### **Alta Coesão, Baixo Acoplamento**
   - **Alta Coesão:** As responsabilidades dentro de uma classe devem estar intimamente relacionadas.
     - Exemplo ruim: Uma classe **Biblioteca** que gerencia empréstimos, livros, e cadastro de leitores (isso deveria estar em classes separadas).
   - **Baixo Acoplamento:** Uma classe deve depender de outras o mínimo possível.
     - Exemplo: A classe **Livro** não deve saber nada sobre como a classe **Leitor** funciona.

---

4. ### **Delegue Tarefas**
   - Não sobrecarregue uma única classe. Quando algo não parece ser responsabilidade de uma classe, delegue para outra.
   - Exemplo:
     - O sistema precisa gerenciar o histórico de empréstimos.
       - Não coloque essa responsabilidade na classe **Livro** ou na classe **Leitor**.
       - Crie uma classe separada, como **HistoricoEmprestimos**.

---

5. ### **Use Interfaces e Abstrações**
   - Quando uma classe pode interagir com diferentes tipos de objetos, use **interfaces** ou **classes abstratas**.
   - Exemplo:
     - Uma biblioteca pode emprestar livros, mas também pode emprestar DVDs ou revistas. Em vez de criar métodos específicos para cada tipo, use uma interface como **IEmprestavel**.

---

## **Passo a Passo para Criar Classes**
1. **Liste os Objetos do Sistema**
   - Identifique os principais "atores" ou entidades do sistema.
   - Exemplo em um sistema de biblioteca: **Livro**, **Leitor**, **Empréstimo**, **Biblioteca**, etc.

2. **Defina as Responsabilidades de Cada Objeto**
   - Pergunte-se: O que este objeto faz? Que dados ele precisa armazenar?
   - Exemplo:
     - **Livro:** Gerencia estado e dados do livro (título, autor, disponibilidade).
     - **Leitor:** Gerencia informações do leitor e os livros que ele pegou emprestado.
     - **Empréstimo:** Registra detalhes de cada transação de empréstimo.

3. **Defina Dados e Métodos**
   - Para cada classe, identifique:
     - **Dados:** Quais informações precisam ser armazenadas?
     - **Métodos:** Quais ações a classe deve realizar?
   - Exemplo:
     - Classe **Livro**:
       - Dados: Título, Autor, Disponibilidade.
       - Métodos: `Emprestar`, `Devolver`.
     - Classe **Leitor**:
       - Dados: Nome, CPF, Livros emprestados.
       - Métodos: `EmprestarLivro`, `DevolverLivro`.

4. **Identifique Relações Entre as Classes**
   - Pense em como as classes se relacionam:
     - **Associação:** Um leitor pode emprestar vários livros.
     - **Composição:** Um empréstimo sempre envolve um livro e um leitor.
     - **Herança:** Se houver variações de classes com comportamentos semelhantes.

---

## **Exemplo Prático: Sistema de Locadora**
Vamos aplicar isso para criar um pequeno sistema de locadora.

### Classes e Responsabilidades
1. **Filme**
   - **Responsabilidade:** Representa um filme da locadora.
   - **Dados:** Título, Gênero, Disponibilidade.
   - **Métodos:** `Emprestar`, `Devolver`.

2. **Cliente**
   - **Responsabilidade:** Representa um cliente da locadora.
   - **Dados:** Nome, CPF, Filmes alugados.
   - **Métodos:** `AlugarFilme`, `DevolverFilme`.

3. **Locadora**
   - **Responsabilidade:** Gerencia o catálogo de filmes e as transações de aluguel.
   - **Dados:** Lista de filmes, Lista de clientes.
   - **Métodos:** `RegistrarCliente`, `BuscarFilme`, `RegistrarEmprestimo`.

---

### Código Simplificado
```csharp
public class Filme
{
    public string Titulo { get; set; }
    public string Genero { get; set; }
    public bool Disponivel { get; private set; } = true;

    public void Emprestar()
    {
        if (!Disponivel)
            throw new InvalidOperationException("O filme já está emprestado.");
        Disponivel = false;
    }

    public void Devolver()
    {
        Disponivel = true;
    }
}

public class Cliente
{
    public string Nome { get; set; }
    public string CPF { get; set; }
    public List<Filme> FilmesAlugados { get; private set; } = new List<Filme>();

    public void AlugarFilme(Filme filme)
    {
        filme.Emprestar();
        FilmesAlugados.Add(filme);
    }

    public void DevolverFilme(Filme filme)
    {
        if (!FilmesAlugados.Contains(filme))
            throw new InvalidOperationException("O filme não foi alugado por este cliente.");
        filme.Devolver();
        FilmesAlugados.Remove(filme);
    }
}

public class Locadora
{
    public List<Filme> Filmes { get; private set; } = new List<Filme>();
    public List<Cliente> Clientes { get; private set; } = new List<Cliente>();

    public void RegistrarCliente(Cliente cliente)
    {
        Clientes.Add(cliente);
    }

    public Filme BuscarFilme(string titulo)
    {
        return Filmes.FirstOrDefault(f => f.Titulo == titulo && f.Disponivel);
    }

    public void RegistrarEmprestimo(Cliente cliente, string titulo)
    {
        Filme filme = BuscarFilme(titulo);
        if (filme == null)
            throw new InvalidOperationException("Filme não disponível.");
        cliente.AlugarFilme(filme);
    }
}
```

---

## **Dicas ao Projetar Classes**
1. Pense em cada classe como um "especialista" no que ela representa.
2. Evite que uma classe faça muito ou dependa de muitas outras classes.
3. Sempre pergunte: **Esta responsabilidade pertence a esta classe?**
4. Experimente começar com pequenos sistemas e aumente a complexidade gradualmente.

---

Vamos projetar um **sistema de agendamento de consultas médicas** com foco em organizar responsabilidades das classes e como distribuir métodos e propriedades de forma clara. Acompanhe o raciocínio passo a passo.

---

## **Definição do Sistema**
### Cenário:
1. Uma clínica médica oferece serviços e precisa gerenciar **médicos**, **pacientes** e **consultas**.
2. Um médico pode realizar várias consultas.
3. Um paciente pode agendar consultas com diferentes médicos.
4. A consulta tem data, horário e status (agendada, cancelada ou concluída).

---

## **Identificação das Classes**
1. **Médico**
   - Representa os médicos cadastrados na clínica.
   - Dados: Nome, Especialidade, CRM.
   - Responsabilidade: Gerenciar suas informações e consultas associadas.

2. **Paciente**
   - Representa os pacientes da clínica.
   - Dados: Nome, CPF, Contato.
   - Responsabilidade: Gerenciar suas informações e o histórico de consultas.

3. **Consulta**
   - Representa o agendamento de uma consulta.
   - Dados: Médico, Paciente, Data, Hora, Status.
   - Responsabilidade: Representar o agendamento, alterar status e validar disponibilidade.

4. **Agendamento**
   - Centraliza a lógica de gerenciar consultas.
   - Dados: Lista de médicos, pacientes e consultas.
   - Responsabilidade: Registrar, alterar ou cancelar consultas.

---

## **Modelo de Relacionamento**
1. **Paciente** está associado a várias **Consultas**.
2. **Médico** está associado a várias **Consultas**.
3. **Consulta** conecta **Paciente** e **Médico** em uma data e hora específica.

---

## **Código Prático**
Abaixo está a implementação básica do sistema:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Medico
{
    public string Nome { get; set; }
    public string Especialidade { get; set; }
    public string CRM { get; set; }
    public List<Consulta> Consultas { get; private set; } = new List<Consulta>();

    public Medico(string nome, string especialidade, string crm)
    {
        Nome = nome;
        Especialidade = especialidade;
        CRM = crm;
    }

    public bool VerificarDisponibilidade(DateTime dataHora)
    {
        return !Consultas.Any(c => c.DataHora == dataHora && c.Status == "Agendada");
    }
}

public class Paciente
{
    public string Nome { get; set; }
    public string CPF { get; set; }
    public string Contato { get; set; }
    public List<Consulta> Consultas { get; private set; } = new List<Consulta>();

    public Paciente(string nome, string cpf, string contato)
    {
        Nome = nome;
        CPF = cpf;
        Contato = contato;
    }
}

public class Consulta
{
    public Medico Medico { get; set; }
    public Paciente Paciente { get; set; }
    public DateTime DataHora { get; set; }
    public string Status { get; private set; } = "Agendada";

    public Consulta(Medico medico, Paciente paciente, DateTime dataHora)
    {
        Medico = medico;
        Paciente = paciente;
        DataHora = dataHora;
    }

    public void Cancelar()
    {
        Status = "Cancelada";
    }

    public void Concluir()
    {
        Status = "Concluída";
    }
}

public class Agendamento
{
    private List<Medico> Medicos { get; set; } = new List<Medico>();
    private List<Paciente> Pacientes { get; set; } = new List<Paciente>();
    private List<Consulta> Consultas { get; set; } = new List<Consulta>();

    public void AdicionarMedico(Medico medico)
    {
        Medicos.Add(medico);
    }

    public void AdicionarPaciente(Paciente paciente)
    {
        Pacientes.Add(paciente);
    }

    public Consulta AgendarConsulta(Medico medico, Paciente paciente, DateTime dataHora)
    {
        if (!medico.VerificarDisponibilidade(dataHora))
            throw new InvalidOperationException("Médico indisponível nesse horário.");

        var consulta = new Consulta(medico, paciente, dataHora);
        medico.Consultas.Add(consulta);
        paciente.Consultas.Add(consulta);
        Consultas.Add(consulta);

        return consulta;
    }

    public List<Consulta> ListarConsultas()
    {
        return Consultas.OrderBy(c => c.DataHora).ToList();
    }
}
```

---

## **Como Funciona**
1. **Médico**
   - Gerencia sua agenda (lista de consultas).
   - Valida se está disponível para um horário específico.

2. **Paciente**
   - Guarda informações pessoais.
   - Acompanha seu histórico de consultas.

3. **Consulta**
   - Conecta um médico e um paciente em um horário específico.
   - Permite alterar o status (cancelar, concluir).

4. **Agendamento**
   - Centraliza toda a lógica do sistema.
   - Gerencia a lista de médicos, pacientes e consultas.
   - Facilita o acesso às operações de agendamento e listagem.

---

## **Exemplo de Uso**
Aqui está como usar o sistema em prática:

```csharp
class Program
{
    static void Main(string[] args)
    {
        // Criando médicos
        Medico medico1 = new Medico("Dr. João", "Cardiologista", "CRM12345");
        Medico medico2 = new Medico("Dra. Ana", "Dermatologista", "CRM67890");

        // Criando pacientes
        Paciente paciente1 = new Paciente("Carlos Silva", "123.456.789-00", "11 99999-8888");
        Paciente paciente2 = new Paciente("Maria Santos", "987.654.321-00", "11 88888-7777");

        // Criando o sistema de agendamento
        Agendamento agendamento = new Agendamento();
        agendamento.AdicionarMedico(medico1);
        agendamento.AdicionarMedico(medico2);
        agendamento.AdicionarPaciente(paciente1);
        agendamento.AdicionarPaciente(paciente2);

        // Agendando consultas
        var consulta1 = agendamento.AgendarConsulta(medico1, paciente1, new DateTime(2025, 01, 28, 14, 0, 0));
        var consulta2 = agendamento.AgendarConsulta(medico2, paciente2, new DateTime(2025, 01, 28, 15, 0, 0));

        // Listando consultas
        foreach (var consulta in agendamento.ListarConsultas())
        {
            Console.WriteLine($"Consulta: {consulta.DataHora} - {consulta.Medico.Nome} com {consulta.Paciente.Nome} ({consulta.Status})");
        }

        // Cancelando uma consulta
        consulta1.Cancelar();
        Console.WriteLine($"Consulta de {consulta1.Paciente.Nome} com {consulta1.Medico.Nome} foi cancelada.");
    }
}
```

---

## **Vantagens dessa Abordagem**
1. **Organização:** Cada classe tem uma responsabilidade clara e específica.
2. **Facilidade de manutenção:** Novas funcionalidades podem ser adicionadas sem impactar muito o código existente.
3. **Reutilização:** As classes **Médico**, **Paciente**, e **Consulta** podem ser reutilizadas em outros contextos.




