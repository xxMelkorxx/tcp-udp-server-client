from socket import *

def start_tcp_server(addr):
    """
    Запуск TCP-сервера.
    :param addr: Адрес сервера.
    """
    # Создание сокета.
    with socket(family=AF_INET, type=SOCK_STREAM) as s:
        # Связывание адреса и порта сокета.
        s.bind(addr)
        # Запуск приёма TCP.
        s.listen()
        while True:
            print('Ожидание соединения...')
            try:
                # Установление соединения с клиентом.
                conn, addr = s.accept()
                print(f'IP-клиента: {addr}')
                # Получение сообщение от клиента
                data = conn.recv(1024).decode()
                print(f'Клиент: {data}')
                if data == 'stop':
                    conn.send('Сервер остановлен...'.encode())
                    conn.close()
                    break
                # Отправка ответного сообщения клиенту.
                answer = input('Ответ клиенту: ').encode()
                conn.send(answer)
                conn.close()
            except ConnectionRefusedError as e:
                print(str(e))
                print('Клиент не отвечает...')
            except ConnectionResetError as e:
                print(str(e))
                print('Клиент не отвечает...')

def start_udp_server(addr):
    """
    Запуск UDP-сервера.
    :param addr: Адрес сервера.
    """
    # Создание сокета.
    with socket(family=AF_INET, type=SOCK_DGRAM) as s:
        # Связывание адреса и порта сокета.
        s.bind(addr)

        while True:
            try:
                print('Ожидание соединения...')
                # Установление соединения и получение сообщение от клиента.
                data, addr = s.recvfrom(1024)
                print(f'Адрес клиента: {addr[0]}:{addr[1]}; Cообщение: {data.decode()}')
                if data.decode() == 'stop':
                    s.sendto('Сервер остановлен...'.encode(), addr)
                    break
                # Отправка ответного сообщения клиенту.
                answer = input('Ответ клиенту: ').encode()
                s.sendto(answer, addr)
            except ConnectionResetError as e:
                print(str(e))
                print('Клиент не отвечает...')

###########################################################################################################################
if __name__ == '__main__':
    # Данные сервера.
    host = '192.168.1.114'
    port = 777

    while True:
        socket_kind = input('Что хотите запустить (TCP - 1 или UDP - 2): ')

        if socket_kind == '1':
            start_tcp_server((host, port))
        elif socket_kind == '2':
            start_udp_server((host, port))
        else:
            break
