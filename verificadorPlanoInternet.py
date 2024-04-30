def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

# Exemplos de entrada e saída
exemplos = [10, 19, 21]
for consumo in exemplos:
    print("Entrada:", consumo)
    print("Saída:", recomendar_plano(consumo))
    print()
