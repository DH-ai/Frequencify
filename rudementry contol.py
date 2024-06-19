import sounddevice as sd
import numpy as np
import keyboard
import threading

# Shared variable to control sound playback
is_playing = False
sample_rate = 44100

def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    return wave

def play_sound_continuously(frequency):
    global is_playing
    wave = generate_sine_wave(frequency, duration=0.5)  # Long duration
    while is_playing:
        sd.play(wave, samplerate=sample_rate)
        sd.wait()  # Wait until playback is finished

def on_key_press(e):
    global is_playing
    key = e.name
    print(is_playing)
    if key == 'a' and not is_playing:
        is_playing = True
        threading.Thread(target=play_sound_continuously, args=(440,)).start()  # 440 Hz
    elif key == 's' and not is_playing:
        is_playing = True
        threading.Thread(target=play_sound_continuously, args=(494,)).start()  # 494 Hz
    elif key == 'd' and not is_playing:
        is_playing = True
        threading.Thread(target=play_sound_continuously, args=(523,)).start()  # 523 Hz

def on_key_release(e):
    global is_playing
    key = e.name
    if key in ('a', 's', 'd'):
        is_playing = False
        print(is_playing)
        sd.stop()

# Register key press and release handlers
keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)

print("Press 'a', 's', 'd' to play sounds. Release the key to stop the sound. Press 'esc' to exit.")

# Keep the program running
keyboard.wait('esc')
print("Exiting...")
