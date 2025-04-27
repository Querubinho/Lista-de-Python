class banco:
    def __init__(self):
        self.usuarios = {
            'admin': {'senha': '1234', 'saldo': 0, 'historico': []},
            'user1': {'senha': 'abcd', 'saldo': 0, 'historico': []}
        }
        self.usuario_atual = None
        self.menu_principal()
    
    def menu_principal(self):
        while True:
            print("\nBem vindo, cliente.")
            print("1. Login")
            print("2. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.login_interativo()
                if self.usuario_atual:
                    self.menu_usuario()
            elif opcao == "2":
                print("Volte logo!!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def login_interativo(self):
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        
        if usuario in self.usuarios and self.usuarios[usuario]['senha'] == senha:
            self.usuario_atual = usuario
            print(f"\nBem-vindo, {usuario}!")
            return True
        else:
            print("\nUsuário ou senha incorretos.")
            return False
    
    def menu_usuario(self):
        while self.usuario_atual:
            print(f"\nOla, {self.usuario_atual}!")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver extrato")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.depositar_interativo()
            elif opcao == "2":
                self.sacar_interativo()
            elif opcao == "3":
                self.extrato()
            elif opcao == "4":
                print(f"\nLogout realizado. Até logo, {self.usuario_atual}!")
                self.usuario_atual = None
            else:
                print("Opção inválida. Tente novamente.")
    
    def depositar_interativo(self):
        while True:
            valor = input("\nDigite o valor do depósito: R$")
            try:
                valor = float(valor)
                if valor > 0:
                    self.depositar(valor)
                    break
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
    
    def depositar(self, valor):
        self.usuarios[self.usuario_atual]['saldo'] += valor
        transacao = f"Depósito: +R${valor:.2f}"
        self.usuarios[self.usuario_atual]['historico'].append(transacao)
        print(f"\nDepósito realizado. Novo saldo: R${self.usuarios[self.usuario_atual]['saldo']:.2f}")
    
    def sacar_interativo(self):
        while True:
            valor = input("\nDigite o valor do saque: R$")
            try:
                valor = float(valor)
                if valor > 0:
                    if self.usuarios[self.usuario_atual]['saldo'] >= valor:
                        self.sacar(valor)
                        break
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
    
    def sacar(self, valor):
        self.usuarios[self.usuario_atual]['saldo'] -= valor
        transacao = f"Saque: -R${valor:.2f}"
        self.usuarios[self.usuario_atual]['historico'].append(transacao)
        print(f"\nSaque realizado. Novo saldo: R${self.usuarios[self.usuario_atual]['saldo']:.2f}")
    
    def extrato(self):
        print(f"\nExtrato de {self.usuario_atual}")
        print("Histórico de transações:")
        
        if not self.usuarios[self.usuario_atual]['historico']:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.usuarios[self.usuario_atual]['historico']:
                print(f"- {transacao}")
        
        print(f"\nSaldo atual: R${self.usuarios[self.usuario_atual]['saldo']:.2f}")


banco = banco()
