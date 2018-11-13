#!/usr/bin/env Python
# -*- conding:utf-8 -*-
# Author : wuchongyao
# Date : 2018/10/23
# Feature : udp client


import socket


HOST = '172.17.9.101'
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        print("UDP Client start")
        data = input("input data to send:\n")
        sock.sendto(data.encode(), ADDR)
        data, addr = sock.recvfrom(BUFSIZE)
        print("get : ", data.decode())
    except Exception as e:
        print(e)

sock.close()
