import requests
import socket
from termcolor import colored



#Title
print(colored('>> Type the website address to get inforation from <<', 'yellow', attrs=['bold', 'underline']))
#subtitle
print(colored('example: google.com', 'dark_grey'))

input = input('Domain: https://')

req = requests.get('https://' + input)

ip = socket.gethostbyname(input)

print('\n' + colored('IP address: ', 'light_yellow') + colored(ip, 'green'))

for key, value in req.headers.items():
    print(colored(key, 'light_yellow') + ": " + colored(value, 'green'))

# print(colored(req.headers, 'light_green'))