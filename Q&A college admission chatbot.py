import random
import re

knowledge_base = {
    "transport facilities": "Yes Transportation Facilities available covering 50 kilometers from college",
    "admission fee": "You need to pay a one time fee of Rs.5000",
    "application deadline": "The application deadline is December 1st for regular decision.",
    "application requirements": "You'll need to submit your transcripts, test scores, essays, and letters of recommendation.",
    "admission requirements": " The requirements vary depending on your program of interest, but generally include transcripts, test scores, essays, and letters of recommendation. You can find more specific details on the college website.",
    "application deadline": "The deadline for CSE admission is at 31/04/2024. However, I recommend applying early to increase your chances of acceptance.",
    "canteen": "The canteen offers a variety of options, including vegetarian and healthy choices. There are also several cafes and restaurants on campus if you're looking for something different.",
    "Professors": " The faculty at MIT are highly qualified and passionate about their subjects. They are generally approachable and supportive of their students.",
    "research opportunities for undergraduates": "Yes, several departments offer research opportunities for students. You can talk to your professors or department head to learn more about available options.",
    "labs": " The labs are modern and well-equipped with the latest technology. You'll have access to all the resources you need for your studies and research.",
    "Seminars and Events": " Yes, the college regularly hosts lectures, workshops, and seminars by renowned scholars and professionals. It's a great way to learn from experts and explore new ideas.",
}

conversation_history = []
user_info = {}  # Store collected user information for personalization


def greet():
    print("Welcome to the College Admission Q&A Bot! I'm here to help answer your questions about the application process.")
    ask_user_name()  # Collect user's name for personalization


def ask_user_name():
    name = input("Before we start, could you please tell me your name? ")
    user_info["name"] = name
    print(f"Nice to meet you, {name}! Feel free to ask me any questions about college admission.")


def handle_question(question):
    for keyword in knowledge_base:
        if re.search(keyword, question, re.IGNORECASE):
            response = knowledge_base[keyword]
            try:
                response = personalize_response(response, conversation_history, user_info)
            except KeyError:
                pass  # Handle cases where personalization isn't possible
            return response

    return "I'm not sure I understand that question. Could you rephrase it or try asking something different?"


def personalize_response(response, conversation_history, user_info):
    # Implement logic to tailor responses based on previous interactions and user information
    if "name" in user_info:
        response = response.replace("you", user_info["name"])  # Address user by name.
    return response


def main():
    greet()
    while True:
        question = input("You: ")
        answer = handle_question(question)
        print("Bot:", answer)
        conversation_history.append((question, answer))

        if question.lower() in ["goodbye", "bye", "quit"]:
            print("Thanks for using the College Admission Q&A Bot, " + user_info.get("name", "friend") + "! Have a great day.")
            break


if __name__ == "__main__":
    main()