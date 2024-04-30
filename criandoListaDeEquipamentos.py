# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
def cadastro_equipamento():
  equipamentos=[]
  
  for _ in range(3):
    equipamento = input()
    equipamentos.append(equipamento)
    
  return equipamentos

equipamentos  = cadastro_equipamento()
# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in equipamentos:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")