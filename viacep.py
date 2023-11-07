import requests, json
from os import system

system('cls')

cep = input('\nInforme seu cep: ')

if '-' in cep:
	cep = cep.replace('-', '')

req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
request = req.json()

print(f"\nLogradouro: {request['logradouro']}")
print(f"Bairro: {request['bairro']}")
print(f"Cidade: {request['localidade']}")
print(f"Estado: {request['uf']}")
print(f"Código de área: {request['ddd']}")
print(f"Cep: {request['cep']}\n")

input('\nEnter para continuar\n')
