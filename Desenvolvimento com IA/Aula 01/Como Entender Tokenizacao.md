A **tokenização** é o primeiro e mais fundamental passo no processamento de linguagem natural (NLP). Ela é o processo de quebrar um texto bruto em unidades menores chamadas **tokens**, que servirão como as "peças de montar" para a inteligência artificial.

Imagine que você está tentando ensinar uma criança a ler: antes de entender a frase inteira, ela precisa identificar as sílabas ou palavras individualmente. A IA faz exatamente isso, mas de uma forma matemática.

---

## 🔍 Como funciona na prática?

A IA não enxerga "letras" como nós. Ela trabalha com números. A tokenização transforma o texto em algo processável em três etapas principais:

### 1. A Quebra (Splitting)

Diferentes modelos usam diferentes estratégias para quebrar o texto:

* **Por Palavra:** Cada palavra é um token. (Ex: `Gato` = 1 token).
* **Por Caractere:** Cada letra é um token. (Ex: `G`, `a`, `t`, `o` = 4 tokens).
* **Por Sub-palavras (Sub-words):** É o método usado pelo ChatGPT (algoritmo BPE - *Byte Pair Encoding*). Palavras comuns são mantidas inteiras, mas palavras raras são fatiadas.

### 2. O Mapeamento (Vocabulary Lookup)

Cada pedaço de texto (token) corresponde a um **ID numérico** único em um dicionário pré-definido.

> Exemplo: O token "SENAI" pode ser o número `15890` no dicionário da OpenAI.

### 3. A Conversão Numérica

No final, a frase `"O SENAI é ótimo"` vira uma lista de números como `[46, 15890, 321, 5432]`. É com essa sequência que a rede neural realiza seus cálculos.

---

## 🛠️ Por que usamos sub-palavras?

Antigamente, se a IA encontrasse uma palavra que não estava no seu dicionário (como um termo técnico novo), ela travava (o erro `<UNK>` - *Unknown*).

Com a tokenização por sub-palavras:

* A palavra **"Araraquara"** pode ser dividida em `Arar` + `a` + `quara`.
* Mesmo que a IA nunca tenha visto a palavra inteira, ela conhece os pedaços e consegue processar o significado.

---

## 💡 Por que o programador deve se importar?

1. **Limites de Contexto:** As IAs têm um limite de memória (ex: 128k tokens). Se você colar um código gigante, ele pode ser cortado porque excedeu o número de tokens, não necessariamente de palavras ou caracteres.
2. **Custo:** APIs como a da OpenAI cobram por **mil tokens**. Espaços extras, indentações excessivas e comentários longos custam dinheiro real.
3. **Idiomas:** O português costuma gastar mais tokens do que o inglês para dizer a mesma coisa, pois nossas palavras são mais longas e menos comuns no "treinamento" global, resultando em mais quebras de sub-palavras.

---

### ✅ Resumo Visual

`Texto` ➔ `Tokens (Pedaços)` ➔ `IDs (Números)` ➔ `Vetores (Significado)`

## 🧩 O Exemplo: "O SENAI em Araraquara"

Se passarmos essa frase por um tokenizador moderno (como o do GPT-4), a IA não verá apenas 4 palavras. Ela poderá dividir a frase assim:

1. **"O"** (Um token para a letra maiúscula e o espaço)
2. **" SENAI"** (Um token inteiro, pois é uma sigla muito comum)
3. **" em"** (Um token para a preposição)
4. **" Arar"** (Primeira parte da cidade)
5. **"aquara"** (Segunda parte da cidade)

### Por que ela faz isso?

A IA utiliza uma técnica chamada **Byte Pair Encoding (BPE)**. Se uma palavra é muito comum (como "SENAI"), ela vira um token único. Se uma palavra é rara ou complexa (como "Araraquara"), a IA a quebra em pedaços menores que ela já conhece de outras palavras (como "Araras" ou "Guarapuava").

---

