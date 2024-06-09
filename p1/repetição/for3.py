dic = {"Hinata": 10, "Kageyama": 9, "Tsukki": 11}
num = int(input("Digite o numero de jogadores a serem adicionados: "))
for i in range(num):
    jogador = str(input("Nome do jogador: "))
    if jogador in dic:
        print("O jogador já está no dicionario")
        print(dic)
    else:
        numero = int(input("Número do jogador: "))
        dic[f"{jogador}"] = numero
        print(dic)