import numpy as np
import time
import csv
import os
import subprocess

# ---------------------------------
# Function to read CPU frequency
# ---------------------------------
def get_cpu_freq_mhz():
    """Return current ARM CPU frequency (MHz) using vcgencmd."""
    out = subprocess.check_output(
        ["vcgencmd", "measure_clock", "arm"],
        text=True
    )
    freq_hz = int(out.strip().split('=')[1])
    return freq_hz / 1_000_000.0


# ---------------------------------
# Combined Benchmark
# ---------------------------------
def run_latency_freq_bench(sizes=None, repeats=3, outfile="../Results/latency_freq_results.csv"):
    """
    Run a combined benchmark that measures both:
      - Latency (time for matrix multiplication)
      - CPU frequency (MHz)
    for each matrix size.
    Saves all data to a CSV.
    """

    os.makedirs(os.path.dirname(outfile), exist_ok=True)

    if sizes is None:
        sizes = range(64, 2049, 64)

    rows = []
    threads = (
        os.environ.get("OPENBLAS_NUM_THREADS")
        or os.environ.get("OMP_NUM_THREADS")
        or "auto"
    )

    print(f"Running combined latency + frequency benchmark | BLAS threads: {threads}")
    print("matrix_n, avg_latency_s, avg_cpu_freq_mhz")

    for n in sizes:
        total_time = 0.0
        freqs = []

        for _ in range(repeats):
            A = np.random.random((n, n)).astype(np.float32)
            B = np.random.random((n, n)).astype(np.float32)

            # measure frequency before and after multiplication
            freq_before = get_cpu_freq_mhz()

            t0 = time.perf_counter()
            _ = A @ B
            t1 = time.perf_counter()

            freq_after = get_cpu_freq_mhz()

            total_time += (t1 - t0)
            freqs.append((freq_before + freq_after) / 2)

        avg_time = total_time / repeats
        avg_freq = np.mean(freqs) if freqs else None

        print(f"{n:7d}, {avg_time:.6f}, {avg_freq:.1f} MHz")

        rows.append([n, avg_time, avg_freq, repeats, threads])

    # Save results
    with open(outfile, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["matrix_n", "avg_latency_s", "cpu_freq_mhz", "repeats", "blas_threads"])
        w.writerows(rows)

    print(f"\n✅ Combined results saved to {os.path.abspath(outfile)}")


# ---------------------------------
# Run when executed directly
# ---------------------------------
if __name__ == "__main__":
    run_latency_freq_bench()
