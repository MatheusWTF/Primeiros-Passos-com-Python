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
  return len(palavra)

def n_palindromes(palavra):
  letras = list(palavra)
  e_palindrome = True
  for letra in letras:
    if letra == letras[-1]:
      letras.pop(-1)
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