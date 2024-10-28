
### Sistema de Controle de Ponto Simples

#### Descrição do Caso de Uso
Os funcionários de uma pequena empresa precisam registrar seu ponto de entrada e saída todos os dias. Esse sistema deve registrar o horário de entrada e saída, calcular a quantidade de horas trabalhadas e exibir o total de horas do dia ao final do expediente.

#### Requisitos
1. **Tela inicial**: Exibe botões para "Marcar Entrada", "Marcar Saída" e "Exibir Registro do Dia".
2. **Marcação de entrada e saída**: Ao clicar em "Marcar Entrada" ou "Marcar Saída", o sistema registra o horário atual e armazena em uma lista (em memória).
3. **Cálculo das horas trabalhadas**: Quando o funcionário marca a saída, o sistema calcula a diferença entre os horários de entrada e saída para obter as horas trabalhadas.
4. **Exibir Registro do Dia**: Exibe em uma `Text` ou `Label` os horários de entrada, saída e o total de horas trabalhadas no dia.

#### Estrutura do Sistema

- **Listas e dicionários**: Para armazenar os registros de entrada e saída do dia.
- **Decisões e loops**: Condicionais para verificar se o horário de entrada ou saída já foi registrado e loops para exibir os registros.
- **Interface com Tkinter**: 
    - Botões para marcar entrada, saída e exibir o registro do dia.
    - Campos de `Label` para exibir horários e mensagens.

#### Funcionalidades Detalhadas

1. **Marcar Entrada**: Registra a hora atual no sistema e exibe uma mensagem confirmando a marcação.
    - Se o usuário já tiver marcado entrada, exibe uma mensagem informando que a entrada já foi registrada.

2. **Marcar Saída**: Registra a hora de saída e calcula as horas trabalhadas.
    - Se a entrada não foi registrada, informa o usuário.
    - Exibe o total de horas trabalhadas ao final do expediente.

3. **Exibir Registro do Dia**: Lista os horários de entrada, saída e o total de horas trabalhadas na interface.

#### Exemplo de Layout

- **Botões**:
  - "Marcar Entrada"
  - "Marcar Saída"
  - "Exibir Registro do Dia"
  
- **Labels** para:
  - Exibir mensagens de confirmação.
  - Exibir o total de horas trabalhadas ao final do expediente.
