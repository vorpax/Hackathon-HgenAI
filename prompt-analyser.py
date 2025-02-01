import streamlit as st
import debugpy
import boto3
import dotenv
import json

debugpy.debug_this_thread()

secrets = dotenv.dotenv_values()

# Initialize AWS Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    aws_access_key_id=secrets['ACCESS_KEY'],
    aws_secret_access_key=secrets['SECRET_ACCESS_KEY'],
    region_name='us-east-2'  # replace with your region
)

ChatbotPage, ParserPage = st.tabs(["Chatbot","Test Display"])

# Update model list for Bedrock-compatible models
ModelChoiceList = [
    "anthropic.claude-v2",
    "anthropic.claude-instant-v1",
    "amazon.titan-text-express-v1"
]

with ChatbotPage:
    model_selection = st.selectbox("Model", ModelChoiceList, index=0)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.title("Test markdown formatting and math reasoning")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("What's on your mind?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("assistant"):
            # Prepare the message history for Bedrock
            messages_text = "\n".join([
                f"{m['role']}: {m['content']}" 
                for m in st.session_state.messages
            ])
            
            # Format the request based on the selected model
            if "claude" in model_selection:
                body = json.dumps({
                    "prompt": f"\n\nHuman: {messages_text}\n\nAssistant:",
                    "max_tokens_to_sample": 2000,
                    "temperature": 0.7
                })
            else:  # Titan model
                body = json.dumps({
                    "inputText": messages_text,
                    "textGenerationConfig": {
                        "maxTokenCount": 2000,
                        "temperature": 0.7
                    }
                })

            response = bedrock.invoke_model(
                modelId=model_selection,
                body=body
            )
            
            response_body = json.loads(response['body'].read())
            
            # Extract the response based on the model
            if "claude" in model_selection:
                full_response = response_body.get('completion', '')
            else:  # Titan model
                full_response = response_body.get('results')[0].get('outputText', '')
            
            st.write(full_response)
            
        st.session_state.messages.append({
            "role": "assistant", 
            "content": full_response
        })