## 🔢 A Transformação em Números

Após a quebra, cada token é convertido em um número (ID) dentro de um dicionário gigante.

| Token | ID Numérico (Exemplo) |
| --- | --- |
| O | 42 |
| SENAI | 15890 |
| em | 345 |
| Arar | 8921 |
| aquara | 4432 |

Para a IA, a frase **"O SENAI em Araraquara"** é processada como a sequência: `[42, 15890, 345, 8921, 4432]`.

---

## 💡 3 Curiosidades Técnicas para sua Aula

1. **Espaços contam:** Na maioria dos modelos, o espaço antes de uma palavra faz parte do token (ex: `" casa"` é um token diferente de `"casa"`).
2. **Linguagens de Programação:** Na programação, a tokenização é muito eficiente. Palavras-chave como `if`, `while` e `return` costumam ser tokens únicos, o que ajuda a IA a não errar a sintaxe básica.
3. **A Regra dos 75%:** Em média, para o inglês e português, **1.000 tokens equivalem a cerca de 750 palavras**. É por isso que o limite de "contexto" de uma IA é medido em tokens, não em páginas.

---

Ver a tokenização em tempo real é o que faz o conceito "clicar" na cabeça do aluno.

A ferramenta oficial e mais utilizada para isso é o **OpenAI Tokenizer**.

### 🔗 Onde acessar:

* **Site:** [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)

---

### 🧪 Experimento prático para fazer agora:

Quando você abrir o site, tente colar o seguinte código Python e observe a mágica:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

