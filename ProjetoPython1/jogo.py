import perguntas
import random

print("Bem-Vindo ao Quem quer ser um milionario!")
escolha = input("Deseja iniciar? \n 1: Sim \n 2: Não")

if int(escolha) == 1:
    aberto = True
else:
    aberto = False

while aberto:
    id_pergunta = random.randint(-1, 7)
    print("Vamos começar!!!")
    print("--===X 1º Bloco: Fáceis X===--")
    primeira = perguntas.getPerguntaFacil(int(id_pergunta))
    print(f"1ª Pergunta - {primeira}")
    print(perguntas.getOpcoesFacil(int(id_pergunta)))
    palpite = input("")
    if palpite == perguntas.getRespostaFacil(int(id_pergunta)):
        print("Parabéns, voce acertou!!")
    else:
        print("ERROUU!, tente outra vez")
        aberto = False

    id_pergunta2 = random.randint(-1, 7)
    while id_pergunta2 == id_pergunta:
        id_pergunta2 = random.randint(-1, 7)

    print(f"2ª Pergunta - {perguntas.getPerguntaFacil(int(id_pergunta2))}")
    print(perguntas.getOpcoesFacil(int(id_pergunta2)))
    palpite = input("")
    if palpite == perguntas.getRespostaFacil(int(id_pergunta2)):
        print("Parabéns, você acertou!!")
    else:
        print("ERROUU!, tente outra vez!")
        aberto = False

    id_pergunta3 = random.randint(-1, 7)
    while id_pergunta3 == id_pergunta or id_pergunta3 == id_pergunta2:
        id_pergunta3 = random.randint(-1, 7)

    print(f"3ª Pergunta - {perguntas.getPerguntaFacil(int(id_pergunta3))}")
    print(perguntas.getOpcoesFacil(int(id_pergunta3)))
    palpite = input("")
    if palpite == perguntas.getRespostaFacil(int(id_pergunta3)):
        print("Parabéns, você acertou!!")
    else:
        print("ERROUU!, tente outra vez!")
        aberto = False

    id_pergunta4 = random.randint(-1, 7)
    while (
        id_pergunta4 == id_pergunta
        or id_pergunta4 == id_pergunta2
        or id_pergunta4 == id_pergunta3
    ):
        id_pergunta4 = random.randint(-1, 7)

    print(f"4ª Pergunta - {perguntas.getPerguntaFacil(int(id_pergunta4))}")
    print(perguntas.getOpcoesFacil(int(id_pergunta4)))
    palpite = input("")
    if palpite == perguntas.getRespostaFacil(int(id_pergunta4)):
        print("Parabéns, você acertou!!")
    else:
        print("ERROUU!, tente outra vez!")
        aberto = False

    id_pergunta5 = random.randint(-1, 7)
    while (
        id_pergunta5 == id_pergunta
        or id_pergunta5 == id_pergunta2
        or id_pergunta5 == id_pergunta3
        or id_pergunta5 == id_pergunta4
    ):
        id_pergunta5 = random.randint(-1, 7)

    print(f"5ª Pergunta - {perguntas.getPerguntaFacil(int(id_pergunta5))}")
    print(perguntas.getOpcoesFacil(int(id_pergunta5)))
    palpite = input("")
    if palpite == perguntas.getRespostaFacil(int(id_pergunta5)):
        print("Parabéns, você acertou!!")
    else:
        print("ERROUU!, tente outra vez!")
        aberto = False
    
    print("===============X=============")
    print(
        "Parabéns você concluiu o 1º Bloco, ganhando 1.000 reais. Agora você deve escolher parar e sair com esse dinheiro ou ficar e ter chance de ganhar 1 milhão"
    )
    escolha = input("1: Sair com 1000 reais \n 2: Continuar \n")
    if escolha == 2:
        print("Ok, você escolheu continuar então prosseguimos")
        print("--===X 2º Bloco: Médias X===--")
        print(f"1ª Pergunta - {perguntas.getPerguntaMedia(int(id_pergunta))}")
        print(perguntas.getOpcoesMedia(int(id_pergunta)))
        palpite = input("")
        if palpite == perguntas.getRespostaMedia(int(id_pergunta)):
            print("Parabéns, voce acertou!!")
        else:
            print("ERROUU!, tente outra vez")
            aberto = False
        
        print(f"2ª Pergunta - {perguntas.getPerguntaMedia(int(id_pergunta2))}")
        print(perguntas.getOpcoesMedia(int(id_pergunta2)))
        palpite = input("")
        if palpite == perguntas.getRespostaMedia(int(id_pergunta2)):
            print("Parabéns, você acertou!!")
        else:
            print("ERROUU!, tente outra vez!")
            aberto = False

        print(f"3ª Pergunta - {perguntas.getPerguntaMedia(int(id_pergunta3))}")
        print(perguntas.getOpcoesMedia(int(id_pergunta3)))
        palpite = input("")
        if palpite == perguntas.getRespostaMedia(int(id_pergunta3)):
            print("Parabéns, você acertou!!")
        else:
            print("ERROUU!, tente outra vez!")
            aberto = False

        print(f"4ª Pergunta - {perguntas.getPerguntaMedia(int(id_pergunta4))}")
        print(perguntas.getOpcoesMedia(int(id_pergunta4)))
        palpite = input("")
        if palpite == perguntas.getRespostaMedia(int(id_pergunta4)):
            print("Parabéns, você acertou!!")
        else:
            print("ERROUU!, tente outra vez!")
            aberto = False

        print(f"5ª Pergunta - {perguntas.getPerguntaMedia(int(id_pergunta5))}")
        print(perguntas.getOpcoesMedia(int(id_pergunta5)))
        palpite = input("")
        if palpite == perguntas.getRespostaMedia(int(id_pergunta5)):
            print("Parabéns, você acertou!!")
        else:
            print("ERROUU!, tente outra vez!")
            aberto = False

        print("===============X=============")
