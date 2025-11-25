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
    