import logging

#Set up logging
logging.basicConfig(
    filename="goalie_tracker.log",
    filemode="a",
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger("goalie_tracker")

def log_and_print(message, level="info"):
    print(message)
    if level == "info":
        logger.info(message)
    elif level == "error":
        logger.error(message)
    elif level == "warning":
        logger.warning(message)