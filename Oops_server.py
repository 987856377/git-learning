#!/usr/bin/python
# -*- coding:utf8 -*-

from socket import *
import cv2
import numpy as np
import urllib.request
import re

url = urllib.request.urlopen("http://txt.go.sohu.com/ip/soip")
text = url.read()
ip = re.compile(r'\d+.\d+.\d+.\d+').findall(str(text))
print(str("当前IP: "), ip)

# 创建socket
sk = socket(AF_INET, SOCK_STREAM)
# 绑定ip端口
ip_port = ('0.0.0.0', 1823)
sk.bind(ip_port)
#打开监听
sk.listen(10)
print("服务器监听就绪")

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

#有客户端连接
conn, addr = sk.accept()
print(str('链接成功，客户端为：'), addr)

#接收客户端传来的信息
length = recvall(conn,16).decode()
stringData = recvall(conn, int(length))
#将数据解码
data = np.fromstring(stringData, dtype='uint8')
decimg=cv2.imdecode(data,1)
#保存图片
cv2.imwrite("capture.jpg",decimg)
print("接收完成")

# 关闭链接
conn.close()
sk.close()
