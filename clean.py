#The bandpass function creates weights according to params that the filter uses.

def bandpass(lowcut, highcut, fs, order=3):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = butter(order, [low, high], 'bandpass', analog=False, output="sos")
    return sos

cutoff_high = 0.5
cutoff_low = 30

fs = 200
order = 3
sos = bandpass(cutoff_low, cutoff_high, fs, order=order)

#sos => weights for filter. We can use this to clean the signal.

maxx = np.max(signal)
minn = np.min(signal)
signal = (signal - minn) / (maxx - minn + 1e-6)
signal = sosfilt(sos, signal)

