**Caso de Uso: Cálculo de IMC (Índice de Massa Corporal)**

### 1. **Título**: Cálculo de IMC

### 2. **Descrição**:
Este caso de uso descreve o comportamento de um sistema que permite ao usuário calcular o Índice de Massa Corporal (IMC) com base na altura e no peso fornecidos. O sistema realiza o cálculo, exibe o resultado e classifica o IMC de acordo com os parâmetros estabelecidos pela Organização Mundial da Saúde (OMS).

### 3. **Ator Principal**: Usuário (pode ser uma pessoa comum ou um profissional de saúde)

### 4. **Pré-condições**:
- O sistema está em funcionamento.
- O usuário deve ter acesso aos dados de peso (em kg) e altura (em metros).

### 5. **Fluxo Principal**:
1. O usuário acessa o sistema de cálculo de IMC.
2. O sistema solicita ao usuário que insira o peso (em quilogramas).
3. O sistema solicita ao usuário que insira a altura (em metros).
4. O usuário insere os dados solicitados e confirma.
5. O sistema calcula o IMC utilizando a fórmula:

   \[
   IMC = peso/altura^2
   \]

6. O sistema exibe o resultado do IMC.
7. O sistema classifica o IMC de acordo com os seguintes intervalos:
   - Abaixo de 18.5: Abaixo do peso
   - Entre 18.5 e 24.9: Peso normal
   - Entre 25.0 e 29.9: Sobrepeso
   - Acima de 30.0: Obesidade
8. O sistema oferece a opção de realizar um novo cálculo ou encerrar a sessão.

### 6. **Fluxo Alternativo**:
- Se o usuário inserir dados inválidos (como letras ou valores negativos), o sistema exibe uma mensagem de erro e solicita a correção dos dados.

### 7. **Pós-condições**:
- O IMC é calculado e exibido ao usuário.
- A classificação do IMC é fornecida com base nos valores inseridos.

### 8. **Exceções**:
- Se o usuário inserir valores incorretos, o sistema exibirá uma mensagem de erro até que os dados corretos sejam fornecidos.

### 9. **Regras de Negócio**:
- O cálculo do IMC deve seguir a fórmula estabelecida pela OMS.
- A classificação do IMC deve seguir os parâmetros estabelecidos pela OMS.

### 10. **Fórmula do IMC**:

\[
IMC = peso (kg)/altura (m)^2
\]

Essa estrutura pode servir de base para a implementação de um programa simples ou até ser expandida para um software mais completo com funcionalidades adicionais, como histórico de cálculos.
