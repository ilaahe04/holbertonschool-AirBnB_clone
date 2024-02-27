#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
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
