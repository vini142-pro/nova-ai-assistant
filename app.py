
from core.assistant import chat
from voice.speech_to_text import listen
from voice.text_to_speech import speak


def main():
    print("\n🤖 AI Voice + Chat Assistant")
    print("1. Chat mode")
    print("2. Voice mode")
    print("Type 'exit' to stop.\n")

    while True:
        mode = input("Choose mode (1/2): ").strip()

        if mode.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        if mode not in ("1", "2"):
            print("Please choose 1 or 2.\n")
            continue

        while True:
            if mode == "1":
                user_message = input("\nYou: ").strip()

                if user_message.lower() == "exit":
                    break

            else:
                user_message = listen()

                if user_message is None:
                    continue

                if user_message.lower().strip() == "exit":
                    break

            if not user_message:
                continue

            try:
                response = chat(user_message)
                print(f"\nAssistant: {response}\n")
                speak(response)

            except Exception as error:
                print(f"Something went wrong: {error}")

        print("\nReturning to mode selection...\n")


if __name__ == "__main__":
    main()

