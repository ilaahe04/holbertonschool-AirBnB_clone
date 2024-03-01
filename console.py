#!/usr/bin/python3
"""
Our cmd Module
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    Our Command Class
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "Review": Review,
               "State": State, "City": City,
               "Amenity": Amenity, "Place": Place}

    @staticmethod
    def isfloat(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def validity(arg="", check_count=1):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if check_count == 1 and arg not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return False
        if check_count == 2 or check_count == 3:
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
                return False
            if len(args) < 2:
                print("** instance id missing **")
                return False
            if args[0] + '.' + args[1] not in storage.all().keys():
                print("** no instance found **")
                return False
        if check_count == 3:
            if len(args) < 3:
                print("** attribute name missing **")
                return False
            if len(args) < 4:
                print("** value missing **")
                return False
        return True

    def do_create(self, arg=""):
        '''Creates a new instance of a class\nUsage: create <class_name>'''
        if HBNBCommand.validity(arg, 1):
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg=""):
        '''Shows an instance of a class\nUsage: create <class_name> <id>'''
        args = arg.split()
        if HBNBCommand.validity(arg, 2):
            key = args[0] + '.' + args[1]
            print(storage.all()[key])

    def do_destroy(self, arg):
        '''Destroys an instance of a class\nUsage: destroy <class_name> <id>'''
        args = arg.split()
        if HBNBCommand.validity(arg, 2):
            key = args[0] + '.' + args[1]
            del storage.all()[key]
            storage.save()

    def do_all(self, arg=""):
        '''Shows every instance'''
        if arg == "":
            all_list = map(lambda x: str(x), storage.all().values())
            print(list(all_list))
        elif arg in HBNBCommand.classes.keys():
            all_list = []
            for key in storage.all().keys():
                if arg in key:
                    all_list.append(str(storage.all()[key]))
            print(all_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg=""):
        '''Updates attributes of an instance
Usage: update <class name> <id> <attribute name> "<attribute value>"'''
        args = arg.split()
        if HBNBCommand.validity(arg, 3):
            key = args[0] + "." + args[1]
            if args[3].isdigit():
                val = int(args[3])
            elif HBNBCommand.isfloat(args[3]):
                val = float(args[3])
            else:
                val = args[3].strip("\"")
            setattr(storage.all()[key], args[2], val)

    def do_count(self, arg):
        '''Counts instances of a class\nUsage: count <class_name>'''
        if HBNBCommand.validity(arg, 1):
            count = 0
            for key in storage.all().keys():
                if arg in key:
                    count += 1
            print(count)

    def default(self, line):
        args = line.split(".")
        commands = {"create": self.do_create, "all": self.do_all,
                    "show": self.do_show, "destroy": self.do_destroy,
                    "update": self.do_update, "count": self.do_count}
        command_attrs = args[1].split("(")
        command = command_attrs[0]
        print(command)
        if command in commands.keys():
            cn = args[0]
            attrs = re.sub("[),\"]", "", command_attrs[1])
            if attrs == "":
                commands[command](f"{cn}")
            else:
                commands[command](f"{cn} {attrs}")
        else:
            super().default(line)

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
