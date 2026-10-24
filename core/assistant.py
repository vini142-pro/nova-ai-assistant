
from ai.llm import get_response

previous_interaction_id = None


def chat(user_message):
    global previous_interaction_id

    response, interaction_id = get_response(
        user_message,
        previous_interaction_id,
    )

    previous_interaction_id = interaction_id

    return response
