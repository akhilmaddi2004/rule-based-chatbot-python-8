## 🤖 Rule-Based Chatbot Using Python

This project contains a simple command-line chatbot built entirely using basic Python control flow.
The aim is to simulate how a chatbot works without using NLP libraries or ML models.
It demonstrates input handling, looping, conditional logic, and rule-based responses.

## 📌 Project Objective

Build a basic chatbot that:

1. Takes user input continuously.
2. Responds using predefined rules.
3. Handles multiple types of queries.
4. Exits when the user types a specific command.
This project helps understand how text-based conversation logic works before moving to real NLP or ML-based chatbots.

## 📁 Folder Structure
chatbot-task8/
│
├── chatbot.py        # Main chatbot script
└── samples/
    └── screenshot.png  

## 🛠️ Technologies Used

- Python 3
- No external libraries (to keep it rule-based and simple)

## 📜 How the Chatbot Works

The chatbot follows these rules:
1. Reads input using input().
2. Normalizes text with .lower() to avoid case issues.
3. Checks conditions with if-elif-else.
4. Prints a matching response.
5. Repeats the loop until user types "bye" or "exit".
This is the foundation of every rule-based chatbot.

## 📌 Features

✔ Greets the user
✔ Answers basic questions
✔ Gives time/date info
✔ Responds to unknown queries
✔ Supports exit commands
✔ Handles multiple intents with keywords
✔ Structured, readable logic
✔ Beginner-friendly but cleaner than typical basic solutions

## 💻 Code (chatbot.py)

This is the complete working solution:

# Rule-Based Chatbot

def get_response(msg):
    msg = msg.lower()

    # Greetings
    if msg in ["hi", "hello", "hey", "hii"]:
        return "Hello! How can I help you today?"
    
    # About bot
    elif "who are you" in msg or "what are you" in msg:
        return "I'm a simple rule-based chatbot built using Python."
    
    # Help
    elif "help" in msg:
        return "You can ask me about weather, time, greetings, or general questions."
    
    # Weather intent
    elif "weather" in msg:
        return "I can't access real-time weather, but it looks like a good day to code!"
    
    # Time intent
    elif "time" in msg:
        return "I cannot fetch system time here, but you can check your device clock."
    
    # Internship intent
    elif "internship" in msg:
        return "Internships help you gain real-world skills. Keep practicing."
    
    # Exit conditions
    elif msg in ["bye", "exit", "quit"]:
        return "exit" # signal to break loop
    
    # Fallback
    else:
        return "I don't understand that yet. Try asking something else."
    
def start_chat():
    print("Chatbot Activated. Type 'exit' to stop.\n")

    while True:
        user = input("You: ").strip()

        if not user:
            print("Bot : Please type something.")
            continue
        
        response =get_response(user)

        if response == "exit":
            print("Bot : Goodbye!")
            break
        
        print("Bot:", response)

if __name__ == "__main__":
    start_chat()
    
## 📤 Sample Output (examples.txt)
Chatbot Activated. Type 'exit' to stop.

You: hi
Bot: Hello! How can I help you today?
You: what is your name?
Bot: I don't understand that yet. Try asking something else.
You: who created you?
Bot: I don't understand that yet. Try asking something else.
You: who are you
Bot: You can ask me about weather, time, greetings, or general questions.
You: time
Bot: I cannot fetch system time here, but you can check your device clock.
You: internship
Bot: Internships help you gain real-world skills. Keep practicing.
You: bye
Bot : Goodbye!

## 🚀 How to Run

1. Install Python
2. Open terminal inside project folder
3. Run:

python chatbot.py

## 📌 What This Project Demonstrates

- Control flow mastery
- Looping logic
- Input sanitization
- Conditional branching
- Basic text processing
- Chat simulation without NLP
- Clean and readable code structure

## 📈 Future Improvements

- Add small talk responses
- Add pattern matching
- Add sentiment logic
- Convert into a Tkinter GUI
- Upgrade to an ML/NLP-powered chatbot
