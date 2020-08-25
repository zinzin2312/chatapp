import json
import socket
from threading import Thread  # ,  active_count

from user import User


def send(msg):
    s.send(bytes(msg, "utf8"))
    # print(active_count())


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
Specify address and port of the server to connect to.
"""

host = "127.0.0.1"
port = 33000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

"""
    Each client will have an unique user
"""
user = User()

message = "{init}"

if __name__ == "__main__":
    Thread(target=receive).start()
    try:
        while True:
            send(create_message(message))
            if message.startswith("{name}"):
                old_name = user.name
                user.change_name(message[6:])
                message = "I changed my name from " + old_name + " to " + user.name
                continue
            if message.startswith("{quit}"):
                break
            message = input()
    finally:
        send(create_message(message))
        s.close()
