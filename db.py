'''
Defines all database queries and methods
'''

import mysql.connector as mysql

# -----VOLUNTEER/MEMBER TABLE-----#
'''
getAllFromV():
INPUT: None
OUTPUT: All records in Volunteers table
'''


def getAllFromV():
    stmt = "SELECT * FROM volunteers"
    cursor.execute(stmt)
    result = cursor.fetchall()
    # convert to view
    if result == "":
        print("No results")
    else:
        for x in result:
            print(x)


'''
getActiveMembers():
INPUT: None
OUTPUT: All active members of Peace (list)
'''


def getActiveMembers():
    stmt = "SELECT vFName, vLName FROM volunteers WHERE vMember=1"
    cursor.execute(stmt)
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        for x in result:
            print(x)


'''
getRecordOfV()
INPUT: name (string)
OUTPUT: The record that matches <name> (list)
'''


def getRecordOfV(name):
    n = name.split(" ")
    stmt = "SELECT vEmail, vPhone FROM volunteers WHERE vFName= %s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for ", name)
        for x in result:
            print(x)


'''
getEmail()
INPUT: name (string)
OUTPUT: The email of <name> (string)
'''


def getEmail(name):
    n = name.split(" ")
    stmt = "SELECT vEmail FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for ", name)
        for x in result:
            print(x)


'''
getPhone()
INPUT: name (string)
OUTPUT: The phone number of <name> (string)
'''


def getPhone(name):
    n = name.split(" ")
    stmt = "SELECT vPhone FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for ", name)
        for x in result:
            print(x)


'''
getBirthday()
INPUT: name (string)
OUTPUT: The birthday of <name> (datetime)
'''


def getBirthday(name):
    n = name.split(" ")
    stmt = "SELECT vBirthday FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for ", name)
        for x in result:
            print(x)


'''
getMarriageInfo()
INPUT: name (string)
OUTPUT: Marriage status, Anniversary, Partner of record with <name> (list)
'''


def getMarriageInfo(name):
    n = name.split(" ")
    stmt = "SELECT vMarriageStatus, vPartner, vAnniversary  FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for ", name)
        for x in result:
            print(x)


'''
getChurchBkgd()
INPUT: name (string)
OUTPUT: Past and current Church membership history (list)
'''


def getChurchBkgd(name):
    n = name.split(" ")
    stmt = "SELECT vChurchBackground FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for ", name)
        for x in result:
            print(x)


'''
getBaptism()
INPUT: name (string)
OUTPUT: Date of baptism of record with <name> (datetime)
'''


def getBaptism(name):
    n = name.split(" ")
    stmt = "SELECT vDateBaptism FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


'''
getConfirmation()
INPUT: name (string)
OUTPUT: Date of confirmation of record with <name> (datetime)
'''


def getConfirmation(name):
    n = name.split(" ")
    stmt = "SELECT vDateConfirmation FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


'''
getListChildren()
INPUT: name (string)
OUTPUT: Children of record with <name> (list)
'''


def getListChildren(name):
    n = name.split(" ")
    stmt = "SELECT vListChildren FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


'''
getVHistory()
INPUT: name (string)
OUTPUT: Volunteer history of record with <name> (list)
'''


def getVHistory(name):
    n = name.split(" ")
    stmt = "SELECT vHistory FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


'''
getSkills()
INPUT: name (string)
OUTPUT: Skills of record with <name> (list)
'''


def getSkills(name):
    n = name.split(" ")
    stmt = "SELECT vSkills FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


'''
getInterests()
INPUT: name (string)
OUTPUT: Interests of record with <name> (list)
'''


def getInterests(name):
    n = name.split(" ")
    stmt = "SELECT vInterests FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


'''
getHobbies()
INPUT: name (string)
OUTPUT: Hobbies of record with <name> (list)
'''


def getHobbies(name):
    n = name.split(" ")
    stmt = "SELECT vHobbies FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


'''
getQualified()
INPUT: name (string)
OUTPUT: Qualifications of record with <name> (list)
'''


def getQualified(name):
    n = name.split(" ")
    stmt = "SELECT vQualified FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


'''
getGifts()
INPUT: name (string)
OUTPUT: Spiritual gifts of record with <name> (list)
'''


def getGifts(name):
    n = name.split(" ")
    stmt = "SELECT vGifts FROM volunteers WHERE vFName=%s AND vLName=%s"
    cursor.execute(stmt, [n[0], n[1]])
    result = cursor.fetchall()
    if result == "" or result == []:
        print("No results")
    else:
        print("Results for", name)
        for x in result:
            print(x)


