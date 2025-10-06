import pandas as pd
import matplotlib.pyplot as plt

def plot_benchmark(csv_file):
    # -----------------------------
    # Load data
    # -----------------------------
    df = pd.read_csv(csv_file)

    # If GFLOPS column not present, compute it
    if "GFLOPS" not in df.columns:
        df["GFLOPS"] = 2 * (df["matrix_n"] ** 3) / (df["avg_latency_s"] * 1e9)

    # -----------------------------
    # Plot 1: Matrix size vs Runtime
    # -----------------------------
    plt.figure(figsize=(7,5))
    plt.plot(df["matrix_n"], df["avg_latency_s"], marker="o")
    plt.title("Matrix Size vs Runtime (Latency)")
    plt.xlabel("Matrix Size (n x n)")
    plt.ylabel("Average Runtime (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # -----------------------------
    # Plot 2: Matrix size vs GFLOPS
    # -----------------------------
    plt.figure(figsize=(7,5))
    plt.plot(df["matrix_n"], df["GFLOPS"], marker="o", color="green")
    plt.title("Matrix Size vs Performance (GFLOPS)")
    plt.xlabel("Matrix Size (n x n)")
    plt.ylabel("GFLOPS (Billion Floating Point Ops/sec)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Return dataframe for further analysis
    return df
