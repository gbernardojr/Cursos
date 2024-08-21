palavra1 = input("Digite uma palavra para criptografar: ")
palavracripto = ""
for letra in palavra1:
    numeroDaLetra = ord(letra)
    numeroDaLetra = numeroDaLetra + 1
    letraCodificada = chr(numeroDaLetra)
    palavraCripto = palavraCripto + letraCodificada
print(f"Palavra criptografada:{palavraCripto}")

palavra2 = input("Digite uma palavra para criptografar: ")
palavracripto = ""
for letra in palavra2:
    numeroDaLetra = ord(letra)
    numeroDaLetra = numeroDaLetra + 1
    letraCodificada = chr(numeroDaLetra)
    palavraCripto = palavraCripto + letraCodificada
print(f"Palavra criptografada:{palavraCripto}")

senha    = input("Digite uma senha   para criptografar: ")
palavracripto = ""
for letra in senha:
    numeroDaLetra = ord(letra)
    numeroDaLetra = numeroDaLetra + 1
    letraCodificada = chr(numeroDaLetra)
    palavraCripto = palavraCripto + letraCodificada
print(f"Palavra criptografada:{palavraCripto}")
