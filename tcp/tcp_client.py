#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : wuchongyao
# Date : 2018/10/23
# Feature : tcp server


import socket


HOST = ''
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)

while True:
    try:
        data = input("input data to send:\n")
        sock.send(data.encode())
        data = sock.recv(BUFSIZE).decode()
        if not data:
            break
        print("get : ", data)
    except Exception as e:
        print(e)

sock.close()
