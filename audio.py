import sounddevice as sd
import wavio

class audio:

    def __init__(self):
        pass

    def record_audio(self, duration, output_file):
        fs = 44100  # Sample rate
        recording = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait for the recording to complete

        wavio.write(output_file, recording, fs, sampwidth=2)  # Save the recording to a WAV file

    def process(self):
        duration = 15  # Recording duration in seconds
        output_file = "test.wav"

        self.record_audio(duration, output_file)

        print("Recording complete. Audio saved as 'recorded_audio.wav'")

        return "OK"

# Usage