# MIGHT MAKE MORE FLEXIBLE WITH UI
'''
getBirthdaysBetween()
INPUT: datetime 1, datetime 2
OUTPUT: List of all people with birthdays between date1 and date2
'''
'''
getContactWithSkills()
INPUT: list of skills []
OUTPUT: All (name, email, phone) records with skills that match input
'''
'''
getContactWithInterests()
INPUT: list of interests []
OUTPUT: All (name, email, phone) records with skills that match input
'''
'''
getContactWithGifts()
INPUT: list of spiritual gifts []
OUTPUT: All (name, email, phone) records with skills that match input
'''
'''
getContactWithHobbies()
INPUT: list of skills []
OUTPUT: All (name, email, phone) records with skills that match input
'''

# SETTERS
'''
addNewRecord()
INPUT: fName (str, MAN.), lName (str, MAN.), email (str, MAN.), phone (str), birthday (datetime; year-month-day), marriageStatus (str)
    partner (str), anniversary (datetime; year-month-day), churchbckg(str), baptism (datetime; year-month-day), 
    confirmation (datetime; year-month-day),children (list [str]), history (list [str]), skills (list[str]), interests (list[str]), 
    gifts (list[str]), hobbies (list[str]), qualifiedFor (list[str]), member(int [0,1], MAN.)
OUTPUT: Success if given name is not already in db, failure otherwise
'''


def addNewRecord(fName, lName, email, phone, birthday, marriageStatus, partner, anniversary, church, baptism,
                 confirmation, children, history, skills, interests, gifts, hobbies, qualifiedFor, member):
    if fName=="" or fName==None:
        print("Firstname is required")
    elif lName=="" or lName==None:
        print("Lastname is required")
    elif email=="" or email==None:
        print("Email is required")
    elif member == None:
        print("Member status must be either 0 (non member) or 1 (member)")
    else:
        stmt = "INSERT INTO volunteers VALUES (fName,lName, email, phone, birthday, marriageStatus,partner, anniversary, church, baptism, confirmation," \
           "children, history, skills, interests, gifts, hobbies, qualifiedFor, member);"
        cursor.execute(stmt)
    #result = cursor.fetchall()

def updateEmail(name, nEmail):
    n = name.split(" ")
    stmt = "UPDATE volunteers SET vEmail = %s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt,nEmail, n[0], n[1] )

def updatePhone(name, nPhone):
    n = name.split(" ")
    stmt = "UPDATE volunteers SET vPhone = %s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt,nPhone, n[0], n[1] )

def updateName (name, nName):
    n = name.split(" ")
    nn = nName.split(" ")
    stmt = "UPDATE volunteers SET vFName = %s, vLName = %s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt, nn[0], nn[1], n[0], n[1])

def updateMarriage(name, status, partner, anniversary):
    n = name.split(" ")
    stmt = "UPDATE volunteers SET vMarraigeStatus = %s, vPartner = %s, vAnniversary = %s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt, status, partner, anniversary, n[0], n[1])

def updateBaptism (name, baptism):
    n = name.split(" ")
    stmt = "UPDATE volunteers SET vDateBaptism = %s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt, baptism, n[0], n[1])

def updateConfirmation(name, conf):
    n = name.split(" ")
    stmt = "UPDATE volunteers SET vDateConfirmation = %s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt, conf, n[0], n[1])

def updateChildren(name, children):
    # get current children and append new to list
    n = name.split(" ")
    current = "SELECT vListChildren FROM volunteers WHERE vFName=%s AND vLName=%s;"
    cursor.execute(current, n[0],n[1])
    result = cursor.fetchall()
    for x in result:
        if x not in children:
            children.append()
    stmt = "UPDATE volunteers SET vListChildren=%s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt, children, n[0], n[1])

def updateQualifications(name, qual):
    # get current qualifications and append new to list
    n = name.split(" ")
    current = "SELECT vQualifiedFor FROM volunteers WHERE vFName=%s AND vLName=%s;"
    cursor.execute(current, n[0], n[1])
    result = cursor.fetchall()
    for x in result:
        if x not in qual:
            qual.append()
    stmt = "UPDATE volunteers SET vQualifiedFor=%s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt, qual, n[0], n[1])

def updateMemberStatus(name, status):
    n = name.split(" ")
    stmt = "UPDATE volunteers SET vMember=%s WHERE vFName=%s AND vLName=%s;"
    cursor.execute(stmt, status, n[0], n[1])

# -----JOBS TABLE-----#

if __name__ == '__main__':
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        host = input("Enter host: ")
        database = input("Enter database: ")
        # init cnxn to db
        cnxn = mysql.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print(cnxn)
        # init cursor
        cursor = cnxn.cursor()
    except ConnectionError:
        print("cnxn failed, we'll  get em nexttime")
