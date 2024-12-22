from xml.dom.minidom import parse
import json


dom = parse("xml\imobiliaria.xml")


imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')

imobiliaria = [ ]

for imovel in imoveis:
    descricao = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue

    proprietario = imovel.getElementsByTagName('proprietario')[0]
    nome = proprietario.getElementsByTagName('nome')[0].firstChild.nodeValue
    emails = [email.firstChild.nodeValue for email in proprietario.getElementsByTagName('email')]
    telefones = [telefone.firstChild.nodeValue for telefone in proprietario.getElementsByTagName('telefone')]

    endereco = imovel.getElementsByTagName('endereco')[0]
    rua = endereco.getElementsByTagName('rua')[0].firstChild.nodeValue
    bairro = endereco.getElementsByTagName('bairro')[0].firstChild.nodeValue
    cidade = endereco.getElementsByTagName('cidade')[0].firstChild.nodeValue
    numero = endereco.getElementsByTagName('número')[0].firstChild.nodeValue if endereco.getElementsByTagName('número') else None

    caracteristicas = imovel.getElementsByTagName('caracteristicas')[0]
    tamanho = caracteristicas.getElementsByTagName('tamanho')[0].firstChild.nodeValue
    num_quartos = caracteristicas.getElementsByTagName('numQuartos')[0].firstChild.nodeValue
    num_banheiros = caracteristicas.getElementsByTagName('numBanheiros')[0].firstChild.nodeValue

    valor = imovel.getElementsByTagName('valor')[0].firstChild.nodeValue
    
    imovel_dict = { }

    print(f'''
    descricao:{descricao}
    proprietario: 
        nome: {nome},
        emails: {emails},
        telefones: {telefones}
    endereco:
        rua: {rua},
        bairro: {bairro},
        cidade: {cidade},
        numero: {numero}
    caracteristicas": 
        tamanho: {tamanho},
        numQuartos: {num_quartos},
        numBanheiros: {num_banheiros}
    
    valor: {valor}
    ''')

    imovel_dict["descricao"] = descricao

    imovel_dict["proprietario"] = {
        "nome": nome,
        "emails": emails,
        "telefones": telefones
    }

    imovel_dict["endereco"] = {
        "rua": rua,
        "bairro": bairro,
        "cidade": cidade,
        "numero": numero
    }

    imovel_dict["caracteristicas"] = {
        "tamanho": tamanho,
        "num_quartos": num_quartos,
        "num_banheiros": num_banheiros
    }

    imovel_dict["valor"] = valor
    
    imobiliaria.append(imovel_dict)


with open("imobiliaria.json", "w") as json_file:
    json.dump(imobiliaria, json_file, indent=2)