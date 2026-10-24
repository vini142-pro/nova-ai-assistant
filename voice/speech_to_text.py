
import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening... Speak now!")

            recognizer.adjust_for_ambient_noise(
                source, duration=0.5
            )
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=10
            )

        print("Recognizing your speech...")

        text = recognizer.recognize_google(
            audio, language="en-IN"
        )

        print(f"You said: {text}")
        return text

    except sr.WaitTimeoutError:
        print("No speech detected. Try again.")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError as error:
        print(f"Speech recognition service error: {error}")
    except OSError as error:
        print(f"Microphone error: {error}")

    return None
