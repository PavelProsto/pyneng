# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_add = input("Введите IP адрес в формате 10.0.1.1 ")
cont = ip_add.split('.')
try:
    for ip in cont:
        if ip.isdigit():
            pass
        else:
            #print("Неправильный IP-адрес")
            break
        if int(ip) in range(1,256):
            pass
        else:
            #print("Неправильный IP-адрес")
            break
    if ip_add == '255.255.255.255':
        print('local broadcast')
    elif int(ip_add.split('.')[0]) in range(1,224):
        print('unicast')
    elif int(ip_add.split('.')[0]) in range(224,240):
        print('multicast')
    elif ip_add == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
#print(cont)
#try:
#    for ip in cont:
#        if ip.isdigit():
#            if ip not in range(1,256):
#                print("Неправильный ")
#                break
except (ValueError):
    print("Неправильный IP-адрес")

