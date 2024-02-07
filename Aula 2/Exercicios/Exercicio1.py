print("Digite o valor de a e b, para que as operações sejam feitas.")
a = input("Valor de A:")
b = input("Valor de B:")

soma = int(a) + int(b)
print("A soma de a e b é : "+str(soma))
print("---------------x----------------")
subtracao = int(a) - int(b)
print("A subtração de a e b é : "+str(subtracao))
print("---------------x----------------")
multiplicacao = int(a) * int(b)
print("A multiplicacao de a e b é : "+str(multiplicacao))
print("---------------x----------------")

if int(b) == 0:
    print("Não é possivel dividir um número por 0")
else:
    divisao = int(a) / int(b)
    print("A divisao de a e b é : "+str(divisao))
print("---------------x----------------")
if int(b) == 0:
    print("Não é possivel dividir um número por 0")
else:
    divisao_inteira = int(a) // int(b)
    print("A divisao inteira de a e b é : "+str(divisao_inteira))
print("---------------x----------------")
if int(b) == 0:
    print("Não é possivel dividir um número por zero")
else:
    resto = int(a) % int(b)
    print("O resto da divisao de a e b é : "+str(resto))
print("---------------x----------------")
potencia = int(a)**int(b)
print("A potenciação de a elevado a b é : "+str(potencia))
print("---------------x----------------")
areaCirculo = (int(a)**2)*3.14
print("Considerando 'a' como uma medida do raio de uma circunferência, a área da mesma seria: "+str(areaCirculo))