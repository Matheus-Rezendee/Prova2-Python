def e_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def verificar_primos(numeros):
    primos = [num for num in numeros if e_primo(num)]
    return primos

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

numeros_primos = verificar_primos(numeros)
print("Números primos:", numeros_primos)
