#### Принцип работы
Основным "мозгом" системы является Raspberry Pi. К нему подключен модуль камеры и USB-модем (без внешнего IP).
На Raspberry Pi поднят веб-сервер с веб-интерфейсом на PHP (через который управляется из внешнего мира). Чтобы можно было достучаться до Raspberry Pi из внешнего мира, поднят VPN-туннель (OpenVPN) до сервера с внешним IP.

На Raspberry Pi Python-скрипт "общается" с Arduino по шине [I2C](https://ru.wikipedia.org/wiki/I%C2%B2C).

Питанием всего этого пока происходит от БП 5V 2A. Raspberry Pi подключен к нему через реле, управляемое Arduino'й.

Чтобы построить такое же устройство, нужно выолнить 3 шага:

1. [**Hardware**](https://github.com/sanygus/smartdev/tree/master/hardware). Првильно собрать схему.
2. **Software-OS**. Сконфигурироавть Raspbian.
3. [**Software**](https://github.com/sanygus/smartdev/tree/master/software). Использовать ПО.
