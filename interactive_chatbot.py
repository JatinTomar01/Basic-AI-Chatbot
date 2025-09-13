import random

greetings = ["hello", "hi", "hey", "greetings", "sup"]
greeting_responses = [
    "Hello, {name}!",
    "Hi there, {name}!",
    "Hey {name}, how can I help you?",
    "Greetings, {name}!",
    "Howdy, {name}!"
]

farewells = ["bye", "goodbye", "see you", "farewell"]
farewell_responses = [
    "Goodbye, {name}!",
    "See you later, {name}!",
    "Bye, {name}! Have a great day!",
    "Take care, {name}!"
]

questions = ["how are you", "how are you doing", "what's up"]
question_responses = [
    "I'm just a bot, but I'm glad to chat with you!",
    "All systems go, {name}!",
    "I'm here to help you, {name}!"
]

menu_options = [
    "1. Tell me a joke",
    "2. Give me a fun fact",
    "3. Take a quiz",
    "4. Remember my favorite color",
    "5. Ask about my mood",
    "6. Show conversation history",
    "7. Say goodbye"
]

jokes = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why was the math book sad? Because it had too many problems.",
    "Why don't programmers like nature? Too many bugs.",
    "Why did the Python programmer go broke? Because his code had too many exceptions!"
]

fun_facts = [
    "Did you know? Python is named after Monty Python, not the snake!",
    "The first computer bug was a real bug—a moth stuck in a computer.",
    "AI stands for Artificial Intelligence.",
    "The word 'robot' comes from a Czech word meaning 'forced labor'."
]

quizzes = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "What does 'AI' stand for?",
        "answer": "artificial intelligence"
    }
]

def get_response(user_input, name, memory, history):
    user_input = user_input.lower().strip()
    history.append(f"{name}: {user_input}")

    # Greetings
    for word in greetings:
        if word in user_input:
            response = random.choice(greeting_responses).format(name=name)
            history.append(f"Bot: {response}")
            return response
    # Farewells
    for word in farewells:
        if word in user_input:
            response = random.choice(farewell_responses).format(name=name)
            history.append(f"Bot: {response}")
            return response
    # Questions
    for word in questions:
        if word in user_input:
            response = random.choice(question_responses).format(name=name)
            history.append(f"Bot: {response}")
            return response
    # Menu options
    if user_input == "1":
        response = random.choice(jokes)
        history.append(f"Bot: {response}")
        return response
    if user_input == "2":
        response = random.choice(fun_facts)
        history.append(f"Bot: {response}")
        return response
    if user_input == "3":
        quiz = random.choice(quizzes)
        print(f"Quiz: {quiz['question']}")
        answer = input("Your answer: ").lower().strip()
        history.append(f"{name}: {answer}")
        if answer == quiz['answer']:
            response = "Correct! 🎉"
        else:
            response = f"Oops! The correct answer was '{quiz['answer']}'."
        history.append(f"Bot: {response}")
        return response
    if user_input == "4":
        fav = input("What's your favorite color? ").strip()
        memory['color'] = fav
        response = f"I'll remember that your favorite color is {fav}!"
        history.append(f"Bot: {response}")
        return response
    if user_input == "5":
        mood = input("How are you feeling today? ").strip().lower()
        memory['mood'] = mood
        if "good" in mood or "happy" in mood or "great" in mood:
            response = f"That's awesome, {name}! 😊"
        elif "sad" in mood or "bad" in mood:
            response = f"I'm here for you, {name}. Want to hear a joke to cheer up?"
        else:
            response = f"Thanks for sharing your mood, {name}."
        history.append(f"Bot: {response}")
        return response
    if user_input == "6":
        print("\n--- Conversation History ---")
        for line in history:
            print(line)
        print("--- End of History ---\n")
        return "Displayed conversation history."
    if user_input == "7":
        response = random.choice(farewell_responses).format(name=name)
        history.append(f"Bot: {response}")
        return response
    # Memory-based interaction
    if "color" in memory:
        if f"{memory['color']}" in user_input:
            response = f"{memory['color']} is a beautiful color, {name}!"
            history.append(f"Bot: {response}")
            return response
    return f"I'm not sure how to respond to that, {name}. Please choose an option or ask something else!"

def main():
    print("Welcome to the Enhanced Interactive AI Chatbot!")
    name = input("First, what's your name? ")
    memory = {}
    history = []
    print(f"Hi {name}! Let's chat. Type 'menu' anytime to see options or 'bye' to exit.")

    while True:
        user_input = input(f"{name}: ")
        if user_input.lower().strip() == "menu":
            print("Choose an option:")
            for option in menu_options:
                print(option)
            continue
        response = get_response(user_input, name, memory, history)
        print("Bot:", response)
        # Exit if user types a farewell or chooses option 7
        if any(word in user_input.lower() for word in farewells) or user_input.strip() == "7":
            print("\nHere's your conversation history before you go:")
            for line in history:
                print(line)
            break

if __name__ == "__main__":
    main()