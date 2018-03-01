# encoding: utf-8
# author: Matheus D. Rodrigues

import random

def criar_matrix(x, y, min, max):
  matrix = []
  linha = []
  while len(matrix) != x:
    n = random.uniform(min, max)
    linha.append(n)

    if len(linha) == y:
      matrix.append(linha)
      linha = []
  return matrix

x, y, intervalo_init, intervalo_end = int(input("Quantidade de Linhas: ")), int(input("Quantidade de Colunas: ")), float(input("Valor Mínimo: ")), float(input("Valor Máximo: "))

matriz = criar_matrix(x, y, intervalo_init, intervalo_end)

maior_valor = 0
maior_valor_linha = 0
maior_valor_coluna = 0

maior_intervalo = 0
linha_intervalo = 0

produto_maiores = []
soma_menores = []

print("\n", "Matriz")
for linha in matriz:
  print(linha)

  maior = max(linha)
  menor = min(linha)

  if maior > maior_valor:
    maior_valor = maior
    maior_valor_linha = matriz.index(linha) + 1
    maior_valor_coluna = linha.index(maior) + 1
  
  intervalo = maior - menor

  if intervalo > maior_intervalo:
    maior_intervalo = intervalo
    linha_intervalo = matriz.index(linha) + 1
  
  maiores = []
  maior1 = max(linha)
  maiores.append(maior1)
  linha.pop(linha.index(maior1))
  maior2 = max(linha)
  maiores.append(maior2)
  produto = 1
  for n in maiores:
    produto *= n
  produto_maiores.append(produto)

  menores = []
  menor1 = min(linha)
  menores.append(menor1)
  linha.pop(linha.index(menor1))
  menor2 = min(linha)
  menores.append(menor2)
  soma = 0
  for n in menores:
    soma  += n
  soma_menores.append(soma)

print("\n", "Maior Valor", "\n", maior_valor, "-> Linha:", maior_valor_linha, ", Coluna:", maior_valor_coluna)

print( "Produto dos maiores valores de Cada Linha")
for n in produto_maiores:
  print(n)

print("Soma dos menores valores de Cada Linha")
for n in soma_menores:
  print(n)

print("Linha de maior intervalo entre maior e menor valor é:", linha_intervalo)