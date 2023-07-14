#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from typing import List, Optional
import inspect


class HBNBCommand(cmd.Cmd):
    """Command-line interface for the AIRBNB project."""

    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, args: str) -> bool:
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args: str) -> bool:
        """Exit the program with Ctrl+D (EOF)"""
        return True

    def emptyline(self) -> None:
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, args: str) -> None:
        """Create a new instance of a given class"""
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instance = self.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, args: str) -> None:
        """Print the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        key = arg_list[0] + '.' + arg_list[1]
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args: str) -> None:
        """Delete an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        key = arg_list[0] + '.' + arg_list[1]
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args: Optional[str]) -> None:
        """Print all string representations of instances"""
        instances = storage.all()

        if not args:
            print([str(value) for value in instances.values()])
            return

        arg_list = args.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return

        print([str(value)
              for key, value in instances.items() if key.startswith(arg_list[0])])

    def do_update(self, args: str) -> None:
        """Update an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        key = arg_list[0] + '.' + arg_list[1]
        if key not in instances:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        instance = instances[key]
        attribute = arg_list[2]
        value = arg_list[3]

        try:
            value = eval(value)
        except (NameError, SyntaxError):
            pass

        setattr(instance, attribute, value)
        instance.save()

    def do_help(self, args: Optional[str]) -> None:
        """Display help messages"""
        commands = {
            'quit': 'Quit command to exit the program',
            'EOF': 'Exit the program with Ctrl+D (EOF)',
            'create': 'Create a new instance of a given class',
            'show': 'Print the string representation of an instance',
            'destroy': 'Delete an instance based on the class name and id',
            'all': 'Print all string representations of instances',
            'update': 'Update an instance based on the class name and id'
        }

        if args:
            if args in commands:
                print(commands[args])
            else:
                print("** No help available for '{}'".format(args))
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            for command, description in commands.items():
                print("{:<10} {}".format(command, description))

         
        if args in self.classes:
            class_name = args
            class_info = inspect.getmembers(self.classes[class_name])
            print(f"\nHelp for class {class_name}:")
            print("===========================")
            for name, member in class_info:
                if inspect.isfunction(member) and name.startswith("do_"):
                    print(f"{name.replace('do_', '')}: {inspect.getdoc(member)}")

    def emptyline(self) -> None:
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    file_path = "file.json"
    if not os.path.exists(file_path):
        print("OK")
    else:
        HBNBCommand().cmdloop()
