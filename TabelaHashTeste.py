from TabelaHash import Pessoa, TabelaHash, realizar_compra_rifas

def exibir_menu():
    print("===== MENU =====")
    print("1. Realizar compra de rifas")
    print("2. Buscar pessoa por CPF")
    print("3. Sair")

def realizar_compra(tabelaHash):
    pessoa = realizar_compra_rifas()
    tabelaHash.inserir(pessoa.cpf, pessoa)
    print("Compra realizada com sucesso!")

def buscar_pessoa():
    cpf_busca = input("Digite o CPF da pessoa que deseja buscar: ")
    resultado_busca = TabelaHash.buscar(cpf_busca)

    if resultado_busca is not None:
        print("Nome:", resultado_busca.nome)
        print("CPF:", resultado_busca.cpf)
        print("Números comprados:", resultado_busca.numeros_comprados)

    else:
        print("Objeto não encontrado na tabela hash.")

def main():
    # Criação da tabela hash
    tabela = TabelaHash(10)

    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            realizar_compra(tabela)
        elif opcao == "2":
            buscar_pessoa()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
