import openai
import os

# Ensure the API key is set
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(messages):
    """
    Calls the OpenAI ChatCompletion API.
    
    Args:
        messages (list): List of messages to send to the API.

    Returns:
        dict: The assistant's response message.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message
