"""
Registration Station project
"""

def read_file(file_name):
    file = open(file_name, 'r')
    contents = file.readlines()
    
    # file.close()
    return contents
    """
    Read and return contents of text file
    """


def input_user_name():
    
    username_input = input("Select username: 4 April - Johannesburg Physical - No prior experience\n")
    username = username_input

    return username
    """
    Takes username as input
    """


def correct_or_incorrect():

#     check = input("""Select username: Please enter valid existing username
# Select username: 4 April - Johannesburg Physical - No prior experience\n""")
#     return check


def correct_details():
    file = get_file_contents()
    username = input_user_name()

    for line in file:
        if username in file:
            return line

    incorrect = line.split('-')
    input_date = input("Replace the date here:\n")
    input_location = input("Replace the location here:\n")
    input_experience = input("Replace the experience here:\n")
    incorrect[1] = input_date
    incorrect[2] = input_location
    incorrect[3] = input_experience
    
    new_string = f"{username} - {incorrect[1]} - {incorrect[2]} - {incorrect[3]}" 
    print(new_string)
    for line in file:
        if username in line:
            file[1]= new_string
            
            return file[1]
    

    # corrected = incorrect.replace( old_value,new_value)
    
    """
    Prompt to correct and write user details to text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """

def get_file_contents():

    file_contents = read_file('bootcampers.txt')
    return file_contents



def find_username(file_name):

    username = input_user_name()
    
    for line in file_name:
       if username in line:
            return line
    
    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
    @return corresponding information for username
       """
    


if __name__ == "__main__":
    registrations_file = get_file_contents()
    information = find_username(registrations_file)
    print(information)
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()