"""
Registration Station project
"""
import sys

def read_file(file_name):

    with open(file_name, 'r', errors= 'ignore') as file:
        contents = file.readlines()
    return contents
    """
    Read and return contents of text file
    """


def input_user_name():
    username_input= sys.argv[1]

    return username_input

   
    """
    Takes username as input
    """


def correct_or_incorrect():

    check = input("Is this correct? (Y/n):\n").lower()
    if check == 'y':
        return 'correct'
    return 'incorrect'


def correct_details():
    username = input_user_name() #TODO: delete the line first then add it

    date = input("Replace the date here:\n")
    location = input("Replace the location here:\n")
    experience = input("Replace the experience here:\n")
    
    new_details = f"{username} - {date} - {location} - {experience}" 

    with open('bootcampers.txt', 'a') as file:
        file.write(new_details + '\n')

    return new_details
        
    """
    Prompt to correct and write user details to text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """

def get_file_contents():

    return read_file('bootcampers.txt')


def find_username(file_name):
    #while True:
    username = input_user_name()
    details = file_name

    # for line in details:
    #     if not line:
    #         continue

    # for line in details:
    #     if username in line:
    #         print(line)
    #         return f"Select username: {line}"
    #     else:
    #         return "Select username: Please enter a valid existng username"

    for line in details:
        print(line)
        if username in line:
            user, info = line.strip().split('-', 1)
            return f"Select username: {info} \n"
     
    
    # for line in details:
    #     if username in line:
    #         return print(f"Select username: {line} \n")
    #     elif username in details[1]:
    #         print(details[1])
    #         return print(f"Select username: {details[1]} \n")
    #     elif username in details[2]:
    #         print(details[2])
    #         return print(f"Select username: {details[2]} \n")
    #     else:
    #         return "Select username: Please enter a valid existing username"
 
    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
    @return corresponding information for username
       """
    


if __name__ == "__main__":
    registrations_file = get_file_contents()
    information = find_username(registrations_file)
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()

