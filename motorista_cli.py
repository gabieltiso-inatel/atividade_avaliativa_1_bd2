from motorista_dao import MotoristaDAO

from motorista import Motorista
from passageiro import Passageiro
from corrida import Corrida

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao: MotoristaDAO):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("create", self.criar_motorista)
        self.add_command("read", self.ler_dados_motorista)
        self.add_command("update", self.atualizar_motorista)
        self.add_command("delete", self.deletar_motorista)

    def criar_motorista(self):
        nota_motorista = input("Digite a nota do motorista: ")
        motorista = Motorista([], int(nota_motorista))

        quantidade_corridas = int(input("Digite a quantidade de corridas que deseja inserir para esse motorista: "))
        for _ in range(0, quantidade_corridas):
            nome_passageiro = input("Digite o nome do passageiro: ")
            documento_passageiro = input("Digite o documento do passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento_passageiro)

            nota_corrida = int(input("Digite a nota da corrida: "))
            distancia_corrida = float(input("Digite a distancia da corrida: "))
            valor_corrida = float(input("Digite o valor da corrida: "))
            corrida = Corrida(nota_corrida, distancia_corrida, valor_corrida, passageiro)
            
            motorista.adicionar_corrida(corrida)
        
        self.motorista_dao.criar_motorista(motorista)

    def ler_dados_motorista(self):
        id = input("Digite o id do motorista: ")
        motorista = self.motorista_dao.ler_dados_motorista(id)

        if motorista:
            print(f"Nota do motorista: {motorista['nota']}")
            print("INFORMAÇÕES DAS CORRIDAS: ")
            for corrida in motorista['corridas']:
                print(f"Nota: {corrida['nota']}, Distância: {corrida['distancia']}, Valor: {corrida['valor']}")
                print(f"Nome do passageiro: {corrida['passageiro']['nome']}, Documento do passageiro: {corrida['passageiro']['documento']}")

    def atualizar_motorista(self):
        id = input("Digite o id do motorista: ")
        nota = int(input("Digite a nova nota do motorista: "))

        self.motorista_dao.atualizar_motorista(id, nota)

    def deletar_motorista(self):
        id = input("Digite o id do motorista")
        self.motorista_dao.deletar_motorista(id)
        
    def run(self):
        print("Welcome to the driver CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
