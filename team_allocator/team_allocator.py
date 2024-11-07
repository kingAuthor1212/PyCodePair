'''
    This is the team allocator project solution example project
'''


def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_students = []
    
    for x in student_list:
        x = x.lower().replace(" ", "")
        if "durban" in x:
            dbn_students.append(x)
    return dbn_students


def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []
    
    for x in student_list:
        x  = x.lower().replace(" ", "")
        if "capetown" in x:
            cpt_students.append(x)

    return cpt_students


def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []
    for student in student_list:
        clean_student = student.replace(" ", "").lower()
        if "johannesburg" in clean_student:
            jhb_students.append(clean_student)
    return jhb_students



def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []

    for student in student_list:
        clean_student = student.replace(" ", "").lower()
        if "phokeng" in clean_student:
            nw_students.append(clean_student)
    return nw_students

    
def dbn_physical_students(dbn_physical):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_students = dbn_campus_students(dbn_physical)
    dbn_physical_students = []

    for x in dbn_students:
        if "physical" in x:
            dbn_physical_students.append(x)

    return dbn_physical_students


def dbn_physical_teams(physical_teams):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    dbn_teams_four = dbn_physical_students(physical_teams)
    dbn_teams = []
    for x in range(0, len(dbn_teams_four), 4):
        team = dbn_teams_four[x:x+4]
        dbn_teams.append(team)
    return dbn_teams

def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''



def cpt_physical_students(cpt_physical):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    cpt_students = cpt_campus_students(cpt_physical)
    cpt_physical_students =  []

    for x in cpt_students:
        if "physical" in x:
            cpt_physical_students.append(x)

    return cpt_physical_students


def cpt_physical_teams(physical_teams):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''

    cpt_teams_four = cpt_physical_students(physical_teams)
    cpt_teams = []
    for x in range(0, len(cpt_teams_four), 4):
        team = cpt_teams_four[x:x+4]
        cpt_teams.append(team)
    return cpt_teams

def cpt_teams_file(capetown_final_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''


def jhb_physical_students(students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    jhb_students = jhb_campus_students(students)
    jhb_physical_students = []

    for student in jhb_students:
        if "physical" in student:
            jhb_physical_students.append(student)
    return jhb_physical_students



def jhb_physical_teams(students):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    jhb_physical_teams = []
    jhb_physical = jhb_physical_students(students)

    while len(jhb_physical) != 0:
        x = jhb_physical[:4]
        jhb_physical_teams.append(x)
        del jhb_physical[:4]

    return jhb_physical_teams

def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''
    teams = jhb_physical_teams(jhb_final_teams)
    strings = []

    for list in teams:
        for element in list:
            for item in element.split("-"):
                strings.append(item)
            strings.append("\n")
        
    with open("campus_teams.txt", "w") as text_file:
        text_file.write('\n'.join(strings))


def nw_physical_students(students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    nw_students = nw_campus_students(students)
    nw_physical_students = []

    for student in nw_students:
        if "physical" in student:
            nw_physical_students.append(student)
    return nw_physical_students


def nw_physical_teams(students):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''
    nw_physical_teams = []
    nw_physical = jhb_physical_students(students)

    while len(nw_physical) != 0:
        x = nw_physical[:4]
        nw_physical_teams.append(x)
        del nw_physical[:4]

    return nw_physical_teams


def nw_teams_file(nw_final_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''
    teams = nw_physical_teams(nw_final_teams)
    strings = []

    for list in teams:
        for element in list:
            for item in element.split("-"):
                strings.append(item)
            strings.append("\n")
        
    with open("campus_teams.txt", "w") as text_file:
        text_file.write('\n'.join(strings))


def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    
    virtual_campus = []
    for student in student_list:
        if "Virtual" in student:
            virtual_campus.append(student)
    return virtual_campus


def virtual_teams(students):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''
    virtual_teams = []
    virtual = get_virtual_students(students)
    virtual= [student.replace(" ", "").lower() for student in virtual]

    while len(virtual) != 0:
        x = virtual[:4]
        virtual_teams.append(x)
        del virtual[:4]

    return virtual_teams


def virtual_teams_file(students):
    '''
    write and save the information in the virtual_teams into a textfile
    '''
    teams = []
    virtual = get_virtual_students(students)


    while len(virtual) != 0:
        x = virtual[:4]
        teams.append(x)
        del virtual[:4]

    strings = []

    for list in teams:
        for element in list:
            for item in element.split("-"):
                strings.append(item)
            strings.append("\n")
        
    with open("virtual_teams.txt", "w") as text_file:
        text_file.write(''.join(strings))

if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    pass
