from cmd import Cmd
import os

class MyPrompt(Cmd):

    prompt = '>>> ' #specifies the command line prompt
    
    #prints welcome message
    intro = "Welcome! type help to list avaialable commands"

    #defining exit function
    def do_exit(self, inp):
        print("come back soon!")
        return True

    #defining add command
    def do_add(self, inp): #function to add two numbers together
        try:
            x = input('')
            y = input ('')
            z = int(x) + int(y)
            print("'{}' + '{}' + equals '{}'".format(x, y, z))
        except ValueError: #handles exception thrown for any value other than integers
            print("Invalid input, enter integers only")

    #defining list function
    def do_list(self, inp):
        dir = os.listdir('C:/Users/KIKE/Desktop/pythonprojects')
        for file in dir:
            print(file)

    # defining help functions
    def help_add(self):
        print("Adds 2 numbers together.")

    def help_exit(self):
        print("Exits the prompt.")

    def help_list(self):
        print("Lists the contents of the present directory")

p = MyPrompt()
p.cmdloop()
