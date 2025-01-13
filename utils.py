from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread
import itertools

done = False
global loading_message

def loading_icon():
    global loading_message

    slash_icons = ['|', '/', '-', '\\']
    moon_icons = ['🌑', '🌘', '🌗', '🌖', '🌕', '🌔', '🌓', '🌒']
    for c in itertools.cycle(moon_icons):
        if done:
            break
        terminal.write('\r'+loading_message+c)
        terminal.flush()
        sleep(0.1)
    terminal.write('\rDone!    ')
    terminal.flush()

loading_message = "Hi Jack...  "
t = Thread(target=loading_icon)
t.start()
sleep(5)
done = True