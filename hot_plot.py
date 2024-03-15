import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors
import random
from datetime import datetime, timedelta
start_time = datetime(2024, 1, 30)

data = {
    "fft_return": [
        {
            "ts": (start_time + timedelta(hours=i)).strftime("%Y-%m-%dT%H:%M:%S"),
            "data_fft": {
                "acc_rms_x": {
                    "freq": list(range(1, 101)),
                    "magnitude": [random.random() * 0.15 for _ in range(100)]
                }
            }
        }
        for i in range(100)
    ]
}
ts_list = [datetime.strptime(entry['ts'], "%Y-%m-%dT%H:%M:%S") for entry in data['fft_return']]
freq = data['fft_return'][0]['data_fft']['acc_rms_x']['freq']
magnitude = [entry['data_fft']['acc_rms_x']['magnitude'] for entry in data['fft_return']]
magnitude = np.flipud(np.transpose(np.array(magnitude)))
print(magnitude[30])


magnitude[50] = np.linspace(0, 1, 100)
magnitude[80] = np.linspace(0.3, 0.3, 100)
magnitude[20] = np.linspace(0.2, 0.2, 100)
# magnitude[40] = np.linspace(0.6, 0.6, 50)

print(magnitude[30])
# 设置图像显示比例
plt.imshow(magnitude, cmap='inferno', interpolation='bilinear', aspect='auto')
plt.colorbar()  # 添加颜色条


# 修改X轴和Y轴标签
plt.xticks(np.arange(0, len(ts_list), step=10), [ts.strftime("%H:%M") for ts in ts_list[::10]], rotation=45)
plt.yticks(np.arange(0, len(freq), step=10), freq[::-1][::10])

plt.xlabel('Time')
plt.ylabel('Frequency')
plt.tight_layout()  # 自动调整布局
plt.show()
