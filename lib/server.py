#!/usr/bin/env python

import socket


def server(port):
    ip = 'localhost'
    buffer_size = 126  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(0)

    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(buffer_size)
        if not data:
            break
        print "received data:", data
        conn.send(data)  # echo
    conn.close()
