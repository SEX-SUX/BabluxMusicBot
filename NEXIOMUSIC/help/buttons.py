from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    BBUTTON = [
        [
            InlineKeyboardButton("• ɢꝛᴏᴜᴘ •", callback_data="NEXIOPLUS HELP_Group"),
            InlineKeyboardButton("• ᴧᴄᴛɪᴏи •", callback_data="NEXIOPLUS HELP_Action"),
            InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="NEXIOPLUS HELP_Sticker")
        ],
        [
            InlineKeyboardButton("• ᴛᴧɢ-ᴧʟʟ •", callback_data="NEXIOPLUS HELP_TagAll"),
            InlineKeyboardButton("• ɪᴍᴘᴏsᴛᴇꝛ •", callback_data="NEXIOPLUS HELP_Imposter"),
            InlineKeyboardButton("• ᴛ-ᴅᴧꝛᴇ •", callback_data="NEXIOPLUS HELP_TD")
        ],
        [
            InlineKeyboardButton("• ʜᴧsʜ-ᴛᴧɢ •", callback_data="NEXIOPLUS HELP_HT")
        ],
        [
            InlineKeyboardButton("• ттѕ •", callback_data="NEXIOPLUS HELP_TTS"),
            InlineKeyboardButton("• ғᴜи •", callback_data="NEXIOPLUS HELP_Fun")
        ],    
        [
            InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data=f"NEXIO123"), 
        ]
        ]
    
    MBUTTON = [
        [
            InlineKeyboardButton("• ᴀɪ •", callback_data="NEXIOPLUS HELP_ChatGPT"),
            InlineKeyboardButton("• ɪɴғᴏ •", callback_data="NEXIOPLUS HELP_Info"),
            InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="NEXIOPLUS HELP_Sticker")
        ],
        [
            InlineKeyboardButton("• ᴇxᴛꝛᴧ •", callback_data="NEXIOPLUS HELP_Extra"),
            InlineKeyboardButton("• ɪᴍᴧɢᴇ •", callback_data="NEXIOPLUS HELP_Image"),
            InlineKeyboardButton("• sᴇᴧꝛᴄʜ •", callback_data="NEXIOPLUS HELP_Search")
        ],
        [
            InlineKeyboardButton("• ǫᴜɪʟʏ •", callback_data="NEXIOPLUS HELP_Q")
        ],
        [
            InlineKeyboardButton("• ғᴏиᴛ •", callback_data="NEXIOPLUS HELP_Font"),
            InlineKeyboardButton("• ɢᴧᴍᴇ •", callback_data="NEXIOPLUS HELP_Game"),
            InlineKeyboardButton("• ᴛ-ɢꝛᴧᴘʜ •", callback_data="NEXIOPLUS HELP_TG")
        ],    
        [
            InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data=f"NEXIO123"), 
        ]
        ]
    SBUTTON = [
        [
            InlineKeyboardButton("• 1 •", callback_data="NEXIO_CP"),
            InlineKeyboardButton("• 2 •", callback_data="NEXIOO_CP"),
        ],
        [
            InlineKeyboardButton("• 3 •", callback_data="settingsback_helper"),
            InlineKeyboardButton("• 4 •", callback_data="settingsback_helper"),
            
        ]
        ]
