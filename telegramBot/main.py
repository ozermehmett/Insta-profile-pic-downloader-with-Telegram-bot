import telegram
import instaloader
from telegram.ext import Updater, CommandHandler

TOKEN = 'BOT TOKEN'   #botunuzun tokenini buraya yapıştırıyoruz

bot = telegram.Bot(token=TOKEN)

L = instaloader.Instaloader()

def start(update, context):   #start komutuna verilecek cevap 
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! This bot is ready to send the profile photo of any Instagram user you want.\nPlease write in the following format:\n/profile username")

def profile(update, context):   #profile komutu gelirse döndürülecek fonk.
    username = context.args[0]
    print(username)
    
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        
        profile_pic_url = profile.profile_pic_url
        
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=profile_pic_url)
        
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hata! Lütfen geçerli bir kullanıcı adı girin.")

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('profile', profile))

updater.start_polling()
updater.idle()
