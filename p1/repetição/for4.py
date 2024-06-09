frase = str(input("Insira a frase desejada: "))
vogais = "aeiouAEIOU"
contador = 0
for i in frase:
    if i in vogais:
        contador +=1
        print(f"O número de vogais na frase é {contador}")