from pygame import *
import sys

init()

screen = display.set_mode((1890, 1417))


display.set_caption('none')


background = image.load('./диалоги/2этап(шахматы)/1.png')

screen.blit(background, (0, 0))
for i in range(1, 83):
    if 11 <= i <= 19:
        time.delay(1500)
    elif 51 <= i <= 57:
        time.delay(150)
    else:
        time.delay(270)
    background = image.load('./диалоги/2этап(шахматы)/' + str(i) + '.png')
    screen.blit(background, (0, 0))
    display.flip()



while 1:
    for i in event.get():
        if i.type == QUIT:

            sys.exit()




