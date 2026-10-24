
from google import genai
from config import GEMINI_API_KEY

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY missing. Check your .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)


def get_response(user_message, previous_interaction_id=None):
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=user_message,
        previous_interaction_id=previous_interaction_id,
    )

    return interaction.output_text, interaction.id
