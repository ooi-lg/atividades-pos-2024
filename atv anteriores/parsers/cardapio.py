from xml.dom.minidom import parse

dom = parse("xml/cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

cardapio = [ ]


for prato in pratos:
    id_prato = prato.getAttribute('id')
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
    ingredientes = [ingrediente.firstChild.nodeValue for ingrediente in prato.getElementsByTagName('ingrediente')]
    preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
    moeda = prato.getElementsByTagName('preco')[0].getAttribute('moeda')
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
    tempo_preparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue
    
    prato_dict = {}
    
    prato_dict["id"] = id_prato
    prato_dict["nome"] = nome
    prato_dict["descricao"] = descricao
    prato_dict["ingredientes"] = ingredientes
    prato_dict["preco"] = preco
    prato_dict["moeda"] = moeda if moeda else "N/A"
    prato_dict["calorias"] = calorias
    prato_dict["tempo_preparo"] = tempo_preparo
    
    
    cardapio.append(prato_dict)


def exibir_detalhes(prato):
    print(f'''
    Nome: {prato["nome"]}
    Descrição: {prato["descricao"]}
    Ingredientes: {', '.join(prato["ingredientes"])}
    Preço: {prato["preco"]} ({prato["moeda"]})
    Calorias: {prato["calorias"]}
    Tempo de Preparo: {prato["tempo_preparo"]}
    ''')


while True:
    print("Menu de Pratos")
    print("Escolha um prato para ver detalhes:")
    
    for prato in cardapio:
        print(f'{prato["id"]}: {prato["nome"]}')

    escolha = input("Digite o ID do prato (ou 'sair' para encerrar): ")
    
    if escolha.lower() == 'sair':
        print('''
                  Saindo do programa.
                  ''')
        break

    
    prato_selecionado = next((prato for prato in cardapio if prato["id"] == escolha), None)
    
    if prato_selecionado:
        exibir_detalhes(prato_selecionado)
    else:
        print('''
                ID inválido. Tente novamente.
            ''')
