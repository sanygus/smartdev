##Software
####[Arduino](https://github.com/sanygus/smartdev/tree/master/software/arduino)
**Не для Raspberry Pi, на отдельном компьютере**

1. Установить [Arduino IDE](https://www.arduino.cc/en/Main/Software) (>=1.6.6)
2. Подключить Arduino UNO через USB
3. Открыть [Sketch](https://github.com/sanygus/smartdev/tree/master/software/arduino/sketch.ino) в Arduino IDE
4. Настроить Arduino IDE:
  1. Инструменты -> Плата -> Arduino UNO
  2. Инструменты -> Порт -> [COMxx] (для Windows: можно определить в Диспетчере устройств)
5. Файл -> Вгрузить (Ctrl+U)

####Веб-интерфейс ([www](https://github.com/sanygus/smartdev/tree/master/software/www))
В основном управление всем устройством и просмотр информации осуществляется через web-интерфейс.
Работает на PHP.

Требования: *Apache 2* + *PHP 5*

####Общение с Arduino ([python](https://github.com/sanygus/smartdev/tree/master/software/python))
Python скрипт *c.py* общается с arduino и выполняет необходимые комманды.

* *voff.var* - значение вольтажа для отключения
* *von.var* - значение вольтажа для включения (после отключения)
