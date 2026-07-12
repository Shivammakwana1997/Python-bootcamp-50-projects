'''
your are building a simple app that register users
you want to separate concerns : geeting input , vaildating it , and saving it 
task:
write register_user() that calls :
get input()
valiadate_input()
save_to_db()
'''


def get_input():
    print("Getting user input")


def validate_input():
    print("Validating user info")


def save_to_db():
    print("Saving user to database")


def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("user registered successfully")

register_user()