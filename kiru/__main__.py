import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from kiru import LOGGER, app, userbot
from kiru.core.call import Anony
from kiru.misc import sudo
from kiru.plugins import ALL_MODULES
from kiru.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    # Assistant strings check ko thoda saaf (clean) banaya gaya hai
    if not any([config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5]):
        LOGGER(__name__).error("Assistant client variables (STRING1-5) defined nahi hain, exiting...")
        return

    await sudo()

    # Banned users load karne ka logic
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"Banned users load karne mein error: {e}")

    # Bot start karein
    await app.start()

    # Modules import karein
    for all_module in ALL_MODULES:
        importlib.import_module("kiru.plugins." + all_module)
    
    LOGGER("kiru.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await Anony.start()

    # Stream call setup
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("kiru").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        exit()
    except Exception as e:
        LOGGER("kiru").error(f"Streaming error: {e}")

    await Anony.decorators()
    
    # Hex code ko normal text mein badal diya gaya hai readability ke liye
    LOGGER("kiru").info("Kiru Music Bot Started Successfully.")
    
    await idle()
    
    # Graceful Shutdown
    await app.stop()
    await userbot.stop()
    LOGGER("kiru").info("Stopping Kiru Music Bot...")

if __name__ == "__main__":
    # Modern Python (3.7+) ke liye asyncio.run best hai
    try:
        asyncio.run(init())
    except KeyboardInterrupt:
        pass
