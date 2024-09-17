saldo = 0  # Variável global para o saldo da conta

def depositar(quantia):
    global saldo
    if quantia <= 0:
        raise ValueError("A quantia de depósito deve ser positiva.")
    saldo += quantia

def sacar(quantia):
    global saldo
    if quantia > saldo:
        raise ValueError("Saldo insuficiente.")
    saldo -= quantia

def verificar_saldo():
    return saldo
