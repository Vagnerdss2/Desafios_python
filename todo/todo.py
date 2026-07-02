'''
Gerenciador de Lista de Tarefas (To-Do List): Um aplicativo de linha de comando onde o usuário pode adicionar,
 listar, marcar como concluída e remover tarefas de uma lista.
'''
import time

contador = 1
tarefas = {}

while True:
    opcao = int(input("Oque deseja fazer: \n"
                      "1 - Adicionar tarefa\n"
                      "2 - Visualizar tarefa\n"
                      "3 - Remover tarefa\n"
                      "4 - Concluir tarefa\n"
                      "5 - Sair\n"))
    print("=" * 15)
    if opcao == 1:
        tarefas[contador] = {"tarefa":input("Digite a tarefa: "),"concluido": False}
        contador += 1
        print("Tarefa adicionada com sucesso!")
        print("=" * 15)
    elif opcao == 2:
        for item in tarefas:
            if not tarefas[item]["concluido"]:
                print(f'Tarefa {item}: {tarefas[item]["tarefa"]}')
        print("=" * 15)

    elif opcao == 3:
        tarefa_id = int(input("Digite o id do tarefa que deseja deletar: "))
        if tarefa_id in tarefas:
        # del tarefas[int(input("Digite o numero da tarefa pra deletar: "))]
            del tarefas[tarefa_id]
            print("Tarefa removida com sucesso!")
            print("=" * 15)
    elif opcao == 4:
        tareda_concluida = int(input("Digite o id da tarefa a ser concluida: "))
        if tareda_concluida in tarefas:
            tarefas[tareda_concluida]["concluido"] =  True
            print("Tarefa concluida com sucesso!")
            print("=" * 15)
        else:
            print("Opção invalida!")
            print("=" * 15)
            continue
    elif opcao == 5:
        print("Saindo do programa...")
        time.sleep(1)
        break
    else:
        print("Opção invalida!")
        print("=" * 15)
        continue