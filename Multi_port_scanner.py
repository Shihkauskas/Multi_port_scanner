# -*- coding:utf-8 -*-

import time
import socket
from concurrent.futures import ThreadPoolExecutor


def one_port_scan(host, port):
    start = time.time()
    with socket.socket() as scan:
        try:
            scan.connect((host, port))
        except socket.error:
            print('\nВремя сканирования: ', format(time.time() - start, '.2f'))
            print(port, ' -- close')
        else:
            print('\nВремя сканирования: ', format(time.time() - start, '.2f'))
            print(port, ' -- open')


def connect(host, port, results=None):
    try:
        socket.socket().connect((host, port))
        if results is not None:
            results.append(port)
        print(port, ' -- open')
        return True
    except:
        return False


def multi_port_scan(host):
    start = time.time()
    open_ports = []
    socket.setdefaulttimeout(0.5)
    with ThreadPoolExecutor(max_workers=512) as executor:
        print('\nИдёт сканирование ' + host, '\n')

        for port in range(65536):
            executor.submit(connect, host, port, open_ports)

    open_ports.sort()
    print('\nСканирование завершено\n')
    print('Время сканирования:', format(time.time() - start, '.2f'), ' сек')
    print('Открытых портов:', len(open_ports))
    print(', '.join([str(i) for i in open_ports]))  # Dark magic


def main():
    print('\n\t[1] --- сканировать один порт')
    print('\t[2] --- сканировать все порты\n')

    choice_list = input('Выберите параметр: ')
    if choice_list == '1':
        one_port_scan(
            input('Введите хост: '),
            int(input('Введите порт: '))
        )
    elif choice_list == '2':
        multi_port_scan(
            input('Введите хост: '))
    else:
        print('\nНе правильно выбран параметр!')


if __name__ == "__main__":
    main()
