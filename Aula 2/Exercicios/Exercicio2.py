nome = input("Digite o seu primeiro nome:")
sobrenome = input("Digite o seu sobrenome:")

nome_completo = nome + sobrenome

print("Seu nome completo: "+nome_completo)
print("---------------x----------------")

frase = input("Digite uma frase:")

fraseMinuscula = frase.lower()
fraseMaiuscula = frase.upper()
listaFrase = frase.split() # Criando uma lista de palavras de frase
trocarPalavra = frase.replace(listaFrase[0], "Python") # Trocando a primeira palavra da frase por python

print("Sua frase com todas as letras maiusculas: "+fraseMaiuscula)
print("---------------x----------------")
print("Sua frase com todas as letras minusculas: "+fraseMinuscula)
print("---------------x----------------")
print("Trocando a primeira palavra da frase por python: "+trocarPalavra)
