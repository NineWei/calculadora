# Menu

from operacoes import *

while True:
    op = int(input("Digite a escolha de 1 a 4: "))
    if op == 1:
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
        resultado = somar(n1, n2)
        print(f"O resultado é {resultado}")
    elif op == 2:
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
        resultado = subtrair(n1, n2)
        print(f"O resultado é {resultado}")   
    elif op == 3:
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
        resultado = dividir(n1, n2)
        print(f"O resultado é {resultado:.0f}")
    elif op == 4:
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
        resultado = multiplicar(n1, n2)
        print(f"O resultado é {resultado}")



