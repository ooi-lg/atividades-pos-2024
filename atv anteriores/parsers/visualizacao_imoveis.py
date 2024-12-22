import json

with open("imobiliaria.json", "r") as json_file:
    imobiliaria = json.load(json_file)


def exibir_detalhes(imovel):
    print(f'''
    Descrição: {imovel["descricao"]}
    Proprietário:
        Nome: {imovel["proprietario"]["nome"]}
        Emails: {', '.join(imovel["proprietario"]["emails"]) if imovel["proprietario"]["emails"] else "Nenhum"}
        Telefones: {', '.join(imovel["proprietario"]["telefones"]) if imovel["proprietario"]["telefones"] else "Nenhum"}
    Endereço:
        Rua: {imovel["endereco"]["rua"]}
        Bairro: {imovel["endereco"]["bairro"]}
        Cidade: {imovel["endereco"]["cidade"]}
        Número: {imovel["endereco"]["numero"] if imovel["endereco"]["numero"] else "Não especificado"}
    Características:
        Tamanho: {imovel["caracteristicas"]["tamanho"]}
        Número de Quartos: {imovel["caracteristicas"]["num_quartos"]}
        Número de Banheiros: {imovel["caracteristicas"]["num_banheiros"]}
    Valor: {imovel["valor"]}
    ''')


while True:
        print("Menu de Imóveis")
        print("Escolha um imóvel para ver detalhes:")
        

        id_imovel = 0
        for imovel in imobiliaria:
            print(f"{id_imovel}. Descrição: {imovel['descricao']}")
            id_imovel += 1

        escolha = input("Digite o ID do imóvel (ou 'sair' para encerrar): ")
        
        if escolha.lower() == 'sair':
            print('''
                  Saindo do programa.
                  ''')
            break

        try:        
            id_imovel = int(escolha)
            if 0 <= id_imovel < len(imobiliaria):
                exibir_detalhes(imobiliaria[id_imovel])
            else:
                print('''
                      ID inválido. Tente novamente.
                      ''')
        except ValueError:
       
            print('''
                  Entrada inválida. Digite um número válido ou 'sair' para encerrar."
                  ''')

