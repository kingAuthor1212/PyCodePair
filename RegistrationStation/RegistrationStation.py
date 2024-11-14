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
    username_input= input("Select username: ")

    return username_input

   
    """
    Takes username as input
    """


def correct_or_incorrect():

    check = input("Is this correct? (Y/n): ")
    if check == 'y':
        return "correct"
    elif check == 'n':
        return 
    


def correct_details():
    username = input("Username: ")#TODO: delete the line first then add it
    date = input("Date: ")
    location = input("Location: ")
    experience = input("Experience: ")
    
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

def get_file_contents(file_name="bootcampers.txt"):

    return read_file(file_name)


def find_username(file_name):
    #while True:
    username = input_user_name()
    details = get_file_contents(file_name)

   
    for line in details:
        if username in line:
            # print(line)
            user, info = line.strip().split(' - ', 1)
            print(info)
            return info
        
    print("Please enter valid existing username")
    return find_username(file_name)
 
    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
    @return corresponding information for username
       """
    


if __name__ == "__main__":
    information = find_username("bootcampers.txt")
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        # else:
        #     correct_details()
