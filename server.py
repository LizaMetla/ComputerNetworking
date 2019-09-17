import json
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # тот кто принимат данные
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # закрывать старые соединения и
# открывать новые с каждым запуском
server_socket.bind(('localhost', 5000))
server_socket.listen()  # для принятия данных сервером


def inPolygon(x, y, xp, yp):
    c = 0
    for i in range(len(xp)):
        if (((yp[i] <= y and y < yp[i - 1]) or (yp[i - 1] <= y and y < yp[i])) and (
                x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])): c = 1 - c
    return c


while True:
    print('Before .accept()')
    client_socket, addr = server_socket.accept()  # принимает подключения возвращая кортеж
    print('Connection from', addr)

    while True:
        print('Before .recv()')
        request = client_socket.recv(4096)  # объём памяти под каждое сообщение и возвр сообщение клиента серверу

        if not request:
            break
        else:
            points = json.loads(request.decode())
            ans = str(inPolygon(*points))
            client_socket.send(ans.encode())


