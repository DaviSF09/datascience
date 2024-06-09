lista = []
numero = int(input("Qual o número de itens a ser adicionado na lista? "))
for i in range(numero):
    item = str(input("Digite um item a ser adicionado na lista: "))
    if item in lista:
        print("O item já está na lista")
        print(lista)
    else:
        lista.append(item)
        print(lista)