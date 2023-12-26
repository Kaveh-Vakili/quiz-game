from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for index in question_data:


    q = index['question']
    a = index['correct_answer']
    question_bank.append(Question(q, a))


# print(question_bank[0].text)

user_quiz = QuizBrain(question_bank)
user_quiz.next_question()
