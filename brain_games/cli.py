import prompt

def name_user():
    name = prompt.string('May I have your name? ')
    return name

def welcome_user():
    print("Welcome to the Brain Games!")
    print(f"Hello, {name_user()}!")
    
