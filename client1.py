# client1.py
from multiprocessing.managers import BaseManager
import time

SERVER_IP = '172.26.92.170'
PORT = 50000
AUTHKEY = b'abc'

class ChatManager(BaseManager):
    pass

# Register (no callable on client side)
ChatManager.register('get_queue1')
ChatManager.register('get_queue2')

if __name__ == "__main__":
    manager = ChatManager(address=(SERVER_IP, PORT), authkey=AUTHKEY)
    manager.connect()

    q_send = manager.get_queue1()   # send to Client2
    q_recv = manager.get_queue2()   # receive from Client2

    print("Client1 connected to server.")
    msg = f"Client1 says hello!"
    print(f"[Client1 SEND]: {msg}")
    q_send.put(msg)
    while True :
        reply = q_recv.get()                            # 1. receive reply first
        print(f"[Client1 RECEIVED]: {reply}")
        msg = input("Please Enter your Next Message: ")  # 2. then send
        print(f"[Client1 SEND]: {msg}")
        q_send.put(msg)
        if msg == "exit":
            break
        time.sleep(1)