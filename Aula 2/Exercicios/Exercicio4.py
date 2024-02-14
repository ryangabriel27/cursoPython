tem_sol = False
tem_chuva = False

if tem_sol and not tem_chuva:
    dia_ensolarado = True
    print("O dia está ensolarado!")
if tem_chuva and not tem_sol:
    dia_chuvoso = True
    print("O dia está chuvoso")
if not tem_chuva and not tem_sol:
    print("O dia está nublado")
    dia_nublado = True
print("---------------x----------------")
print("---x VERIFICAR SE O NÚMERO É PAR OU NÃO x---")

numeroDigitado = input("Digite um número")

if int(numeroDigitado)%2 == 0:
    print("É um número par")
else:
    print("É um numero ímpar")
print("---------------x----------------")

print("---x LAÇO DE REPETIÇÃO x---")
numeros = [3,15,19,21,30,47,69]

for numero in numeros:
    if numero%2 == 1 & numero%3 ==0:
        print(str(numero)+" - É um número ímpar e múltiplo de 3")
print("---------------x----------------")

print("---x VERIFICA IDADE x---")

idade_usuario = input("Digite sua idade: ")

if 18 <= idade_usuario <= 65:
    print("Sua idade está dentro do intervalo de 18 a 65 anos")

