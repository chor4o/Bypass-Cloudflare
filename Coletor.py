#!/usr/bin/env python3
# Script para coletar o cookie _cfuvid de uma URL e salvar em cookie.txt by cHoR4o
#
# Descrição:
#   Este script faz uma requisição HTTP para a URL informada,
#   extrai o cookie _cfuvid da resposta e salva no arquivo cookie.txt.
#
# Como usar:
#   python3 coletor.py -u https://target.example.com
#
#   O cookie será salvo no arquivo cookie.txt no diretório atual.

import argparse
import requests

def coletar_cookies(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    cookies = response.cookies.get_dict()
    if '_cfuvid' in cookies:
        with open('cookie.txt', 'w') as file:
            file.write(f"_cfuvid={cookies['_cfuvid']}\n")
        print("Cookie _cfuvid salvo em cookie.txt")
    else:
        print("Cookie _cfuvid não encontrado na resposta.")

parser = argparse.ArgumentParser(description='Coletar cookie _cfuvid de uma URL e salvar em cookie.txt')
parser.add_argument('-u', '--url', type=str, required=True, help='URL alvo para coletar cookies')
args = parser.parse_args()

coletar_cookies(args.url)
