#!/usr/bin/env Python
# -*- conding:utf-8 -*-
# Author : wuchongyao
# Date : 2018/10/23
# Feature : udp server


import socket


HOST = ''
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDR)

while True:
    try:
        print('UDP Server start...')
        data, addr = sock.recvfrom(BUFSIZE)
        print('get : ', data.decode('utf-8'))
        sock.sendto(data, addr)
    except Exception as e:
        print(e)

sock.close()
