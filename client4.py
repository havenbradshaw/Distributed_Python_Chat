# client4.py
from multiprocessing.managers import BaseManager
import time

SERVER_IP = '172.26.92.170'
PORT = 50000
AUTHKEY = b'abc'

class ChatManager(BaseManager):
    pass

ChatManager.register('get_queue3')
ChatManager.register('get_queue4')

if __name__ == "__main__":
    manager = ChatManager(address=(SERVER_IP, PORT), authkey=AUTHKEY)
    manager.connect()

    q_recv = manager.get_queue3()   # receive from Client3
    q_send = manager.get_queue4()   # send to Client3

    print("Client4 connected to server.")

    while True:
        msg = q_recv.get()
        print(f"[Client4 RECEIVED]: {msg}")

        reply = input("Your reply: ")
        print(f"[Client4 SEND]: {reply}")
        q_send.put(reply)
        if (reply== "exit"):
            break
        time.sleep(1)