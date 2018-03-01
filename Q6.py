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

n, b = int(input("Digite o número: ")), int(input("Digite a base: "))
while n > 0 or 2 < b < 9:
  print(converte(n, b))
  n, b = int(input("Digite o número: ")), int(input("Digite a base: "))