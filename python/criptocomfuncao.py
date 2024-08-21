def criptografa(palavraAlvo):
    palavraCripto = ""
    for letra in palavraAlvo:
        numeroDaLetra = ord(letra)
        numeroDaLetra = numeroDaLetra + 1
        letraCodificada = chr(numeroDaLetra)
        palavraCripto = palavraCripto + letraCodificada
    return palavraCripto
    
palavra1 = input("Digite uma palavra para criptografar: ")
print(f"Palavra criptografada:{criptografa(palavra1)}")

palavra2 = input("Digite uma palavra para criptografar: ")
print(f"Palavra criptografada:{criptografa(palavra2)}")

senha    = input("Digite uma senha   para criptografar: ")
print(f"Palavra criptografada:{criptografa(senha)}")
