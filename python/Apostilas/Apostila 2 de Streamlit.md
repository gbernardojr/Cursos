 O **Streamlit** é uma biblioteca Python que permite criar aplicativos web interativos de forma rápida e intuitiva. Abaixo está uma descrição dos principais componentes do Streamlit, com exemplos de código para cada um:

---

## **1. Textos e Títulos**  
Usados para exibir informações textuais no aplicativo.

### **Exemplos:**
```python
import streamlit as st

st.title("Título Principal")  # Título grande
st.header("Cabeçalho da Seção")  # Cabeçalho médio
st.subheader("Subseção")  # Subcabeçalho
st.write("Texto normal")  # Texto comum
st.markdown("**Markdown** suportado!")  # Permite formatação Markdown
st.code("print('Hello, Streamlit!')")  # Exibe código formatado
```

---

## **2. Widgets de Entrada (Inputs)**  
Permitem interação do usuário.

### **Exemplos:**
```python
import streamlit as st

# Botão
if st.button("Clique aqui"):
    st.write("Botão pressionado!")

# Caixa de seleção
check = st.checkbox("Concordo com os termos")
if check:
    st.write("Aceito!")

# Radio button
opcao = st.radio("Escolha uma opção:", ["Python", "JavaScript", "Rust"])

# Selectbox
linguagem = st.selectbox("Linguagem favorita:", ["Python", "Java", "C++"])

# Slider
idade = st.slider("Idade:", 0, 100, 25)  # (min, max, default)

# Text input
nome = st.text_input("Digite seu nome:")

# Text area
bio = st.text_area("Escreva sua biografia:")

# Upload de arquivo
arquivo = st.file_uploader("Envie um arquivo:")
```

---

## **3. Exibição de Dados**  
Mostra dados em tabelas, gráficos e outros formatos.

### **Exemplos:**
```python
import streamlit as st
import pandas as pd
import numpy as np

# DataFrame
df = pd.DataFrame({"Nome": ["Ana", "João", "Maria"], "Idade": [25, 30, 22]})
st.dataframe(df)  # Tabela interativa

# Tabela estática
st.table(df)

# Gráficos
st.line_chart(df.set_index("Nome"))  # Gráfico de linha
st.bar_chart(df.set_index("Nome"))   # Gráfico de barras

# Exibir JSON
st.json({"nome": "Streamlit", "versao": "1.0"})
```

---

## **4. Layout e Organização**  
Controla a estrutura do aplicativo.

### **Exemplos:**
```python
import streamlit as st

# Sidebar (barra lateral)
st.sidebar.title("Menu")
st.sidebar.button("Opção 1")

# Colunas
col1, col2 = st.columns(2)
with col1:
    st.write("Coluna 1")
with col2:
    st.write("Coluna 2")

# Expanders (seções expansíveis)
with st.expander("Detalhes"):
    st.write("Conteúdo oculto que pode ser expandido.")

# Tabs (abas)
tab1, tab2 = st.tabs(["Aba 1", "Aba 2"])
with tab1:
    st.write("Conteúdo da Aba 1")
with tab2:
    st.write("Conteúdo da Aba 2")
```

---

## **5. Status e Progresso**  
Mostra indicadores de carregamento e progresso.

### **Exemplos:**
```python
import streamlit as st
import time

# Spinner (carregamento)
with st.spinner("Processando..."):
    time.sleep(2)
    st.success("Concluído!")

# Barra de progresso
progresso = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    progresso.progress(i + 1)

# Mensagens de status
st.error("Erro!")
st.warning("Aviso!")
st.info("Informação")
st.success("Sucesso!")
```

---

## **6. Mídia**  
Exibe imagens, vídeos e áudios.

### **Exemplos:**
```python
import streamlit as st

# Imagem
st.image("imagem.jpg", caption="Legenda")

# Áudio
st.audio("audio.mp3")

# Vídeo
st.video("video.mp4")
```

---

## **7. Cache e Otimização**  
Melhora a performance com armazenamento em cache.

### **Exemplo:**
```python
import streamlit as st

@st.cache_data  # Armazena dados em cache
def carregar_dados():
    return pd.read_csv("dados.csv")

df = carregar_dados()
st.dataframe(df)
```

---

