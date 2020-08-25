import socket
import json
from threading import Thread
from user import User


def send(msg):
    s.send(bytes(msg, "utf8"))
    Thread(target=receive).start()


def receive():
    while True:
        msg = s.recv(1024).decode("utf8")
        print(msg)


def create_message(msg):
    package = {'user': user.__dict__,
               'msg': msg}
    json_package = json.dumps(package)
    return json_package


"""
Host address and port of the server. Note that the address and port your machine is using is NOT the same
"""

host = "127.0.0.1"
port = 33000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
user = User()

message = "{init}"

if __name__ == "__main__":
    while True:
        if message.startswith("{name}"):
            old_name = user.name
            user.change_name(message[6:])
            message = "I changed my name from " + old_name + " to " + user.name
            continue
        send(create_message(message))
        message = input("Say something: ")
