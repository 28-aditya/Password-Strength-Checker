class PasswordValidator:
    '''

        Parameters:
            1. Must contain an upper case letter
            2. Must contain a lower case letter
            3. Must contain a special character
            4. Cannot have first or last name in the password
            5. Must have at least 8 characters
            6. Must not be in the 500 most common passwords file


    '''
    def __init__(self, password, firstName, lastName):

        self.password = password
        self.firstName = firstName
        self.lastName = lastName

        # PASSWORD PARAMETERS

        self.hasUpperCase = False
        self.hasLowerCase = False
        self.hasSpecialChar = False
        self.noFirstName = False
        self.noLastName = False
        self.isGreaterThan8 = False
        self.notCommon = False

        self.passwordIsValid = False

    def check_upper_lower_special(self):
        self.hasLowerCase = any(character.islower() for character in self.password)
        self.hasUpperCase = any(character.isupper() for character in self.password)
        self.hasSpecialChar = any(not character.isalnum() for character in self.password)

    def check_first_last_name(self):
        self.noFirstName = self.firstName.lower() not in self.password.lower()
        self.noLastName = self.lastName.lower() not in self.password.lower()

    def check_common(self):
        with open("10k_Most_Common.txt") as mostCommonPasswords:
            commonPasswords = {commonPassword.strip() for commonPassword in mostCommonPasswords}
        self.notCommon = self.password not in commonPasswords

    def check_length(self):
        self.isGreaterThan8 = len(self.password)>=8

    def validate_password(self):

        self.check_upper_lower_special()
        self.check_common()
        self.check_length()
        self.check_first_last_name()

        validity_parameters = (
            self.hasUpperCase,
            self.hasLowerCase,
            self.hasSpecialChar, 
            self.noFirstName,
            self.noLastName,
            self.isGreaterThan8,
            self.notCommon,
        )

        self.passwordIsValid = all(validity_parameters)
        if self.passwordIsValid:
            print("Your Password Is Valid")
            return [self.passwordIsValid, validity_parameters]
        else:
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
            
            return [self.passwordIsValid, validity_parameters]