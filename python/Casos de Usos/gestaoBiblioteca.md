Aqui está o caso de uso para o sistema de gerenciamento de livros da biblioteca. Esse caso de uso descreve o objetivo principal, os atores envolvidos, o fluxo de ações e o comportamento esperado das funções do sistema.

---

### Caso de Uso: Gerenciamento de Livros da Biblioteca

#### 1. **Objetivo**
   Permitir que os usuários realizem operações básicas de gerenciamento de livros em uma biblioteca, incluindo a adição, consulta, atualização, remoção e listagem de livros. O sistema facilita o controle dos livros disponíveis, bem como a manutenção dos dados de cada livro.

#### 2. **Ator**
   - **Bibliotecário**: Usuário que opera o sistema para gerenciar os livros da biblioteca.

#### 3. **Pré-condições**
   - O sistema deve estar ativo e acessível ao bibliotecário.
   - Cada livro possui um código único para identificação, juntamente com informações sobre o título, autor e ano de publicação.

#### 4. **Cenário Principal (Fluxo de Eventos)**

   ##### Ações Primárias do Sistema:
   
   1. **Adicionar Livro**
      - O bibliotecário fornece o `código`, `título`, `autor` e `ano` de publicação do livro.
      - O sistema armazena o livro no "banco de dados" dicionário.
      - **Resultado**: Uma mensagem de confirmação indica que o livro foi adicionado com sucesso.
   
   2. **Buscar Livro**
      - O bibliotecário fornece o `código` do livro que deseja consultar.
      - O sistema verifica se o livro existe no banco de dados.
      - **Se o livro for encontrado**: Exibe as informações do livro (título, autor e ano).
      - **Se o livro não for encontrado**: Exibe uma mensagem informando que o livro não está cadastrado.

   3. **Atualizar Livro**
      - O bibliotecário fornece o `código` do livro e as informações que deseja atualizar (título, autor ou ano).
      - O sistema verifica se o livro existe no banco de dados.
      - **Se o livro for encontrado**: Atualiza os campos fornecidos com os novos dados.
      - **Se o livro não for encontrado**: Exibe uma mensagem informando que o livro não está cadastrado.
      - **Resultado**: O sistema confirma a atualização bem-sucedida do livro.

   4. **Remover Livro**
      - O bibliotecário fornece o `código` do livro que deseja remover.
      - O sistema verifica se o livro existe no banco de dados.
      - **Se o livro for encontrado**: O sistema remove o livro do banco de dados.
      - **Se o livro não for encontrado**: Exibe uma mensagem informando que o livro não está cadastrado.
      - **Resultado**: O sistema confirma que o livro foi removido.

   5. **Listar Todos os Livros**
      - O bibliotecário solicita a listagem de todos os livros.
      - O sistema recupera todos os registros no banco de dados.
      - **Se houver livros cadastrados**: Exibe a lista completa com código, título, autor e ano de cada livro.
      - **Se não houver livros cadastrados**: Informa que a biblioteca está vazia.

#### 5. **Fluxo Alternativo**
   - **Falha ao Adicionar Livro**: Se o bibliotecário tentar adicionar um livro com um `código` que já existe, o sistema deve exibir uma mensagem de erro informando que o código do livro é duplicado e não pode ser adicionado.
   - **Livro Não Encontrado em Busca, Atualização ou Remoção**: Se o código fornecido não corresponder a nenhum livro cadastrado, o sistema exibe uma mensagem informando que o livro não está registrado.

#### 6. **Pós-condições**
   - Os dados dos livros devem estar sempre consistentes no banco de dados. Toda modificação (adição, atualização ou remoção) realizada pelo bibliotecário deve refletir corretamente na biblioteca.
   - O bibliotecário é notificado sobre o sucesso ou falha de cada operação solicitada.

#### 7. **Exemplo de Operação**

   - **Situação**: Um bibliotecário precisa adicionar um novo livro, consultar um livro existente, atualizar o ano de publicação de um livro e listar todos os livros cadastrados.
   - **Ações**:
     1. Adiciona o livro "Dom Quixote" com código "001".
     2. Consulta o livro com código "001" e verifica as informações.
     3. Atualiza o ano de publicação do livro "Dom Quixote" para 1615.
     4. Lista todos os livros, visualizando o livro atualizado.
   - **Resultado Esperado**: Cada operação é realizada com sucesso e o sistema exibe as informações atualizadas.

---

Esse caso de uso é simples, mas cobre as operações básicas de um sistema de gerenciamento de livros, tornando-o ideal para alunos compreenderem como um dicionário pode ser utilizado para simular um banco de dados básico em Python.
