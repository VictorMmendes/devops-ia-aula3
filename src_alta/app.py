def somar(a, b):
    return a + b


def dividir(a, b):
    if b == 0:
        raise ValueError("Nao e possivel dividir por zero")

    return a / b
