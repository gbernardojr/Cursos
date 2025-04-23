**como criar uma rede local de blockchain para sua criptomoeda interna usando o Ganache**. É **100% gratuito**, fácil de configurar e perfeito para testes ou uso controlado dentro da empresa.  

---

### **O que é o Ganache?**  
O [Ganache](https://trufflesuite.com/ganache/) é uma ferramenta da **Truffle Suite** que cria uma blockchain Ethereum **local** para desenvolvimento. Ele vem com:  
✅ 10 contas pré-fundeadas (com Ether fictício).  
✅ Sem taxas de transação (gas fee).  
✅ Interface gráfica ou linha de comando.  

---

## **📝 Passo a Passo: Criando sua Rede com Ganache**  

### **1. Instalação**  
Escolha uma das versões:  

#### **Opção 1: Ganache GUI (Interface Gráfica - Recomendado para iniciantes)**  
- **Download**: [https://trufflesuite.com/ganache/](https://trufflesuite.com/ganache/)  
- Disponível para Windows, macOS e Linux.  

#### **Opção 2: Ganache CLI (Linha de Comando - Para mais controle)**  
```bash
npm install -g ganache
```

---

### **2. Iniciando a Rede**  
#### **Se usou a GUI:**  
1. Abra o Ganache.  
2. Clique em **"Quickstart"** (ou crie um workspace personalizado).  
3. Pronto! A rede está rodando em `http://127.0.0.1:7545`.  

#### **Se usou a CLI:**  
```bash
ganache --port 7545
```
(A rede será iniciada no mesmo endereço.)  

🔹 **Você verá 10 contas com 100 ETH falsos cada (para testes).**  

---

### **3. Conectando o MetaMask à Rede do Ganache**  
Para interagir com sua blockchain:  
1. Abra o **MetaMask**.  
2. Clique em **"Networks"** > **"Add Network"**.  
3. Preencha os dados:  
   - **Network Name**: Ganache Local  
   - **RPC URL**: `http://127.0.0.1:7545`  
   - **Chain ID**: `1337` (padrão do Ganache)  
   - **Currency Symbol**: ETH (ou personalizado)  

4. **Importe uma conta**:  
   - No Ganache, clique no ícone 🔑 de uma conta para copiar a **private key**.  
   - No MetaMask, vá em **"Import Account"** e cole a chave.  

✅ Agora você tem ETH "fake" para deployar contratos!  

---

### **4. Criando e Deployando seu Token (ERC-20)**  
Vamos usar o **Remix IDE** (online e gratuito):  

#### **Passo 1: Acesse o Remix**  
👉 [https://remix.ethereum.org/](https://remix.ethereum.org/)  

#### **Passo 2: Crie um Novo Contrato**  
1. Na aba **"File Explorer"**, crie um arquivo `MeuToken.sol`.  
2. Cole este código **simples de token ERC-20**:  

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MeuTokenEmpresa is ERC20 {
    constructor(uint256 initialSupply) ERC20("Token Interno", "TKI") {
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }
}
```

#### **Passo 3: Compile o Contrato**  
1. Vá para a aba **"Solidity Compiler"**.  
2. Selecione a versão `0.8.0` ou superior.  
3. Clique em **"Compile MeuToken.sol"**.  

#### **Passo 4: Faça o Deploy na Rede Ganache**  
1. Vá para a aba **"Deploy & Run Transactions"**.  
2. Em **"Environment"**, selecione **"Injected Provider - MetaMask"** (conectado à rede Ganache).  
3. Em **"Contract"**, escolha `MeuTokenEmpresa`.  
4. No campo **"initialSupply"**, coloque a quantidade (ex: `1000000` para 1 milhão de tokens).  
5. Clique em **"Deploy"**.  

🔹 **Confirme a transação no MetaMask** (não custa nada, pois é uma rede local).  

---

### **5. Adicionando o Token no MetaMask**  
1. No MetaMask, vá para **"Assets"** > **"Import Tokens"**.  
2. Cole o **endereço do contrato** (disponível no Remix após o deploy).  
3. O símbolo (`TKI`) e decimais (`18`) devem aparecer automaticamente.  
4. Clique em **"Add Custom Token"**.  

✅ Pronto! Seu token interno agora aparece na carteira.  

---

## **🚀 O que Fazer Agora?**  
- **Distribua tokens** para funcionários (envie via MetaMask).  
- **Crie um sistema interno** para gerenciar transações.  
- **Teste regras** como:  
  - Congelar contas.  
  - Queimar tokens.  
  - Adicionar administradores.  

---

### **🔎 Dica Avançada: Personalize seu Token**  
Você pode adicionar funções como:  
- **Taxa em transferências** (ex: 1% vai para a empresa).  
- **Permissões** (só o dono pode mintar novos tokens).  
- **Congelar carteiras suspeitas**.  

---

## **Conclusão**  
Você criou uma **rede blockchain privada e gratuita** com Ganache, perfeita para testes ou uso interno na empresa. Se precisar evoluir para uma rede mais robusta (como uma **sidechain** ou **mainnet**), podemos explorar outras opções.  

