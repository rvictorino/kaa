import Tkinter
from multiprocessing import Process, Queue
from chat import server, client
from kaagui import KaaGui
__author__ = 'victorino'

if __name__ == '__main__':
    # port to listen with server
    listening_port = int(raw_input('port to listen (2049 - 65635): '))
    if listening_port < 2049 or listening_port > 65635:
        print 'Wrong number. Abort.'
        exit

    # ip of the contact
    contact_ip = raw_input('contact ip address: ')
    if contact_ip == '':
        contact_ip = 'localhost'

    # port of the contact
    contact_port = int(raw_input('contact port: '))
    if contact_port < 2049 or contact_port > 65635:
        print 'Wrong number. Abort.'
        exit

    # username
    username = raw_input('your username: ')

    buffer_size = 1024

    server_queue = Queue()
    # start server
    server_process = Process(target=server, args=(listening_port, buffer_size, server_queue))
    server_process.daemon = True
    print 'Starting server...'
    server_process.start()

    # waiting signal from server
    msg = server_queue.get()
    if msg == 0:
        print 'server started.'
    else:
        print 'error starting server.'
        exit

    client_queue = Queue()
    # start client
    client_process = Process(target=client, args=(contact_ip, contact_port, username, buffer_size, client_queue))
    client_process.daemon = True
    print 'Starting client...'
    client_process.start()

    # waiting signal from server
    msg = client_queue.get()
    if msg == 0:
        print 'client started.'
    else:
        print 'error starting client.'
        exit

    # init the GUI
    root = Tkinter.Tk()
    kaa = KaaGui(root, username, client_queue, server_queue)
    kaa.master.title("Kaa")
    kaa.pack()
    # start the GUI
    root.mainloop()

    server_process.join()
    client_process.join()
