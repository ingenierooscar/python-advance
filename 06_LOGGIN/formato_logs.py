import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

nombre = "Paco"
logging.error(f"{nombre} creo el error")

logging.debug("log de debugging")
logging.info("log de info")
logging.warning("log de advertencia")
logging.error("log de error")
logging.critical("log de error critico")

try:
    division = 2 / 0
except:
    logging.exception("Division por cero")
