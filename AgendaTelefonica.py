agendaTelefonica = {}

def adicionarContato(numero, nome):
    agendaTelefonica[numero] = nome

def buscarContato(nome):
  if nome in agendaTelefonica:
      return f"O número de telefone de {nome} é {agendaTelefonica[nome]}"
  else:
      return "Contato não encontrado"

def listarContatos(agenda):
    for nome, numero in agenda.items():
        print(f"{nome}: {numero}")

while True:
    print("\nEscolha uma opção:")
    print("1 - Salvar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("0 - Sair")

    opcao = int(input("O que deseja fazer? "))

    if opcao == 0:
        print("Saindo do programa...")
        break

    elif opcao == 1:
        quantidade = int(input("Quantos contatos quer salvar? "))

        for nome in range(quantidade):
            numero = input("\nForneça um número: ")
            nome = input("Qual nome quer salvar esse contato: ")
            adicionarContato(numero, nome)

        print(agendaTelefonica)

    elif opcao == 2:
        busca_nome = input("Qual contato você procura? ")
        resultado_busca = buscarContato(busca_nome)
        print(resultado_busca)

    elif opcao == 3:
        listarContatos(agendaTelefonica)

    else:
        print("Opção inválida! Escolha uma opção válida.")
