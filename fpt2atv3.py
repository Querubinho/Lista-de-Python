class cinema:
    def __init__(self):
        print("\nReserva de Assentos")
        while True:
            try:
                total = int(input("Quantos assentos terá o evento? "))
                self.total_assentos = total
                self.assentos = {i: False for i in range(1, total+1)}
                break
            except ValueError:
                print("Por favor, digite um número válido.")
        
        self.menu()
    
    def menu(self):
        while True:
            print("\nMenu de Reservas")
            print("1. Ver mapa de assentos")
            print("2. Reservar assento")
            print("3. Cancelar reserva")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.mostrar_mapa()
            elif opcao == "2":
                self.reservar_assento_interativo()
            elif opcao == "3":
                self.cancelar_reserva_interativo()
            elif opcao == "4":
                print("Bom filme!!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def mostrar_mapa(self):
        print("(O = Disponível, X = Ocupado)\n")
        
        for i in range(1, self.total_assentos+1):
            status = "X" if self.assentos[i] else "O"
            print(f"{i:02d}: {status}", end="  ")
            if i % 5 == 0:
                print()
        print()
    
    def reservar_assento_interativo(self):
        self.mostrar_mapa()
        
        while True:
            try:
                numero = int(input("\nDigite o número do assento que deseja reservar: "))
                if 1 <= numero <= self.total_assentos:
                    self.reservar_assento(numero)
                    break
                else:
                    print(f"Por favor, digite um número entre 1 e {self.total_assentos}.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    def reservar_assento(self, numero):
        if not self.assentos[numero]:
            self.assentos[numero] = True
            print(f"\nAssento {numero} reservado com sucesso!")
        else:
            print(f"\nAssento {numero} já está ocupado.")
    
    def cancelar_reserva_interativo(self):
        self.mostrar_mapa()
        
        while True:
            try:
                numero = int(input("\nDigite o número do assento que deseja cancelar: "))
                if 1 <= numero <= self.total_assentos:
                    self.cancelar_reserva(numero)
                    break
                else:
                    print(f"Por favor, digite um número entre 1 e {self.total_assentos}.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    def cancelar_reserva(self, numero):
        if self.assentos[numero]:
            self.assentos[numero] = False
            print(f"\nReserva do assento {numero} cancelada.")
        else:
            print(f"\nAssento {numero} não estava reservado.")

evento = cinema()
