import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/sameer/Desktop/Codespace/Optimization-of-AI-models-for-edge-devices/Benchmarking/FLOPS/logs/matmul_benchmark_temps.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['temperature_C'], marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.title('Raspberry Pi Temperature Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()

# Save the plot as an image file
plt.savefig('/home/sameer/Desktop/Codespace/Optimization-of-AI-models-for-edge-devices/Benchmarking/FLOPS/results/temperature_plot.png')

plt.show()
