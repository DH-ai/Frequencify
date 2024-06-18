import numpy as np
import sounddevice as sd
import time
import matplotlib as mlt
import matplotlib.pyplot as plt
import keyboard

# Function to generate a sine wave with given frequency and duration
def generate_sine_wave(frequency, duration, sampling_rate,wave_type:str="sine")->np.array:
    """
    Generate a sound with defualt parameter

    Args:
        frequency (int or float):
        duration (int or float).
        sampling rate (int or float).
        type (str): Defaults to "sine" other arguments include , "square".
    Returns:
        np.array
    """
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    if wave_type=="square":
        print("ddas")
        for i in range(int(duration*sampling_rate)):
            if wave[i]>0.5:
                wave[i]=1
            else:
                wave[i]=0
    
    
    return wave


def addNpArray(arr1:np.array,arr2:np.array,sr,dr)->np.array:
    


    return arr1+arr2
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


frequencies = [100, 200, 400, 800, 1600, 3200]  # Frequencies in Hz


sampling_rate=44200
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
duration =3
# audioStream = input("Give input string ")
# # dur = float(input("Duration: "))
# wave1 = generate_sine_wave(200,duration,sampling_rate=sampling_rate)
# wave2=generate_sine_wave(400,duration,sampling_rate=sampling_rate)
# wave3= addNpArray(wave1,wave2,sampling_rate,duration)
# wave4= wave2+wave1
# wave4=generate_sine_wave(600,duration,sampling_rate=sampling_rate)

# sqrWave = generate_sine_wave(200,duration,sampling_rate,"square")
# print("Playing square wave")
# play_wave(sqrWave,sampling_rate)

# print("Playing wave 1")
# play_wave(wave1,sampling_rate=sampling_rate)
# print("Playing wave 2")
# play_wave(wave2,sampling_rate=sampling_rate)
# print("Playing wave 3")
# play_wave(wave3,sampling_rate=sampling_rate)
# print("Playing wave 4")
# play_wave(wave1+wave2,sampling_rate=sampling_rate)
# print("Playing wave 5")
# play_wave(wave4,sampling_rate=sampling_rate)
#square wave
def on_key_press(event):
    if event.name=='up':
        print("in it")
        play_wave(generate_sine_wave(frequency=400,duration=,sampling_rate=sampling_rate),sampling_rate)
    elif event.name=='esc':
        print("OUT")
        return False
        
def main ():
    keyboard.hook(  on_key_press)
    keyboard.wait('esc')

main()

