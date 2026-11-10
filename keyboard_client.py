


def keyboard_client():
    import pynput,socket
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(("192.168.10.173", 8080))

    keyboard_controller = pynput.keyboard.Controller()
    while True:
        data = socket_client.recv(1024)
        print("Received data")
        if not data:
            break
        message = data.decode('utf-8')
        if message.startswith("Key."):
            key_name = message.replace("Key.", "")
            try:
                key =pynput.keyboard.Key[key_name]
                keyboard_controller.press(key)
                keyboard_controller.release(key)
            except KeyError:
                print(f"Unknown key: {key_name}")
        else:
            key = message.replace("'","")
            keyboard_controller.type(key)

if __name__ == "__main__":
    keyboard_client()



