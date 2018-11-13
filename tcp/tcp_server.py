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
sock.bind(ADDR)
sock.listen(1)

while True:
    try:
        print("等待连接...")
        conn, addr = sock.accept()
        print("连接成功")

        while True:
            data = conn.recv(BUFSIZE)
            print('收到数据：', data.decode('utf-8'))
            if data:
                conn.sendall(data)  # 在这里处理数据
            else:
                print(f'没收到{addr}的数据')
                break
        
        conn.close()
    except Exception as e:
        print(e)
    
sock.close()