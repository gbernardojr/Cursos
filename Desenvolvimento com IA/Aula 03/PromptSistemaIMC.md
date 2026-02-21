## Prompt CTIF – Programa de Cálculo de IMC em Python

**C – Contexto**

Você é um programador experiente em Python que cria exemplos didáticos para iniciantes em programação. O código será utilizado por alunos que estão aprendendo lógica de programação e programação em Python pela primeira vez. Portanto, o código precisa ser simples, claro e bem comentado.

---

**T – Tarefa**

Crie um programa em Python que calcule o IMC (Índice de Massa Corporal) de uma pessoa. O programa deve solicitar ao usuário o peso em quilogramas e a altura em metros, calcular o IMC e informar também a classificação de acordo com os padrões da **Organização Mundial da Saúde**.

---

**I – Instruções**

* Utilizar Python em modo console.
* Solicitar ao usuário:

  * peso (kg)
  * altura (m)
* Calcular o IMC usando a fórmula:

[
IMC = \frac{peso}{altura^2}
]

* Mostrar o valor do IMC com **duas casas decimais**.
* Exibir a classificação correspondente:

Tabela de classificação:

* IMC < 18.5 → Abaixo do peso
* 18.5 ≤ IMC < 25 → Peso normal
* 25 ≤ IMC < 30 → Sobrepeso
* 30 ≤ IMC < 35 → Obesidade grau I
* 35 ≤ IMC < 40 → Obesidade grau II
* IMC ≥ 40 → Obesidade grau III

Outras exigências:

* Utilizar estruturas condicionais (`if`, `elif`, `else`).
* Incluir comentários explicando cada parte do código.
* Manter o código simples e adequado para iniciantes.

---

**F – Formato da Resposta**

A resposta deve conter:

1. Explicação breve do funcionamento do programa.
2. Código completo em Python.
3. Comentários dentro do código explicando cada etapa.

---

✅ **Prompt final (para usar diretamente em IA):**

> Você é um programador experiente em Python que cria exemplos didáticos para iniciantes. Crie um programa em Python que calcule o IMC (Índice de Massa Corporal). O programa deve pedir ao usuário o peso em kg e a altura em metros, calcular o IMC utilizando a fórmula IMC = peso / altura² e mostrar o resultado com duas casas decimais. Além disso, deve mostrar a classificação do IMC conforme a tabela da Organização Mundial da Saúde: abaixo de 18.5 (abaixo do peso), entre 18.5 e 24.9 (peso normal), entre 25 e 29.9 (sobrepeso), entre 30 e 34.9 (obesidade grau I), entre 35 e 39.9 (obesidade grau II) e acima de 40 (obesidade grau III). O código deve rodar em modo console, utilizar estruturas condicionais (if/elif/else), ser simples para iniciantes e conter comentários explicando cada parte do código. Apresente uma breve explicação antes do código.

