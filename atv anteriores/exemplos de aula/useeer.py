import requests
api_url = "http://jsonplaceholder.typicode.com/users"
print("digite 1 para listar todos os usuarios ")
print("digite 2 para listar tarefas os usuarios ")
print("digite 3 para grud  dos usuarios ")
opcao = input("digite:" )


if opcao == "1":
    response = requests.get(api_url).json()
    for user in response:
        print(f"{user['id']} - {user['name']}")

elif opcao == "2":
    user_id= input("digite id")
    response = requests.get(f"{api_url}/{user_id}/todos").json()
    for todo in response:
        print(todo['title'])

elif opcao == "3":
    print("digite 1 para ciar novo usuario")
    print("digite 2 para ler os dados de um usuario")
    print("digite 3 para atualizar os dados de um usuario")
    print("digite 4 para remover  usuario")
    user_option = input("digite")
    
    if user_option == "1":
        user_data={}
        user_data["name"] = input("digite o nome do usuario ")
        user_data["username"] = input("digite o username do usuario ")
        user_data["email"] = input("digite o email do usuario ")
        user_address = {}
        user_address["street"] = input("digite o endereco do usuario ")
        user_address["city"] = input("digite o cidade do usuario ")

        user_data["address"] = user_data
        response = requests.post(api_url, json=user_data).status_code
        if response == 201:
            print("sucesso")
        else:
            print("falha")

    elif user_option == "2":
        user_id = input("digite o id")
        response = requests.get(api_url+"/"+user_id).json()
        print(response)

    elif user_option == "3":
        user_id = input("digite o id")
        old_user = requests.get(api_url+"/"+user_id).json()
        print(f"voce esta modificando o usuario {old_user['name']}")
        old_user["name"] = input("digite o novo nome do usuario ")
        old_user["username"] = input("digite o novo username do usuario ")
        old_user["email"] = input("digite o novo email do usuario ")
        response = requests.patch(api_url+"/"+user_id, json=old_user).status_code
        if response == 200:
            print("sucesso")
        else:
            print("falha")


    elif user_option == "4":
        user_id = input("digite o id")
        response = requests.delete(api_url+"/"+user_id).status_code
        if response == 200:
            print("sucesso")
        else:
            print("falha")

    else: 
        print("erro")
else:
    print("ERRO")