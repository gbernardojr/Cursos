Certamente, Luca! Aqui está um manual básico sobre coleções em Python, com exemplos práticos para facilitar o entendimento.

# Manual sobre Coleções em Python

## 1. Tipos de Coleções em Python

Python oferece várias estruturas de dados incorporadas, comumente chamadas de coleções, para armazenar e manipular dados de maneiras diferentes. As principais coleções são:

- **Listas** (`list`)
- **Tuplas** (`tuple`)
- **Conjuntos** (`set`)
- **Dicionários** (`dict`)

### 1.1 Listas

As listas são coleções ordenadas e mutáveis, o que significa que podem ser alteradas após a criação.

#### Criação de Listas

```python
# Lista vazia
minha_lista = []

# Lista com elementos
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
```

#### Acessando e Modificando Elementos

```python
# Acessando elementos
print(frutas[0])  # Saída: maçã
print(numeros[-1])  # Saída: 5

# Modificando elementos
frutas[1] = "uva"
print(frutas)  # Saída: ['maçã', 'uva', 'laranja']
```

#### Métodos Comuns

```python
# Adicionando elementos
numeros.append(6)
print(numeros)  # Saída: [1, 2, 3, 4, 5, 6]

# Removendo elementos
numeros.remove(3)
print(numeros)  # Saída: [1, 2, 4, 5, 6]

# Ordenando a lista
numeros.sort()
print(numeros)  # Saída: [1, 2, 4, 5, 6]

# Tamanho da lista
print(len(numeros))  # Saída: 5
```

### 1.2 Tuplas

As tuplas são coleções ordenadas e imutáveis, o que significa que não podem ser alteradas após a criação.

#### Criação de Tuplas

```python
# Tupla vazia
minha_tupla = ()

# Tupla com elementos
coordenadas = (4, 5)
cidades = ("São Paulo", "Rio de Janeiro", "Belo Horizonte")
```

#### Acessando Elementos

```python
# Acessando elementos
print(coordenadas[0])  # Saída: 4
print(cidades[-1])  # Saída: Belo Horizonte
```

### 1.3 Conjuntos

Os conjuntos são coleções não ordenadas e sem duplicatas. Muito úteis para operações matemáticas de conjuntos.

#### Criação de Conjuntos

```python
# Conjunto vazio
meu_conjunto = set()

# Conjunto com elementos
letras = {"a", "b", "c", "a"}
print(letras)  # Saída: {'a', 'b', 'c'}
```

#### Operações Comuns

```python
# Adicionando elementos
letras.add("d")
print(letras)  # Saída: {'a', 'b', 'c', 'd'}

# Removendo elementos
letras.remove("b")
print(letras)  # Saída: {'a', 'c', 'd'}

# União de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
print(conjunto1 | conjunto2)  # Saída: {1, 2, 3, 4, 5}

# Interseção de conjuntos
print(conjunto1 & conjunto2)  # Saída: {3}
```

### 1.4 Dicionários

Os dicionários são coleções não ordenadas de pares chave-valor. Úteis para associar dados relacionados.

#### Criação de Dicionários

```python
# Dicionário vazio
meu_dicionario = {}

# Dicionário com elementos
aluno = {
    "nome": "João",
    "idade": 21,
    "curso": "Engenharia"
}
```

#### Acessando e Modificando Elementos

```python
# Acessando valores
print(aluno["nome"])  # Saída: João

# Modificando valores
aluno["idade"] = 22
print(aluno)  # Saída: {'nome': 'João', 'idade': 22, 'curso': 'Engenharia'}
```

#### Métodos Comuns

```python
# Adicionando novo par chave-valor
aluno["nota"] = 8.5
print(aluno)  # Saída: {'nome': 'João', 'idade': 22, 'curso': 'Engenharia', 'nota': 8.5}

# Removendo par chave-valor
del aluno["curso"]
print(aluno)  # Saída: {'nome': 'João', 'idade': 22, 'nota': 8.5}

# Verificando se uma chave existe
print("idade" in aluno)  # Saída: True

# Obtendo todas as chaves
print(aluno.keys())  # Saída: dict_keys(['nome', 'idade', 'nota'])

# Obtendo todos os valores
print(aluno.values())  # Saída: dict_values(['João', 22, 8.5])
```

## 2. Exemplos Práticos de Uso de Coleções

### 2.1 Exemplo com Lista: Controle de Estoque

```python
estoque = ["caneta", "caderno", "borracha", "lápis"]

# Adicionar novo item ao estoque
estoque.append("marcador")
print(estoque)  # Saída: ['caneta', 'caderno', 'borracha', 'lápis', 'marcador']

# Remover item do estoque
estoque.remove("lápis")
print(estoque)  # Saída: ['caneta', 'caderno', 'borracha', 'marcador']

# Verificar se um item está em estoque
print("borracha" in estoque)  # Saída: True
```

### 2.2 Exemplo com Tupla: Coordenadas Geográficas

```python
localizacao = (23.5505, -46.6333)  # Latitude e Longitude de São Paulo

# Acessar coordenadas
latitude = localizacao[0]
longitude = localizacao[1]
print(f"Latitude: {latitude}, Longitude: {longitude}")  # Saída: Latitude: 23.5505, Longitude: -46.6333
```

### 2.3 Exemplo com Conjunto: Itens Únicos

```python
nomes = {"Ana", "Beto", "Clara", "Ana"}  # Ana aparece duas vezes

print(nomes)  # Saída: {'Ana', 'Beto', 'Clara'} (Ana aparece apenas uma vez)

# Adicionar novo nome
nomes.add("Diana")
print(nomes)  # Saída: {'Ana', 'Beto', 'Clara', 'Diana'}
```

### 2.4 Exemplo com Dicionário: Cadastro de Alunos

```python
alunos = {
    "123": {"nome": "João", "curso": "Matemática"},
    "456": {"nome": "Maria", "curso": "Física"}
}

# Acessar informações de um aluno
print(alunos["123"]["nome"])  # Saída: João

# Adicionar novo aluno
alunos["789"] = {"nome": "Pedro", "curso": "Química"}
print(alunos)  # Saída: {'123': {'nome': 'João', 'curso': 'Matemática'}, '456': {'nome': 'Maria', 'curso': 'Física'}, '789': {'nome': 'Pedro', 'curso': 'Química'}}
```

## 3. Conclusão

As coleções são uma parte fundamental da programação em Python, oferecendo flexibilidade e eficiência para armazenar e manipular dados. Cada tipo de coleção tem suas características e casos de uso específicos, permitindo que você escolha a melhor opção para cada situação.

Com estes exemplos, você tem uma base sólida para começar a trabalhar com coleções em Python. Se precisar de mais detalhes ou exemplos específicos, sinta-se à vontade para perguntar!
