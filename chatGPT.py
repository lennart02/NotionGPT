import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def AskGPT3(content):

  messages = [
  {"role": "system", "content" : "You’re a helpful assistant"}
  ]

  
  messages.append({"role": "user", "content": content})

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

  chat_response = completion.choices[0].message.content
  return chat_response

if(__name__ == "__main__"):
  content = input("User: ")
  response = AskGPT3(content)
  print(f'ChatGPT: {response}')