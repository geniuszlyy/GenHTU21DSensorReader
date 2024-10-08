# Конфигурационные классы и константы для работы с HTU21D

class HTU21DMode:
    WITH_HOLD = 0
    WITHOUT_HOLD = 1

class SensorRegisters:
    I2C_ADDR = 0x40
    CMD_TEMP_HOLD = 0xE3
    CMD_TEMP_NO_HOLD = 0xF3
    CMD_HUMID_HOLD = 0xE5
    CMD_HUMID_NO_HOLD = 0xF5
    CMD_WRITE_REG = 0xE6
    CMD_READ_REG = 0xE7
    CMD_RESET = 0xFE

class UserRegOptions:
    RES_MASK = 0x81
    RES_RH12_TEMP14 = 0x00
    RES_RH10_TEMP13 = 0x80
    RES_RH8_TEMP12 = 0x01
    RES_RH11_TEMP11 = 0x81
    BATTERY_LOW = 0x40
    HEATER_BIT = 0x04
    DISABLE_OTP = 0x02

class TempUnits:
    CELSIUS = 0
    FAHRENHEIT = 1
