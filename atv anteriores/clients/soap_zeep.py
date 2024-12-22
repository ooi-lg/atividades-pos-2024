import requests
from xml.dom.minidom import parseString
import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

country_code = "NO"

result = client.service.CapitalCity(sCountryISOCode=country_code)

print(f"A capital da Noruega ({country_code}) é {result}")

wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

numero = input("Digite um número para converter para extenso em inglês: ")

result = client.service.NumberToWords(ubiNum=numero)

print(f"O número {numero} por extenso em inglês é: {result}")