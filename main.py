from htu21d import HTU21DSensor
import utime

# Инициализация датчика HTU21D
sensor = HTU21DSensor()
sensor.initialize()

# Установка разрешения (RH12 и TEMP14)
sensor.set_resolution(sensor.RegOptions.RES_RH12_TEMP14)

# Включение нагревателя, если не активен
if not sensor.is_heater_active:
    sensor.toggle_heater()

# Постоянное считывание данных с датчика и вывод их на экран
print("Текущие данные: Температура (°C), Влажность (%)")
while True:
    try:
        temp = sensor.read_temperature(sensor.Mode.WITHOUT_HOLD, sensor.Units.CELSIUS)
        humidity = sensor.read_humidity(sensor.Mode.WITHOUT_HOLD)
        print(f"[Температура: {temp:.2f}°C, Влажность: {humidity:.2f}%]")
    except OSError:
        print("Ошибка чтения данных. Повторная попытка...", end="")
    utime.sleep(60)
