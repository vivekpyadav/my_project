import logging

def setup_logger():
    """
    Set up logging configuration.
    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger
