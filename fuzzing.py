#!/usr/bin/env python3
"""
Script para fuzzing de diretórios em uma URL, enviando cookies de um arquivo.

Uso:
    python3 fuzzing.py -u <url> -w <wordlist> -c <cookie_file>

Exemplo:
    python3 fuzzing.py -u https://target.example.com -w wordlist.txt -c cookie.txt

Descrição:
    - -u: URL base para teste
    - -w: Arquivo com lista de diretórios/palavras para fuzzing
    - -c: Arquivo com cookie(s) para enviar nas requisições (uma linha por cookie)

Criado por Paulo Luis e alterado e adaptado por cHor4o
"""

import argparse
import requests
import time
import random

def main():
    parser = argparse.ArgumentParser(description='Fuzzing de diretórios com cookie')
    parser.add_argument('-u', '--url', type=str, required=True, help='URL base para teste')
    parser.add_argument('-w', '--wordlist', type=str, required=True, help='Arquivo wordlist para fuzzing')
    parser.add_argument('-c', '--cookie', type=str, required=True, help='Arquivo de cookie(s)')
    args = parser.parse_args()

    # Carrega os cookies do arquivo (uma linha por cookie)
    with open(args.cookie, 'r') as f:
        cookies_list = [line.strip() for line in f if line.strip()]

    # Carrega a wordlist
    with open(args.wordlist, 'r') as f:
        words = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    # User-Agent (Android Chrome)
    user_agent = "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Mobile Safari/537.36"
    headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document'
    }

    for word in words:
        # Escolhe um cookie aleatório se houver mais de um
        cookie = random.choice(cookies_list) if cookies_list else None
        cookies = {}
        if cookie:
            # Monta dicionário de cookies para requests (se cookie é "nome=valor")
            if '=' in cookie:
                k, v = cookie.split('=', 1)
                cookies[k] = v
            else:
                print(f"Formato inválido de cookie: {cookie}. Usando sem cookie.")
        url = args.url.rstrip('/') + '/' + word.lstrip('/')
        try:
            # Adiciona delay aleatório entre 2 e 6 segundos (para stealth)
            time.sleep(random.uniform(2, 6))
            response = requests.get(url, headers=headers, cookies=cookies, allow_redirects=False)
            if response.status_code != 404:
                print(f"[+] {url} => {response.status_code}")
        except Exception as e:
            print(f"Erro ao acessar {url}: {e}")

if __name__ == "__main__":
    main()
