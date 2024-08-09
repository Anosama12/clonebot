#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "6753060421:AAFzWtkn6xLmOY5EM_OKbae80MQJGWgVkbU"

    # Get from my.telegram.org
    APP_ID = int(24367625)

    # Get from my.telegram.org
    API_HASH = "b27d49e801eca418acc68d35c5fa768e"

    # Generate a user session string
    TG_USER_SESSION = "BQG2SaYALSFUemAdNPhFRG3jekt3Zk3T-_WB6jdR9GR0035e8GRcQKshQYgj1TQIFWInCrxTm_ASl30ftxu9wqbotis7DRzzr6XxC_xJ-YdjpnE6ktWudB0ss6XNjSwR92iUI-9B0ewCvaVNws54PFySK4dK41BIGnPwgXJI2ifNt-sVnf8Qe4FQQKfB7RGcvqAowGy2vzoc1JnqBTU9kHk0dk_TTiJeCKlMrMbFD6IiYQWVhO1VxCFEUL9C9_hC-q2DjWtPO7U7ne_ntCKUtlT88sFGR_8DYFdYF172C-rToepj-yeyeSGc623OPRVdACQiTCFwsuPZ9VX_ZT6VgK0PQpM4PAAAAABXZYVDAA"

    # Database URI
    DB_URI = "mongodb+srv://rjkundra:Kayamkhani@cluster0.s6lvxxs.mongodb.net/?retryWrites=true&w=majority"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
