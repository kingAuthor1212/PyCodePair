"""
Registration Station project
"""

def read_file(file_name):
    file = open(file_name, 'r')
    contents = file.read()
    print(contents)
    file.close()
    return file
    """
    Read and return contents of text file
    """


def input_user_name():
    username_input = input("Enter Your Username Here:\n")
    
    return username_input
    """
    Takes username as input
    """


def correct_or_incorrect():

    """
    Prompt to ask if details are correct or not
    @return correct or incorrect
    """


def correct_details():

    """
    Prompt to correct and write user details to text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """

def get_file_contents():

    """Return desired text file"""


def find_username(file_name):

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