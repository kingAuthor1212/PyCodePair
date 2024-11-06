"""
Registration Station project
"""

def read_file(file_name):
    file = open(file_name, 'r')
    contents = file.readlines()
    print(contents)
    # file.close()
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

    check = input("Is this correct?:\n")
    return check


def correct_details():

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

    username = input("Enter username: ")

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
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()