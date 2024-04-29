import openai
from decouple import config

from functions.database import get_recent_messages, get_recent_messages_fd


# Retrieve Enviornment Variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Open AI - Chat GPT
# Convert audio to text
def get_chat_response(message_input):

  messages = get_recent_messages()
  user_message = {"role": "user", "content": "guest requirment: " + message_input}
  messages.append(user_message)
  print(messages)

  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    message_text = response["choices"][0]["message"]["content"]
    return message_text
  except Exception as e:
    return
  
def get_chat_response_fd(message_input):

  messages = get_recent_messages_fd()
  user_message = {"role": "user", "content": "Hotel Management admin: " + message_input}
  messages.append(user_message)
  print(messages)

  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    message_text = response["choices"][0]["message"]["content"]
    return message_text
  except Exception as e:
    return
