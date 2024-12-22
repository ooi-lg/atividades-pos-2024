from xml.dom.minidom import parse
import json
dom = parse("biblioteca.xml")

# Elemento raiz do XML (biblioteca)
biblioteca = dom.documentElement

# Recebe uma lista dos elementos com tag "livro"
livros = biblioteca.getElementsByTagName('livro')


biblioteca = [ ]
# Acessa as informações de cada livro
for livro in livros:
    categoria = livro.getAttribute('categoria')
    elemento_titulo = livro.getElementsByTagName('título')[0]
    titulo = elemento_titulo.firstChild.nodeValue
    elemento_autor = livro.getElementsByTagName('autor')[0]
    origem = elemento_autor.getAttribute('origem')
    autor = elemento_autor.firstChild.nodeValue
    elemento_ano = livro.getElementsByTagName('ano')[0]
    ano = elemento_ano.firstChild.nodeValue
    livro_dict = { }
    print("Categoria:", categoria)
    print("Título:", titulo)
    print(f'Autor: {autor} ({origem})')
    print("Ano:", ano)
    print("---\n")

    livro_dict["categoria"] = categoria
    livro_dict["titulo"] = titulo
    livro_dict["autor"] = autor
    livro_dict["origem"] = origem
    livro_dict["ano"] = ano
    biblioteca.append(livro_dict)
with open("biblioteca.json", "w") as json_file:
    json.dump(biblioteca, json_file, ident=2)
print(biblioteca)



