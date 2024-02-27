import psutil

def recursos_cpu():
    nucleos = psutil.cpu_count(logical=False)
    print("Cantidad de nucleos: ",nucleos)

    carga = psutil.getloadavg()
    print("Carga avg: ",carga)

    usa = psutil.cpu_percent(interval=5, percpu=True)
    print("Procentaje de uso CPU: ",usa)