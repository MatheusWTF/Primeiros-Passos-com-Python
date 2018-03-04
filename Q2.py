# enconding: utf-8
# author: Matheus D. Rodrigues

def n_vogais(palavra):
  vogais = {"a", "e", "i", "o", "u", "á", "à", "â", "ã", "ä", "é", "è", "ê", "ë", "í", "ì", "î", "ï", "ó", "ò", "ô", "õ", "ö", "ú", "ù", "û", "ü"}
  quantidade = 0
  for letra in palavra.lower():
    if letra in vogais:
      quantidade += 1
  return quantidade

def n_digitos(palavra):
  n_digitos = 0
  numeros = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  for d in palavra:
    if d in numeros:
      n_digitos +=1
  return n_digitos

def n_palindromes(palavra):
  pali = []
  for letra in palavra:
    if letra == ' ':
      pass
    else:
      pali.append(letra)
  e_palindrome = True
  for letra in pali:
    if letra == pali[-1]:
      pali.pop(-1)
    else:
      e_palindrome = False
      break
  return e_palindrome

lista, entrada = [], input("Digite uma palavra ou Sentença: ")
vogais = 0
digitos = 0
palindromes = 0
while entrada != '':
  lista.append(entrada)
  vogais += n_vogais(entrada)
  digitos += n_digitos(entrada)
  palindromes += 1 if n_palindromes(entrada) else 0
  entrada = input("Digite uma palavra ou Sentença: ")

lista = sorted(lista, key=len, reverse=True)

print("\nQuantidade de Vogais: ",vogais)
print("Quantidade de Dígitos: ",digitos)
print("Maior Sentença/Palavra: ",lista[0])
print("Quantidade de Palíndromes: ",palindromes)