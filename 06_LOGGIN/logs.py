import logging

logging.basicConfig(level=logging.DEBUG, 
    filename="ejemplo logs",
    filemode="w"
)

logging.debug("log de debugging")
logging.info("log de info")
logging.warning("log de advertencia")
logging.error("log de error")
logging.critical("log de error critico")