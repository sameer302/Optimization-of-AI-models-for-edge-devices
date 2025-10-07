import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================================
# 1️⃣ Plot Matrix Size vs Latency and CPU Frequency
# ============================================================

def plot_latency_and_freq(csv_path="./Results/latency_freq_results.csv",
                          save_path="./Results/matrix_size_vs_latency_freq.png",
                          show_table=False):
    """
    Plot Matrix Size vs Latency and CPU Frequency.
    Displays inline (in Jupyter) and saves the plot as PNG/JPG.

    Parameters:
        csv_path : str  → path to the CSV file
        save_path : str → where to save the plot image
        show_table : bool → whether to print first few rows of the data
    """

    # Load data
    df = pd.read_csv(csv_path)
    if show_table:
        print("📊 First few rows of data:")
        print(df.head(), "\n")

    # Round frequency to remove minor fluctuations
    df["cpu_freq_mhz_rounded"] = df["cpu_freq_mhz"].round(0)
    mean_freq = df["cpu_freq_mhz"].mean()

    # Ensure output folder exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Create the plot
    fig, ax1 = plt.subplots(figsize=(7, 5))

    # Latency (blue, left axis)
    ax1.plot(df["matrix_n"], df["avg_latency_s"], 'o-', color='tab:blue', label="Latency (s)")
    ax1.set_xlabel("Matrix Size (n)")
    ax1.set_ylabel("Latency (seconds)", color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # CPU Frequency (red, right axis)
    ax2 = ax1.twinx()
    ax2.plot(df["matrix_n"], df["cpu_freq_mhz_rounded"], 'x', color='tab:red', alpha=0.5, label="Measured Freq (MHz)")
    ax2.axhline(mean_freq, color='tab:red', linestyle='--', label=f"Avg Freq ≈ {mean_freq:.0f} MHz")
    ax2.set_ylabel("CPU Frequency (MHz)", color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Title, grid, legend
    plt.title("Matrix Size vs Latency and CPU Frequency")
    plt.grid(True, linestyle='--', alpha=0.6)
    fig.tight_layout()

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc="best")

    # Save and show
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()

    print(f"✅ Latency-Frequency plot saved to: {os.path.abspath(save_path)}")


# ============================================================
# 2️⃣ Plot Matrix Size vs GFLOPS and CPU Frequency
# ============================================================

def plot_gflops_and_freq(csv_path="./Results/latency_freq_results.csv",
                         save_path="./Results/matrix_size_vs_gflops_freq.png",
                         show_table=False):
    """
    Plot Matrix Size vs GFLOPS and CPU Frequency.
    Displays inline (in Jupyter) and saves the plot as PNG/JPG.

    Parameters:
        csv_path : str  → path to the CSV file
        save_path : str → where to save the plot image
        show_table : bool → whether to print first few rows of the data
    """

    # Load data
    df = pd.read_csv(csv_path)
    if show_table:
        print("📊 First few rows of data:")
        print(df.head(), "\n")

    # Compute GFLOPS
    df["GFLOPS"] = 2 * (df["matrix_n"] ** 3) / (df["avg_latency_s"] * 1e9)

    # Round frequency to remove decimal noise
    df["cpu_freq_mhz_rounded"] = df["cpu_freq_mhz"].round(0)
    mean_freq = df["cpu_freq_mhz"].mean()

    # Ensure output folder exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Create the plot
    fig, ax1 = plt.subplots(figsize=(7, 5))

    # GFLOPS (green, left axis)
    ax1.plot(df["matrix_n"], df["GFLOPS"], 'o-', color='tab:green', label="GFLOPS")
    ax1.set_xlabel("Matrix Size (n)")
    ax1.set_ylabel("GFLOPS (Billion Floating Point Ops/sec)", color='tab:green')
    ax1.tick_params(axis='y', labelcolor='tab:green')

    # CPU Frequency (red, right axis)
    ax2 = ax1.twinx()
    ax2.plot(df["matrix_n"], df["cpu_freq_mhz_rounded"], 'x', color='tab:red', alpha=0.5, label="Measured Freq (MHz)")
    ax2.axhline(mean_freq, color='tab:red', linestyle='--', label=f"Avg Freq ≈ {mean_freq:.0f} MHz")
    ax2.set_ylabel("CPU Frequency (MHz)", color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Title, grid, legend
    plt.title("Matrix Size vs GFLOPS and CPU Frequency")
    plt.grid(True, linestyle='--', alpha=0.6)
    fig.tight_layout()

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc="best")

    # Save and show
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()

    print(f"✅ GFLOPS-Frequency plot saved to: {os.path.abspath(save_path)}")
