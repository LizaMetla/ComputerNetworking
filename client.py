#!/usr/bin/env python3
import json
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000  # The port used by the server


def points_input() -> tuple:
    x1 = int(input('x1 = '))
    y1 = int(input('y1 = '))
    x2 = int(input('x2 = '))
    y2 = int(input('y2 = '))
    x3 = int(input('x3 = '))
    y3 = int(input('y3 = '))
    x4 = int(input('x4 = '))
    y4 = int(input('y4 = '))
    x0 = int(input('x0 = '))
    y0 = int(input('y0 = '))

    return (x0, y0, (x1, x2, x3, x4), (y1, y2, y3, y4))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # создаётся клиентский сокет
    s.connect((HOST, PORT))  # запрос для создания соединения
    s.sendall(json.dumps(points_input()).encode())  # отправление данных по сокету от клиента
    data = s.recv(1024)  # сообщения , что отвечает сервер

ans = data.decode()
if ans == '1':
    print('Точка находится в указанной прямоугольной области')
else:
    print('Точка не находится в указанной прямоугольной области')


