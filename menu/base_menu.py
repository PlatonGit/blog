from input_utils import (get_input_function, get_num_input_function)
from custom_exceptions import (UserExitException, UserInputTextException, UserInputNumException)


class Option:
    def __init__(self, id, title, mode):
        self.id = id
        self.title = title
        self.mode = mode


class BaseMenu:
    def __init__(self, title, options):
        self.title = title
        self.options = options


    def show(self):
        print('\n---------------', self.title, '---------------')
        for option in self.options:
            print(f'[{option.id}] - {option.title}')


    def user_id_input(self):
        input_func = get_num_input_function()

        while True:
            try:
                self.show()
                input_id = input_func('\nEnter option\'s id: ')
                mode = self.options[int(input_id) - 1].mode
                break
            except (UserInputNumException, ValueError):
                print(f'\n>>> Invalid input; enter a number from {self.options[0].id} to {self.options[-1].id}. <<<')          
            except IndexError:
                print(f'\n>>> Index {input_id} doesn\'t exist; input a number from {self.options[0].id} to {self.options[-1].id}. <<<')
              
        return mode


    def user_text_input(self, string):
        input_func = get_input_function()

        def get_text(string):
            while True:
                try:
                    print('\n---------------', self.title, '---------------\n')
                    input_text = input_func(string)
                    return input_text
                except UserInputTextException:
                    print(f'\n>>> Invalid input; some of inputted symbols are not recognized by programm. <<<')

        text = get_text(string)
        return text


    def user_num_input(self, string):
        input_func = get_num_input_function()

        def get_num(string):
            while True:
                try:
                    print('\n---------------', self.title, '---------------\n')
                    input_num = input_func(string)
                    return input_num
                except UserInputNumException:
                    print(f'\n>>> Invalid input; input must be a number. <<<')
        
        num = get_num(string)
        return num

            