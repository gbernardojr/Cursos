# Manual de Introdução ao Git e GitHub

## 1. Introdução

### 1.1 O que é Git?
Git é um sistema de controle de versão distribuído, amplamente utilizado para rastrear mudanças no código-fonte durante o desenvolvimento de software. Ele permite que múltiplos desenvolvedores trabalhem no mesmo projeto de forma eficiente e colaborativa.

### 1.2 O que é GitHub?
GitHub é uma plataforma de hospedagem de código-fonte que usa o Git para versionamento. Ele permite que desenvolvedores armazenem seus repositórios online e colaborem com outros desenvolvedores.

## 2. Configurando o Git

### 2.1 Instalando o Git
Para instalar o Git, você pode visitar o [site oficial](https://git-scm.com/downloads) e seguir as instruções para o seu sistema operacional.

### 2.2 Configurando o Git
Após a instalação, você precisa configurar o Git com seu nome de usuário e e-mail. Estes serão usados para identificar suas mudanças nos repositórios.

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

## 3. Clonando um Repositório Remoto

Clonar um repositório significa copiar todo o seu conteúdo para a sua máquina local.

### 3.1 Obtendo a URL do Repositório
No GitHub, navegue até o repositório que deseja clonar e clique no botão verde "Code". Copie a URL fornecida.

### 3.2 Comando para Clonar
Abra seu terminal e execute o comando a seguir substituindo `URL_DO_REPOSITORIO` pela URL copiada:

```bash
git clone URL_DO_REPOSITORIO
```

Por exemplo:

```bash
git clone https://github.com/usuario/repositorio.git
```

## 4. Adicionando Novos Módulos

### 4.1 Criando Novos Arquivos
Você pode criar novos arquivos ou pastas diretamente no diretório do seu repositório local.

### 4.2 Adicionando Arquivos ao Staging Area
Para adicionar novos arquivos ou mudanças à área de preparação (staging area), use o comando:

```bash
git add NOME_DO_ARQUIVO
```

Para adicionar todos os arquivos modificados, use:

```bash
git add .
```

## 5. Fazendo o Commit

### 5.1 Criando um Commit
Um commit é uma captura das mudanças feitas no código. Para criar um commit, use o comando:

```bash
git commit -m "Mensagem do commit"
```

Certifique-se de escrever uma mensagem de commit clara e descritiva.

## 6. Atualizando o Repositório Remoto

### 6.1 Puxando Atualizações do Repositório Remoto
Antes de enviar suas mudanças, é uma boa prática puxar as atualizações do repositório remoto para evitar conflitos.

```bash
git pull origin main
```

### 6.2 Enviando Commits para o Repositório Remoto
Para enviar suas mudanças para o repositório remoto, use o comando:

```bash
git push origin main
```

Substitua `main` pelo nome do branch em que você está trabalhando, se for diferente.

## 7. Conclusão

Este manual cobre os passos básicos para começar a usar Git e GitHub. Com a prática, você se tornará mais confortável com esses comandos e poderá explorar funcionalidades mais avançadas do Git e GitHub. Boa codificação!
