user_dict = {}


class NameAlreadyExistError(Exception):
    pass

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except NameAlreadyExistError:
            return "User already saved!"
    return wrapper

@input_error
def handle_add(user_input): 
    command, name, phone = user_input.split(' ')
    if name in user_dict:
        raise NameAlreadyExistError
    user_dict.update({name : phone})
    return 'User {name} was succesfully added!'

def handle_show_all():
    result = ''
    for name, phone in user_dict.items():
        result += f'{name} : {phone} \n'
    return result

def handler(user_input):
    if user_input.startswith('add'):
        return handle_add(user_input)
    elif user_input.startswith('show all'):
        return handle_show_all()

def main():
    while True:
        user_input = input(">>> ")
        if user_input == 'exit':
            print('Goodbye!')
            break
        print(handler(user_input))

if __name__ == "__main__":
    main()