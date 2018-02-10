import telepot
token = 'Put Your Telegram token key here'
TelegramBot = telepot.Bot(token)

from telepot.loop import MessageLoop
def handle(msg):
 print(msg)
MessageLoop(TelegramBot, handle).run_as_thread()


TelegramBot.sendMessage(331008222, 'Whats up ?')
