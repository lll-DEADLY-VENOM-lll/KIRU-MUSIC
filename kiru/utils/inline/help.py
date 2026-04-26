from pyrogram import types
import config 

class HelpPanel:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

    def help_markup(self, _lang: dict, back: bool = False) -> types.InlineKeyboardMarkup:
        if back:
            rows = [[self.ikb(text=_lang["back"], callback_data="help back"), 
                     self.ikb(text=_lang["close"], callback_data="help close")]]
        else:
            # Ye buttons aapke strings ke hisaab se hone chahiye
            cbs = ["admins", "auth", "blist", "lang", "ping", "play", "queue", "stats", "sudo"]
            buttons = [self.ikb(text=_lang[f"help_{cb}"], callback_data=f"help {cb}") for cb in cbs]
            rows = [buttons[i : i + 3] for i in range(0, len(buttons), 3)]
            # Owner button
            rows.append([self.ikb(text="ᴏᴡɴᴇʀ", url=f"tg://user?id={config.OWNER_ID}")])
            
        return self.ikm(rows)

    def help_back_markup(self, _lang: dict) -> types.InlineKeyboardMarkup:
        rows = [[
            self.ikb(text=_lang["back"], callback_data="help back"), 
            self.ikb(text=_lang["close"], callback_data="help close")
        ]]
        return self.ikm(rows)

# --- SAHI EXPORTS (Yeh lines fix karengi error) ---

# Pehle instance banayein
_hp = HelpPanel()

# Plugin line 29 (help_pannel(_, True)) ke liye ise function banana zaroori hai
help_pannel = _hp.help_markup

# Baaki functions
help_back_markup = _hp.help_back_markup

def private_help_panel(_):
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Hᴇʟᴘ",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
