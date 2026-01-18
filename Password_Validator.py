class PasswordValidator:
    '''

        Parameters:
            1. Must contain at least one upper case letter
            2. Must contain at least one lower case letter
            3. Must contian at least one number
            4. Must contain at least one special character
            5. Cannot have first or last name in the password
            6. Must have at least 8 characters
            7. Must not be in the 10k most common passwords file


    '''
    def __init__(self, password, firstName, lastName):

        self.password = password
        self.firstName = firstName
        self.lastName = lastName

        # PASSWORD PARAMETERS

        self.hasUpperCase = False
        self.hasLowerCase = False
        self.hasNumber = False
        self.hasSpecialChar = False
        self.noFirstName = False
        self.noLastName = False
        self.isGreaterThan8 = False
        self.notCommon = False

        self.passwordIsValid = False

    def checkUpperLowerSpecialNumber(self):
        self.hasLowerCase = any(character.islower() for character in self.password)
        self.hasUpperCase = any(character.isupper() for character in self.password)
        self.hasNumber = any(character.isdigit() for character in self.password)
        self.hasSpecialChar = any(not character.isalnum() for character in self.password)

    def checkFirstLastName(self):
        self.noFirstName = self.firstName.lower() not in self.password.lower()
        self.noLastName = self.lastName.lower() not in self.password.lower()

    def checkCommon(self):
        with open("10k_Most_Common.txt") as mostCommonPasswords:
            commonPasswords = {commonPassword.strip() for commonPassword in mostCommonPasswords}
        self.notCommon = self.password not in commonPasswords

    def checkLength(self):
        self.isGreaterThan8 = len(self.password)>=8

    def validatePassword(self):

        self.checkUpperLowerSpecialNumber()
        self.checkCommon()
        self.checkLength()
        self.checkFirstLastName()

        self.validityParameters = (
            self.hasUpperCase,
            self.hasLowerCase,
            self.hasNumber,
            self.hasSpecialChar, 
            self.noFirstName,
            self.noLastName,
            self.isGreaterThan8,
            self.notCommon,
        )

        self.passwordIsValid = all(self.validityParameters)
        if self.passwordIsValid:
            print("Your Password Is Valid")
            return [self.passwordIsValid,self.validityParameters]
        else:
            if not self.hasNumber:
                print("Password Must Contain At Least One Number")
            if not self.isGreaterThan8:
                print("Password Must Be At Least 8 Characters")
            if not self.notCommon:
                print("Your Password Is Too Common")
            if not self.noFirstName:
                print("Password Cannot Contain First Name")
            if not self.noLastName:
                print("Password Cannot Contain Last Name")
            if not self.hasLowerCase:
                print("Password Must Contain At Least One Lower Case Letter")
            if not self.hasUpperCase:
                print("Password Must Contain At Least One Upper Case Letter")
            if not self.hasSpecialChar:
                print("Password Must Contain At Least One Special Character (Ex: @, !, #, _)")
            
            return [self.passwordIsValid, self.validityParameters]