#!/usr/bin/env python3
import numpy as np
import time
import subprocess
import csv
import argparse

# --- Helper functions ---
def get_temp():
    """Read CPU temperature in °C."""
    out = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
    return float(out.replace("temp=", "").replace("'C\n", ""))

def get_freq():
    """Read CPU frequency of core 0 in MHz."""
    out = subprocess.check_output(
        ["cat", "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"],
        shell=True
    ).decode()
    return int(out.strip()) / 1000.0  # kHz → MHz

def get_voltage():
    """Read core voltage in V."""
    out = subprocess.check_output(["vcgencmd", "measure_volts", "core"]).decode()
    return float(out.replace("volt=", "").replace("V\n", ""))

def get_throttled():
    """Read throttled flags (hex string)."""
    out = subprocess.check_output(["vcgencmd", "get_throttled"]).decode()
    return out.strip()

# --- Benchmark function ---
def run_benchmark(N=512, dtype="float32", iters=200, outfile="thermal_log.csv"):
    """
    Run matrix multiplication benchmark on Raspberry Pi 5.
    Saves telemetry (runtime, temp, freq, voltage, throttled) into a CSV file.
    """
    dtype_map = {"float32": np.float32, "float64": np.float64}
    dtype = dtype_map[dtype]

    with open(outfile, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["iter", "runtime_s", "temp_C", "cpu_freq_MHz", "voltage_V", "throttled"])

        # Fixed matrices for consistency
        A = np.random.rand(N, N).astype(dtype)
        B = np.random.rand(N, N).astype(dtype)

        for i in range(1, iters + 1):
            t0 = time.time()
            _ = np.dot(A, B)
            t1 = time.time()

            runtime = t1 - t0
            temp = get_temp()
            freq = get_freq()
            volt = get_voltage()
            throttled = get_throttled()

            writer.writerow([i, runtime, temp, freq, volt, throttled])
            f.flush()

            print(f"Iter {i}/{iters}: time={runtime:.4f}s "
                  f"temp={temp:.1f}°C freq={freq:.0f}MHz "
                  f"volt={volt:.3f}V throttle={throttled}")

# --- CLI entry point ---
def main():
    parser = argparse.ArgumentParser(description="Thermal benchmarking on Raspberry Pi 5")
    parser.add_argument("--N", type=int, default=512, help="Matrix size N for NxN multiplication")
    parser.add_argument("--dtype", choices=["float32","float64"], default="float32", help="Data type")
    parser.add_argument("--iters", type=int, default=200, help="Number of iterations")
    parser.add_argument("--outfile", type=str, default="thermal_log.csv", help="Output CSV file")

    # ✅ Allow Jupyter to pass its hidden -f argument without error
    args, unknown = parser.parse_known_args()

    run_benchmark(args.N, args.dtype, args.iters, args.outfile)

if __name__ == "__main__":
    main()
