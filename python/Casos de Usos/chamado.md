### Exercício: Sistema de Registro e Consulta de Chamados de Suporte Técnico

**Caso de uso:**
Uma empresa de suporte técnico deseja informatizar o processo de abertura e consulta de chamados. O sistema deve permitir que o atendente registre o nome do cliente, o tipo de problema, uma breve descrição, a prioridade e a data de abertura. O sistema também deve permitir consultar chamados já registrados através do número do chamado, além de iniciar novos registros com facilidade. 

**Requisitos funcionais:**
1. **Registro de chamados:**
   - O sistema deve permitir registrar um chamado contendo:
     - Nome do cliente
     - Tipo de problema (campo de seleção com opções predefinidas)
     - Descrição do problema (campo de texto livre)
     - Prioridade (opções: "Baixa", "Média", "Alta")
     - Data de abertura (preenchida automaticamente com a data atual)
     - Número do chamado (gerado automaticamente e sequencialmente)

2. **Botão "Novo Chamado":**
   - Ao clicar neste botão, o sistema deve limpar todos os campos de entrada (exceto o número do chamado, que deve ser atualizado automaticamente para o próximo número).

3. **Botão "Localizar Chamado":**
   - O sistema deve permitir localizar um chamado a partir do número. Ao inserir o número do chamado e clicar em "Localizar Chamado", os dados do chamado correspondente devem ser carregados e exibidos na tela para visualização ou edição.

4. **Salvar chamado:**
   - O sistema deve salvar os dados do chamado em um arquivo JSON contendo as informações fornecidas.

**Instruções para desenvolvimento:**

1. **Interface gráfica (Tkinter):**
   - Crie uma única janela com os seguintes campos e botões:
     - **Nome do cliente:** Entry para inserir o nome do cliente.
     - **Tipo de problema:** Combobox ou OptionMenu com opções predefinidas (por exemplo, "Problema de Rede", "Falha de Software", "Erro de Hardware").
     - **Descrição do problema:** Text (campo de várias linhas) para descrever o problema.
     - **Prioridade:** Combobox ou OptionMenu com opções: "Baixa", "Média", "Alta".
     - **Data de abertura:** Label que exibe automaticamente a data de abertura (data atual).
     - **Número do chamado:** Label que exibe o número do chamado gerado automaticamente.
     - **Campo para inserir o número do chamado a ser localizado:** Entry para o atendente digitar o número de um chamado existente e clicar em "Localizar Chamado".
     - **Botão "Novo Chamado":** Para limpar todos os campos e preparar o sistema para um novo registro.
     - **Botão "Localizar Chamado":** Para buscar um chamado salvo e preencher os campos com as informações correspondentes.
     - **Botão "Salvar chamado":** Para salvar os dados do chamado atual em um arquivo JSON.

2. **Funcionalidades:**
   - **Geração do número do chamado:** O sistema deve gerar automaticamente um número de chamado sequencial, que será exibido no campo "Número do chamado".
   - **Salvar chamado:** Quando o atendente clicar no botão "Salvar chamado", o sistema deve gravar as informações do chamado em um arquivo JSON no seguinte formato:
     ```json
     {
       "numero_chamado": 1,
       "cliente": "Nome do Cliente",
       "tipo_problema": "Problema de Rede",
       "descricao": "O cliente relatou que não consegue se conectar à rede.",
       "prioridade": "Alta",
       "data_abertura": "2024-09-09"
     }
     ```
   - **Novo Chamado:** Quando o atendente clicar no botão "Novo Chamado", todos os campos de entrada devem ser limpos (exceto o campo "Número do chamado", que deve ser atualizado para o próximo número disponível).
   - **Localizar Chamado:** Quando o atendente digitar um número de chamado existente e clicar em "Localizar Chamado", o sistema deve buscar no arquivo JSON pelo número do chamado e preencher todos os campos com os dados correspondentes. Se o chamado não for encontrado, uma mensagem de erro deve ser exibida.

3. **Fluxo de trabalho:**
   - Os alunos devem implementar as funções para limpar os campos e gerar um novo número ao clicar em "Novo Chamado".
   - Devem implementar a lógica para buscar um chamado no arquivo JSON pelo número ao clicar em "Localizar Chamado" e carregar os dados na interface.
   - O número do chamado deve ser gerado automaticamente e salvo junto com os demais dados ao clicar em "Salvar chamado".
   - Cada novo chamado deve ser adicionado ao final do arquivo JSON, e o próximo número de chamado deve ser incrementado sequencialmente.

**Dicas para os alunos:**
- Para gerar o número do chamado de forma sequencial, é possível salvar o último número gerado no arquivo JSON e incrementá-lo ao abrir um novo chamado.
- Para limpar os campos da interface, utilize o método `delete()` para campos Entry e Text.
- Para localizar um chamado pelo número, carregue os dados do arquivo JSON e busque o chamado correspondente ao número fornecido.

---
