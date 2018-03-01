# encoding: utf-8
# author: Matheus D. Rodrigues

import math

lista_tuplas = []
distancias = []

def criar_tuplas(x, y):
  coord = (x, y)
  lista_tuplas.append(coord)

def distancia_pontos():
  for i in lista_tuplas:
    for j in lista_tuplas:
      if i == j or j < i:
        pass
      else:
        dx = i[0] - j[0]
        dy = i[1] - j[1]
        dist = math.sqrt((dx**2) + (dy**2))
        result = {"dist": dist, "primeiro_ponto": i, "segundo_ponto": j}
        distancias.append(result)

def print_lista():
  print(len(lista_tuplas))
  for n in lista_tuplas:
    print(n)

def maior_menor():
  maior_dist = 0
  menor_dist = math.inf
  maior_dist_position = ""
  menor_dist_position = ""
  for valor in distancias:
    if valor["dist"] > maior_dist:
      maior_dist = valor["dist"]
      maior_dist_position = valor["primeiro_ponto"], valor["segundo_ponto"]
    if valor["dist"] < menor_dist:
      menor_dist = valor["dist"]
      menor_dist_position = valor["primeiro_ponto"], valor["segundo_ponto"]
  print("A maior distância entre os pontos é entre:", maior_dist_position)
  print("A menor distância entre os pontos é entre:", menor_dist_position)

def media_coord():
  x_total = 0
  y_total = 0
  for each in lista_tuplas:
    x_total += each[0]
    y_total += each[1]
  print("Ponto Médio: (", (x_total//len(lista_tuplas)), ",", (y_total//len(lista_tuplas)), ")")

x_input, y_input = int(input("Insira um número (x):")), int(input("Insira um número (y):"))
while x_input > 0 and y_input > 0 and x_input != "" and y_input != "":
  criar_tuplas(x_input, y_input)
  x_input, y_input = int(input("Insira um número (x):")), int(input("Insira um número (y):"))

distancia_pontos()
print_lista()
maior_menor()
media_coord()