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


# SETTERS


# -----JOBS TABLE-----#

if __name__ == '__main__':
    username=input("Enter username: ")
    password=input("Enter password: ")
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
    # init cursor (to exe queries)
    cursor = cnxn.cursor()
