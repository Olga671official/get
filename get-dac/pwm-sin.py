#!/usr/bin/env python3

import pwm_dac
import signal_generator
import time

AMPLITUDE = 1.65   # Амплитуда сигнала (В) - половина от 3.3В
FREQUENCY = 2      # Частота сигнала (Гц)
OFFSET = 1.65      # Смещение сигнала (В) - середина диапазона 0-3.3В
DURATION = 0.1     # Длительность шага обновления (сек)

POINTS_PER_PERIOD = 100

def main():
    dac = None
    
    try:
        dac = pwm_dac.PWM_DAC()
        
        print("Генерация синусоидального сигнала...")
        print(f"Амплитуда: {AMPLITUDE}В, Частота: {FREQUENCY}Гц, Смещение: {OFFSET}В")
        print("Для остановки нажмите Ctrl+C")
        
        while True:
            for voltage in signal_generator.sine_wave(
                amplitude=AMPLITUDE,
                frequency=FREQUENCY,
                offset=OFFSET,
                duration=DURATION,
                samples=POINTS_PER_PERIOD
            ):
                dac.set_voltage(voltage)
                time.sleep(DURATION / POINTS_PER_PERIOD)
                
    except KeyboardInterrupt:
        print("\nГенерация остановлена пользователем")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if dac is not None:
            print("Очистка ресурсов ЦАП...")
            dac.cleanup()  # или dac.__del__() в зависимости от реализации
            print("Завершение работы")

if __name__ == "__main__":
    main()
