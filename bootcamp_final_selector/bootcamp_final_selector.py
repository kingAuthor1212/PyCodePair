

def user_name():
    # Request user name input
    print("Enter username: ", end='')

def read_file(username):
    '''
    Use this function to open and read the contents of the file student_results.txt 
    in order that you may extract the user's results
    '''
    student_results = {}

    try:
        with open('student_results.txt', 'r') as file:
            section = None
            for line in file:
                line = line.strip()
                if line == "exam_results:":
                    section = "exam"
                elif line == "group_project:":
                    section = "group_project"
                elif line == "Daily_exercises:":
                    section = "daily_exercises"
                elif section and line:
                    student, score = line.split(" - ")
                    score = int(score)
                    if student == username:
                        student_results[section] = score
    except FileNotFoundError:
        print("File not found.")
    
    return student_results

def get_student_scores(student_results):
    # Ensure all necessary sections are available, default to 0 if missing
    exam_score = student_results.get("exam", 0)
    group_project_score = student_results.get("group_project", 0)
    daily_exercises_score = student_results.get("daily_exercises", 0)
    
    # Return the scores in a list
    return [exam_score, group_project_score, daily_exercises_score]

def exam_score(scores):

    total_score = sum(scores)
    average_score = total_score / len(scores)
    adjusted_score = average_score - 2  
    return round(adjusted_score)




def exam_percentage(list_scores):
    '''
    Return the user's exam score as the exam percentage.
    
    Parameters:
    - list_scores (list): A list of scores in the format [exam, group_project, daily_exercises]
    
    Returns:
    - int: The exam percentage.
    '''
    
    # The exam score is already in percentage terms out of 100
    return list_scores[0]

def group_project_score(list_scores):
    '''
    Return the user's group project score directly.
    
    Parameters:
    - list_scores (list): A list of scores in the format [exam, group_project, daily_exercises]
    
    Returns:
    - int: The group project score.
    '''
    
    # Directly return the group project score
    return list_scores[1]

# bootcamp_final_selector.py

def group_project_percentage(list_scores):
    '''
    Calculate the user's group project percentage.
    
    Parameters:
    - list_scores (list): A list of scores in the format [exam, group_project, daily_exercises]
    
    Returns:
    - int: The adjusted group project percentage.
    '''
    
    # Extract the group project score
    group_project_score = list_scores[1]
    
    # Calculate the percentage based on max score of 10, scaled to 50%
    group_project_percentage = (group_project_score * 100 / 10) * 0.5
    
    # Return the rounded result
    return round(group_project_percentage)


def daily_exercise_score(list_scores):
    '''
    Calculate the adjusted daily exercise score based on a scaling factor.
    
    Parameters:
    - list_scores (list): A list of scores in the format [exam, group_project, daily_exercises]
    
    Returns:
    - int: The adjusted daily exercise score, rounded to the nearest integer.
    '''
    
    # Extract daily exercise score
    daily_exercises = list_scores[2]
    
    # Calculate the score scaled out of 20 (based on 30 max points for daily exercises)
    daily_exercise_score = (daily_exercises * 20) / 30
    
    # Return the rounded result
    return round(daily_exercise_score)



def daily_exercise_percentage(list_scores):
    '''
    Calculate the user's daily exercise percentage.
    Parameters:
    - list_scores (list): A list of scores in the format [exam, group_project, daily_exercises]
    
    Returns:
    - int: The rounded daily exercise percentage.
    '''
    
    # The daily exercise score is the third item in the list
    daily_exercises = list_scores[2]
    
    # Calculate the percentage based on a maximum of 30 points
    daily_exercise_percentage = (daily_exercises / 30) * 100
    
    # Return the rounded percentage
    return round(daily_exercise_percentage)


def final_result(exam, group_project, daily_exercise):
    # Sum of the three scores for final result
    return exam + group_project + daily_exercise

def type_of_pass(final_score):
    # Determine the type of pass based on the final score
    if final_score >= 70:
        return "First Class Pass"
    elif final_score >= 40:
        return "Pass"
    else:
        return "Fail"



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
