contador = 1
while contador < 100000:
  contador = + 1
  print("contador: ", contador)
  if contador >= 100000:
    print("Você chegou a 100000 pontos")

Calculadora
n1 = float(input("digite o primeiro número: "))
n2 = float(input("digte o segundo número: "))
operacao = input("digite a operação(+-*/): ")
if operacao == "+" :
  resultado = n1 + n2
elif operacao == "-" :
    resultado = n1 - n2
elif operacao == "*" :
    resultado n1 * n2
elif operacao == "/" :
  resultado = n1 / n2
else print ("Erro Tente Novamente")
print(resultado)
