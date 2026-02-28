## Contexto (Context)

Você é um engenheiro de software sênior especializado em aplicações desktop Python para o setor de saúde. Sua missão é criar uma aplicação **monousuário** de agenda médica simples, robusta e intuitiva, destinada ao uso diário por secretárias de consultórios médicos ou pequenas clínicas.

A aplicação deve rodar localmente em computadores Windows (principalmente), mas ser compatível com Linux e macOS.  
Como se trata de uso **monousuário**, utilizaremos **SQLite** como banco de dados (arquivo único .db na pasta da aplicação ou em local configurável).  
A interface gráfica deve ser moderna, limpa e fácil de usar mesmo por pessoas com pouca familiaridade com computadores.  
Priorize usabilidade, validações fortes, mensagens claras de erro/sucesso e proteção básica contra duplicidade de agendamentos no mesmo horário.

## Tarefa (Task)

Desenvolva uma aplicação desktop em **Python** chamada **"Agenda Médica Simples"** com as seguintes funcionalidades principais:

1. Tela principal: grade (tabela) mostrando todos os horários de **08:00 às 18:00** em intervalos fixos de **30 minutos** (08:00, 08:30, 09:00, ..., 17:30, 18:00).
   - A grade deve exibir a **data atual** por padrão.
   - Deve haver um seletor de data (calendário ou campo de data) para navegar para qualquer outro dia.
   - Ao mudar a data, a grade deve ser recarregada imediatamente mostrando os agendamentos daquele dia.

2. Cada linha da grade representa um slot de 30 minutos.
   - Slots livres: fundo claro (ex: branco ou cinza claro), sem texto ou com "Livre".
   - Slots ocupados: fundo colorido suave (ex: azul claro ou verde claro), mostrando:
     - Nome do paciente (primeiros 25–30 caracteres + "..." se muito longo)
     - Convênio (abreviado se necessário)
     - Ícones ou botões pequenos ao lado: ✏️ (editar) e 🗑️ (liberar/excluir)

3. Operações principais:
   - **Novo agendamento**: botão grande e visível "Novo Agendamento" (ou +)
     Ao clicar, abre formulário/modal com campos:
       - Nome completo do paciente (obrigatório)
       - Data de nascimento (formato DD/MM/AAAA, obrigatório, validar formato e idade plausível)
       - Convênio (texto livre, opcional)
       - Data do atendimento (pré-preenchida com a data da grade atual)
       - Horário (combo-box ou lista com os horários de 30 em 30 min disponíveis naquele dia)
     Validação: não permitir salvar se o horário já estiver ocupado.

   - **Editar agendamento**: clicar no ícone ✏️ → abrir o mesmo formulário preenchido → permitir alterar qualquer campo (inclusive data e horário, com validação de conflito).

   - **Liberar horário / Cancelar agendamento**: clicar no ícone 🗑️ → confirmação simples ("Deseja realmente liberar este horário?") → remove o registro.

4. Busca rápida:
   - Campo de texto "Buscar paciente..." na parte superior da tela
   - Ao digitar (mínimo 3 caracteres), filtrar a grade mostrando apenas os horários que contenham o texto digitado no nome do paciente (busca parcial, case-insensitive)
   - Botão "Limpar busca" ou tecla ESC para voltar à visualização completa

5. Banco de dados SQLite:
   - Nome do arquivo sugerido: agenda_medica.db (na mesma pasta do executável ou em subpasta data/)
   - Tabela principal: agendamentos
     colunas:
       id                 INTEGER PRIMARY KEY AUTOINCREMENT
       data               DATE            NOT NULL            (formato 'YYYY-MM-DD')
       horario            TIME            NOT NULL            (formato 'HH:MM')
       nome_paciente      TEXT            NOT NULL
       data_nascimento    DATE            NOT NULL            ('YYYY-MM-DD')
       convenio           TEXT            NULL

6. Requisitos técnicos adicionais:
   - Interface gráfica: use **Tkinter** (padrão) ou **CustomTkinter** (visual moderno) ou **PyQt6** / **PySide6** (se optar por visual mais profissional)
   - Tratamento de erros amigável (caixas de mensagem)
   - Evitar duplicidade de horário no mesmo dia (chave única composta data + horario)
   - Permitir que a aplicação seja empacotada com PyInstaller posteriormente

## Entrada (Input)

- Dados inseridos pela secretária via formulários:
  - Nome do paciente (str)
  - Data de nascimento (str → validada como data)
  - Convênio (str)
  - Data do agendamento (date)
  - Horário (time – apenas múltiplos de 30 min)

- Filtro de busca: texto parcial do nome

## Formato de Entrega Esperado (Output / Format)

Forneça:

1. Código Python completo e organizado em arquivos/classes (ou um único arquivo bem comentado se for simples)
2. Estrutura sugerida de pastas (se houver mais de um arquivo)
3. Script de criação do banco SQLite (schema + índices úteis)
4. Comentários explicativos em português nas partes principais
5. Instruções mínimas de como executar (dependências, comando)
6. Sugestão de bibliotecas extras (se usar CustomTkinter, ttkbootstrap, etc.)
7. (Opcional) Sugestões de melhorias futuras (ex: relatórios, cores por convênio, backup automático do .db)

Comece agora a implementação da aplicação seguindo exatamente essas especificações.
