class adm_estoque:
    def __init__(self):
        self.produtos = []
        self.menu()
    
    def menu(self):
        while True:
            print("\nBem vindo!!")
            print("1. Adicionar produto")
            print("2. Listar produtos")
            print("3. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.adicionar_produto_interativo()
            elif opcao == "2":
                self.listar_produtos()
            elif opcao == "3":
                print("Volte sempre!!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def adicionar_produto_interativo(self):
        nome = input("Digite o nome do produto: ")
        
        while True:
            quantidade = input("Digite a quantidade em estoque: ")
            try:
                quantidade = int(quantidade)
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        
        while True:
            preco = input("Digite o preço unitário (ex: 29.90): ")
            try:
                preco = float(preco)
                break
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
        
        self.adicionar_produto(nome, quantidade, preco)
    
    def adicionar_produto(self, nome, quantidade, preco):
        self.produtos.append({
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
        })
        print(f"\nProduto '{nome}' adicionado ao estoque.")
    
    def listar_produtos(self):
        if not self.produtos:
            print("\nEstoque vazio.")
            return
        
        total = 0
        print("\n--- Produtos em Estoque ---")
        for i, produto in enumerate(self.produtos, 1):
            valor = produto['quantidade'] * produto['preco']
            total += valor
            print(f"{i}. {produto['nome']}")
            print(f"   Quantidade: {produto['quantidade']}")
            print(f"   Preço unitário: R${produto['preco']:.2f}")
            print(f"   Valor total: R${valor:.2f}\n")
        
        print(f"VALOR TOTAL DO ESTOQUE: R${total:.2f}")

estoque = adm_estoque()
