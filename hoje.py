def main():
    nome = ""
    idade = 0
    email = ""
    cidade = ""
    profissao = ""
    opcao = 0

    while True: # while true (enquanto for verdadeiro executa o código )
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar usuário")
        print("2. ver dados cadastrados")
        print("3. sair do sistema")
        print("======================")
        opcao = int(input("Escolha uma opção:")) 

        if opcao == 1:
            nome = input("\nDigite seu nome:")
            idade = input("Digite sua idade")
            email = input("Digite seu email")
            cidade = input("Digite a cidade")
            profissao = input("Digite a profissao")
            print("\nDados cadastrados com sucesso! \n")

        elif opcao == 2: # elif (senão se)
            if nome == "" and idade == 0 and email == "" and cidade == "" and profissao == "":
                print("\nNenhum dado cadastrado ainda!\n")
            else:
                print("\n=== DADOS CADATRADOS ===")
                print(f"Nome: {nome}")
                print(f"idade: {idade}")
                print(f"email: {email}")
                print(f"cidade: {cidade}")
                print(f"profissao: {profissao}")
        elif opcao == 3:
            print("\nEncerrando o sistema...\n")
            break # Sai do loop while, terminando o programa
        else: # else (senão)
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main() #Chama a função principal do programa
            