### **Resumo dos Principais Componentes:**
| **Categoria**       | **Componentes**                          |
|---------------------|------------------------------------------|
| **Textos**          | `title`, `header`, `write`, `markdown`   |
| **Inputs**          | `button`, `checkbox`, `slider`, `text_input` |
| **Dados**           | `dataframe`, `table`, `chart`, `json`    |
| **Layout**          | `sidebar`, `columns`, `expander`, `tabs` |
| **Status**          | `spinner`, `progress`, `error`, `success`|
| **Mídia**           | `image`, `audio`, `video`                |
| **Cache**           | `@st.cache_data`, `@st.cache_resource`   |

---

### **Exemplo Completo (App Simples):**
```python
import streamlit as st

st.title("App de Exemplo")
nome = st.text_input("Qual é o seu nome?")
idade = st.slider("Idade:", 0, 100)

if st.button("Enviar"):
    st.write(f"Olá {nome}, você tem {idade} anos!")
    st.balloons()  # Animações de balões
```

O **Markdown** é uma linguagem de formatação simples muito usada em aplicativos como Streamlit, GitHub, Jupyter Notebook e outras plataformas. Ele permite formatar texto sem a necessidade de HTML ou CSS.  

Abaixo estão as **principais formatações Markdown** suportadas no Streamlit (e na maioria dos ambientes que usam Markdown):

---

## **1. Títulos (Headers)**  
Usam `#` para definir níveis de cabeçalho.  

```markdown
# Título Principal (H1)  
## Subtítulo (H2)  
### Subseção (H3)  
#### Título menor (H4)  
```

**Exemplo no Streamlit:**  
```python
st.markdown("# Título Principal")
st.markdown("## Subtítulo")
```

---

## **2. Ênfase no Texto (Negrito e Itálico)**  

| Formatação       | Sintaxe          | Resultado         |
|------------------|------------------|-------------------|
| **Negrito**      | `**texto**`      | **texto**         |
| *Itálico*        | `*texto*`        | *texto*           |
| ~~Tachado~~      | `~~texto~~`      | ~~texto~~         |
| `Código inline`  | `` `texto` ``    | `texto`           |

**Exemplo:**  
```python
st.markdown("**Negrito**, *itálico*, ~~tachado~~ e `código`.")
```

---

## **3. Listas**  

### **Lista não ordenada** (marcadores)  
```markdown
- Item 1  
- Item 2  
  - Subitem (2 espaços ou Tab)  
```

### **Lista ordenada** (números)  
```markdown
1. Primeiro item  
2. Segundo item  
```

**Exemplo:**  
```python
st.markdown("""
- Maçã  
- Banana  
   - Nanica  
1. Primeiro  
2. Segundo  
""")
```

---

## **4. Links e Imagens**  

### **Link**  
```markdown
[Texto do link](https://exemplo.com)  
```

### **Imagem**  
```markdown
![Legenda da imagem](caminho/da/imagem.jpg)  
```

**Exemplo no Streamlit:**  
```python
st.markdown("[Google](https://www.google.com)")
st.markdown("![Logo Streamlit](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png)")
```

---

## **5. Tabelas**  

```markdown
| Nome      | Idade | Profissão   |
|-----------|-------|-------------|
| João      | 25    | Engenheiro  |
| Maria     | 30    | Cientista   |
```

**Exemplo:**  
```python
st.markdown("""
| Linguagem | Popularidade |
|-----------|--------------|
| Python    | Alta         |
| Java      | Média        |
""")
```

---

## **6. Blocos de Código**  

### **Inline**  
`` `print("Hello")` `` → `print("Hello")`  

### **Bloco de código (multilinha)**  
````markdown
```python
def hello():
    print("Streamlit")
```
````

**Exemplo no Streamlit:**  
```python
st.markdown("""
```python
def soma(a, b):
    return a + b
```
""")
```

---

## **7. Linhas Horizontais (Divisores)**  
Usa `---`, `***` ou `___`.  

```markdown
Texto antes  
---  
Texto depois  
```

**Exemplo:**  
```python
st.markdown("Texto acima\n---\nTexto abaixo")
```

---

## **8. Citações (Blockquotes)**  
Usa `>` no início.  

```markdown
> Esta é uma citação.  
> Continua aqui.  
```

**Exemplo:**  
```python
st.markdown("> Frase inspiradora aqui.")
```

---

## **9. HTML (Suporte Limitado no Streamlit)**  
Algumas tags HTML funcionam dentro do `st.markdown()`.  

