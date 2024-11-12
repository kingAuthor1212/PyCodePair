# Abdur-Raheem Lee <abdur-raheem@wethinkcode.co.za>
import random
def read_file():
    '''
    Reads contents from the text file (questions.txt)
    @return a list of five random questions
    '''
    with open ("questions.txt", "r") as questions:
        questions_list = random.shuffle(questions.readlines.split())
        list_of_questions=[]
        for i in range(5):
            list_of_questions.append(questions_list.pop())
        return list_of_questions
        

def ask_questions(list_of_questions):
    '''
    Sends quesions one at a time to be displayed
    @param list of five questions
    @return a list of questions the user answer incorrectly
    '''
    incorrect_question = []
    for i, question in enumerate(list_of_questions):
        userAnswer = display_question(i + 1, question)
        correct_answer = question.split(', ')[1]
        if not is_correct_answer(correct_answer, userAnswer):
            incorrect_question.append(question)
    return incorrect_question
        

def display_question(question_number, question):
    '''
    Displays a single question from the list of questions
    Takes in an answer
    @param a single question
    @return the answer given by the user
    '''
    quest_parts = question.split(', ')
    print(f"{question_number}. {quest_parts[0]}")
    for option in quest_parts[1:]:
        print(option)
    # user_answer = input("Your answer (A, B, C :) ").strip().upper()
    # return user_answer

def is_correct_answer(solution, user_answer):
    '''
    Checks if the answer given by the user is correct
    @param solution - The correct answer
    @param user_answer - The answer entered by the user
    @return boolean indicating if user answered correctly or not
    '''
    if  str(solution) == str(user_answer):
        return True
    else:
        return False


def next_round(current_round):
    '''
    Calculates the next round
    @param current round completed
    @return integer next round
    '''
    return current_round+1


if __name__ == '__main__':

    score = 0
    current_round = 0
    question_list = read_file()

    while score < 5:
        current_round = next_round(current_round)
        question_list = ask_questions(question_list)
        score = 5 - len(question_list)
