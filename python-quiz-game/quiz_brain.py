class QuizBrain():
    def __init__(self, questions):
        self.score = 0
        self.question_number = 0
        self.questions = questions

    def nextQuestion(self):
        current_question = self.questions[self.question_number].text
        correct_answer = self.questions[self.question_number].answer
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number} {current_question} (True/False): ")
        self.check_answer(user_answer, correct_answer)


    def still_has_question(self):
        return self.question_number < len(self.questions)
    

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("You got that right.🥳")
        else:
            print("You are wrong.😢")
        print(f"Your Score: {self.score}/{self.question_number}")
        print(f"The correct answer was: {correct_answer}")
        