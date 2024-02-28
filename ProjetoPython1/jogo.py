import perguntas
import random

print("Bem-Vindo ao Quem quer ser um milionario!")
escolha = input("Deseja iniciar? \n 1: Sim \n 2: Não")

if(int(escolha) == 1):
    aberto = True
else:
    aberto = False

while(aberto):
    id_pergunta = random.randint(0, 1)
    print("Vamos começar!!!")
    print("--===X 1º Bloco: Fáceis X===--")
    print("1ª Pergunta - "+perguntas.banco_perguntas_facil[id_pergunta]['pergunta'])
    print(perguntas.getOpcoesFacil(id_pergunta))
    palpite = input()
    if(palpite == perguntas.banco_perguntas_facil[id_pergunta]['resposta_correta']):
        print("Parabéns, voce acertou!!")
    else:
        print("ERROUU!, tente outra vez")
        aberto = False
