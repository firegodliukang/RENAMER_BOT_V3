"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP** 
	Daily  Upload  limit unlimited
	Price Rs 100  🇮🇳/🌎 2$  per Month
	
	
	Pay Using Upi I'd ```theanimeguy@apl```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/inferno_scorpion")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/imgaurav1214"),
        			InlineKeyboardButton("Other Methods",url = "https://t.me/inferno_scorpion")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP** 
	Daily  Upload  limit unlimited 
	Price Rs 100  🇮🇳/🌎 2$  per Month
	
	
	Pay Using Upi I'd ```theanimeguy@apl```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/inferno_scorpion")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/imgaurav1214"),
        			InlineKeyboardButton("Other Methods",url = "https://t.me/inferno_scorpion")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
