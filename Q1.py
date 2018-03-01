# enconding: utf-8
# author: Matheus D. Rodrigues

n, entrada = int(input("Digite um Número: ")), []
while n >= 0:
  if len(entrada) > 5:
    menor = min(entrada)
    if menor < n:
      position = entrada.index(menor)
      del entrada[position]
    else:
      pass
  entrada.append(n)
  n = int(input("Digite um Número: "))

entrada.sort(reverse=True)

for i in range(0,5):                      
  print(entrada[i])