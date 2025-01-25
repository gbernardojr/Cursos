# Apostila de Introdução ao Pytest

## Introdução

O **Pytest** é uma ferramenta de testes em Python que simplifica a criação e execução de testes unitários. Ele é amplamente utilizado por sua simplicidade, flexibilidade e rica gama de funcionalidades. Nesta apostila, você aprenderá os conceitos básicos e como criar e executar testes utilizando o Pytest.

### O que você precisa

- Python instalado em sua máquina (versão 3.7 ou superior).
- Pytest instalado. Você pode instalá-lo utilizando o comando:

```bash
pip install pytest
```

## 1. Conceitos Fundamentais de Testes

### 1.1 O que são testes unitários?
Testes unitários são utilizados para verificar se uma "unidade" de código (uma função, por exemplo) está funcionando como esperado. A ideia é isolar cada parte do código e verificar seu comportamento.

### 1.2 Por que usar testes unitários?
- **Qualidade**: Detecta problemas cedo no processo de desenvolvimento.
- **Segurança**: Modificações futuras no código têm menor probabilidade de introduzir erros.
- **Automação**: Pode ser integrado a ferramentas de CI/CD para garantir que o código continue funcionando conforme esperado ao longo do tempo.

## 2. Introdução ao Pytest

### 2.1 Estrutura básica de um teste com Pytest

Vamos começar com um exemplo simples. Crie um arquivo chamado `test_example.py`:

```python
def soma(a, b):
    return a + b

def test_soma():
    assert soma(1, 2) == 3
    assert soma(-1, 1) == 0
```

### 2.2 Executando o teste

Para rodar o Pytest, execute o comando abaixo no terminal, dentro do diretório onde o arquivo `test_example.py` está localizado:

```bash
pytest
```

O Pytest encontrará automaticamente os arquivos de teste (aqueles que começam com `test_` ou contêm a palavra `test` no nome) e executará todas as funções que também começam com `test_`.

Se tudo estiver correto, você verá uma saída como:

```bash
======================================== test session starts ========================================
collected 1 item

test_example.py .  [100%]

========================================= 1 passed in 0.01s =========================================
```

### 2.3 A função assert
O Pytest usa a palavra-chave `assert` do Python para verificar se as condições especificadas são verdadeiras. Se a condição falhar, o Pytest automaticamente registra o erro e falha no teste.

## 3. Testando Funções com Pytest

Agora, vamos criar exemplos mais elaborados para testar diferentes tipos de funções.

### 3.1 Testando exceções

O Pytest facilita o teste de exceções utilizando o `pytest.raises`. Considere o exemplo abaixo:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida!")
    return a / b

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError, match="Divisão por zero não permitida!"):
        divide(10, 0)
```

### 3.2 Testando múltiplos cenários com pytest.mark.parametrize

Para testar múltiplas entradas, você pode usar o `@pytest.mark.parametrize`. Isso evita duplicação de código e deixa os testes mais organizados:

```python
import pytest

@pytest.mark.parametrize("a, b, resultado", [
    (1, 2, 3),
    (-1, -1, -2),
    (100, 50, 150)
])
def test_soma_parametrizado(a, b, resultado):
    assert soma(a, b) == resultado
```

## 4. Organização dos Testes

### 4.1 Nomeando arquivos e funções de teste
- Arquivos de teste: Devem começar com `test_` ou terminar com `_test.py`.
- Funções de teste: Sempre devem começar com `test_`, para que o Pytest as identifique corretamente.

### 4.2 Estrutura de diretórios

Em projetos maiores, uma boa prática é organizar seus testes em um diretório separado. Por exemplo:

```
meu_projeto/
    src/
        main.py
    tests/
        test_main.py
```

## 5. Fixtures: Preparando o Ambiente para os Testes

As **fixtures** no Pytest são usadas para configurar e limpar os recursos necessários para um teste. Vamos a um exemplo prático:

```python
import pytest

@pytest.fixture
def dados():
    return {"usuario": "João", "idade": 30}

def test_dados_usuario(dados):
    assert dados["usuario"] == "João"
    assert dados["idade"] == 30
```

Aqui, a fixture `dados` cria os dados necessários para o teste, e o Pytest a injeta automaticamente na função de teste `test_dados_usuario`.

### 5.1 Escopo das Fixtures

Você pode definir o **escopo** das fixtures (por exemplo, se a fixture deve ser executada antes de cada teste, uma vez por módulo, ou mesmo uma vez por sessão). Para isso, utilize o parâmetro `scope`:

```python
@pytest.fixture(scope="module")
def recurso_compartilhado():
    return "Este é um recurso que será utilizado por vários testes."
```

## 6. Boas Práticas em Testes com Pytest

### 6.1 Escreva testes pequenos e focados
Cada teste deve validar apenas uma parte específica do seu código. Isso facilita a detecção de erros e mantém os testes mais legíveis.

### 6.2 Teste casos de sucesso e de falha
Para garantir que seu código está robusto, teste tanto os cenários positivos (em que o código deve funcionar) quanto os negativos (onde ele deve falhar).

### 6.3 Use fixtures para reduzir duplicação de código
Ao utilizar fixtures, você pode evitar repetir a configuração e desmontagem de recursos em diferentes testes.

### 6.4 Teste exceções
Certifique-se de que o código está lidando corretamente com os erros e lançando exceções quando necessário.

## 7. Relatórios e Saída Detalhada

O Pytest possui diversas opções para gerar relatórios e visualizar os resultados dos testes de forma mais detalhada. Por exemplo, para ver a saída completa de cada teste, você pode usar:

```bash
pytest -v
```

E para criar relatórios em formato de arquivo, é possível utilizar plugins como o `pytest-html`, que gera relatórios em HTML:

```bash
pip install pytest-html
pytest --html=resultado_teste.html
```

## 8. Conclusão

O Pytest é uma ferramenta poderosa para testes em Python, oferecendo simplicidade e flexibilidade para desenvolver e manter testes em qualquer tipo de projeto. Utilizando os conceitos vistos nesta apostila, você poderá começar a escrever testes de forma eficaz, garantindo a qualidade e a estabilidade do seu código.

### Próximos Passos

- Explore o site oficial do Pytest (https://pytest.org) para mais informações.
- Pratique a criação de testes em diferentes cenários para se familiarizar ainda mais com as funcionalidades avançadas.

Boa sorte e bons testes!
