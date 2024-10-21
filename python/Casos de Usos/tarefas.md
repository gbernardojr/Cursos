### Caso de Uso: **Gerenciador de Tarefas Simples**

#### Objetivo:
Desenvolver um programa em Python que funcione como um **gerenciador de tarefas** simples. O usuário poderá adicionar, listar, marcar como concluídas e excluir tarefas. 
Os dados das tarefas devem ser armazenados temporariamente em uma lista durante a execução do programa.

#### Descrição Geral:
- O programa permitirá ao usuário gerenciar uma lista de tarefas.
- Cada tarefa terá um **nome** e um **status** (concluída ou não concluída).
- O usuário pode visualizar todas as tarefas, adicionar novas, marcar uma como concluída ou excluir uma tarefa.
- Ao final do programa, todas as informações sobre as tarefas serão perdidas, pois não há banco de dados ou arquivo de armazenamento permanente.

#### Funcionalidades:
1. **Adicionar Tarefa**: O usuário pode adicionar uma nova tarefa.
2. **Listar Tarefas**: O usuário pode visualizar a lista de tarefas com o status (concluída ou não).
3. **Marcar Tarefa como Concluída**: O usuário pode marcar uma tarefa como concluída.
4. **Excluir Tarefa**: O usuário pode excluir uma tarefa da lista.
5. **Sair**: O usuário pode encerrar o programa.

#### Fluxo Principal:
   - Se escolher "Adicionar Tarefa", o programa solicita o nome da nova tarefa.
   - Se escolher "Listar Tarefas", o programa exibe todas as tarefas com seu status.
   - Se escolher "Marcar Tarefa como Concluída", o programa solicita o número da tarefa a ser marcada.
   - Se escolher "Excluir Tarefa", o programa solicita o número da tarefa a ser removida.


### Possíveis Expansões:
- Permitir salvar as tarefas em um arquivo de texto ou JSON para persistência de dados.
- Adicionar a funcionalidade de editar o nome de uma tarefa.
- Criar um sistema de prioridades para as tarefas.
- Adicionar prazos ou categorias às tarefas.
