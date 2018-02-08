import telepot
token = '400007530:AAFIqRztleyDEbc8dsw-lEtx8p6NlzIIg0Y'
TelegramBot = telepot.Bot(token)

from telepot.loop import MessageLoop
def handle(msg):
 print(msg)
MessageLoop(TelegramBot, handle).run_as_thread()


TelegramBot.sendMessage(331008222, 'Whats up ?')
