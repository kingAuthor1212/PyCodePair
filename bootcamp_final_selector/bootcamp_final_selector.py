def user_name():
    '''
    Use this function to get the user input (username)
    '''
    pass


def read_file(username):
    '''
    Use this function to open and read the contents of the file student_results.txt 
    in order that you may extract the users results
    '''
     
    return student_results

    
def get_student_scores(student_results):
    '''
    Use this function to get all the users relevant scores
    '''
    return list_scores
    
def exam_score(list_scores):
    '''
    Use this function to calculate the users exam score:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    
    return round(exam_score)


def exam_percentage(list_scores):
    '''
    Use this function to calculate the users exam percentage:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    
    return round(exam_percentage)


def group_project_score(list_scores):
    '''
    Use this function to calculate the users group project score:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    
    return round(group_project_score)


def group_project_percentage(list_scores):
    '''
    Use this function to calculate the users group project percentage:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    
    return round(group_project_percentage)


def daily_exercise_score(list_scores):
    '''
    Use this function to calculate the users daily exercise score:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    
    return round(daily_exercise_score)


def daily_exercise_percentage(list_scores):
    '''
    Use this function to calculate the users daily exercise percentage:
    One for the exam (out of 100), 
    one for the group project (out of 10), 
    one for daily exercises (out of 30). 
    The exam will weigh 60%, the group project 20% and the daily exercises 20%.
    '''
    
    
    return round(daily_exercise_percentage)


def final_result(exam_result, group_project, daily_exercise):
    final_result = ""
    '''
    Use this function to calculate the user's final result out a 100
    '''
   
    return round(final_result)


def type_of_pass(final_result):
    
    '''
    Use this function to determine whether they scored a first class pass, or an average pass 
    or if the user has failed.
    First Class Pass -  90 and  above
    Pass - 40 to 89 
    Fail - below 40
    '''
    
    return type_of_pass



# calling function


if __name__ == '__main__':
    '''
    Do not edit this section, these are the function calls
    '''
    username = user_name()
    student_results = read_file(username)
    list_scores = get_student_scores(student_results)
    exam_result = exam_score(list_scores)
    exam_percentage = exam_percentage(list_scores)
    group_project = group_project_score(list_scores)
    group_project_percentage = group_project_percentage(list_scores)
    daily_exercise = daily_exercise_score(list_scores)
    daily_exercise_percentage = daily_exercise_percentage(list_scores)
    average_score = final_result(exam_result, group_project, daily_exercise)
    type_of_pass(average_score)