```python
st.markdown("<span style='color: red;'>Texto vermelho</span>", unsafe_allow_html=True)
```

---

### **Resumo das Principais Formatações**  

| **Formatação**       | **Sintaxe Markdown**          |
|----------------------|-------------------------------|
| Título               | `# Título`, `## Subtítulo`    |
| Negrito              | `**texto**`                   |
| Itálico              | `*texto*`                     |
| Tachado              | `~~texto~~`                   |
| Link                 | `[texto](url)`                |
| Imagem               | `![legenda](url)`             |
| Lista não ordenada   | `- item`                      |
| Lista ordenada       | `1. item`                     |
| Tabela               | `\| col1 \| col2 \|`          |
| Bloco de código      | ```python\ncode\n```          |
| Linha horizontal     | `---`                         |
| Citação              | `> texto`                     |

---

### **Exemplo Completo no Streamlit**  
```python
import streamlit as st

st.markdown("""
# Título Principal  
## Subtítulo  

**Negrito**, *itálico*, ~~tachado~~ e `código`.  

### Lista:  
- Item 1  
- Item 2  

### Tabela:  
| Nome  | Idade |  
|-------|-------|  
| João  | 25    |  

### Código:  
```python
print("Hello, Streamlit!")
```  

> Citação inspiradora.  

---  
Fim do texto.  
""")
```

No **Markdown** (incluindo no Streamlit), você pode exibir **equações matemáticas** (usando LaTeX) e **códigos-fonte** com formatação adequada. Vamos ver como fazer isso:

---

## **1. Equações Matemáticas (LaTeX)**  
O Markdown suporta fórmulas matemáticas usando sintaxe **LaTeX**, especialmente em ambientes que renderizam MathJax (como Streamlit, Jupyter Notebook, GitHub, etc.).

### **Sintaxe Básica:**
- **Equações inline (no meio do texto):**  
  ```markdown
  $equação$
  ```
  Exemplo:  
  ```markdown
  A fórmula da área do círculo é $A = \pi r^2$.
  ```
  Saída:  
  A fórmula da área do círculo é $A = \pi r^2$.

- **Equações em destaque (centralizadas):**  
  ```markdown
  $$
  equação
  $$
  ```
  Exemplo:  
  ```markdown
  A equação de Einstein é:
  $$
  E = mc^2
  $$
  ```
  Saída:  
  A equação de Einstein é:  
  $$
  E = mc^2
  $$

### **Exemplos de Fórmulas em LaTeX:**
| **Descrição**          | **LaTeX**                     | **Renderização**            |
|------------------------|-------------------------------|-----------------------------|
| Soma                  | `$\sum_{i=1}^{n} i$`         | $\sum_{i=1}^{n} i$         |
| Integral              | `$\int_{a}^{b} x^2 \,dx$`    | $\int_{a}^{b} x^2 \,dx$    |
| Fração                | `$\frac{a}{b}$`              | $\frac{a}{b}$              |
| Raiz quadrada         | `$\sqrt{x}$`                 | $\sqrt{x}$                 |
| Letras gregas         | `$\alpha, \beta, \Omega$`    | $\alpha, \beta, \Omega$    |
| Matriz                | `$\begin{matrix} a & b \\ c & d \end{matrix}$` | $\begin{matrix} a & b \\ c & d \end{matrix}$ |

### **No Streamlit:**
```python
import streamlit as st

st.markdown(r"""
### Equações no Streamlit:
- **Inline:** A área do círculo é $A = \pi r^2$.
- **Destaque:**
  $$
  \frac{\partial f}{\partial t} + \nabla \cdot \mathbf{J} = 0
  $$
""")
```

---

## **2. Código-Fonte (Syntax Highlighting)**  
Para exibir código com formatação e destaque de sintaxe, use **blocos de código** com a linguagem especificada.

### **Sintaxe:**
- **Código inline:**  
  ```markdown
  `print("Hello")`
  ```
  Saída: `print("Hello")`

- **Bloco de código (multilinha):**  
  ````markdown
  ```python
  def soma(a, b):
      return a + b
  ```
  ````
  Saída:
  ```python
  def soma(a, b):
      return a + b
  ```

