import requests
from xml.dom.minidom import parseString


url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

while True:

  print('''
    Escolha uma das opções:
    1 - CountryCurrency
    2 - CapitalCity
    3 - CountryFlag
    4 - Sair
    ''')
  
  opcao = input("Digite a opção que você quer fazer: ")

  if opcao == '1':
    funcao = "CountryCurrency"
  elif opcao == '2':
    funcao = "CapitalCity"
  elif opcao == '3':
    funcao = "CountryFlag"
  elif opcao == '4':
    print("tchau")
    break
  else:
    print("Opção inválida. Tente novamente.")
    continue
    
  country = input("Digite o código do país: ")
  


  payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <{funcao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country}</sCountryISOCode>
        </{funcao}>
      </soap:Body>
    </soap:Envelope>"""

  headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }


  response = requests.request("POST", url, headers=headers, data=payload)

  content = parseString(response.text)

  if opcao == '2' or opcao == '3':
        print(content.documentElement.getElementsByTagName(f"m:{funcao}Result")[0].firstChild.nodeValue)
  elif opcao == '1':
        print(content.documentElement.getElementsByTagName(f"m:sName")[0].firstChild.nodeValue)
