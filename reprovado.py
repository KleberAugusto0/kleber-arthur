
from conta import calcular
from CalcularDesconto import calcular_desconto

while True:
    print("\nOlá, tudo bem coleguinhas!")
    print("Se você quiser a função feita pelo Arthur escolha a opção 1.")
    print("Se você quiser a função feita pelo Kleber escolha a opção 2.")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        preco = float(input("Digite o preço original: "))
        desconto = float(input("Digite o percentual de desconto: "))

        resultado = calcular_desconto(preco, desconto)
        print(f"Preço com desconto: R$ {resultado:.2f}")

    elif opcao == 2:
        calcular()

    elif opcao == 0:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")

    voltar = input("\nDeseja voltar ao menu? (s/n): ").lower()

    if voltar != "s":
        print("Programa encerrado!")
        break