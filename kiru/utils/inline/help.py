from pyrogram import types
import config # Ya 'from kiru import config' agar root se hai

class HelpPanel:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

    def help_markup(self, _lang: dict, back: bool = False) -> types.InlineKeyboardMarkup:
        if back:
            rows = [[self.ikb(text=_lang["back"], callback_data="help back"), 
                     self.ikb(text=_lang["close"], callback_data="help close")]]
        else:
            cbs = ["admins", "auth", "blist", "lang", "ping", "play", "queue", "stats", "sudo"]
            buttons = [self.ikb(text=_lang[f"help_{cb}"], callback_data=f"help {cb}") for cb in cbs]
            rows = [buttons[i : i + 3] for i in range(0, len(buttons), 3)]
            rows.append([self.ikb(text="ᴏᴡɴᴇʀ", url=f"tg://user?id={config.OWNER_ID}")])
            
        return self.ikm(rows)

# YE LINE ZAROOR ADD KAREIN (Instance create karein)
help_pannel = HelpPanel()
