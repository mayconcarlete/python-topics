from dotenv import load_dotenv
import sys
load_dotenv()
import os

EMAIL_KEY = os.getenv('EMAIL')
NAME_KEY = os.getenv('NAME')

if len(sys.argv) == 2:
    print('Temos uma configuração setada...')
    configuration = sys.argv[1].upper()
    print(f'Usando a configuração: {configuration}')
    if configuration == 'DEV':
        email = os.getenv('DEV_EMAIL')
        name = os.getenv('DEV_NAME')
        print(f'name:{name} - email:{email}')
    else:
        email = os.getenv('PROD_EMAIL')
        name = os.getenv('PROD_NAME')
        print(f'name:{name} - email:{email}')
else:
    print('Rodando configuracao padrão')
    email = os.getenv('PROD_EMAIL')
    name = os.getenv('PROD_NAME')
    print(f'name:{name} - email:{email}')