from socket import *

def start_tcp_client(addr):
    """
    # Запуск TCP-клиента.
    :param addr: Адрес сервера.
    """
    while True:
        # Создание сокета.
        s = socket(family=AF_INET, type=SOCK_STREAM)
        # Устанавление тайм-аута на ответ от сервера.
        s.settimeout(10)
        try:
            # Формирование сообщения серверу.
            data = input('Напиши серверу: ').encode()
            if not data:
                s.close()
                break
            # Соединения с сервером.
            s.connect(addr)
            # Отправка сообщения серверу.
            s.send(data)
            # Получение ответа от сервера.
            data = s.recv(1024).decode()
            print(f"Сервер: {data}")
        except ConnectionRefusedError:
            print('Сервер не отвечает...')
            continue
        except TimeoutError:
            print('Вышло время ожидание ответа от сервера...')
            continue
        finally:
            s.close()

def start_udp_client(addr):
    """
    # Запуск UDP-клиента.
    :param addr: Адрес сервера.
    """
    while True:
        # Создание сокета.
        s = socket(family=AF_INET, type=SOCK_DGRAM)
        # Устанавление тайм-аута на ответ от сервера.
        s.settimeout(10)
        try:
            # Формирование сообщения серверу.
            data = str.encode(input('Напиши серверу: '))
            if not data:
                s.close()
                break
            # Отправка сообщения серверу.
            s.sendto(data, addr)
            # Получение ответа от сервера.
            data = s.recvfrom(1024)
            print(f"Сервер: {data[0].decode()}")
        except ConnectionResetError:
            print('Отсутствует соединение с сервером...')
        except TimeoutError:
            print('Вышло время ожидание ответа от сервера...')
        finally:
            s.close()

###########################################################################################################################
if __name__ == '__main__':
    # Данные сервера.
    host = '192.168.1.114'  # '192.168.9.31'
    port = 777

    while True:
        socket_kind = input('Что хотите запустить (TCP - 1 или UDP - 2): ')

        if socket_kind == '1':
            start_tcp_client((host, port))
        elif socket_kind == '2':
            start_udp_client((host, port))
        else:
            break
