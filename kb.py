def typecom():
    from pynput.keyboard import Key,Controller
    import time

    keyboard = Controller()

    keyboard.type("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)