### **Linguagens Suportadas:**  
Você pode especificar a linguagem para syntax highlighting (cores diferentes para palavras-chave, strings, etc.). Exemplos:
- ````markdown
  ```python
  print("Hello")
  ```
  ````
- ````markdown
  ```javascript
  console.log("Hello");
  ```
  ````
- ````markdown
  ```sql
  SELECT * FROM tabela;
  ```
  ````

### **No Streamlit:**
```python
import streamlit as st

st.markdown("""
### Exemplo de Código Python:
```python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
```
### Exemplo de SQL:
```sql
SELECT nome, idade FROM usuarios WHERE idade > 18;
```
""")
```

---

## **3. Combinação de Equações e Código**  
Você pode misturar ambos em um mesmo documento. Exemplo:

```python
import streamlit as st

st.markdown(r"""
### Cálculo da Distância Euclidiana:
A distância entre dois pontos $(x_1, y_1)$ e $(x_2, y_2)$ é:
$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

### Implementação em Python:
```python
import math

def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
```
""")
```

---

## **Resumo Final**  
| **Recurso**       | **Sintaxe Markdown**                     | **Exemplo**                     |
|-------------------|------------------------------------------|----------------------------------|
| Equação inline    | `$equação$`                              | `$E = mc^2$`                    |
| Equação destacada | `$$ equação $$`                          | `$$\sum_{i=1}^{n} i$$`          |
| Código inline     | `` `código` ``                           | `` `print("Hello")` ``          |
| Bloco de código   | ````markdown<br>```linguagem<br>código<br>```<br>```` | Veja exemplos acima. |

---

### **Dica Extra no Streamlit**  
Se você quiser **equações em destaque** com numeração (como em LaTeX puro), pode usar ambientes como `\begin{equation}` (mas isso depende do renderizador). No Streamlit, o suporte é limitado a `$$ ... $$` e `$ ... $`.

No **Streamlit**, você pode usar **HTML e CSS** para personalizar seu aplicativo além das opções nativas do Markdown. No entanto, existem algumas limitações e cuidados a serem tomados. Vamos explorar como fazer isso:

---

## **1. Usando HTML no Streamlit**
O Streamlit permite inserir HTML diretamente via `st.markdown()` com o parâmetro `unsafe_allow_html=True`.

