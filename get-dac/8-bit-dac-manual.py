#!/usr/bin/env python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(pins, GPIO.OUT)
dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динмаический диапазон ЦАП (0.00 - {dynamic_range:.2f}) В")
        print("Устанавливаем 0.0 В")
        return 0
    
    return int(voltage / dynamic_range * 255)

def dec2bin(number):
    return [int(bit) for bit in bin(number)[2:].zfill(8)]

def number_to_dac(n):
    if not (0 <= n <= 255):
        print("Out of range [0, 255]")
        return
    bits = dec2bin(n)
    print(n, bits)
    GPIO.output(pins, bits)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            dac_bits = number_to_dac(number)
            print(number, dac_bits)
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()
