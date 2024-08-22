print("Jogo da Forca")
print("Desenvolvido por: Gilberto Ap Bernardo Junior")
print("Copywrite 2024")
print("versão Beta")

palavraSecreta = input("Digite a palava secreta: ")

linha = ""
for i in range(len(palavraSecreta)):
    linha = linha + "__ "
    
print(linha)

totalErros   = 0
totalAcertos = 0

print("\nPontuação")
print(f"- Total de Erros  : {totalErros}")
print(f"- Total de Acertos: {totalAcertos}")

letrasCertas = ""
letrasErradas = ""

while True:
    letra = input("Digite uma letra: ")

    if letra in palavraSecreta:
        totalAcertos = totalAcertos + 1
        letrasCertas = letrasCertas + letra
        linha = " "
        for i in range(len(palavraSecreta)):
            if palavraSecreta[i] in letrasCertas:
                linha = linha + palavraSecreta[i] + " "
            else:
                linha = linha + "__ "
        print(linha)
        linha = ' '                            
    else:
        totalErros = totalErros + 1
        letrasErradas = letrasErradas + letra
        print("A resposta está ??? Erradaaaa!! ")
        
    print("\nPontuação")
    print(f"- Total de Erros  : {totalErros}")
    print(f"- Letras erradas: {letrasErradas}")
    print(f"- Total de Acertos: {totalAcertos}")
    print(f"- Letras certas: {letrasCertas}")
    print("\n")
    
    if totalAcertos == len(palavraSecreta):
        print("Você ganhou!!!")
        break
    if totalErros == 6:
        print("Você perdeu!!!")
        break
        

