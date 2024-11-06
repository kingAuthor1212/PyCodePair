from xml.dom import UserDataHandler
 
def user_details():
    """
    Prompt user input
    """
    user_details_list = []
    while len(user_details_list) < 4:
        first_name = input("Insert your first name: ")
        user_details_list.append(first_name)

        last_name = input("Insert your last name: ")
        user_details_list.append(last_name)


        cohort = input("Insert your cohort: ")
        user_details_list.append(cohort)

        campus = input("Insert the campus you will be attending in: ")
        user_details_list.append(campus)

    return user_details_list


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """


def user_campus(campus):
    """
    Return valid campus abbreviations
    """


if __name__ == '__main__':
    print(user_details())
    