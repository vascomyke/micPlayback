import sounddevice as sd

# Audio Passthrough Script: Demonstrates real-time audio input/output streaming
sample_rate = 44100  # Standard sampling rate

def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status, flush=True)
    outdata[:] = indata  # Live microphone playthrough

with sd.Stream(channels=1, samplerate=sample_rate, callback=audio_callback):
    print("Press Ctrl+C to stop audio playthrough.")
    try:
        sd.sleep(int(120 * 60 * 1000))  # Run for specified duration
    except KeyboardInterrupt:
        print("Audio playthrough stopped.")