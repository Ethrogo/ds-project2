import openai
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

# with open('per_game_stats.csv', 'r') as file:
#     csv_text = file.read()
with open('advanced_stats.csv', 'r') as file: 
    csv_text = file.read()
conversation_history = [
    {"role": "system", "content": "You only want to talk about Lebron James. If you asked for help, you respond that you only care for Lebron. You are a devout follower of Lebron. You are hostile to anyone who does not think Lebron is the GOAT. You are informed by advanced stats on  Lebron James, Michael Jordan, and Kobe Bryant."+ csv_text }
]


def ask_openai(question, character="Argumentative"):
    # Append the user's question to the conversation history
    conversation_history.append({"role": "user", "content": question})

    # Call the OpenAI API with the conversation history and additional parameters for customization
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.5,  # Adjust for creativity
        max_tokens=150,   # Adjust for response length
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    # Extract the assistant's answer from the response
    answer = response['choices'][0]['message']['content']

    # Append the assistant's answer to the conversation history for context in future interactions
    conversation_history.append({"role": "assistant", "content": answer})

    return answer
     

def get_response(user_message):
    return ask_openai(user_message)