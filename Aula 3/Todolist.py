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
            print(f"° {tarefa}")
        print("------x------")
        print(" ")
        
    elif escolha == 3:
        
        print("Você escolheu editar uma tarefa")
        tarefa_editar = input("Digite o nome da tarefa a ser editada: ")
        nomeTarefa = tarefa_editar.lower().strip()
        encontraTarefa = False
        for tarefa in listaDeTarefa:
            if str(tarefa).lower() == nomeTarefa:
                salva_index = listaDeTarefa.index(tarefa)
                novaTarefa = input("Digite o novo nome da tarefa: ")
                listaDeTarefa.remove(tarefa)
                listaDeTarefa.insert(salva_index, novaTarefa)
                
    elif escolha == 4:
        
        print("Excluir uma tarefa")
        decisao = int(input("A tarefa a ser excluída esta concluída \n 1- Sim \n 2- Não \n"))
        if decisao == 1:
            tarefa_excluir = input("Digite o nome da tarefa a ser excluída: ")
            nomeTarefa = tarefa_excluir.lower()+"(Concluída)"
            encontraTarefa = False
            for tarefa in listaDeTarefa:
                if str(tarefa).lower().replace(" ","") == nomeTarefa.replace(" ",""):
                    listaDeTarefa.remove(tarefa)
                    print("Tarefa excluída com sucesso!")
                    encontraTarefa = True
            if not encontraTarefa:
                print("Tarefa não encontrada!")
            print("------x------")
            print(" ")
        elif decisao == 2:
            tarefa_excluir = input("Digite o nome da tarefa a ser excluída: ")
            nomeTarefa = tarefa_excluir.lower()
            encontraTarefa = False
            
            for tarefa in listaDeTarefa:
                if tarefa.lower().strip() == nomeTarefa:
                    listaDeTarefa.remove(tarefa)
                    print("Tarefa excluída com sucesso!")
                    encontraTarefa = True
            if not encontraTarefa:
                print("Tarefa não encontrada!")
            print("------x------")
            print(" ")
        else: 
            print("ERRO!1")
            print("------x------")
            print(" ")
        
    elif escolha == 5:
        
        print("Concluiu uma tarefa, agora marque ela como concluída!")
        tarefa_concluida = input("Digite o nome da tarefa: ")
        nomeTarefa = tarefa_concluida.lower()
        encontraTarefa = False
        for tarefa in listaDeTarefa:
            if tarefa.lower() == nomeTarefa:
                salva_index = listaDeTarefa.index(tarefa)
                listaDeTarefa.remove(tarefa)
                listaDeTarefa.insert(salva_index, tarefa+" (Concluída)")  
        
    elif escolha == 6:
        
        print("Você escolheu sair, Tchau!!")
        aberto = False
        
    else:
        print("Erro")
