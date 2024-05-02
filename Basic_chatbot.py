import random

# Responses dictionary
responses = {
    "hello": ["Hey there"],
    "Hi": ["Hi!"],
    "how are you": ["I'm doing well, thank you for asking.", "I'm fine, how about you?"],
    "what is your name": ["My name is ChatBot.", "You can call me ChatBot."],
    "how old are you": ["I am a computer program, so I don't have an age."],
    "what can you do": ["I can help you with various tasks. Just ask!", "I'm here to assist you."],
    "what time is it": ["I'm sorry, I can't provide the current time."],
    "where are you from": ["I am a virtual assistant, so I don't have a physical location."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!"],
    "do you like pizza": ["I don't have taste buds, but I've heard pizza is quite popular!"],
    "bye": ["Goodbye! Have a great day."]
}

# Function to respond to user input
def respond_to_question(question):
    if question.lower() in responses:
        return random.choice(responses[question.lower()])
    else:
        return "I'm sorry, I didn't understand that."

# User interaction
def user_interaction():
    questions_asked = 0
    while questions_asked < 3:
        user_input = input("User: ")
        bot_response = respond_to_question(user_input)
        print("ChatBot:", bot_response)
        questions_asked += 1

# Main function
def main():
    print("ChatBot: Hello! How can I assist you today?")
    user_interaction()
    print("ChatBot: Goodbye! Have a great day.")

if __name__ == "__main__":
    main()
