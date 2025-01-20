# Caso de Uso: Controle de Funcionários - Departamento de RH

Você é responsável pelo departamento de RH de uma empresa e precisa manter o controle sobre os salários, bônus e dados dos funcionários. O objetivo é calcular a soma dos salários de todos os funcionários, identificar quais funcionários receberam bônus, classificar os funcionários por faixa salarial e buscar informações adicionais sobre as suas áreas de atuação.

## Dados fornecidos:

Você tem duas tabelas na planilha:

### Tabela de Funcionários

| Funcionário | Cargo        | Salário | Bônus | Departamento     |
|-------------|--------------|---------|-------|------------------|
| João        | Analista    | 3500    | 500   | TI               |
| Maria       | Gerente     | 8000    | 1000  | Marketing        |
| Pedro       | Analista    | 3000    | 0     | TI               |
| João        | Coordenador | 5000    | 0     | RH               |
| Maria       | Analista    | 4000    | 800   | Financeiro       |
| Pedro       | Coordenador | 6000    | 500   | TI               |
| João        | Analista    | 3500    | 600   | Marketing        |
| Maria       | Coordenador | 7500    | 0     | RH               |
| Pedro       | Gerente     | 9000    | 1200  | Marketing        |
| João        | Gerente     | 7500    | 900   | TI               |

### Tabela de Departamentos

| Departamento | Localização |
|--------------|-------------|
| TI           | São Paulo  |
| Marketing    | Rio de Janeiro |
| RH           | Brasília     |
| Financeiro   | São Paulo   |

## Tarefas:

### 1. Soma Total de Salários

Crie uma fórmula para calcular a soma total dos salários de todos os funcionários da empresa.

**Dica**: Utilize a função `SOMA` para somar todos os valores na coluna "Salário":

```excel
=SOMA(C2:C10)
```

### 2. Soma de Bônus por Departamento

Calcule o total de bônus pagos para cada departamento, utilizando a função `SOMASE`. Por exemplo, para calcular o total de bônus do departamento de TI:

```excel
=SOMASE(E2:E10; "TI"; D2:D10)
```

### 3. Classificação de Funcionários com Base no Salário

Estabeleça que, para a faixa de salário:

- **Menor que 4000**: "Junior"
- **Entre 4000 e 7000**: "Pleno"
- **Maior que 7000**: "Sênior"

Utilize a função `SE` para classificar os funcionários com base no salário.

**Dica**: A fórmula seria algo como:

```excel
=SE(C2<4000; "Junior"; SE(C2<=7000; "Pleno"; "Sênior"))
```

### 4. Busca de Localização do Departamento

Crie uma coluna adicional para buscar a localização de cada departamento usando a função `PROCV`. Por exemplo, se o departamento for "TI", a fórmula deve retornar "São Paulo".

**Dica**: A fórmula para buscar a localização do departamento seria:

```excel
=PROCV(E2; G2:H5; 2; FALSO)
```

## Passos do Exercício:

1. Calcule a soma total dos salários de todos os funcionários.
2. Calcule o total de bônus por departamento.
3. Classifique cada funcionário como "Junior", "Pleno" ou "Sênior" com base no seu salário.
4. Busque a localização de cada departamento.
