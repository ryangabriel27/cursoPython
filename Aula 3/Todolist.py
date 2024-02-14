print("---x TODOLIST x---")

aberto = True

listaDeTarefa = []

while aberto:
    
    escolha = int(
        input(
            "Bem-vindo!! O que deseja fazer?\n 1- Adicionar uma nova tarefa \n 2- Ver a lista de tarefas \n 3- Editar uma tarefa \n 4- Excluir uma tarefa \n 5- Marcar uma tarefa como concluída \n 6- Sair \n "
        )
    )
    print(escolha)
    
    if escolha == 1:
        
        print("Você escolheu adicionar uma tarefa!")
        tarefaAdiconada = input("Digite o nome da tarefa a ser adicionada: ")
        listaDeTarefa.append(str(tarefaAdiconada))
        print("Tarefa adicionada com sucesso!!")
        print("------x------")
        print(" ")
        
    elif escolha == 2:
        
        print("Você escolheu ver a lista de tarefas!")
        print("--== Lista ==--")
        for tarefa in listaDeTarefa:
            print(f"{listaDeTarefa.index(tarefa)+1}. {tarefa}")
        print("------x------")
        print(" ")
        
    elif escolha == 3:
        print("Você escolheu editar uma tarefa")
        tarefa_editar = int(input("Digite o número da tarefa a ser editada: "))
        if tarefa_editar >= 0:
            for tarefa in listaDeTarefa:
                if tarefa == listaDeTarefa[tarefa_editar - 1]:
                    novoNome = input("Digite o novo nome da tarefa")
                    del listaDeTarefa[tarefa_editar - 1]
                    listaDeTarefa.insert((tarefa_editar-1), novoNome)
                
                
    elif escolha == 4:
        
        print("Excluir uma tarefa")
        tarefa_excluir = int(input("Digite o número da tarefa a ser excluída: "))
        encontraTarefa = False
        if tarefa_excluir >= 0:
            del listaDeTarefa[tarefa_excluir - 1]
            print("Tarefa excluída com sucesso!")
            encontraTarefa = True
        if not encontraTarefa:
            print("Tarefa não encontrada!")
            print("------x------")
            print(" ")
    elif escolha == 5:
        
        print("Concluiu uma tarefa, agora marque ela como concluída!")
        tarefa_concluida = int(input("Digite o número da tarefa: "))
        encontraTarefa = False
        if tarefa_concluida >= 0:
            for tarefa in listaDeTarefa:
                if tarefa == listaDeTarefa[tarefa_concluida - 1]:
                    listaDeTarefa.remove(tarefa)
                    listaDeTarefa.insert((tarefa_concluida - 1), tarefa+" (Concluída)")
            encontraTarefa = True  
        if not encontraTarefa:
            print("Tarefa não encontrada!")
            print("------x------")
            print(" ")
        
    elif escolha == 6:
        
        print("Você escolheu sair, Tchau!!")
        aberto = False
        
    else:
        print("Erro")
