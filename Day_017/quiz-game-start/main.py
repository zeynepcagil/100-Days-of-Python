from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_test=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_test,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed quiz! \n Your final score was: {quiz.score}/{quiz.question_number}")