from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER

class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info("Bot initialize ho raha hai...")
        super().__init__(
            name="kiru",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        
        # Bot ki details fetch karna
        self.id = self.me.id
        self.name = f"{self.me.first_name} {self.me.last_name or ''}".strip()
        self.username = self.me.username
        self.mention = self.me.mention

        # Logger Group check aur message bhejna
        if config.LOGGER_ID:
            try:
                # Pehle check karein ki bot admin hai ya nahi
                chat_member = await self.get_chat_member(config.LOGGER_ID, self.id)
                if chat_member.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error(
                        "Bot aapke LOGGER_ID group mein admin nahi hai. Kirpya isse admin banayein."
                    )
                    # exit() # Aap chahein toh band kar sakte hain

                # Log message bhejna
                log_text = (
                    f"<b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ !</b>\n\n"
                    f"<b>ɪᴅ :</b> <code>{self.id}</code>\n"
                    f"<b>ɴᴀᴍᴇ :</b> {self.name}\n"
                    f"<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{self.username}"
                )
                await self.send_message(chat_id=config.LOGGER_ID, text=log_text)
                
            except errors.ChannelInvalid:
                LOGGER(__name__).error("LOGGER_ID galat hai ya bot us group ka hissa nahi hai.")
            except errors.PeerIdInvalid:
                LOGGER(__name__).error("LOGGER_ID invalid hai.")
            except Exception as e:
                LOGGER(__name__).error(f"Logger group error: {e}")
        else:
            LOGGER(__name__).warning("LOGGER_ID set nahi hai, log message nahi bheja gaya.")

        LOGGER(__name__).info(f"Music Bot started as {self.name} (@{self.username})")

    async def stop(self):
        LOGGER(__name__).info("Bot stop ho raha hai...")
        await super().stop()
