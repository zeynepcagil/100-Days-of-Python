# 📘 100 Days of Code – Day 17: OOP Quiz Game

## 🎯 Concepts Learned
- Object-Oriented Programming (OOP) in Python
- Creating and using classes and objects
- Class attributes and instance methods (`__init__`, `self`)
- Separating logic into different classes
- Creating a list of objects from structured data
- Looping through questions dynamically
- Keeping score and displaying final results

## 🧠 Key Takeaways
- Using classes improves structure, reusability, and readability of code.
- The `Question` class is used to store individual question data (text + answer).
- The `QuizBrain` class controls the flow of the quiz (asking questions, checking answers).
- Using `while quiz.still_has_questions():` to manage the game loop safely.
- Data separation: keeping raw question data separate from logic and UI.

## ✅ What I Did
- Defined a `Question` class with two attributes: `text` and `answer`.
- Parsed a list of dictionaries to build a `question_bank` as a list of `Question` objects.
- Built a `QuizBrain` class to:
  - Track the current question number.
  - Ask questions with `next_question()`.
  - Check for remaining questions using `still_has_questions()`.
- Created a main program to run the quiz using a simple game loop.
- Displayed final score after all questions.

## 💡 Ideas for Expansion
- Add difficulty levels and categories.
- Shuffle questions randomly.
- Pull real questions from the Open Trivia DB API.
- Build a GUI version using Tkinter or PyQt.
- Add a timer per question or track response time.
- Web version using Flask or Django with database integration.

## 🔜 Next Step
I'd like to create a **Quiz App** that fetches questions from an API, possibly with category and difficulty filters, and displays them in a GUI or web format. Might try it in the next few days as a mini side project!
