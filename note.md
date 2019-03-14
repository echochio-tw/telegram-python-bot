Saved an image sent to bot using the following handle function:
```
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'photo':
        bot.download_file(msg['photo'][-1]['file_id'], './file.png')
```
note 1:that the example code overwrites new images on the old one, you may want to generate the file name dynamically instead of hard coding one.

note 2: msg['photo'] is a list of different sizes of image, first element is a small thumbnail so i used -1 (last photo) to get the photo with highest quality

```
sudo yum install zbar
sudo yum install pyzbar  
```

（1）in shell
```
zbarimg barcode.jpg
```
（2）in python
```
>>> from pyzbar.pyzbar import decode
>>> from PIL import Image
>>> decode(Image.open('code128.png'))
```
