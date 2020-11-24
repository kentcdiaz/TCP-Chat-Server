import socket
import threading
question = input("What is the ip your trying to connect to ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = client.connect_ex((question, 337))
if result == 0:
    nickname = input("Choose your nickname: ")
    def receive():
        while True:
            try:
                message = client.recv(1024).decode('ascii')
                if message == 'NICK':
                    client.send(nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("An error occured!")
                client.close()
                break
    def write():
        while True:
            message = '{}: {}'.format(nickname, input(''))
            client.send(message.encode('ascii'))
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
else:
    print("Server is not running")
    print("Press Enter to Continue")
    input()