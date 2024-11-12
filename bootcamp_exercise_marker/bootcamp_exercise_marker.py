# Abdur-Raheem Lee <abdur-raheem@wethinkcode.co.za>
import random

def read_file():
    '''
    Reads contents from the text file (questions.txt)
    @return a list of five random questions
    '''
    #Naledi made changes:
    with open ("questions.txt", "r") as questions:
        questions_list = questions.readlines()
    random.shuffle(questions_list)
    #list_of_questions = questions_list[:5]
    return questions_list
    

def ask_questions(list_of_questions):
    '''
    Sends quesions one at a time to be displayed
    @param list of five questions
    @return a list of questions the user answer incorrectly
    '''
    if not list_of_questions or not isinstance(list_of_questions, list):
        raise ValueError("list_of_questions must be a non-empty list")
    
    incorrect_question = []
    for i, question in enumerate(list_of_questions):
        # Ensure the question format is correct before processing
        parts = question.split(', ')
        if len(parts) < 2:
            print(f"Skipping invalid question format: {question}")
            continue
        
        userAnswer = display_question(i + 1, question)
        correct_answer = parts[1].strip().upper()
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
    quest_list = question.split(', ')
    print(f"{question_number}. {quest_list[0]}")
    for option in quest_list[1:]:
        print(option)
    userAnswer = input("Your answer (A, B, C :) ").strip().upper()
    return userAnswer

def is_correct_answer(solution, userAnswer):
    '''
    Checks if the answer given by the user is correct
    @param solution - The correct answer
    @param user_answer - The answer entered by the user
    @return boolean indicating if user answered correctly or not
    '''
    return solution.strip().upper() == userAnswer

def next_round(current_round):
    '''
    Calculates the next round
    @param current round completed
    @return integer next round
    '''
    return current_round +1

if __name__ == '__main__':

    score = 0
    current_round = 0
    question_list = read_file()

    while score < 5:
        current_round = next_round(current_round)
        question_list = ask_questions(question_list)
        score = 5 - len(question_list)