import re
import random

# Sample dataset of conversations
dataset = [
    {"input": "Hi there!", "intent": "greeting", "response": "Hello! How can I assist you?"},
    {"input": "How do I reset my password?", "intent": "password_reset", "response": "To reset your password, please visit our website and follow the instructions."},
    {"input": "What's the weather today?", "intent": "weather", "response": "The weather today is sunny with a high of 75°F."},
    # Add more sample conversations as needed
]

# Text Preprocessing: Clean and tokenize the text data
def preprocess_text(text):
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text.split()  # Tokenize text into words

# Intent Recognition: Use keyword matching to understand user intent
def recognize_intent(input_text):
    input_text = preprocess_text(input_text)
    for conv in dataset:
        if any(word in input_text for word in preprocess_text(conv['input'])):
            return conv['intent']
    return "unknown"

# Response Generation: Design a response generation mechanism based on predefined templates
def generate_response(intent):
    responses = [conv['response'] for conv in dataset if conv['intent'] == intent]
    if responses:
        return random.choice(responses)
    else:
        return "I'm sorry, I'm not sure how to respond to that."

# User Interaction: Implement a simple command-line interface
def chat():
    print("Chatbot: Hello! How can I assist you?")
    while True:
        user_input = input("User: ")
        intent = recognize_intent(user_input)
        response = generate_response(intent)
        print("Chatbot:", response)

# Learning and Improvement: No implementation provided in this basic example

# Run the chatbot
if __name__ == "__main__":
    chat()
