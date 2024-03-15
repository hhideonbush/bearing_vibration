import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

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

# 提取数据
ts_list = [datetime.strptime(entry['ts'], "%Y-%m-%dT%H:%M:%S") for entry in data['fft_return']]
freq = data['fft_return'][0]['data_fft']['acc_rms_x']['freq']
magnitude = [entry['data_fft']['acc_rms_x']['magnitude'] for entry in data['fft_return']]

# 转换时间戳为数值
ts_numeric = [(ts - min(ts_list)).total_seconds() / 3600 for ts in ts_list]

# 转换 magnitude 到二维数组
magnitude = np.array(magnitude)

# 创建图形
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制每个频率对应的竖直面
for i, f in enumerate(freq):
    ax.bar(ts_numeric, magnitude[:, i], zs=f, zdir='y', alpha=0.8)

# 添加标签
ax.set_xlabel('Timestamp')
ax.set_ylabel('Frequency')
ax.set_zlabel('Magnitude')

# 设置视角
ax.view_init(elev=45, azim=45)  # 将视角调整为从上方俯视图

plt.show()
