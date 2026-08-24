import tkinter as tk
from tkinter import scrolledtext


# ============================================================
# DecodeLabs - Artificial Intelligence
# Project 1: Rule-Based AI Chatbot
# ============================================================


# ============================================================
# CHATBOT LOGIC
# ============================================================

def get_bot_response(user_input):

    # Convert input to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # --------------------------------------------------------
    # EXIT COMMANDS
    # --------------------------------------------------------
    if user_input in [
        "bye",
        "goodbye",
        "exit",
        "quit",
        "see you",
        "see you later"
    ]:
        return "Goodbye! 👋 Have a great day!"

    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------
    elif user_input in [
        "hi",
        "hello",
        "hey",
        "hii",
        "hiii",
        "heyy",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return "Hello! 👋 Nice to meet you. How can I help you?"

    # --------------------------------------------------------
    # WHO ARE YOU
    # --------------------------------------------------------
    elif user_input in [
        "who are you",
        "who r you",
        "tell me about yourself",
        "introduce yourself",
        "what are you"
    ]:
        return (
            "I am DecodeBot 🤖, a simple rule-based "
            "Artificial Intelligence chatbot."
        )

    # --------------------------------------------------------
    # BOT NAME
    # --------------------------------------------------------
    elif user_input in [
        "what is your name",
        "what's your name",
        "your name",
        "tell me your name",
        "what should i call you"
    ]:
        return "My name is DecodeBot. 🤖"

    # --------------------------------------------------------
    # HOW ARE YOU
    # --------------------------------------------------------
    elif user_input in [
        "how are you",
        "how are you doing",
        "are you fine",
        "are you okay",
        "how do you feel",
        "how r u"
    ]:
        return "I'm doing great! 😊 Thanks for asking."

    # --------------------------------------------------------
    # WHAT CAN YOU DO
    # --------------------------------------------------------
    elif user_input in [
        "what can you do",
        "what do you do",
        "what are your features",
        "how can you help me",
        "help",
        "tell me your features"
    ]:
        return (
            "I can answer predefined questions, handle greetings, "
            "provide basic information about AI and Python, "
            "and continue conversations using rule-based logic."
        )

    # --------------------------------------------------------
    # ARTIFICIAL INTELLIGENCE
    # --------------------------------------------------------
    elif user_input in [
        "what is ai",
        "what is artificial intelligence",
        "define ai",
        "define artificial intelligence",
        "explain ai",
        "explain artificial intelligence",
        "tell me about ai",
        "tell me about artificial intelligence"
    ]:
        return (
            "Artificial Intelligence (AI) is a field of computer "
            "science that focuses on creating systems that can "
            "perform tasks that normally require human intelligence."
        )

    # --------------------------------------------------------
    # MACHINE LEARNING
    # --------------------------------------------------------
    elif user_input in [
        "what is machine learning",
        "define machine learning",
        "explain machine learning",
        "tell me about machine learning"
    ]:
        return (
            "Machine Learning is a part of Artificial Intelligence "
            "where computers learn patterns from data and use them "
            "to make predictions or decisions."
        )

    # --------------------------------------------------------
    # RULE-BASED AI
    # --------------------------------------------------------
    elif user_input in [
        "what is rule based ai",
        "what is rule based chatbot",
        "what is a rule based chatbot",
        "how does this chatbot work",
        "how do you work",
        "how does the chatbot work"
    ]:
        return (
            "I work using predefined rules. I compare your input "
            "with specific conditions using if-else statements "
            "and then provide the appropriate response."
        )

    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------
    elif user_input in [
        "what is python",
        "tell me about python",
        "explain python",
        "why python",
        "what is python language",
        "what is python programming"
    ]:
        return (
            "Python is a high-level programming language known for "
            "its simple syntax. It is widely used in AI, machine "
            "learning, web development, automation and data science."
        )

    # --------------------------------------------------------
    # IF ELSE
    # --------------------------------------------------------
    elif user_input in [
        "what is if else",
        "what is if else statement",
        "explain if else",
        "why use if else",
        "what is an if else statement"
    ]:
        return (
            "An if-else statement is used for decision making. "
            "The program checks a condition and executes the "
            "appropriate block of code."
        )

    # --------------------------------------------------------
    # LOOP
    # --------------------------------------------------------
    elif user_input in [
        "what is a loop",
        "what is loop",
        "why use loop",
        "why while loop",
        "what is while loop",
        "explain while loop"
    ]:
        return (
            "A loop repeatedly executes a block of code. "
            "This chatbot uses a continuous loop so it can "
            "keep accepting messages until you exit."
        )

    # --------------------------------------------------------
    # PROJECT
    # --------------------------------------------------------
    elif user_input in [
        "what is this project",
        "tell me about this project",
        "project details",
        "what is project 1",
        "tell me about project 1"
    ]:
        return (
            "This is Project 1: Rule-Based AI Chatbot. "
            "The project demonstrates control flow, decision-making "
            "and basic AI concepts using Python."
        )

    # --------------------------------------------------------
    # PROJECT OBJECTIVE
    # --------------------------------------------------------
    elif user_input in [
        "what is the objective",
        "what is the goal",
        "project objective",
        "what is the purpose of this project",
        "purpose of this project"
    ]:
        return (
            "The objective is to create a simple rule-based chatbot "
            "that responds to predefined user inputs using "
            "if-else logic and a continuous loop."
        )

    # --------------------------------------------------------
    # TECHNOLOGY
    # --------------------------------------------------------
    elif user_input in [
        "what technology did you use",
        "what technologies are used",
        "which technology is used",
        "what programming language",
        "which programming language",
        "what tools are used"
    ]:
        return (
            "This project uses Python. The graphical interface "
            "is created using Tkinter, while the chatbot logic "
            "uses if-else conditions and a continuous loop."
        )

    # --------------------------------------------------------
    # TKINTER
    # --------------------------------------------------------
    elif user_input in [
        "what is tkinter",
        "why tkinter",
        "what is tkinter used for",
        "why did you use tkinter"
    ]:
        return (
            "Tkinter is Python's standard library for creating "
            "graphical user interfaces. I use it to create "
            "this chatbot window."
        )

    # --------------------------------------------------------
    # CONTROL FLOW
    # --------------------------------------------------------
    elif user_input in [
        "what is control flow",
        "explain control flow",
        "why control flow"
    ]:
        return (
            "Control flow determines the order in which statements "
            "in a program are executed. If-else statements and "
            "loops are examples of control flow."
        )

    # --------------------------------------------------------
    # AI VS RULE-BASED CHATBOT
    # --------------------------------------------------------
    elif user_input in [
        "are you real ai",
        "are you an ai",
        "are you artificial intelligence",
        "are you a real ai"
    ]:
        return (
            "I am a basic rule-based AI chatbot. I do not learn "
            "like modern machine-learning systems. I respond "
            "according to predefined rules."
        )

    # --------------------------------------------------------
    # GREETING RESPONSE
    # --------------------------------------------------------
    elif user_input in [
        "nice to meet you",
        "nice meeting you",
        "good to meet you"
    ]:
        return "Nice to meet you too! 😊"

    # --------------------------------------------------------
    # THANK YOU
    # --------------------------------------------------------
    elif user_input in [
        "thank you",
        "thanks",
        "thank",
        "thanks a lot",
        "thank you so much"
    ]:
        return "You're very welcome! 😊"

    # --------------------------------------------------------
    # SORRY
    # --------------------------------------------------------
    elif user_input in [
        "sorry",
        "i am sorry",
        "my mistake"
    ]:
        return "That's okay! 😊 No problem."

    # --------------------------------------------------------
    # JOKE
    # --------------------------------------------------------
    elif user_input in [
        "tell me a joke",
        "joke",
        "make me laugh",
        "say a joke"
    ]:
        return (
            "Why do programmers prefer dark mode? "
            "Because light attracts bugs! 😂"
        )

    # --------------------------------------------------------
    # FAVORITE / PERSONALITY
    # --------------------------------------------------------
    elif user_input in [
        "what is your favorite color",
        "what is your favourite color",
        "favorite color",
        "favourite colour"
    ]:
        return "My favorite color is blue! 💙"

    # --------------------------------------------------------
    # HAPPY RESPONSE
    # --------------------------------------------------------
    elif user_input in [
        "good",
        "great",
        "awesome",
        "nice",
        "excellent",
        "amazing"
    ]:
        return "That's great to hear! 😄"

    # --------------------------------------------------------
    # NEGATIVE RESPONSE
    # --------------------------------------------------------
    elif user_input in [
        "bad",
        "not good",
        "sad",
        "i am sad"
    ]:
        return (
            "I'm sorry to hear that. 😔 "
            "I hope things get better soon!"
        )

    # --------------------------------------------------------
    # UNKNOWN INPUT
    # --------------------------------------------------------
    else:
        return (
            "I'm sorry, I don't have a rule for that question yet. "
            "Try asking me about AI, Python, this project, "
            "my name, or what I can do."
        )


# ============================================================
# SEND MESSAGE
# ============================================================

def send_message(event=None):

    user_input = entry_box.get().strip()

    # Don't send an empty message
    if user_input == "":
        return

    # Enable chat area
    chat_area.config(state=tk.NORMAL)

    # Display user's message
    chat_area.insert(
        tk.END,
        "You: " + user_input + "\n",
        "user"
    )

    # Get chatbot response
    response = get_bot_response(user_input)

    # Display chatbot response
    chat_area.insert(
        tk.END,
        "Bot: " + response + "\n\n",
        "bot"
    )

    # Disable chat area again
    chat_area.config(state=tk.DISABLED)

    # Clear input box
    entry_box.delete(0, tk.END)

    # Automatically scroll to bottom
    chat_area.see(tk.END)

    # Close application after exit command
    if user_input.lower() in [
        "bye",
        "goodbye",
        "exit",
        "quit",
        "see you",
        "see you later"
    ]:
        root.after(1500, root.destroy)


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("DecodeBot - Rule-Based AI Chatbot")

root.geometry("700x600")

root.resizable(False, False)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="🤖 DecodeBot",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=(15, 5))


