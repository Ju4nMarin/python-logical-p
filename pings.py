import os

def ping(hostname):
    respuesta = os.system(f"ping {hostname}")
    if respuesta == 0:
        print(f"{hostname} esta activo")
        print(f"{hostname} esta inactivo")


ping("google.com")