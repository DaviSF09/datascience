numeros = [1,2,3,4,5,6,7,8,9,10,11]
for i in numeros:
    if i >= 10:
        print(f"O número atual({i}) é maior que 10")
    elif i < 10:
        print(f"O número atual({i}) é menor que 10")
else:
    print("Iteração concluída")
