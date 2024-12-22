import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass


user = input("Seu usuário do GitHub: ")
password = input("Digite a sua chave de acesso: ")

while True:
    print("Escolha uma opção:")
    print("1. Listar seguidores de um usuário")
    print("2. Seguir um usuário")
    print("3. Deixar de seguir um usuário")
    print("4. Sair")
    
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        name_user = input("Digite o login do usuário para conhecer seus seguidores: ")
        response = requests.get(
            f'https://api.github.com/users/{name_user}/followers',
            auth=HTTPBasicAuth(user, password)
        )
        
        if response.status_code == 200:
            for follower in response.json():
                print(follower['login'])
            print(f"Total de seguidores de {name_user}: {len(response.json())}")
        else:
            print(f"Falha ao obter dados: {response.status_code}")

    elif opcao == '2':
        name_user = input("Digite o login do usuário que você deseja seguir: ")
        response = requests.put(f'https://api.github.com/user/following/{name_user}',
            auth=HTTPBasicAuth(user, password)
        )
        
        if response.status_code == 204:
            print(f"Você agora está seguindo {name_user}.")
        else:
            print(f"Falha ao seguir o usuário: {response.status_code}")

    elif opcao == '3':
        name_user = input("Digite o login do usuário que você deseja deixar de seguir: ")
        response = requests.delete(
            f'https://api.github.com/user/following/{name_user}',
            auth=HTTPBasicAuth(user, password)
        )
        
        if response.status_code == 204:
            print(f"Você deixou de seguir {name_user}.")
        else:
            print(f"Falha ao deixar de seguir o usuário: {response.status_code}")

    elif opcao == '4':
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")
