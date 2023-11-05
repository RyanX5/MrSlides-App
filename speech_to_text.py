import io
from google.oauth2 import service_account
from google.cloud import speech
from pydub import AudioSegment



class audio_to_text:

    def __init__(self):

        pass

    def audio_text(self, filePath):
        response = self.get_response(filePath)
        text = self.check_accuracy(response)

        return text


    def get_response(self, filePath):
        client_file = "api_key.json"
        credentials = service_account.Credentials.from_service_account_file(client_file)
        client = speech.SpeechClient(credentials=credentials)


        audio_file = self.convert_to_mono(filePath)
        # audio_file = filePath
        with io.open(audio_file, 'rb') as f:
            content = f.read()
            audio = speech.RecognitionAudio(content=content)

        sample_rate = self.find_sample_rate(filePath)


        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate,  # Adjust based on your audio file
            language_code="en-US"  # Language code, e.g., "en-US" for English
        )

        response = client.recognize(config=config, audio=audio)
        return response

    
    
    def check_accuracy(self, response):

        confidence = 0.0

        response_final = ""
        count = 0
        
        for result in response.results:
            response_final += result.alternatives[0].transcript
            confidence += result.alternatives[0].confidence
            count += 1

        if confidence > (count*0.7):
            return response_final
        
        else:
            return "error"

    def convert_to_mono(self, file):

        # Load the stereo audio file
        audio = AudioSegment.from_wav(file)

        # Convert stereo to mono
        audio = audio.set_channels(1)

        # Export the mono audio
        audio.export("mono.wav", format="wav")

        return "mono.wav"


    def find_sample_rate(self, file):

            # Path to your audio file (e.g., MP3, WAV, etc.)
        audio_file = file

        # Load the audio file
        audio = AudioSegment.from_file(audio_file)

        # Get the sample rate
        sample_rate = audio.frame_rate

        return sample_rate



            

        
        


