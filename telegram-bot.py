#!/usr/bin/python
# Telegram Remote-Shell

from pprint import pprint
import qrcode,telepot,time,os

# Telegram senders id
authorized_senders = "-3296xxxx"
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

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
            output=os.popen("/home/si/refresh "+host).read()
            bot.sendMessage(chat_id, output)
      if command == '/zsy':
            host = str(args[1])
            output=os.popen("/root/zsy "+host).read()
            bot.sendMessage(chat_id, output)
      if command == '/qr':
            host = str(args[1])
            qr.add_data(host)
            qr.make(fit=True)
            img = qr.make_image()
            img.save("/tmp/photo.png")
            photo = open('/tmp/photo.png', 'rb')
            bot.sendPhoto(chat_id, photo)
bot = telepot.Bot('705891952:AAFA7QQR9b8znxxxxxxxxxxxxxxxxxxxxxxxxx')
bot.message_loop(handle)
while 1:
    time.sleep(10)

