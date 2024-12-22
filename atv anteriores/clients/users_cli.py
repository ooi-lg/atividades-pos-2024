import users_wrapper as users

while True:
    print("Menu de Opções:")
    print("1. Listar todos os usuários")
    print("2. Ler um usuário específico")
    print("3. Criar/Atualizar/Deletar usuários")
    print("6. Sair")

    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        response = users.list()
        for user in response:
            print(f"{user['id']} - {user['name']}")

    elif opcao == "2":
        user_id = input("Digite o ID do usuário: ")
        user = users.read(user_id)
        if user:
            print(f'''
                    {user['id']} - {user['name']} 
                    {user['username']}, {user['email']}
                ''')
        else:
            print("Usuário não encontrado")

    elif opcao == "3":
        print("1. Criar um novo usuário")
        print("2. Atualizar um usuário existente")
        print("3. Deletar um usuário")
        opcao3 = input("Digite sua escolha: ")

        if opcao3 == "1":
            user_data = {}
            user_data["name"] = input("Digite o nome do usuário: ")
            user_data["username"] = input("Digite o username do usuário: ")
            user_data["email"] = input("Digite o email do usuário: ")
            user_address = {}
            user_address["street"] = input("Digite o endereço do usuário: ")
            user_address["city"] = input("Digite a cidade do usuário: ")
            user_data["address"] = user_address
            users.create(user_data)

        elif opcao3 == "2":
            user_id = input("Digite o ID do usuário: ")
            user_data = users.read(user_id)
            if user_data:
                user_data["name"] = input(f"Digite o novo nome do usuário ({user_data['name']}): ") or user_data["name"]
                user_data["username"] = input(f"Digite o novo username do usuário ({user_data['username']}): ") or user_data["username"]
                user_data["email"] = input(f"Digite o novo email do usuário ({user_data['email']}): ") or user_data["email"]
                users.update(user_id, user_data)

        elif opcao3 == "3":
            user_id = input("Digite o ID do usuário: ")
            users.delete(user_id)
        
        else:
            print("Opção inválida.")

    elif opcao == "6":
        print("Tchau")
        break
        
    else:
        print("Opção inválida, tente novamente.")
