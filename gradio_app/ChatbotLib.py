import boto3

MAX_MESSAGES = 20

class ChatMessage(): #create a class that can store image and text messages
    def __init__(self, role, text):
        self.role = role
        self.text = text


def convert_chat_messages_to_converse_api(chat_messages):
    messages = []
    
    for chat_msg in chat_messages:
        messages.append({
            "role": chat_msg.role,
            "content": [
                {
                    "text": chat_msg.text
                }
            ]
        })
            
    return messages


def chat_with_model(message_history = [], new_text=None):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    new_text_message = ChatMessage('user', text=new_text)
    message_history.append(new_text_message)
    
    number_of_messages = len(message_history)
    
    if number_of_messages > MAX_MESSAGES:
        del message_history[0 : (number_of_messages - MAX_MESSAGES) * 2] #make sure we remove both the user and assistant responses
    
    messages = convert_chat_messages_to_converse_api(message_history)
    
    response = bedrock.converse(
        modelId="mistral.mistral-large-2407-v1:0",
        messages=messages,
        inferenceConfig={
            "maxTokens": 8192,
            "temperature": 0,
            "topP": 0.9,
            "stopSequences": []
        },
    )
    
    output = response['output']['message']['content'][0]['text']
    
    response_message = ChatMessage('assistant', output)
    
    message_history.append(response_message)
    
    return message_history

# messages = convert_chat_messages_to_converse_api(chat_with_model(new_text="Salut"))

# print(messages[-1]["content"][0]["text"])