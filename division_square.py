from pygame import *
import sys

init()

screen = display.set_mode((0, 0), FULLSCREEN)


display.set_caption('none')


background = image.load('./разделение квадрата.быт/1.png')

screen.blit(background, (0, 0))
for i in range(1, 16):
    background = image.load('./разделение квадрата.быт/' + str(i) + '.png')
    w, h = display.get_surface().get_size()
    background = transform.scale(background, (w, h))
    screen.blit(background, (0, 0))
    display.flip()


running = True
while running:
    for e in event.get():
        if e.type == K_ESCAPE:
            running = False

quit()