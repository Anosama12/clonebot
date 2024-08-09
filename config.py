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
    TG_USER_SESSION = "BQFz0gkAJ6bG4FkeEkptzHgVg0phYoLDLA8TlgpNxA3d1wDjEDKJv8MfTr8c_z5NKIUjUWy31c-3Xi1VYYiojioi3kjazDjfnH2xDM9MIoTBB6Yuh3ozgDHYNUal-VTOGT66DQgyR6UKFQHZQfSMW2HSTJilJ_hr370AOgThCax-pWXidywO4PSU3O0cEq42fhuEWN4Tvh-g_U908UaUee2NiApL9KNiUGs2aPvT4a4tdONQWXURwaNwljDB-nvvCOhy30Xv6tIJVWRB3n7iAYzy9WQ8kLs_SnfbCi_nrgfti7Pj8RrjEhd5fpwnfaB_XR9yq17ystY06vXqkUvw5FZh3ytP1QAAAAFb8lvPAA"

    # Database URI
    DB_URI = "postgres://avnadmin:AVNS_tdEfuk4UCQi6vZo71ys@pg-3d393bff-sampatel0785-0f1b.k.aivencloud.com:21987/defaultdb?sslmode=require"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
