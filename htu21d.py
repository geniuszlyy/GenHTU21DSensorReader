import utime
from sensor_config import HTU21DMode, SensorRegisters, UserRegOptions, TempUnits
from sensor_utils import process_sensor_data

class HTU21DSensor:
    Mode = HTU21DMode
    RegOptions = UserRegOptions
    Units = TempUnits

    def __init__(self):
        self.i2c = None

    def initialize(self, scl_pin=23, sda_pin=22, frequency=100000):
        from machine import I2C, Pin
        self.i2c = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=frequency)
        self.reset_sensor()
        self.i2c.writeto(SensorRegisters.I2C_ADDR, bytearray([SensorRegisters.CMD_READ_REG]))
        register_value = self.i2c.readfrom(SensorRegisters.I2C_ADDR, 1)[0]
        return register_value == 0x2

    def set_resolution(self, resolution_value):
        current_reg = self._read_register()
        current_reg &= ~UserRegOptions.RES_MASK
        current_reg |= (resolution_value & UserRegOptions.RES_MASK)
        self._write_register(current_reg)

    def toggle_heater(self):
        self._toggle_register_bit(UserRegOptions.HEATER_BIT)

    def toggle_otp(self):
        self._toggle_register_bit(UserRegOptions.DISABLE_OTP)

    def _toggle_register_bit(self, bit_mask):
        current_reg = self._read_register()
        current_reg ^= bit_mask
        self._write_register(current_reg)

    def _read_register(self):
        self.i2c.writeto(SensorRegisters.I2C_ADDR, bytearray([SensorRegisters.CMD_READ_REG]))
        return self.i2c.readfrom(SensorRegisters.I2C_ADDR, 1)[0]

    def _write_register(self, value):
        self.i2c.writeto(SensorRegisters.I2C_ADDR, bytearray([SensorRegisters.CMD_WRITE_REG, value]))

    def read_temperature(self, mode=Mode.WITH_HOLD, unit=Units.CELSIUS, crc_check=True):
        command = SensorRegisters.CMD_TEMP_HOLD if mode == HTU21DMode.WITH_HOLD else SensorRegisters.CMD_TEMP_NO_HOLD
        self.i2c.writeto(SensorRegisters.I2C_ADDR, bytearray([command]))
        utime.sleep_ms(50)

        data = self.i2c.readfrom(SensorRegisters.I2C_ADDR, 3)
        raw_temp = process_sensor_data(data, crc_check)

        temperature = -46.85 + (175.72 * raw_temp / 65536)
        return temperature if unit == self.Units.CELSIUS else (temperature * 9.0) / 5.0 + 32

    def read_humidity(self, mode=Mode.WITH_HOLD, crc_check=True):
        command = SensorRegisters.CMD_HUMID_HOLD if mode == HTU21DMode.WITH_HOLD else SensorRegisters.CMD_HUMID_NO_HOLD
        self.i2c.writeto(SensorRegisters.I2C_ADDR, bytearray([command]))
        utime.sleep_ms(50)

        data = self.i2c.readfrom(SensorRegisters.I2C_ADDR, 3)
        raw_humidity = process_sensor_data(data, crc_check)
        return -6 + (125.0 * raw_humidity / 65536)

    def reset_sensor(self):
        self.i2c.writeto(SensorRegisters.I2C_ADDR, bytearray([SensorRegisters.CMD_RESET]))
        utime.sleep_ms(15)

    @property
    def is_battery_low(self):
        return bool(self._read_register() & UserRegOptions.BATTERY_LOW)

    @property
    def is_heater_active(self):
        return bool(self._read_register() & UserRegOptions.HEATER_BIT)

    @property
    def is_otp_enabled(self):
        return not bool(self._read_register() & UserRegOptions.DISABLE_OTP)