```

### O que você vai notar no site:

1. **Cores Diferentes:** O site vai colorir cada token. Repare que o espaço de indentação (os 4 espaços antes do `print`) ganha uma cor própria — **isso prova que espaços também são tokens e ocupam memória!**
2. **Palavras-chave:** Termos como `def`, `in` ou `if` geralmente são um único token de uma cor só, porque são extremamente comuns.
3. **Caracteres Especiais:** Note como parênteses `()`, dois pontos `:` e chaves `{}` são tratados. Às vezes eles se fundem com a palavra anterior, às vezes são isolados.

---

### 📊 Comparação de Eficiência (Dica para sua aula)

Peça para os alunos compararem estas duas frases no tokenizer:

* **Frase 1 (Inguês):** `Apple` ➔ **1 Token**
* **Frase 2 (Português):** `Maçã` ➔ **Pode gerar 2 ou 3 tokens** (devido ao caractere especial "ç" e ao til "~").

**Por que mostrar isso?**
Para que o aluno entenda por que, em projetos de larga escala ou sistemas com limites rígidos de orçamento, muitos desenvolvedores preferem que a IA processe instruções internas em inglês: **é mais barato e sobra mais espaço para o código.**

---

### 🛠️ Dica de Atividade Prática

Peça para os alunos acessarem o [OpenAI Tokenizer](https://platform.openai.com/tokenizer). Peça que colem um código em Python e observem como os parênteses, indentação e nomes de variáveis são coloridos de forma diferente. Cada cor ali representa um token distinto.

Eu não inventei esses números aleatoriamente; eles vêm de um **Dicionário (Vocabulário)** pré-definido durante o treinamento do modelo. Imagine que, antes de a IA aprender a escrever, os engenheiros criaram uma "lista telefônica" gigante onde cada pedaço de texto (token) recebe um número de índice fixo.

Aqui está o processo detalhado de como chegamos a esses valores:

---

### 1. O Vocabulário Fixo (A "Lista Telefônica")

Modelos como o GPT-4 possuem um vocabulário de aproximadamente **100.277 tokens**. Esse dicionário é imutável após o treinamento.

* O token `casa` será **sempre** o mesmo ID (ex: 2435) naquele modelo.
* O token `apple` será **sempre** outro ID fixo.

### 2. O Processo de Atribuição (Lookup)

Quando você digita um texto, o software faz uma busca rápida nesse dicionário.

* **Input:** "SENAI"
* **Busca:** O software varre o dicionário: "Onde está a string 'SENAI'?"
* **Resultado:** "Está na posição 15.890".
* **Valor numérico:** 15.890.

### 3. Como o dicionário é criado? (Algoritmo BPE)

Você deve estar se perguntando: *Como eles decidiram quais pedaços de palavras merecem um número próprio?*

Usa-se o algoritmo **Byte Pair Encoding (BPE)**:

1. O algoritmo começa com letras individuais (a, b, c...).
2. Ele lê bilhões de páginas da internet e conta quais pares de letras aparecem mais vezes juntos (ex: "e" + "s").
3. Ele funde os pares mais frequentes em um novo token ("es").
4. Ele repete isso milhares de vezes até formar palavras inteiras ou siglas comuns (como "SENAI").
5. No final, os 100 mil "pedaços" mais frequentes ganham um lugar no dicionário e um ID numérico.

---

### 🧪 Exemplo Real com o Tokenizador da OpenAI (cl100k_base)

Se usarmos o padrão exato do ChatGPT atual para a frase **"O SENAI"**:

1. **"O"**: O tokenizador encontra este caractere maiúsculo isolado. No dicionário, ele ocupa a posição **46**.
2. **" SENAI"**: O tokenizador percebe que a sequência "espaço + S + E + N + A + I" é muito comum em textos em português. Ele encontra essa combinação exata na posição **76.542**.

> **Resultado final para a rede neural:** `[46, 76542]`

---

### ⚠️ Por que isso importa para o Programador?

Se você criar uma variável com um nome bizarro como `x_a_b_c_1_2_3`, a IA vai gastar **muitos tokens** (IDs numéricos) para ler esse nome, porque ele não está no dicionário dela como uma palavra inteira. Ela terá que ler `x`, `_`, `a`, `_`, etc.

**Isso consome "memória" (janela de contexto) e custa mais caro na API.**

---

### 💡 Conexão com o Próximo Passo

Esses números (IDs) ainda são apenas "etiquetas". Para a IA entender que "SENAI" tem a ver com "Educação", ela transforma esses IDs em **Embeddings** (vetores de mil dimensões).

É aqui que a "mágica" acontece: saímos da **etiqueta numérica** (o ID do Token) e entramos no **significado semântico**.

Para a IA, os números `46` e `76542` não têm valor por si sós. Para que ela entenda que "SENAI" está relacionado a "Educação" e não a "Culinária", ela usa os **Embeddings**.

---

## 🗺️ O Que São Embeddings? (O Mapa Matemático)

Imagine uma biblioteca gigantesca onde os livros não estão organizados por ordem alfabética, mas por **assunto**. Livros de física ficam próximos uns dos outros; livros de romance ficam em outra ala.

O **Embedding** transforma o ID do token em uma lista de números decimais (um vetor). Cada número nessa lista representa uma "dimensão" ou característica do significado.

### Exemplo Simplificado em 3D:

Vamos supor que as 3 dimensões da IA fossem: [Educação, Tecnologia, Localização].

* **SENAI:** `[0.98, 0.95, 0.10]` (Alto em educação e tecnologia, baixo em localização geográfica específica).
* **Escola:** `[0.90, 0.20, 0.15]` (Próximo de SENAI em educação, mas longe em tecnologia).
* **Pizza:** `[0.01, 0.05, 0.02]` (Longe de ambos em todas as dimensões).

---

## 📐 Como a IA "Pensa"? (Cálculo de Proximidade)

Quando a IA recebe um token, ela projeta esse vetor em um espaço de **milhares de dimensões** (o GPT-4 usa milhares de números para um único token).

Para saber se duas palavras combinam, a rede neural calcula a **Distância de Cosseno** entre os vetores:

1. Se o ângulo entre os vetores for **pequeno**, a IA entende que as palavras são sinônimos ou relacionadas.
2. Se o ângulo for de **90 graus**, elas não têm relação.

> **Curiosidade Matemática:** É por isso que a IA consegue resolver analogias. Se você pegar o vetor de **"Rei"**, subtrair o vetor de **"Homem"** e somar o vetor de **"Mulher"**, o resultado matemático será um vetor muito próximo de **"Rainha"**.

Essa é a parte onde a matemática encontra a semântica. Transformar um **Token ID** (um número inteiro) em um **Vetor** (uma lista de números decimais) é o processo chamado de **Embedding**.

Para a IA, o número `76542` (ID do token "SENAI") é apenas uma etiqueta. Para que ela entenda o *conceito* de SENAI, esse número precisa ser projetado em um mapa de significados.

---

### 1. A Camada de Embedding (O Grande Dicionário de Coordenadas)

Imagine que a IA tem uma tabela gigante. Em uma coluna, estão todos os IDs de tokens. Na outra coluna, está uma lista de **1.536 números** (no caso do modelo *text-embedding-3-small* da OpenAI).

Essa lista de números é o **Vetor**.

### 2. O Espaço Latente (O Mapa de N Dimensões)

Não pense em um mapa 2D (latitude e longitude), mas em um mapa de **1.536 dimensões**.
Cada dimensão representa uma característica abstrata que a IA aprendeu durante o treinamento, por exemplo:

* Dimensão 1: É um ser vivo?
* Dimensão 2: É relacionado a tecnologia?
* Dimensão 3: É um conceito acadêmico?

Quando posicionamos o token nesse mapa, palavras com significados parecidos ficam **geometricamente próximas**.

---

### 3. Como a proximidade é calculada? (Cosseno)

A IA não "lê" a palavra, ela mede a distância e o ângulo entre os vetores.

* **SENAI** e **Educação** terão vetores apontando para direções muito parecidas.
* **SENAI** e **Abacaxi** terão vetores apontando para direções opostas.

A métrica mais comum é a **Similaridade de Cosseno**. Se o ângulo entre dois vetores é zero, o significado é idêntico para a IA.

---

### 4. A Álgebra das Palavras

O que torna isso fascinante é que você pode fazer cálculos matemáticos com esses vetores. O exemplo clássico é:

A IA entende que se você remover o componente "masculino" de Rei e adicionar o "feminino", o ponto resultante no espaço latente é onde reside o conceito de Rainha.

---

### 5. Por que isso é vital para o programador de IA?

Entender vetores permite que você crie sistemas de **Busca Semântica (RAG)**.

* **Busca Tradicional (SQL):** Procura a palavra exata "erro de conexão". Se no banco estiver "falha no link", ele não acha.
* **Busca por Vetores:** A IA transforma "erro de conexão" em um vetor e procura no banco quais frases têm vetores próximos. Ela encontrará "falha no link" porque os vetores são vizinhos no espaço latente.

---

### 💡 Resumo do Fluxo

1. **Input:** "SENAI"
2. **Token ID:** `76542`
3. **Embedding:** `[0.12, -0.59, 0.88, ...]` (Vetor de 1.536 números)
4. **Espaço Latente:** A IA localiza esse ponto e entende o contexto ao redor dele.

---

## 🛠️ Aplicação na Programação (Contexto)

Na nossa **Aula 10**, quando falarmos de busca semântica, o aluno verá que:

* Um erro de `NullPointerException` (Java) e um `NoneType error` (Python) possuem vetores muito próximos.
* A IA entende que ambos são **erros de referência nula**, mesmo escritos de formas diferentes.

---

## 💡 Resumo do Fluxo de Dados

1. **Texto:** `"SENAI"`
2. **Tokenização (BPE):** Divide em pedaços.
3. **Lookup (Dicionário):** Transforma no ID `76542`.
4. **Embedding Layer:** Transforma o ID `76542` no vetor `[0.123, -0.456, 0.789, ...]`.
5. **Processamento:** A rede neural faz cálculos matemáticos com esses vetores para prever o próximo token.
