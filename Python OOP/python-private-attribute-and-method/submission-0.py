class PasswordManager:
    def __init__(self, password: str):
        self.__password = password  
    
    # TODO: Implement the verify_password method
    def __verify_password(self, input_password) -> bool:
        if input_password == self.__password:
            return True
        else:
            return False   

    def verify_password(self, input_password) -> bool:
        return self.__verify_password(input_password)
    
    def get_password(self) -> str:
        return self.__password



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
