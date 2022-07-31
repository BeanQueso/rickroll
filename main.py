from pynput.mouse import Button,Controller
import time
from kb import typecom

mouse = Controller()

#print(mouse.position)

mouse.position = (51,424)
time.sleep(0.1)
mouse.click(Button.left,1)
time.sleep(0.3)
mouse.position = (1340,21)
time.sleep(0.1)
mouse.click(Button.left,1)

typecom()