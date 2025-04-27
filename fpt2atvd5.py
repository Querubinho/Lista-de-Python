class zapzap:
    def __init__(self):
        self.contatos = []
        self.menu()
    
    def menu(self):
        while True:
            print("\nMeus contatos")
            print("1. Adicionar contato")
            print("2. Buscar contato")
            print("3. Listar todos os contatos")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.adicionar_contato_interativo()
            elif opcao == "2":
                self.buscar_contato_interativo()
            elif opcao == "3":
                self.listar_contatos()
            elif opcao == "4":
                print("Ate logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def adicionar_contato_interativo(self):
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        
        self.adicionar_contato(nome, telefone, email)
    
    def adicionar_contato(self, nome, telefone, email):
        self.contatos.append({
            'nome': nome,
            'telefone': telefone,
            'email': email
        })
        print(f"\nContato '{nome}' adicionado com sucesso!")
    
    def buscar_contato_interativo(self):
        if not self.contatos:
            print("\nNenhum contato cadastrado.")
            return
        
        termo = input("\nDigite o nome ou parte do nome para buscar: ")
        self.buscar_contato(termo)
    
    def buscar_contato(self, termo):
        resultados = [c for c in self.contatos if termo.lower() in c['nome'].lower()]
        
        if not resultados:
            print("\nNenhum contato encontrado.")
            return
        
        print("\nContato encontrado:")
        for i, contato in enumerate(resultados, 1):
            print(f"{i}. Nome: {contato['nome']}")
            print(f"   Telefone: {contato['telefone']}")
            print(f"   Email: {contato['email']}")
            print()
    
    def listar_contatos(self):
        if not self.contatos:
            print("\nNenhum contato cadastrado.")
            return
        
        print("\nSeus contatos")
        for i, contato in enumerate(self.contatos, 1):
            print(f"{i}. Nome: {contato['nome']}")
            print(f"   Telefone: {contato['telefone']}")
            print(f"   Email: {contato['email']}")
            print()

agenda = zapzap()
