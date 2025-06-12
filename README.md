Fuzzing Tool with Cookie Support - By Pass Rate limit -  Created by chor4o

🚀 Overview
This tool allows you to perform directory fuzzing on target URLs, sending custom cookies with each request. It is ideal for security testing, endpoint enumeration, and bypassing rate limits on applications protected by Cloudflare with the _cfuvid cookie.
For more information, see the Cloudflare manual:
https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/#_cfuvid-for-rate-limiting-rules
 
✨ Features
•	Directory fuzzing: Tests a list of words as paths on the target URL.
•	Cookie support: Sends custom cookies (e.g., _cfuvid) with each request.
•	Custom User-Agent: Simulates a mobile browser for increased stealth.
•	Advanced headers: Uses real browser headers to avoid detection.
•	Random delay: Between requests to prevent blocking.
•	Easy to use: Command-line interface with clear parameters.
 
📦 Requirements
•	Python 3.x
•	requests library (pip install requests)
 
🛠️ How to Use
1.	Generate the cookie file:
python3 coletor.py -u https://target.example.com

2.	Prepare the wordlist:
o	File wordlist.txt with one path per line.
3.	Run the fuzzing:
python3 fuzzing.py -u https://target.example.com -w wordlist.txt -c cookie.txt

 
📝 Parameters
Parameter	Description
-u	Base URL to test
-w	Wordlist file for fuzzing
-c	Cookie file to send

 
📄 Example Output
[+] https://target.example.com/admin => 200
[+] https://target.example.com/config => 403

 
📜 License
This project is licensed under the MIT License.
 
🤝 Contributions
Contributions are welcome! Feel free to open issues or pull requests.
 
Feel free to copy, modify, and use as needed!