### **Exemplo Básico:**
```python
import streamlit as st

st.markdown("<h1 style='color: red;'>Título em Vermelho</h1>", unsafe_allow_html=True)
```
**Resultado:**  
![Título em vermelho](https://i.imgur.com/XYZ1234.png)

### **Elementos HTML Suportados:**
Você pode usar tags como:
- `<div>`, `<span>`, `<p>`, `<h1>` a `<h6>`
- `<a>` (links), `<img>` (imagens), `<br>` (quebra de linha)
- `<ul>`, `<ol>`, `<li>` (listas)
- `<table>`, `<tr>`, `<td>` (tabelas)

**Exemplo com Link e Imagem:**
```python
st.markdown("""
<a href="https://streamlit.io">Link para o Streamlit</a>
<img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width="200">
""", unsafe_allow_html=True)
```

---

## **2. Usando CSS no Streamlit**
Você pode injetar CSS de três formas:

### **Método 1: CSS Inline (Direto no HTML)**
```python
st.markdown("""
<p style='color: blue; font-size: 20px;'>Texto estilizado com CSS inline</p>
""", unsafe_allow_html=True)
```

### **Método 2: CSS via `<style>` (Global)**
Para aplicar estilos a todo o app:
```python
st.markdown("""
<style>
    .meu-texto {
        color: green;
        font-family: 'Arial';
    }
</style>
<p class="meu-texto">Texto estilizado com classe CSS</p>
""", unsafe_allow_html=True)
```

### **Método 3: Arquivo CSS Externo**
Você pode carregar um arquivo `.css` e injetá-lo no app:
```python
with open("estilos.css") as f:
    css = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
```

---

## **3. Personalização Avançada**
### **Alterar Cor de Fundo:**
```python
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)
```

### **Estilizar Widgets:**
```python
st.markdown("""
<style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.button("Botão Estilizado")
```

### **Centralizar Elementos:**
```python
st.markdown("""
<style>
    .centro {
        display: flex;
        justify-content: center;
    }
</style>
<div class="centro">
    <h2>Texto Centralizado</h2>
</div>
""", unsafe_allow_html=True)
```

---

## **4. Limitações e Cuidados**
1. **Segurança:** Sempre use `unsafe_allow_html=True` com cautela, pois ele pode expor seu app a vulnerabilidades se o conteúdo for dinâmico (como inputs de usuários).
2. **Compatibilidade:** Algumas propriedades CSS podem não funcionar devido ao Shadow DOM do Streamlit.
3. **Responsividade:** O Streamlit tem seu próprio sistema de layout, então alguns estilos podem ser sobrescritos.

---

## **5. Exemplo Completo**
```python
import streamlit as st

# CSS Global
st.markdown("""
<style>
    .destaque {
        background-color: #f0f8ff;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #4682b4;
    }
</style>
""", unsafe_allow_html=True)

# HTML + CSS
st.markdown("""
<div class="destaque">
    <h2>Seção Destacada</h2>
    <p>Este é um exemplo de personalização com HTML/CSS no Streamlit.</p>
</div>
""", unsafe_allow_html=True)

# Widget estilizado
st.markdown("""
<style>
    .stSlider>div>div>div>div {
        background: #4682b4;
    }
</style>
""", unsafe_allow_html=True)

valor = st.slider("Slider Estilizado", 0, 100)
```

---

## **Resumo**
| **Recurso**       | **Como Usar**                                                                 |
|-------------------|------------------------------------------------------------------------------|
| **HTML**          | `st.markdown("<tag>conteúdo</tag>", unsafe_allow_html=True)`                 |
| **CSS Inline**    | `<p style='propriedade: valor;'>texto</p>`                                   |
| **CSS Global**    | `<style>.classe { propriedade: valor; }</style>`                             |
| **Arquivo CSS**   | Carregue um arquivo `.css` e injete com `st.markdown()`                      |
| **Limitações**    | Evite usar para conteúdo dinâmico (XSS) e teste a compatibilidade.           |

Com HTML/CSS, você pode criar apps **muito mais personalizados** no Streamlit! 🎨🚀

Vamos completar o guia com **comandos úteis do Streamlit** que ainda não foram mencionados, cobrindo desde interatividade avançada até gerenciamento de estado e otimização. Aqui está uma lista detalhada:

---

## **Comandos Avançados e Úteis do Streamlit**  
### **1. Controle de Estado (Session State)**  
Gerencia variáveis entre reruns (útil para forms, multi-páginas, etc.).  
```python
import streamlit as st

if 'contador' not in st.session_state:
    st.session_state.contador = 0  # Inicializa

if st.button("Incrementar"):
    st.session_state.contador += 1

st.write("Contador:", st.session_state.contador)
```

---

### **2. Forms (Agrupar Inputs + Botão de Submit Único)**  
Evita reruns a cada input.  
```python
with st.form("meu_form"):
    nome = st.text_input("Nome")
    idade = st.slider("Idade", 1, 100)
    submitted = st.form_submit_button("Enviar")
    
    if submitted:
        st.write(f"{nome}, {idade} anos")
```

---

### **3. Multi-Páginas (Oficial desde Streamlit 1.10+)**
Crie uma pasta `pages/` no mesmo diretório do seu script principal e adicione arquivos `.py` (ex: `pages/02_analise.py`).  
- Estrutura:  
  ```
  meu_app/
  ├── main.py
  └── pages/
      ├── 01_dashboard.py
      └── 02_sobre.py
  ```
- O Streamlit automaticamente cria um menu lateral com as páginas.

---

### **4. Download de Arquivos**  
Permite baixar dados gerados no app.  
```python
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
st.download_button(
    label="Baixar CSV",
    data=df.to_csv().encode("utf-8"),
    file_name="dados.csv",
    mime="text/csv"
)
```

---

### **5. Timeouts e Progresso com st.status()**  
Novo em **Streamlit 1.28+**, mostra status de operações.  
```python
with st.status("Processando...", expanded=True) as status:
    st.write("Carregando dados...")
    time.sleep(2)
    st.write("Aplicando modelo...")
    time.sleep(1)
    status.update(label="Concluído!", state="complete")
```

---

### **6. st.toast (Notificações Temporárias)**  
Exibe mensagens rápidas (versão 1.27+).  
```python
st.toast("Operação concluída!", icon="🎉")
```

---

### **7. st.experimental_rerun()**  
Força um rerun do app (útil após ações críticas).  
```python
if st.button("Recarregar App"):
    st.experimental_rerun()
```

---

### **8. st.empty() (Placeholders Dinâmicos)**  
Atualiza conteúdo sem rerun completo.  
```python
placeholder = st.empty()
if st.button("Atualizar"):
    placeholder.write("Novo conteúdo!")
```

---

### **9. st.echo() (Exibir Código em Tempo de Execução)**  
Mostra o código que está sendo executado.  
```python
with st.echo():
    x = 10
    st.write("O valor de x é", x)  # O código aqui será exibido no app
```

---

### **10. st.help() (Documentação de Objetos Python)**  
Exibe a docstring de funções/objetos.  
```python
st.help(pd.DataFrame)  # Mostra a documentação do DataFrame
```

---

### **11. st.metric (KPIs Dinâmicos)**  
Exibe métricas com variação.  
```python
st.metric("Taxa de Conversão", "75%", "+5%")
```

---

### **12. st.columns (Layouts Complexos)**  
Divide a tela em colunas personalizáveis.  
```python
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.button("Esquerda")
with col2:
    st.button("Centro")
with col3:
    st.button("Direita")
```

---

### **13. st.tabs (Abas Laterais)**  
Organiza conteúdo em abas.  
```python
tab1, tab2 = st.tabs(["Gráficos", "Dados"])
with tab1:
    st.line_chart(data)
with tab2:
    st.dataframe(data)
```

---

### **14. st.spinner (Feedback Durante Processamento)**  
Mostra um spinner durante operações longas.  
```python
with st.spinner("Aguarde..."):
    time.sleep(3)
st.success("Concluído!")
```

---

### **15. st.balloons() e st.snow() (Efeitos Visuais)**  
Celebrações!  
```python
if st.button("Celebrar"):
    st.balloons()  # ou st.snow() para neve
```

---

## **Comandos para Otimização**  
### **16. @st.cache_data (Cache de Dados)**  
Armazena dados em cache para evitar recarregamento.  
```python
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados.csv")  # Só executa uma vez
```

### **17. @st.cache_resource (Cache de Recursos Pesados)**  
Para modelos de ML, conexões de banco, etc.  
```python
@st.cache_resource
def carregar_modelo():
    return pickle.load(open("modelo.pkl", "rb"))
```

---

## **Comandos Úteis para Debug**  
### **18. st.write(st.session_state)**  
Inspect todas as variáveis de estado.  
```python
st.write(st.session_state)  # Debug completo
```

### **19. st.stop()**  
Interrompe a execução do app.  
```python
if erro:
    st.error("Algo deu errado!")
    st.stop()  # O app não continua abaixo deste ponto
```

---

## **Resumo dos Comandos Faltantes**  
| **Categoria**         | **Comandos**                                      | **Uso**                                  |
|-----------------------|--------------------------------------------------|------------------------------------------|
| **Estado**            | `st.session_state`                               | Persistir variáveis entre reruns         |
| **Forms**             | `st.form`, `st.form_submit_button`               | Agrupar inputs                           |
| **Multi-Páginas**     | Pasta `pages/`                                   | Apps com navegação                       |
| **Download**          | `st.download_button`                             | Baixar arquivos                          |
| **Status**            | `st.status`                                      | Feedback de processos longos             |
| **Notificações**      | `st.toast`                                       | Mensagens temporárias                    |
| **Layout**            | `st.tabs`, `st.columns`                          | Organização avançada                     |
| **Otimização**        | `@st.cache_data`, `@st.cache_resource`           | Cache de dados e recursos                |
| **Debug**             | `st.stop()`, `st.write(st.session_state)`        | Depuração                                |

---

### **Exemplo Prático (App com Tudo Junto)**  
```python
import streamlit as st
import pandas as pd
import time

# Session State
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0

# Form
with st.form("meu_form"):
    nome = st.text_input("Nome")
    submitted = st.form_submit_button("Enviar")
    if submitted:
        st.session_state.clicks += 1

# Colunas
col1, col2 = st.columns(2)
with col1:
    st.metric("Cliques", st.session_state.clicks)
with col2:
    if st.button("Recarregar"):
        st.experimental_rerun()

# Download
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
st.download_button("Baixar CSV", df.to_csv(), "dados.csv")

# Status
with st.status("Processando..."):
    time.sleep(2)
    st.toast("Sucesso!", icon="✅")
```

---
