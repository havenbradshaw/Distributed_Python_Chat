# server.py
from multiprocessing.managers import BaseManager
from multiprocessing import Queue

# Shared queues
queue1 = Queue()  # Client1 → Client2
queue2 = Queue()  # Client2 → Client1
queue3 = Queue()  # Client3 → Client4
queue4 = Queue()  # Client4 → Client3

class ChatManager(BaseManager):
    pass

# Register shared objects
ChatManager.register('get_queue1', callable=lambda: queue1)
ChatManager.register('get_queue2', callable=lambda: queue2)
ChatManager.register('get_queue3', callable=lambda: queue3)
ChatManager.register('get_queue4', callable=lambda: queue4)

if __name__ == "__main__":
    manager = ChatManager(address=('', 50000), authkey=b'abc')
    server = manager.get_server()
    print("Server running at 172.21.5.13:50000 ...")
    server.serve_forever()