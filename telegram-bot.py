#!/usr/bin/python
# Telegram Remote-Shell
from datetime import datetime
now = datetime.now()
import telepot,time,os

# Telegram senders id
authorized_senders = "-289xxxxxxx"

try:
    def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        sender = msg['from']['id']
        f = open('trsh.log', 'a')
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        f.write("Chat-id - "+str(chat_id)+", content_type - "+str(content_type)+", Sender - "+str(sender)+", "+date_time+"\n")
        f.close()
        if (authorized_senders == str(chat_id)) and (content_type == 'text'):
            text = msg['text']
            args=text.split()
            command = args[0]
            if command == '/refresh':
                host = str(args[1])
                output=os.popen("/home/si/refresh "+host).read()
                bot.sendMessage(chat_id, output)
            else:
                bot.sendMessage(chat_id,"Error input wait for 10 Seconds")
                time.sleep(10)
                os.popen("kill -9 `ps -ef |grep telegram-bot.py |grep -v grep |awk '{print $2}'`;python /home/si/telegram-bot.py &").read()
        else:
            time.sleep(10)
            bot.sendMessage(chat_id,"Error input wait for 10 Seconds")
            os.popen("kill -9 `ps -ef |grep telegram-bot.py |grep -v grep |awk '{print $2}'`;python /home/si/telegram-bot.py &").read()
    bot = telepot.Bot('57349xxxxx:AAEDZucDqHxxxxxxxxxxxxxxxx')
    bot.message_loop(handle)
    while 1:
        time.sleep(10)
except:
    time.sleep(10)
    os.popen("kill -9 `ps -ef |grep telegram-bot.py |grep -v grep |awk '{print $2}'`;python /home/si/telegram-bot.py &").read()
