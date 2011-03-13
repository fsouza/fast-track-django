def calcular_fatorial(n):
    if n == 0:
        return 1

    return n * calcular_fatorial(n - 1)
