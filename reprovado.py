from conta import calcular
from CalcularDesconto import calcular_desconto

while True:

	print("Olá, tudo bem com você amiguinho? Aqui tem duas funções e você deve escolher uma delas:")
	print("1 - Kleber")
	print("2 - Arthur")
	print("3 - Sair")

	while True:
		try:
			opcao = int(input("Digite o nome de quem você quer escolher: "))
			break
		except ValueError:
			print("Por favor, digite apenas números.")
			continue

	if opcao==1:
		calcular()

	elif opcao==2:
		while True:
			try:
				preco=float(input("Digite o preço original do produto: "))
				break
			except ValueError:
				print("Por favor, digite apenas números.")
				continue
		while True:
			try:
				desconto=float(input("Digite o percentual de desconto: "))
				break
			except ValueError:
				print("Por favor, digite apenas números.")
				continue

		resultado=calcular_desconto(preco, desconto)
		print(f"O preço final do produto com desconto é: R${resultado:.2f}")

	elif opcao==3:
		break
