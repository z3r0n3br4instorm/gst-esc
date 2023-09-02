import numpy as np
import sounddevice as sd
from scipy.signal import find_peaks

def detect_clap(signal, sample_rate):
    # Apply FFT
    fft = np.abs(np.fft.fft(signal))
    frequencies = np.fft.fftfreq(len(fft), d=1/sample_rate)

    # Detect peaks in the frequency spectrum
    peaks, _ = find_peaks(fft, height=10000)  # Adjust the height threshold

    # Analyze detected peaks for clap-like frequencies
    clap_frequency = 20000  # Adjust the clap frequency
    clap_indices = np.where(np.isclose(frequencies[peaks], clap_frequency, atol=50))[0]

    if len(clap_indices) >= 2:
        print("Clap detected!")
        # Perform timing analysis on clap_indices to confirm claps
    else:
        print("No claps detected.")

def callback(indata, frames, time, status):
    if status:
        print(status)

    if any(indata):
        detect_clap(indata[:, 0], sample_rate)

# Set the audio input parameters
sample_rate = 44100  # You might need to adjust this based on your microphone
block_size = 1024

# Start streaming audio input
with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate, blocksize=block_size):
    print("Listening for claps... (Press Ctrl+C to stop)")
    sd.sleep(86400)  # Run for 24 hours; you can adjust this or use any suitable termination condition
