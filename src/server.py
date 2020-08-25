from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import json

users_sockets = {}

host = ''
port = 33000
bz = 1024
addr = host, port
server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)


def accept():
    while True:
        client, client_address = server.accept()
        print(client_address, " connected")
        Thread(target=handle, args=(client,)).start()


def handle(client):
    while True:
        msg = client.recv(bz).decode("utf8")
        msg_obj = json.loads(msg)
        if msg_obj['msg'] == "{init}":
            client.send(bytes('Welcome ' + msg_obj['user']['name'], "utf8"))
            users_sockets[msg_obj['user']['ID']] = client
            continue
        name, message = msg_obj['user']['name'], msg_obj['msg']
        broadcast(message, name)


def broadcast(msg, name):
    for user_id in users_sockets:
        msg1 = name + " says: " + msg
        users_sockets[user_id].send(bytes(msg1, "utf8"))


if __name__ == "__main__":
    server.listen(5)
    print("Waiting for connection")
    accept_thread = Thread(target=accept)
    accept_thread.start()
    accept_thread.join()
    server.close()