subtitle_label = tk.Label(
    root,
    text="Rule-Based Artificial Intelligence Chatbot",
    font=("Arial", 11)
)

subtitle_label.pack(pady=(0, 10))


# ============================================================
# CHAT AREA
# ============================================================

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=75,
    height=25,
    font=("Arial", 11),
    state=tk.DISABLED
)

chat_area.pack(
    padx=20,
    pady=10
)


# ============================================================
# TEXT FORMATTING
# ============================================================

chat_area.tag_config(
    "user",
    font=("Arial", 11, "bold")
)

chat_area.tag_config(
    "bot",
    font=("Arial", 11)
)


# ============================================================
# WELCOME MESSAGE
# ============================================================

chat_area.config(state=tk.NORMAL)

chat_area.insert(
    tk.END,
    "Bot: Hello! 👋 I am DecodeBot.\n"
    "Bot: I am a rule-based AI chatbot.\n"
    "Bot: Ask me about AI, Python, this project, "
    "or what I can do.\n"
    "Bot: Type 'bye', 'exit', or 'quit' to close me.\n\n",
    "bot"
)

chat_area.config(state=tk.DISABLED)


# ============================================================
# INPUT FRAME
# ============================================================

input_frame = tk.Frame(root)

input_frame.pack(
    padx=20,
    pady=10,
    fill=tk.X
)


# ============================================================
# INPUT BOX
# ============================================================

entry_box = tk.Entry(
    input_frame,
    font=("Arial", 12)
)

entry_box.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    padx=(0, 10),
    ipady=8
)


# ============================================================
# SEND BUTTON
# ============================================================

send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    command=send_message
)

send_button.pack(
    side=tk.RIGHT,
    ipadx=15,
    ipady=5
)


# ============================================================
# ENTER KEY
# ============================================================

entry_box.bind(
    "<Return>",
    send_message
)


# ============================================================
# FOCUS ON INPUT BOX
# ============================================================

entry_box.focus()


# ============================================================
# START CHATBOT
# ============================================================

root.mainloop()