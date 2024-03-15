import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D

data = {
    "fft_return": [
        {
            "ts": "2024-01-30T12:34:56",
            "data_fft": {
                "acc_rms_x": {
                    "freq": [1, 2, 3, 4, 5],
                    "magnitude": [0.123, 0.456, 0.789, 0.321, 0.567]
                }
            }
        },
        {
            "ts": "2024-01-30T14:34:56",
            "data_fft": {
                "acc_rms_x": {
                    "freq": [1, 2, 3, 4, 5],
                    "magnitude": [0.789, 0.321, 0.654, 0.987, 0.543]
                }
            }
        },
        {
            "ts": "2024-01-30T16:34:56",
            "data_fft": {
                "acc_rms_x": {
                    "freq": [1, 2, 3, 4, 5],
                    "magnitude": [0.111, 0.222, 0.333, 0.444, 0.555]
                }
            }
        },
        {
            "ts": "2024-01-30T18:34:56",
            "data_fft": {
                "acc_rms_x": {
                    "freq": [1, 2, 3, 4, 5],
                    "magnitude": [0.246, 0.135, 0.579, 0.864, 0.213]
                }
            }
        },
        {
            "ts": "2024-01-30T20:34:56",
            "data_fft": {
                "acc_rms_x": {
                    "freq": [1, 2, 3, 4, 5],
                    "magnitude": [0.753, 0.684, 0.245, 0.936, 0.357]
                }
            }
        }
    ]
}

freq_data = defaultdict(list)

for entry in data["fft_return"]:
    freq = entry["data_fft"]["acc_rms_x"]["freq"]
    magnitudes = entry["data_fft"]["acc_rms_x"]["magnitude"]
    timestamp = datetime.strptime(entry["ts"], "%Y-%m-%dT%H:%M:%S").timestamp()  # 转换为Unix时间戳
    for f, mag in zip(freq, magnitudes):
        freq_data[f].append((timestamp, mag))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

for freq, time_mag_list in freq_data.items():
    timestamps, magnitudes = zip(*time_mag_list)
    ax.plot(timestamps, [freq] * len(timestamps), magnitudes, label=f"Frequency {freq}")

ax.set_xlabel('Time (Unix Timestamp)')
ax.set_ylabel('Frequency')
ax.set_zlabel('Magnitude')

plt.title('Magnitude vs Time vs Frequency')
plt.legend()
plt.tight_layout()
plt.show()
