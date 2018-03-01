# encoding: utf-8
# author: Matheus D. Rodrigues

entrada, lista = input("Definição de Pleito: "), []
while entrada != "":
  if len(lista) < 9:
    candidato = {"nome": entrada, "votos": 0}
    lista.append(candidato)
    entrada = input()
  else:
    break

lista_candidatos = []
for candidatos in lista:
  c = candidato["nome"]
  lista_candidatos.append(c)

voto = input("Votação: ")
while voto in c:
  for candidato in lista:
    if voto == candidato["nome"]:
      candidato["votos"] += 1
    
  voto = input()

print("\n")
for candidato in lista:
  print(candidato["nome"], " com ", candidato["votos"], " voto(s)")