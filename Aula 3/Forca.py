import random

jogo_aberto = True

listaAnimais = ["cachorro"]
listaObjetos = ["abajur", "computador"]
listaCores = ["vermelho"]

while(jogo_aberto):
    print("JOGO DA FORCA, descubra a palavra com até 7 tentativas!!!")
    escolha = int(input("Escolha qual categoria? \n 1- Animais \n 2- Objetos \n 3- Cores"))
    
    if escolha == 1:
        
        randomizador = random.choice(listaAnimais)
        palavraSelecionada = randomizador.split()
        printPalavra = list('_'*len(palavraSelecionada))
        chances = 0
        while chances <= 7:
            letraDigitada = input("Digite uma letra: ").upper()
            if 
    elif escolha == 2:
        randomizador = random.choice(listaObjetos)
    elif escolha == 3:
        randomizador = random.choice(listaCores)
    
        
    