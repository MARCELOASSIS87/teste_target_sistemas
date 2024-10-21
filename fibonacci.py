def sequencia_fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Solicita o número ao usuário
num = int(input("Digite um número: "))

# Gera a sequência de Fibonacci até o número fornecido
fib_sequence = fibonacci_sequence(num)

# Verifica se o número pertence à sequência de Fibonacci
if num in fib_sequence:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")