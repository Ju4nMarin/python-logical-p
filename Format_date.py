from datetime import datetime

ahora = datetime.now()
print(ahora, type(ahora))

fecha = ahora.strftime("%Y-%m-%d")
print(fecha)

format_24H = ahora.strftime("%H:%M:%S")
print(format_24H)

format_12H = ahora.strftime("%I:%M:%S %p")
print(format_12H)