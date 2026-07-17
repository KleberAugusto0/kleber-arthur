def calcular_desconto(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final  = preco_original - valor_desconto
    return preco_final