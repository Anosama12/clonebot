#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import sys
from user import User
from pyrogram import Client
from presets import Presets as Msg
from pyrogram.enums import ParseMode

from config import Config
from config import LOGGER


class Bot(Client):
    USER: User = BQG2SaYALSFUemAdNPhFRG3jekt3Zk3T-_WB6jdR9GR0035e8GRcQKshQYgj1TQIFWInCrxTm_ASl30ftxu9wqbotis7DRzzr6XxC_xJ-YdjpnE6ktWudB0ss6XNjSwR92iUI-9B0ewCvaVNws54PFySK4dK41BIGnPwgXJI2ifNt-sVnf8Qe4FQQKfB7RGcvqAowGy2vzoc1JnqBTU9kHk0dk_TTiJeCKlMrMbFD6IiYQWVhO1VxCFEUL9C9_hC-q2DjWtPO7U7ne_ntCKUtlT88sFGR_8DYFdYF172C-rToepj-yeyeSGc623OPRVdACQiTCFwsuPZ9VX_ZT6VgK0PQpM4PAAAAABXZYVDAA
    USER_ID: int = 5837577167

    def __init__(self):
        super().__init__(
            name="bot_session",
            api_hash=Config.API_HASH,
            api_id=Config.APP_ID,
            bot_token=Config.TG_BOT_TOKEN,
            sleep_threshold=30,
            workers=8,
            plugins={
                "root": "plugins"
            }
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()
        try:
            await self.USER.send_message(usr_bot_me.username, "%session_start%")
        except Exception:
            print(Msg.BOT_BLOCKED_MSG)
            sys.exit()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
