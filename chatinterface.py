import requests
import streamlit as st

# Define the URL of your chatbot API
API_URL = "https://chatbot-27je.onrender.com/prompt"
# Function to send a message to the chatbot API and get a response
def send_message(message):
    response = requests.post(API_URL, json={"text": message})
    json_response = response.json()
    if "response" in json_response:
        return json_response["response"]
    else:
        return None

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

if __name__ == "__main__":
    main()