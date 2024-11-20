consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (Residencial ?, Comercio ? ou Industril ?): ")
if tipo == "Residencial":
    if consumo <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo == "Comercio":
    if consumo <= 5000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "Industril":
    if consumo <= 1000:
        preço = 0.55
    else:
        preço = 0.60
else:
    preço = 0
    print("Erro ! Tipo de instalação desconhecido!")
custo = consumo * preço
print(f"Valor a pagar: R$ {custo:7.2f}")