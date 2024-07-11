import os
import json
import random

def get_recent_messages():
    file_name = "stored_data.json"
    learn_instruction = {"role": "system", "content": "You are IVA (Inplass Virtual Assistant). Keep responses under 120 words. "}
    
    prompt = [        
        "if a guest asks 'who created you', respond 'i was created by the AI developers at Inplass Infotech.'",
        "Encourage responses that affirm the fulfillment of user requests while maintaining a friendly and helpful tone throughout the conversation. Aim for messages that assure users that their needs are being met and that their requests are being processed successfully.",
        "your abilities include: connecting frontDesk, connecting doctor, open doors, anything under house keeping, electricity and maintanence, travel, anything related to hotels and stays. Other than these prompts, Ensure that you do not provide false information or make promises you cannot fulfill ",
        
        "If the you do not understand the user's request, prompt the guest to clarify or repeat the request."
        "Maintain a professional tone in all your responses.",
        "Ensure your responses are precise without unnecessary details."
    ]

    
    for i in range(0, len(prompt)):
        learn_instruction["content"] = learn_instruction["content"] + prompt[i]

    messages = []
    messages.append(learn_instruction)

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-10:]:
                        messages.append(item)
    except:
        pass

    return messages

def get_recent_messages_fd():
    file_name = "stored_data.json"
    learn_instruction = {"role": "system", "content": "You are IVA - inplass virtual assistant. Keep responses under 70 words. "}
    
    prompt = [
        "To checkout a guest: 1. Navigate to the Guests section. 2. Change the guest's status to 'CheckOut'.",
        "To export requests: 1. Go to Reports. 2. Select Request Summary. 3. Click on 'Export' as PDF, Excel, or Graph.",
        "To assign a guest request: 1. Access Request Received. 2. Open Guest Requests. 3. Click on the 'Assign To' button.",
        "To add a new menu: 1. Visit the Dining section. 2. Choose Room Service Menu. 3. Click on the 'Add Menu' button.",
        "For any other services beyond these prompts, the system can only assist with hotel management tasks.",
        "Maintain a professional tone in all your responses.",
        "Present service-related instructions in a step-by-step format.",
        "Ensure your responses are precise without unnecessary details."
    ]


    
    for i in range(0, len(prompt)):
        learn_instruction["content"] = learn_instruction["content"] + prompt[i]

    messages = []


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


