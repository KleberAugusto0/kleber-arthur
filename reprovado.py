print("Reprovado")

while True:
	try:
		numero1=int(input("Digite o primeiro número: "))
		numero2=int(input("Digite o segundo número: "))
		break
	except Exception:
		print("Por favor, digite apenas números inteiros.")
		continue

while True:
	try:
		operacao=input("Digite a operação desejada (+, -, *, /): ")
		if operacao not in ["+", "-", "*", "/"]:
			raise ValueError("Operação inválida. Digite apenas +, -, * ou /.")
		break
	except ValueError as e:
		print(e)
		continue

if operacao == "+":
	resultado = numero1 + numero2

	print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")
	
elif operacao == "-":
	resultado = numero1 - numero2

	print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")

elif operacao == "*":
	resultado = numero1 * numero2

	print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")


elif operacao == "/":
	resultado = numero1 / numero2

	print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")