def main_passwordChecker(password, firstName, lastName):

    '''

    Parameters:
        1. Must contain an upper case letter
        2. Must contain a lower case letter
        3. Must contain a special character
        4. Cannot have first or last name in the password
        5. Must have at least 8 characters
        6. Must not be in the 500 most common passwords file


    '''
    # PARAMETERS
    hasUpperCase = False
    hasLowerCase = False
    hasSpecialChar = False
    noFirstName = False
    noLastName = False
    isGreaterThan8 = False
    notCommon = False
    passwordIsValid = False

    # TEST 1

    for character in "abcdefghijklmnopqrstuvwxyz":
        if character in password:
            hasLowerCase = True
            break

    # TEST 2

    for character in "abcdefghijklmnopqrstuvwxyz":
        if character.upper() in password:
            hasUpperCase = True
            break

    # TEST 3

    for character in password:
        if not character.isalnum():
            hasSpecialChar = True
            break

    # TEST 4

    if firstName.lower() not in password.lower():
        noFirstName = True

    # TEST 5

    if lastName.lower() not in password.lower():
        noLastName = True

    # TEST 6

    if len(password)>=8:
        isGreaterThan8 = True

    # TEST 7

    with open("10k-most-common.txt", "r") as commonPasswords:
        mostCommonPasswords = [p.strip() for p in commonPasswords]
        if password not in mostCommonPasswords:
            notCommon = True
    
    # TESTS COMPLETE

    parameterTuple = (isGreaterThan8,
                       notCommon, 
                       noLastName,
                       noFirstName,
                       hasLowerCase,
                       hasUpperCase,
                       hasSpecialChar)

    if isGreaterThan8 and notCommon and noLastName and noFirstName and hasLowerCase and hasUpperCase and hasSpecialChar:
        passwordIsValid = True
        print("Your password is valid")
        return [passwordIsValid]

    
    else:
        if not isGreaterThan8:
            print("Password Must Be At Least 8 Characters")
        if not notCommon:
            print("Your Password Is Too Common")
        if not noFirstName:
            print("Password Cannot Contain First Name")
        if not noLastName:
            print("Password Cannot Contain Last Name")
        if not hasLowerCase:
            print("Password Must Contain At Least One Lower Case Letter")
        if not hasUpperCase:
            print("Password Must Contain At Least One Upper Case Letter")
        if not hasSpecialChar:
            print("Password Must Contain At Least One Special Character (Ex: @, !, #, _)")

        return [passwordIsValid, parameterTuple]
        