from data import question_data
from questions import Question
from quizbrain import QuizBrain

question_bank = []
for questions in question_data:
    question_answer = questions["answer"]
    question_text = questions["text"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
print("Welcome to google RAPID FIRE QUIZ...")

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
