import logging
logging.basicConfig(level=logging.DEBUG, 
format="%(asctime)s - %(levelname)s - %(message)s", 
filename="ejemplo_logs.log", filemode="w",
datefmt = "%H:%M:%S"
)
nombre = "Juan"

try:
    division = 2/0
except:
    logging.exception(f"{nombre}, no se puede divir en 0")    

logging.debug("Log de debugg")
logging.info("Log de INFO")
logging.warning("Log Warning")
logging.error(f"{nombre} Creo el error")
logging.critical("Critico")