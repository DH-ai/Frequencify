import numpy as np
import matplotlib.pyplot as plt

# Define sample rate and duration
sample_rate = 44100
duration = 0.004

# Generate time axis
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate two sine waves of different frequencies
freq1 = 440  # Frequency of the first sine wave (A4)
freq2 = 880  # Frequency of the second sine wave (A5)

# Generate the two sine waves
wave1 = 0.5 * np.sin(2 * np.pi * freq1 * t)
wave2 = 0.5 * np.sin(2 * np.pi * freq2 * t)

# Add the two waves element-wise
combined_wave = wave1 + wave2
def addNpArray(arr1:np.array,arr2:np.array,sr,dr)->np.array:
    

    for i in range(int(dr*sr)):
        
        arr1[i]+=arr2[i]

    return arr1
wave3=addNpArray(wave1,wave2,sample_rate,duration)
# Plot the waves
plt.figure(figsize=(12, 4))
plt.subplot(4, 1, 1)
plt.title('Wave 1')
plt.plot(t, wave1)
plt.subplot(4, 1, 2)
plt.title('Wave 2')
plt.plot(t, wave2)
plt.subplot(4, 1, 3)
plt.title('Combined Wave')
plt.plot(t, combined_wave)
plt.subplot(4, 1, 4)
plt.title('Wave3')
plt.plot(t, wave3)
plt.tight_layout()
plt.show()

