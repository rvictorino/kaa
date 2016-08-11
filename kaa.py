from chat import server
from chat import client
from multiprocessing import Process, Queue

__author__ = 'victorino'

if __name__ == '__main__':
    listening_port = int(raw_input('port to listen (2049 - 65665): '))
    if listening_port < 2049 or listening_port > 65665:
        print 'Wrong number. Abort.'
        exit()

    contact_ip = raw_input('contact ip address: ')
    if contact_ip == '':
        contact_ip = 'localhost'
    contact_port = int(raw_input('contact port: '))
    pseudo = raw_input('your pseudo: ')

    buffer_size = 126  # Normally 1024, but we want fast response

    queue = Queue()
    server_process = Process(target=server, args=(listening_port, buffer_size, queue))
    server_process.daemon = True
    print 'Starting server'
    server_process.start()

    # waiting signal from server
    msg = queue.get()
    if msg == 0:
        print 'server started'
    else:
        print 'error starting server'
        exit

    print 'Starting client'
    client(contact_ip, contact_port, pseudo)

    server_process.join()
