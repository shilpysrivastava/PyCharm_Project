import logging
import allure


def get_logger(name=__name__):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
        )

        # File handler
        file_handler = logging.FileHandler("PytestBDDFrameworkDemo/logs/test_execution.log")
        file_handler.setFormatter(formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

def allure_log(message):
    allure.attach(
        message,
        name="Log",
        attachment_type=allure.attachment_type.TEXT
    )