from typing import Callable
import validators

contacts = {}


def handle_help(args):
    return """
Command list:
help   - Show this help
add    - Add new contact. Example: add username +0981112233
phone  - Show phone by contact. Example: phone username
change - Change contact phone. Example: change username +0982223344
all    - Show all contacts
exit   - Exit the program
close  - Close the program
hello  - Welcome message 
"""


@validators.input_error(contacts)
def add_contact(args):
    name, phone = args
    contacts[name] = phone

    return "Contact added."

@validators.change_contact_error(contacts)
def change_contact(args):
    name, phone = args

    contacts[name] = phone

    return "Contact changed."

def show_all(args):
    result = []
    for name, phone in contacts.items():
        result.append(f"Name={name}, phone={phone}")
    return '\n'.join(result)

def handle_exit(args):
    print('Good bye!')
    exit(0)

@validators.exact_count_args(1)
def find_by_phone(args):
    name = args[0]

    for contact_name, contact_phone in contacts.items():
        if contact_name.find(name) >= 0:
            return contact_phone

    return 'Contact is not found.'

def welcomme(args):
    return 'How can I help you?'

commands = {
    'help': handle_help,
    'add': add_contact,
    'phone': find_by_phone,
    'change': change_contact,
    'all': show_all,
    'exit': handle_exit,
    'close': handle_exit,
    'hello': welcomme
}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args

def main():
    print("Welcome to the assistant bot!\nContact Manager 1.1.\nEnter 'help' to see all supported commands.")

    while True:
        user_input = input(">> ")
        command, *args = parse_input(user_input)

        if command in commands:
            print(commands[command](args))
        else:
            print(f"Invalid command. Type 'help' to see all supported commands.")

if __name__ == "__main__":
    main()