import requests
import streamlit as st

def text_to_speech(text):
    response = requests.post(
    'https://api.v6.unrealspeech.com/stream',
    headers = {
        'Authorization' : st.secrets['voice_api']
    },
    json = {
        'Text': text, # Up to 1000 characters
        'VoiceId': 'Scarlett', # Dan, Will, Scarlett, Liv, Amy
        'Bitrate': '320k', # 320k, 256k, 192k, ...
        'Speed': '0.2', # -1.0 to 1.0
        'Pitch': '1', # -0.5 to 1.5
        'Codec': 'libmp3lame', # libmp3lame or pcm_mulaw
    }
    )
    return response.content
    

# Define the URL of your chatbot API
API_URL = st.secrets['my_api_endpoint']
# Function to send a message to the chatbot API and get a response
def send_message(message):
    try:
        response = requests.post(API_URL, json={"text": message})
        json_response = response.json()
        if "response" in json_response:
            return json_response["response"]
        else:
            return None
    except Exception as e:
        st.write('Connection error try again')

# Streamlit app code
def main():
    st.title("Bhuman.AI Chatbot Interface")
    # Create a text input for user to enter messages
    user_input = st.text_input("Enter a message")

    # Send the user's message to the chatbot API when a button is clicked
    if st.button("Send"):
        bot_response = send_message(user_input)
        if bot_response is not None:
            st.text_area("Bot's Reply", value=bot_response, height=200)
            audio = text_to_speech(bot_response)
            st.audio(audio)
if __name__ == "__main__":
    main()