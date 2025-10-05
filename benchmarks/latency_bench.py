import numpy as np, time, csv, os

def run_latency_bench(sizes=None, repeats=3, outfile="latency_vs_size.csv"):
    """
    Run latency benchmark for various matrix sizes and save results to CSV.
    Parameters:
        sizes   : iterable of matrix sizes (default: 64–2048 step 64)
        repeats : how many times to repeat each size
        outfile : CSV output filename
    """
    if sizes is None:
        sizes = range(64, 2049, 64)

    rows = []
    threads = (
        os.environ.get("OPENBLAS_NUM_THREADS")
        or os.environ.get("OMP_NUM_THREADS")
        or "auto"
    )

    print(f"Running latency benchmark | BLAS threads: {threads}")
    print("matrix_n, avg_latency_s")

    for n in sizes:
        total = 0.0
        for _ in range(repeats):
            A = np.random.random((n, n)).astype(np.float32)
            B = np.random.random((n, n)).astype(np.float32)
            t0 = time.perf_counter()
            _ = A @ B
            t1 = time.perf_counter()
            total += (t1 - t0)
        avg = total / repeats
        print(f"{n:7d}, {avg:.6f}")
        rows.append([n, avg, repeats, threads])

    with open(outfile, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["matrix_n", "avg_latency_s", "repeats", "blas_threads"])
        w.writerows(rows)

    print(f"\n✅ Results saved to {outfile}")

# allow running directly as script too
if __name__ == "__main__":
    run_latency_bench()
