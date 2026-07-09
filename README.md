<div align="center">

# 🤖 RuleBot — A Rule-Based AI Chatbot

**AI Internship Project 1**

A simple, beginner-friendly command-line chatbot built with pure Python and `if-elif-else` logic — no external libraries or machine learning required.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
- [Sample Conversation](#-sample-conversation)
- [Project Structure](#-project-structure)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## 🌌 Overview

RuleBot is a **rule-based chatbot** — it doesn't use AI/NLP models to understand language. Instead, it matches user input against a predefined set of keywords and phrases using simple `if-elif-else` conditions, then responds accordingly. This project is the foundational first step in an AI internship track, meant to build a solid understanding of control flow, string handling, and program structure in Python before progressing to more advanced NLP-based or ML-based chatbots.

---

## ✨ Features

**Core requirements**
- Responds to greetings: `hello`, `hi`, `hey`
- Answers common questions:
  - "how are you"
  - "what is your name"
  - "who created you"
  - "what can you do"
- Handles exit commands: `bye`, `exit`, `quit`
- Runs continuously in a loop until the user exits

**Bonus features**
- 📋 `help` command — lists everything the bot can do
- 🕒 `date` / `time` — displays the current date and time
- ➕ Simple calculator — `calculate 5 + 3` (supports `+`, `-`, `*`, `/`, with divide-by-zero protection)
- 🧠 Remembers the user's name for the entire session and personalizes every response
- 🧹 Clean, commented, beginner-friendly code following good Python practices

---

## ⚙️ How It Works

1. **Startup** — the bot asks for your name once and stores it in a variable for the session.
2. **Main loop** — a `while True` loop repeatedly asks for input until an exit command is given.
3. **Input normalization** — every input is lowercased and stripped of extra whitespace, so `"Hello"`, `"hello "`, and `"HELLO"` are all treated the same.
4. **Rule matching** — an `if-elif-else` chain checks the normalized input against known keywords/phrases in order:
   - Empty input → prompts the user to type something
   - Exit commands → says goodbye and breaks the loop
   - Greetings → friendly greeting response
   - Question phrases → matched using `in` checks (e.g. `"how are you" in user_input_lower`)
   - `help` → prints the help menu
   - `date`/`time` → formats and prints `datetime.datetime.now()`
   - Anything starting with `calculate` → passed to a dedicated `calculate()` function
   - Anything else → a fallback "I didn't understand that" message
5. **Calculator function** — parses input like `calculate 5 + 3` into three parts (number, operator, number), validates them, then performs the operation with its own `if-elif-else` block. Manual parsing is used instead of `eval()` to keep the code safe and easy to follow.
6. **Exit** — typing `bye`, `exit`, or `quit` prints a personalized goodbye message and `break`s out of the loop, ending the program.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x (no external packages required — uses only the built-in `datetime` module)

### Run it

```bash
python chatbot.py
```

or, depending on your system:

```bash
python3 chatbot.py
```

---

## 💬 Sample Conversation

```
============================================================
 Welcome to RuleBot — a simple rule-based chatbot!
============================================================
Before we start, what's your name? Sarah

Nice to meet you, Sarah! Type 'help' anytime to see what I can do.

Sarah: hello
Bot: Hello Sarah! How can I help you today?
Sarah: how are you
Bot: I'm just a program, so I'm always doing great! How about you?
Sarah: what is your name
Bot: I'm RuleBot, your friendly rule-based chatbot!
Sarah: who created you
Bot: I was created by Sarah as part of an AI internship project!
Sarah: date
Bot: Right now it's Wednesday, 08 July 2026 | 08:22:09 PM
Sarah: calculate 12 + 8
Bot: The result is: 20
Sarah: calculate 10 / 0
Bot: I can't divide by zero!
Sarah: help

Here's what I can help you with:
  - Greet me: hello, hi, hey
  - Ask me:   how are you / what is your name / who created you / what can you do
  - Utilities: 'date' or 'time' -> shows current date & time
               'calculate <num1> <+ - * /> <num2>' -> does simple math
               'help' -> shows this message again
  - Exit:     bye / exit / quit

Sarah: bye
Bot: Goodbye, Sarah! It was great chatting with you. 👋
```

---

## 📁 Project Structure

```
rulebot/
├── chatbot.py     # Complete chatbot source code
└── README.md      # This file
```

Everything lives in a single file by design — this keeps the project approachable for a first internship submission, with clear section comments (`HELPER FUNCTIONS`, `MAIN CHATBOT LOGIC`, `ENTRY POINT`) instead of splitting into multiple modules.

---

## 🗺️ Future Improvements

- [ ] Support more natural phrasing using simple keyword lists instead of exact phrase matches (e.g. detect "how r u", "wats ur name")
- [ ] Add a conversation log that saves the chat history to a `.txt` file
- [ ] Support multi-step calculations (e.g. `2 + 3 * 4`) using a proper expression parser
- [ ] Add more personality — jokes, fun facts, or a "tell me a joke" command
- [ ] Move to NLP-based intent matching (e.g. using `nltk` or spaCy) as a follow-up project
- [ ] Wrap the chatbot logic in a class (`ChatBot`) for better structure as it grows
- [ ] Add unit tests for the `calculate()` function and input parsing

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free to use for learning, internship submissions, and portfolio purposes.

---

<div align="center">

Built with Python — no external libraries required.

</div>
