while True:
    numero_1 = input("Digite um número: ") 
    numero_2 = input("Digite outro número: ") 
    operador = input("Digite o operador (+ - / *): ")

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
    except ValueError: 
        print("Um ou ambos os números não são válidos.")
        continue

    if len(operador) != 1: 
        print("Digite apenas um operador.")
        continue

    operadores_permitidos = ('+', '-', '/', '*')

    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    if operador == '+':
        resultado = numero_1_float + numero_2_float
    elif operador == '-':
        resultado = numero_1_float - numero_2_float
    elif operador == '*':
        resultado = numero_1_float * numero_2_float
    elif operador == '/':
        if numero_2_float == 0:
            print("Divisão por zero não é permitida.")
            continue
        resultado = numero_1_float / numero_2_float

    print(f"O resultado é: {resultado}")

    sair = input("Quer sair? [s]im: ").strip().lower()
    if sair.startswith("s"):
        break
