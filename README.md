Fuzzing Tool with Cookie Support
Uma ferramenta simples e eficaz para fuzzing de diretórios em URLs, com suporte a envio de cookies _cfuvid customizados.

🚀 Visão Geral
Esta ferramenta permite realizar fuzzing de diretórios em URLs alvo, enviando cookies personalizados em cada requisição. Ideal para testes de segurança, enumeração de endpoints e bypass de rate limits em aplicações protegidas com Cloudflare com _cfuvid.

Mais informações ler o manual do cloudflare https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/#_cfuvid-for-rate-limiting-rules

✨ Funcionalidades
Fuzzing de diretórios: Testa uma lista de palavras em caminhos da URL alvo.

Suporte a cookies: Envia cookies customizados (ex: _cfuvid) em cada requisição.

User-Agent personalizado: Simula navegador mobile para maior stealth.

Headers avançados: Headers de navegador real para evitar detecção.

Delay aleatório: Entre requisições para evitar bloqueio.

Fácil de usar: Interface via linha de comando com parâmetros claros.

📦 Requisitos
Python 3.x

Biblioteca requests (pip install requests)

🛠️ Como Usar
Gere o arquivo de cookies:

bash
python3 coletar_cookie.py -u https://target.example.com
Prepare a wordlist:

Arquivo wordlist.txt com um caminho por linha.

Execute o fuzzing:

bash
python3 fuzzing.py -u https://target.example.com -w wordlist.txt -c cookie.txt
📝 Parâmetros
Parâmetro	Descrição
-u	URL base para teste
-w	Arquivo wordlist para fuzzing
-c	Arquivo de cookie(s) para enviar
📄 Exemplo de Saída
text
[+] https://target.example.com/admin => 200
[+] https://target.example.com/config => 403
📜 Licença
Este projeto está licenciado sob a MIT License.

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

Fique à vontade para copiar, modificar e usar conforme suas necessidades!
Se precisar de um logo ou de mais informações, é só pedir!
