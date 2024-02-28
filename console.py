#!/usr/bin/python3
"""
Our cmd Module
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """
    Our Command Class
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}
    def validity(self, args):
    
    def do_create(self, arg=""):
        '''Creates a new instance of a class\nUsage: create <class_name>'''
        if arg == "":
            print("** class name missing **")
        elif arg in HBNBCommand.classes.keys():
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg=""):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] in HBNBCommand.classes.keys():
            key = args[0] + '.' + args[1]
            all_ins = storage.all()
            print(all_ins[key])
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")

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
