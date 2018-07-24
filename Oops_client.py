#!/usr/bin/python
# -*- coding:utf8 -*-

import socket
import cv2
import numpy as np

# 创建socket
sk = socket.socket()
ip_port = ('127.0.0.1', 1823)
#连接服务器
sk.connect(ip_port)
#打开摄像头
cap = cv2.VideoCapture(0)
#读取摄像头捕捉的像素点
ret, frame = cap.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
#将图片进行编码
result, imgencode = cv2.imencode('.jpg', frame, encode_param)
data = np.array(imgencode)
stringData = data.tostring()
#发送信息
sk.send( str(len(stringData)).ljust(16).encode())
sk.send(stringData)
#关闭连接
cap.release()
cv2.destroyAllWindows()
sk.close()