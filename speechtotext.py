import speech_recognition as sr

def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file_path) as source:
            print("Listening to the audio...")
            audio_data = recognizer.record(source)
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)
            print("Transcription successful!")
            return text

    except sr.UnknownValueError:
        return "Sorry, speech could not be understood."
    except sr.RequestError as e:
        return f"API error: {e}"
    except FileNotFoundError:
        return "Audio file not found."

if __name__ == "__main__":
    path = "sample.wav"  # Replace with your file path
    print(convert_audio_to_text(path))
