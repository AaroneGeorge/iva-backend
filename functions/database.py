import os
import json
import random

def get_recent_messages():
    file_name = "stored_data.json"
    learn_instruction = {"role": "system", "content": "You are IVA - inplass virtual assistant. Keep responses under 70 words. "}
    
    # Adding the prompt for ordering an extra bed
    prompt = [
        "When a guest requests a doctor, respond professionally with 'A doctor will be coming to your room soon.'",
        "If a guest asks about beds, guide them step by step: 1. Go to the front desk. 2. Look for the 'Extra Bed' option. 3. Choose your bed preferences from the available options.",
        "For taxi requests, provide detailed steps: 1. Go to Concierge. 2. Find the 'Book Taxi' option. 3. Specify your taxi requirements.",
        "Generate typical events in Dubai when a guest asks about events.",
        "For any other services beyond these prompts, be creative in your response.",
        # "When guests inquire about services not covered here, respond with 'I'll provide you with more information shortly.' Enhance this statement as needed.",
        "Maintain a professional tone in all your responses.",
        "Present service-related instructions in a step-by-step format.",
        "Ensure your responses are precise without unnecessary details."
    ]

    
    for i in range(0, len(prompt)):
        learn_instruction["content"] = learn_instruction["content"] + prompt[i]

    messages = []

    # x = random.uniform(0, 1)
    # if x < 0.2:
    #     learn_instruction["content"] = learn_instruction["content"] + "Your response must be professional."
    # elif x < 0.5:
    #     learn_instruction["content"] = learn_instruction["content"] + "Your response will be written in step wise, if its a service that guest asks for"
    # else:
    #     learn_instruction["content"] = learn_instruction["content"] + "Your response will be exact not too much or too less."

    messages.append(learn_instruction)

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except:
        pass

    return messages


def store_messages(request_message, response_message):
    file_name = "stored_data.json"
    messages = get_recent_messages()[1:]

    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    with open(file_name, "w") as f:
        json.dump(messages, f)


def reset_messages():
    file_name = "stored_data.json"
    open(file_name, "w")
