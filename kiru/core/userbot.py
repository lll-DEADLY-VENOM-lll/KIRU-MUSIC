from pyrogram import Client
import config
from ..logging import LOGGER

# Global lists
assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AnonXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1) if config.STRING1 else None,
            no_updates=True,
        )
        self.two = Client(
            name="AnonXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2) if config.STRING2 else None,
            no_updates=True,
        )
        self.three = Client(
            name="AnonXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3) if config.STRING3 else None,
            no_updates=True,
        )
        self.four = Client(
            name="AnonXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4) if config.STRING4 else None,
            no_updates=True,
        )
        self.five = Client(
            name="AnonXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5) if config.STRING5 else None,
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")
        
        # Ek list banate hain clients ki taaki loop chala sakein
        clients = [
            (self.one, config.STRING1, 1),
            (self.two, config.STRING2, 2),
            (self.three, config.STRING3, 3),
            (self.four, config.STRING4, 4),
            (self.five, config.STRING5, 5),
        ]

        for client, string, index in clients:
            if string:
                try:
                    await client.start()
                    
                    # Force join chats
                    try:
                        await client.join_chat("about_deadly_venom")
                        await client.join_chat("https://t.me/+e4Up6nT3Hs04ZjBl")
                    except Exception:
                        pass
                    
                    assistants.append(index)
                    
                    # Logger Group mein message bhejna
                    try:
                        await client.send_message(config.LOGGER_ID, f"Assistant {index} Started")
                    except Exception:
                        LOGGER(__name__).error(
                            f"Assistant Account {index} failed to access the Log Group. "
                            f"Make sure you added it and promoted as admin!"
                        )
                    
                    # Client details set karna
                    me = await client.get_me()
                    client.id = me.id
                    client.name = me.mention
                    client.username = me.username
                    assistantids.append(client.id)
                    
                    LOGGER(__name__).info(f"Assistant {index} Started as {client.name}")
                    
                except Exception as e:
                    LOGGER(__name__).error(f"Assistant {index} failed to start: {str(e)}")

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        clients = [self.one, self.two, self.three, self.four, self.five]
        for client in clients:
            try:
                if client.is_connected:
                    await client.stop()
            except Exception:
                pass
