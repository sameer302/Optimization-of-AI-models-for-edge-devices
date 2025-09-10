#!/usr/bin/env python3

import numpy as np
import time
import psutil
import threading
import csv
import os

def estimate_flops(matrix_size, iterations=10):
    """
    Performs matrix multiplication and returns GFLOPS and latency in ms.
    """
    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)
    np.dot(A, B) # Warm-up

    start_op_time = time.time()
    for _ in range(iterations):
        np.dot(A, B)
    end_op_time = time.time()

    elapsed_time = end_op_time - start_op_time
    total_ops = 2 * (matrix_size ** 3) * iterations
    flops = total_ops / elapsed_time
    
    gflops = flops / 1e9
    latency_ms = elapsed_time * 1000

    return gflops, latency_ms

def benchmark_loop(max_size=9728, step=512):
    
    available_ram = psutil.virtual_memory().available
    print(f"Available RAM: {available_ram / (1024 ** 2):.2f} MiB")

    for size in range(step, max_size + step, step):
        required_mem = 2 * (size ** 2) * 8
        if required_mem > available_ram * 0.7:
            print(f"Skipping size {size}x{size} - too much memory.")
            continue
        print(f"--- Testing Size: {size}x{size} ---")
        gflops, latency_ms = estimate_flops(size)
        print(f"  -> Latency: {latency_ms:.2f} ms | GFLOPS: {gflops:.2f}")


def read_cpu_temp():
    # For Raspberry Pi: Read temperature (Celsius) from system file
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        return float(f.read()) / 1000

def temperature_logger(csv_path, stop_event, interval=1.0):
    with open(csv_path, mode='w', newline='') as logf:
        writer = csv.writer(logf)
        writer.writerow(['timestamp', 'temperature_C'])
        while not stop_event.is_set():
            ts = time.strftime('%Y-%m-%d %H:%M:%S')
            temp = read_cpu_temp()
            writer.writerow([ts, temp])
            logf.flush()
            time.sleep(interval)

# Place this before you start benchmark_loop()
temp_log_path = "logs/matmul_benchmark_temps.csv"
stop_event = threading.Event()
logger_thread = threading.Thread(target=temperature_logger, args=(temp_log_path, stop_event))
logger_thread.start()

# Run your benchmark code
benchmark_loop()

# After completion, stop the logger and join the thread
stop_event.set()
logger_thread.join()
print(f"Temperature log saved to {temp_log_path}")


