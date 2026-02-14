# 📌 Caso de Uso – Sistema de Lista de Tarefas (To-Do List)

---

## 🧾 Nome do Caso de Uso

**Gerenciar Tarefas Pessoais**

---

## 👤 Ator Principal

Usuário

---

## 🎯 Objetivo

Permitir que o usuário organize suas tarefas diárias, adicionando, visualizando e removendo tarefas por meio de um sistema simples em Python executado no console.

---

## 🖥️ Descrição Geral

O sistema apresenta um menu no console onde o usuário pode escolher ações para gerenciar uma lista de tarefas armazenada temporariamente na memória do programa.

---

## ▶️ Fluxo Principal

1. O usuário executa o programa.
2. O sistema exibe um menu com as opções:

   * Adicionar tarefa
   * Listar tarefas
   * Remover tarefa
   * Sair
3. O usuário escolhe a opção **Adicionar tarefa**.
4. O sistema solicita a descrição da tarefa.
5. O usuário informa a tarefa.
6. O sistema adiciona a tarefa à lista.
7. O sistema retorna ao menu principal.

---

## 🔁 Fluxos Alternativos

### 🔹 A1 – Listar Tarefas

1. O usuário seleciona a opção **Listar tarefas**.
2. O sistema exibe todas as tarefas cadastradas, numeradas.
3. O sistema retorna ao menu.

---

### 🔹 A2 – Remover Tarefa

1. O usuário seleciona **Remover tarefa**.
2. O sistema exibe a lista de tarefas numeradas.
3. O usuário informa o número da tarefa a ser removida.
4. O sistema valida a entrada.
5. A tarefa é removida da lista.
6. O sistema retorna ao menu.

---

### 🔹 A3 – Entrada Inválida

1. O usuário digita uma opção inexistente no menu.
2. O sistema exibe uma mensagem de erro.
3. O sistema retorna ao menu principal.

---

## ⛔ Fluxo de Exceção

### ❌ E1 – Remoção Inexistente

* Se o usuário informar um número de tarefa que não existe:

  * O sistema exibe uma mensagem informando erro.
  * Nenhuma tarefa é removida.
  * O sistema retorna ao menu.

---

## 📦 Pré-condições

* Python instalado.
* Programa executado via terminal.

---

## ✅ Pós-condições

* As tarefas são adicionadas ou removidas apenas durante a execução do programa.
* Ao encerrar o sistema, as tarefas são perdidas (não há persistência).

---

## 💡 Observação Didática (para os alunos)

> Este caso de uso ajuda a entender como transformar uma necessidade do usuário em lógica de programação e, posteriormente, em um **prompt forte usando CTIF**.

