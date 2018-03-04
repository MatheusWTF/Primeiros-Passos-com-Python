# encoding: utf-8
# author: Matheus D. Rodrigues

def converte(decimal, base):
  digitos = [decimal % base]
  while decimal // base != 0:
    decimal //= base
    digitos.append(decimal % base)
  digitos.reverse()
  convertido = ""
  for n in digitos:
    convertido += str(n)
  return convertido

lista, n, b = [], int(input("Digite o número: ")), int(input("Digite a base: "))
while n > 0 and b < 9 and b > 2:
  valor = [n, b]
  lista.append(valor)
  n, b = int(input("Digite o número: ")), int(input("Digite a base: "))

for valor in lista:
  print(converte(valor[0], valor[1]))