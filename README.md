
# EN
**GenHTU21DSensorReader** is a Python-based program designed to read temperature and humidity data from the HTU21D sensor using an ESP32 board. The program communicates with the sensor over the I2C protocol and outputs the data to a console or any connected device. The code has been optimized for clarity, efficiency, and ease of use.

## Features

- Reads temperature and humidity from the HTU21D sensor.
- Outputs temperature in Celsius or Fahrenheit.
- Configurable measurement resolution.
- Toggleable heater for diagnostic use.
- Simple and efficient error handling.
- Easy to integrate into existing projects.


## How to Use 
### Hardware Requirements

- ESP32 Development Board.
- HTU21D Temperature & Humidity Sensor.
- Jumper wires to connect the sensor and ESP32.

### Software Requirements

- Python with `micropython` package installed.
- Suitable tool to upload code to ESP32 (e.g., `ampy` or `rshell`).

## Installation & Setup

1. **Wiring the Sensor**: Connect the HTU21D sensor to the ESP32 board using I2C pins:
   - `SCL` pin to GPIO 23
   - `SDA` pin to GPIO 22
   - Power and ground connections as per the sensor's requirements.

2. **Code Upload**: Clone the repository and upload the required files to your ESP32:
    ```bash
    git clone https://github.com/geniuszly/GenHTU21DSensorReader
    cd GenHTU21DSensorReader
    ```

3. **Uploading to ESP32**: Use `ampy` or `rshell` to upload the `.py` files:
    ```bash
    ampy --port /dev/ttyUSB0 put htu21d.py
    ampy --port /dev/ttyUSB0 put sensor_config.py
    ampy --port /dev/ttyUSB0 put sensor_utils.py
    ampy --port /dev/ttyUSB0 put main.py
    ```

4. **Running the Code**: Once all files are uploaded, run the `main.py` on your ESP32:
    ```bash
    ampy --port /dev/ttyUSB0 run main.py
    ```

## Example Output

```
Текущие данные: Температура (°C), Влажность (%)
[Температура: 24.56°C, Влажность: 45.23%]
[Температура: 24.60°C, Влажность: 45.10%]
[Температура: 24.63°C, Влажность: 45.15%]
[Температура: 24.70°C, Влажность: 45.05%]
[Температура: 24.75°C, Влажность: 45.00%]
...
```
After starting the program, you should see a continuous output of temperature and humidity readings every minute.

![image](https://github.com/user-attachments/assets/2998b0ba-9615-4656-a5f1-79fd074091b7)


## RU

**GenHTU21DSensorReader** — это программа на Python, предназначенная для считывания данных о температуре и влажности с датчика HTU21D с использованием платы ESP32. Программа взаимодействует с датчиком по протоколу I2C и выводит данные на консоль или любое подключенное устройство. Код оптимизирован для простоты, эффективности и легкости использования.

## Возможности

- Считывание температуры и влажности с датчика HTU21D.
- Вывод температуры в градусах Цельсия или Фаренгейта.
- Настраиваемое разрешение измерений.
- Возможность включения/выключения нагревателя для диагностики.
- Простая и эффективная обработка ошибок.
- Легкость интеграции в существующие проекты.

## Как использовать
### Необходимое оборудование

- Плата разработки ESP32.
- Датчик температуры и влажности HTU21D.
- Соединительные провода для подключения датчика и ESP32.

### Программное обеспечение

- Python с установленным пакетом `micropython`.
- Инструмент для загрузки кода на ESP32 (например, `ampy` или `rshell`).

## Установка и настройка

1. **Подключение датчика**: Подключите датчик HTU21D к плате ESP32, используя I2C-пины:
   - Пин `SCL` к GPIO 23
   - Пин `SDA` к GPIO 22
   - Питание и земля в соответствии с требованиями датчика.

2. **Загрузка кода**: Клонируйте репозиторий и загрузите необходимые файлы на ESP32:
    ```bash
    git clone https://github.com/geniuszly/GenHTU21DSensorReader
    cd GenHTU21DSensorReader
    ```

3. **Загрузка на ESP32**: Используйте `ampy` или `rshell` для загрузки файлов `.py`:
    ```bash
    ampy --port /dev/ttyUSB0 put htu21d.py
    ampy --port /dev/ttyUSB0 put sensor_config.py
    ampy --port /dev/ttyUSB0 put sensor_utils.py
    ampy --port /dev/ttyUSB0 put main.py
    ```

4. **Запуск программы**: После загрузки всех файлов выполните запуск `main.py` на ESP32:
    ```bash
    ampy --port /dev/ttyUSB0 run main.py
    ```

## Пример вывода

```
Текущие данные: Температура (°C), Влажность (%)
[Температура: 24.56°C, Влажность: 45.23%]
[Температура: 24.60°C, Влажность: 45.10%]
[Температура: 24.63°C, Влажность: 45.15%]
[Температура: 24.70°C, Влажность: 45.05%]
[Температура: 24.75°C, Влажность: 45.00%]
...
```
После запуска программы вы должны увидеть непрерывный вывод данных о температуре и влажности каждую минуту.

![image](https://github.com/user-attachments/assets/31502c5d-72d7-4c70-bb8f-84180c20d2f0)
