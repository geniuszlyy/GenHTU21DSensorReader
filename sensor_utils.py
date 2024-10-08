# Утилиты для работы с данными датчика
def process_sensor_data(data_bytes, check_crc):
    if len(data_bytes) != 3:
        return 0.0
    raw_data = (data_bytes[0] << 8) | data_bytes[1]
    if check_crc and not verify_crc(raw_data, data_bytes[2]):
        raise ValueError("Ошибка: CRC несовпадает!")
    return raw_data & 0xFFFC

def verify_crc(raw, crc_value):
    remainder = (raw << 8) | crc_value
    divisor = 0x988000
    for _ in range(16):
        if remainder & (1 << (23 - _)):
            remainder ^= divisor
        divisor >>= 1
    return remainder == 0
