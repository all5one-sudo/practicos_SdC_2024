import time
import machine
import os

def int_sum():
    total = 0
    for i in range(333333):
        total += i
    return total

def float_sum():
    total = 0.0
    for i in range(240000):
        total += i
    return total

def log_time():
    file_name = 'time_log.csv'
    if not file_name in os.listdir():
        with open('time_log.csv', 'w') as file:
            file.write('freq(mhz),time(ms)\n')
    for fre in range(75, 136, 1):
        print('Testing...')
        machine.freq(fre * 1000000)
        start_time = time.ticks_ms()
        int_result = int_sum()
        int_time = time.ticks_diff(time.ticks_ms(), start_time)
        start_time = time.ticks_ms()
        float_result = float_sum()
        float_time = time.ticks_diff(time.ticks_ms(), start_time)
        total_time = int_time + float_time
        with open('time_log.csv', 'a') as file:
            file.write('{},{}\n'.format(fre,total_time))
        print('Clock frequency: ', fre, 'MHz')
        #print('Integer sum time: ', tiempo_enteros, 'ms')
        #print('Float sum time', tiempo_flotantes, 'ms')
        print('Total time: ', total_time, 'ms')
        time.sleep(.1)
    for fre in range(140, 251, 10):
        print('Testing...')
        machine.freq(fre * 1000000)
        start_time = time.ticks_ms()
        int_result = int_sum()
        int_time = time.ticks_diff(time.ticks_ms(), start_time)
        start_time = time.ticks_ms()
        float_result = float_sum()
        float_time = time.ticks_diff(time.ticks_ms(), start_time)
        total_time = int_time + float_time
        with open('time_log.csv', 'a') as file:
            file.write('{},{}\n'.format(fre,total_time))
        print('Clock frequency: ', fre, 'MHz')
        #print('Integer sum time: ', tiempo_enteros, 'ms')
        #print('Float sum time', tiempo_flotantes, 'ms')
        print('Total time: ', total_time, 'ms')
        time.sleep(1)

log_time()