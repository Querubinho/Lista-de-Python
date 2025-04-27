class adm_tarefas:
    def __init__(self):
        self.tarefas = []
        self.menu()
    
    def menu(self):
        while True:
            print("\nBem-Vindo!")
            print("1. Adicionar tarefa")
            print("2. Listar tarefas")
            print("3. Marcar tarefa como concluída")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.adicionar_tarefa_interativo()
            elif opcao == "2":
                self.listar_tarefas()
            elif opcao == "3":
                self.marcar_concluida_interativo()
            elif opcao == "4":
                print("Volte sempre!!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def adicionar_tarefa_interativo(self):
        descricao = input("Digite a descrição da tarefa: ")
        prazo = input("Digite o prazo (ex: 05/04/2026): ")
        self.adicionar_tarefa(descricao, prazo)
    
    def adicionar_tarefa(self, descricao, prazo):
        self.tarefas.append({
            'descricao': descricao,
            'prazo': prazo,
            'concluida': False
        })
        print(f"Tarefa '{descricao}' adicionada com sucesso.")
    
    def listar_tarefas(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada.")
            return
        
        print("\nLista de Tarefas")
        print("(Ordenadas por prazo)")
        for i, tarefa in enumerate(sorted(self.tarefas, key=lambda x: x['prazo']), 1):
            status = "✓" if tarefa['concluida'] else "✗"
            print(f"{i}. [{status}] {tarefa['descricao']} (Prazo: {tarefa['prazo']})")
    
    def marcar_concluida_interativo(self):
        self.listar_tarefas()
        if not self.tarefas:
            return
        
        try:
            indice = int(input("\nDigite o número da tarefa concluída: "))
            if 1 <= indice <= len(self.tarefas):
                tarefa = sorted(self.tarefas, key=lambda x: x['prazo'])[indice-1]
                tarefa['concluida'] = True
                print(f"\nTarefa '{tarefa['descricao']}' marcada como concluída!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

gerenciador = adm_tarefas()
