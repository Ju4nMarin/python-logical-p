import requests
import public_ip as ip

requests = requests.get("https://ident.me")
ip_public = requests.text
print(ip_public)

ip_public_2 = ip.get()
print(ip_public_2)