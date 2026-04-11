Você é um desenvolvedor Full-Stack Python sênior especializado em aplicações rápidas com Streamlit e IA Generativa.

Crie **do zero** um webapp completo chamado **CV Turbo** – Analisador e Otimizador de Currículos, utilizando a API do Google Gemini (gemini-1.5-flash ou gemini-1.5-pro).

### Requisitos Funcionais (obrigatórios):

1. **Interface do Usuário (Streamlit)**  
   - Layout moderno, clean e profissional (use st.set_page_config com layout wide, tema dark opcional).  
   - Sidebar esquerda:
     - Campo para colar o texto do currículo (textarea grande).  
     - Botão de upload de PDF (aceitar apenas .pdf).  
     - Campo de texto: “Cargo desejado / Vaga alvo” (pode ser mais de um, separados por vírgula).  
     - Selectbox: Modelo do Gemini (gemini-1.5-flash | gemini-1.5-pro).  
     - Input secreto para Gemini API Key (st.text_input type="password", salvar em session_state).  
   - Área principal com abas (st.tabs):
     - 📄 Currículo Original  
     - 🔍 Análise e Sugestões ATS  
     - 🚀 Versões Otimizadas (3 versões)

2. **Fluxo Principal**  
   - Se o usuário fizer upload de PDF → extrair texto usando Gemini (não usar PyPDF2, pois o Gemini 1.5 nativamente aceita PDF como file).  
   - Se colar texto → usar diretamente.  
   - Ao clicar em “Analisar e Otimizar”, o app deve:
     - Enviar o currículo + cargo desejado para o Gemini via function calling / structured output.
     - Gerar uma resposta JSON completa com a seguinte estrutura exata:

```json
{
  "analise_ats": {
    "score_ats": 85,
    "pontos_fortes": ["lista de 4-6 pontos"],
    "melhorias_necessarias": ["lista de 5-8 melhorias concretas com explicação"],
    "palavras_chave_sugeridas": ["lista de keywords da vaga"]
  },
  "sugestoes_gerais": ["5-7 sugestões de melhoria de redação, quantificação, verbos de impacto, etc."],
  "versoes_otimizadas": [
    {
      "versao": 1,
      "nome": "Versão Focada em Liderança e Resultados",
      "resumo_profissional": "texto completo reescrito",
      "experiencias": [array de objetos com cargo, empresa, período, bullet points reescritos com verbos de impacto],
      "educacao": "reescrita se necessário",
      "habilidades": "lista otimizada"
    },
    // ... duas versões adicionais com foco diferente (ex: técnico, criativo, estratégico)
  ]
}
```

3. **Uso do Gemini (obrigatório usar function calling)**  
   - Usar `google.generativeai` + `genai.GenerativeModel`.  
   - Criar um **system prompt extremamente detalhado** (você deve escrever ele completo dentro do código) que instrua o Gemini a:
     - Ser especialista em recrutamento ATS (Applicant Tracking Systems).
     - Sempre quantificar conquistas quando possível.
     - Usar verbos de impacto fortes (Led, Increased, Reduced, Developed, etc.).
     - Manter o tom profissional e adaptado ao cargo informado.
     - Retornar **sempre** JSON válido (sem markdown, sem explicações fora do JSON).
   - Configurar `response_schema` ou function calling para forçar o JSON exato acima.

4. **Funcionalidades Extras Obrigatórias**  
   - Botão “Baixar como Markdown” para cada versão otimizada.  
   - Botão “Baixar como PDF” (usar `markdown-pdf` ou `weasyprint` – inclua o código completo de instalação via requirements).  
   - Exibir o score ATS de forma visual (progress bar colorido).  
   - Histórico das últimas 3 análises (usando session_state).  
   - Mensagens de loading bonitas com st.spinner e st.toast.  
   - Tratamento de erro amigável (API key inválida, PDF muito grande, JSON inválido, etc.).

5. **Requisitos Técnicos**  
   - Todo o código deve estar em **um único arquivo** `app.py` (para facilitar o deploy no Streamlit Community Cloud).  
   - Usar `st.session_state` para persistir API key e histórico.  
   - Código bem comentado em português (explicando cada parte do prompt do Gemini).  
   - requirements.txt com todas as dependências:  
     `streamlit`, `google-generativeai`, `PyPDF2` (backup), `markdown`, `weasyprint` ou `reportlab`.  
   - Tratamento de limite de tokens e custo (usar flash por padrão).  
   - Design responsivo e bonito (use st.columns, cards com st.container, ícones do emoji).

6. **Boas Práticas**  
   - Nunca expor a API key no código.  
   - Usar `genai.configure(api_key=...)` apenas uma vez.  
   - Incluir um botão “Limpar tudo”.  
   - Tornar o app 100% funcional mesmo se o usuário só colar texto (sem PDF).

Gere o código completo, pronto para rodar com `streamlit run app.py`.  
No final do arquivo, adicione um pequeno README dentro de um st.expander explicando como usar e como obter a chave da Gemini API.

Comece agora gerando o código inteiro.
