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
