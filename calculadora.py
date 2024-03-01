n = float(input("Digite o número 1:"))
m = float(input("Digite o número 2:"))
op = input("Digite a operação:")
if op == "+":
  print(n+m)
elif op == "-":
  print(n-m)
elif op == "*":
  print(n*m)
elif op == "/":
  if m == 0:
    print("erro, não é possível dividir por 0")
  else:
    print(n/m)
else:
  print("Tente novamente, operação inválida")