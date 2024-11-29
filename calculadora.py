def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    else:
        return x / y

def menu():
    print("Calculadora")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "5":
            print("Tchau!")
            break
        elif escolha in ("1", "2", "3", "4"):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if escolha == "1":
                print(f"{num1} + {num2} = {soma(num1, num2)}")
            elif escolha == "2":
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")
            elif escolha == "3":
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
            elif escolha == "4":
                print(f"{num1} / {num2} = {divisao(num1, num2)}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()