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

    s.listen(1)

    conn, addr = s.accept()
    pseudo = conn.recv(buffer_size)
    while True:
        message = conn.recv(buffer_size)
        queue.put(pseudo + '> ' + message)
        conn.send('ok')
    print 'shutting down server'


def client(ip, port, pseudo, buffer_size, queue):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    # signals that process has started
    queue.put(0)

    #trying to  connect contact server
    for i in range(1, 4):
        try:
            s.connect((ip, port))
            connected = True
            break
        except:
            print 'Try ', i, ': error connecting server. Retrying in 5s.'
            time.sleep(5)
    if connected:
        # send username as first message
        s.send(pseudo)
        print 'connected to server.'
    else:
        print'unable to connect server.'
        exit

    while True:
        message = queue.get()
        s.send(message)
        response = s.recv(buffer_size)
        # TODO do something with the server response
    s.close()
