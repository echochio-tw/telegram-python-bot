#!/usr/bin/python
# Telegram Remote-Shell

from pprint import pprint
import telepot,time,os

# Telegram senders id
authorized_senders = "-3250000000"


def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']
    sender = msg['from']['id']
    f = open('trsh.log', 'a')
    f.write("Chat-id - "+str(chat_id)+" Text - "+str(text)+" Sender - "+str(sender)+"\n")
    f.close()
    if (authorized_senders == str(chat_id)):
      args=text.split()
      print(args[0]+" "+args[1]+"\n")
      command = args[0]
      if command == '/flash':
            host = str(args[1])
            output=os.popen("/home/si/flash "+host).read()
            bot.sendMessage(chat_id, output)

bot = telepot.Bot('688781292:AAFfaS1Q6CFz6TAtlQ1xxxxxxxxxxx')
bot.message_loop(handle)
while 1:
    time.sleep(10)
