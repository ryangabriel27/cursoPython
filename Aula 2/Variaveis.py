# Operações com variaveis:
salario = 3000
bonus = 500

salario_total = salario + bonus
print(salario_total)

# Atribuição de Valores:

numero = 42
palavra = " Python"


# Manipulação de Strings:

nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)

# Atualização de Variáveis:

contador = 0
contador = contador + 1
print(contador)

# Variáveis em Estruturas de Controle:

idade = 18
if idade >= 18:
    pode_votar = True
else:
    pode_votar = False

print(pode_votar)

# Fortemente Tipada:
numero = 42
texto = "Python"
# resultado = numero + texto.  Isso resultará em um TypeError
print(str(numero)+" - "+texto)
