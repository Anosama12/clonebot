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
    TG_USER_SESSION = "BQFz0gkAl_Klq8QXafpYaPzIAHzopvREln_fB4GKIRGotSydfUZplT2Ni95XsqfPLyMNxrgU_MLH_zbgxrIuBN9I16NCo-8FwGQlJAcDuU1RvvcPu01TxIXC4c0R3t4_0VXXZ-rZXer6pP1LHMGbwVlVjMnUIrFAj0i7KzbUo8HNVQw-6-Nv_6MDzDdDB2So14KStWzrjkoi6Vur_bFzpXzWzbn3X1J9lpc2Zfo6sz_pUfSJrOfCG34HDXnIIQybExm_MfwNyin_BnreZpekNthMCGFKegMMm3SEnOINUfWAgFYcFaTTFLqMM86SpNDeHZ0PAkwpDa0orq3cIobQTDJir6hPegAAAAFb8lvPAA"

    # Database URI
    DB_URI = "postgres://avnadmin:AVNS_tdEfuk4UCQi6vZo71ys@pg-3d393bff-sampatel0785-0f1b.k.aivencloud.com:21987/defaultdb?sslmode=require"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
