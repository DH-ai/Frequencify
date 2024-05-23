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
# y,x=generate_sine_wave(500,2,20000)
# # Function to play the generated wave
# print(x)

def envelope(wave,duration:int=None)->np.array:
    size = np.shape(wave)
    print(size)
    t= time.time()
    for i in range(0,int(size[0]/5)):
        # print(wave[i],i)
        wave[i]=wave[i]*(i/size[0]/5)
        # print(wave[i],i)
        # time.sleep(0.7)


    for i in range(int(size[0]/5),2*int(size[0]/5)):
        wave[i]=wave[i]*(1- 0.7*(size[0]/5-i/size[0]/2))

    for i in range(2*int(size[0]/5),int(size[0]/2)):
        wave[i]=wave[i-1]
    

    for i in range(int(size[0]/10)):
        wave[i]=wave[i]-wave[9*int(size[0]/10)-1]/int(size[0]/10)
    print(time.time()-t)
    return wave



def play_wave(wave, sampling_rate):
    sd.play(wave, samplerate=sampling_rate)
    sd.wait()
    return "done"

# play_wave(y,44000)



# play_wave(wave,44000)
# figure,axis = plt.subplots(2,1)

# axis[0].plot(x,y)
# axis[0].set_title("NM")
# wave = envelope(y)


# axis[1].plot(x,wave)
# axis[1].set_title("Mod")
# plt.show()
# input()
# Test different frequencies
frequencies = [100, 200, 400, 800, 1600, 3200]  # Frequencies in Hz

# for frequency in frequencies:
#     print(f"Generating and playing sine wave with frequency: {frequency} Hz")
#     wave = generate_sine_wave(frequency, duration, sampling_rate)
#     play_wave(wave, sampling_rate)
sampling_rate=44200
# 5 5 6 8 8 8  8 8  8 8  5 6 8 8 8  8 8  8 8  5 6 8 8 8 8 8  8 8  8 8 7
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
duration = 0.2 # Duration of the wave in seconds
# for freq in music_table:
#     print(freq)
#     play_wave(generate_sine_wave(freq,duration,sampling_rate),sampling_rate)

audioStream = input("Give input string ")
# dur = float(input("Duration: "))
for note in audioStream:
    
    # if (musicdict[note]==0):
        
    #     # wave=generate_sine_wave(10,0.1,sampling_rate)
    #     t= time.time_ns()
    #     # print(time.time_ns())
    #     # time.sleep(0.1)
    #     # print((t- time.time_ns())*-1)
    # else:
    
    wave = generate_sine_wave(musicdict[note],duration,sampling_rate)
    play_wave(wave,sampling_rate)