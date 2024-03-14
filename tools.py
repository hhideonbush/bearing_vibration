import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

def read_original_file(file_name='./data/ftt-sample.sql'):
    '''
    just for demo
    '''
    with open(file_name, 'r') as file:
        lines = file.readlines()

    header = [col.strip() for col in lines[0].split('|')]
    data = [row.strip().split('|') for row in lines[1:]]

    print("Columns:", header)

    # 30 * 13 * x
    print("Data:")
    for i in range(len(data)-2):
        print(i)
        temp = []
        for j in range(4,13):
            temp.append(len(data[i][j]))
        print(temp)
    return header, data


def fft(signal, sampling_rate, debias=True):
    signal_length = len(signal)

    # 去掉偏置
    if debias:
        signal_mean = np.mean(signal)
        signal = signal - signal_mean

    fft_result = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(signal_length, d=1/sampling_rate)
    # 只保留正频率部分 numpy.ndarray
    positive_freq_mask = frequencies >= 0
    positive_frequencies = frequencies[positive_freq_mask]
    magnitude_spectrum = np.abs(fft_result[positive_freq_mask])

    # print(magnitude_spectrum)
    # plt.plot(positive_frequencies, magnitude_spectrum)
    # plt.show()
    return positive_frequencies, magnitude_spectrum


def envelope_spectrum(signal, sampling_rate, debias=True):
    # 去掉偏置
    if debias:
        signal_mean = np.mean(signal)
        signal = signal - signal_mean

    # 使用 Hilbert 变换获取包络线
    analytic_signal = hilbert(signal)
    envelope = np.abs(analytic_signal)

    # 对包络线进行 FFT
    envelope_spectrum = np.fft.fft(envelope)
    frequencies = np.fft.fftfreq(len(envelope), d=1/sampling_rate)

    # 保留正频率部分
    positive_freq_mask = frequencies >= 0
    positive_frequencies = frequencies[positive_freq_mask]
    envelope_spectrum = np.abs(envelope_spectrum[positive_freq_mask])

    return positive_frequencies, envelope_spectrum



if __name__ == "__main__":
    # 生成示例信号
    sampling_rate = 1000  # 采样率
    t = np.arange(0, 1, 1/sampling_rate)  # 时间轴
    frequency = 100  # 信号频率
    signal = np.sin(2 * np.pi * frequency * t)

    # 进行 FFT 分析
    fft(signal, sampling_rate, False)