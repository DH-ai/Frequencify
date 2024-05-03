import numpy as np
import sounddevice as sd
import time
import matplotlib as mlt
import matplotlib.pyplot as plt
# Function to generate a sine wave with given frequency and duration
def generate_sine_wave(frequency, duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    # print(t)
    
    # wave = np.sin(2 * np.pi * frequency * t)
    wave = np.sin(2 * np.pi * frequency * t)
    # print(wave)
    # wave=np.cos(2*np.pi*frequency*t)
    return wave
# y,x=generate_sine_wave(500,0.5,44000)
# # Function to play the generated wave
# print(x)
# plt.title("hoola")
# plt.plot(x,y,color="red")
# plt.show()


def play_wave(wave, sampling_rate):
    sd.play(wave, samplerate=sampling_rate)
    sd.wait()

# play_wave(y,44000)
# print("PLAYED")

# while True:
#     continue
# Test different frequencies
frequencies = [100, 200, 400, 800, 1600, 3200]  # Frequencies in Hz

# for frequency in frequencies:
#     print(f"Generating and playing sine wave with frequency: {frequency} Hz")
#     wave = generate_sine_wave(frequency, duration, sampling_rate)
#     play_wave(wave, sampling_rate)
sampling_rate=96200
# 556888 88 88 56888 88 88 56888 88 88 887
music_table=[392,392,440,1046.50,1046.50,1046.50,1046.50,0,1046.50,1046.50,0,1046.50,1046.50,0,392,392,440,1046.50,1046.50,1046.50,1046.50,0,1046.50,1046.50,0,1046.50,1046.50,0,392,392,440,1046.50,1046.50,1046.50,1046.50,0,1046.50,1046.50,0,1046.50,1046.50,0,1046.50,1046.50,493.88]
musicdict={
    '1':261.63,
    '2':293.66,
    '3':329.63,
    '4':349.23,
    '5':392.23,
    '6':440.00,
    '7':493.88,
    '8':523.25,
    '9':587.33,
    '0':659.25,
    ' ':0,
    '-':0,
    }
# for freq in music_table:
#     # sampling_rate+=1000
#     # frequency = int(input("Freuqency: "))
#     # print(frequency)
#     play_wave(generate_sine_wave(freq,duration,sampling_rate),sampling_rate)

audioStream = input("Give input string ")
# dur = float(input("Duration: "))
duration = 0.2   # Duration of the wave in seconds
for note in audioStream:
    
    if (musicdict[note]==0):
        
        # wave=generate_sine_wave(10,0.1,sampling_rate)
        t= time.time_ns()
        # print(time.time_ns())
        time.sleep(0.1)
        print(t- time.time_ns())
    else:

        wave = generate_sine_wave(2*musicdict[note],duration,sampling_rate)
        play_wave(wave,sampling_rate)