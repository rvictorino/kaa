import socket
import time

__author__ = 'victorino'


def server(port, buffer_size, queue):
    ip = 'localhost'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((ip, port))
    except:
        queue.put(-1)
        exit
    queue.put(0)

    while True:
        s.listen(0)
        conn, addr = s.accept()

        data = conn.recv(buffer_size)
        if not data:
            break
        print addr[0], ':', addr[1], '> ', data, '\n'


def client(ip, port, pseudo):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    connected = False
    for i in range(1, 4):
        try:
            s.connect((ip, port))
            connected = True
            break
        except:
            print 'Try ', i, ': error connecting server. Retrying in 5s.'
            time.sleep(5)
    if connected:
       print 'connected to server.'
    else:
        print'unable to connect server.'
        exit

    end = False
    while not end:
        message = raw_input(pseudo + '> ')
        if message == 'exit':
            end = True
        else:
            s.send(message + '\n')
    s.close()
