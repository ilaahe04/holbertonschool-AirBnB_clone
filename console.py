#!/usr/bin/python3
"""
Our cmd Module
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Our Command Class
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        'EOF to exit the program'
        exit()

    def do_quit(self, arg):
        'Quit to exit the program'
        exit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
