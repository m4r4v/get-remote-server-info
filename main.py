import requests
import socket
from termcolor import colored



#Title
print(colored('\n>>> WEBSITE SERVER INFORMATION <<<', 'cyan', attrs=['bold', 'underline']))
#Description
print(colored('Type the website address to get information from', 'light_yellow'))
#Example
print(colored('example: example.com', 'dark_grey'))
#input
domain = input('Domain: ')
print("\n" + colored('Looking up information for: ', 'light_cyan') + colored('https://' + domain, 'light_blue'))

req = requests.get('https://' + domain)

ip = socket.gethostbyname(domain)

try:
    print('\n' + colored('IP address: ', 'light_cyan') + colored(ip, 'light_blue'))

    for key, value in req.headers.items():
        print(colored(key, 'light_cyan') + ": " + colored(value, 'light_blue'))

    pass

    print("\n" + colored('Author: m4r4v', 'light_yellow'))

except KeyboardInterrupt:
    print("\n\n" + colored('Process interrupted, try again', 'red', attr=['bold']) + "\n")
