import os
from dotenv import load_dotenv


load_dotenv()
def checking():
    login = os.getenv("APP_LOGIN")
    password = os.getenv('APP_PASSWORD')

    if login and password:
        anonymus_login = input('Type your login: ')
        anonymus_password = input('Type your password: ')

        if login == anonymus_login and password == anonymus_password:
            print('You are successfully logged in')
        else:
            print('Login or password is incorrect')
    else:
        print('Environment variables not set')

if __name__ == "__main__":
    checking()

